# ai/computer_vision/object_tracking.py
import cv2
import numpy as np

class ObjectTracker:
    def __init__(self, video_feed):
        self.video_feed = video_feed
        self.tracker = cv2.TrackerKCF_create()

    def track_object(self, frame):
        # Track the object using the KCF tracker
        ok, bbox = self.tracker.update(frame)
        return ok, bbox

    def detect_object(self, frame):
        # Detect the object using YOLOv3
        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        classes = []
        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        heights, widths = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * widths)
                    center_y = int(detection[1] * heights)
                    w = int(detection[2] * widths)
                    h = int(detection[3] * heights)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        return boxes, confidences, class_ids
