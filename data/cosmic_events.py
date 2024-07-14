import pandas as pd
import numpy as np
from kafka import KafkaConsumer

class CosmicEvents:
    def __init__(self, kafka_topic):
        self.kafka_topic = kafka_topic
        self.consumer = KafkaConsumer(self.kafka_topic, bootstrap_servers=['localhost:9092'])

    def consume_events(self):
        for message in self.consumer:
            event = message.value.decode('utf-8')
            yield event

    def process_events(self):
        events = []
        for event in self.consume_events():
            event_data = self._parse_event(event)
            events.append(event_data)
        return pd.DataFrame(events)

    def _parse_event(self, event):
        # Parse event data from Kafka message
        # ...
        return event_data
