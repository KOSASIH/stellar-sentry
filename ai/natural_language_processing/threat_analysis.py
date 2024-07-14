# ai/natural_language_processing/threat_analysis.py
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class ThreatAnalyzer:
    def __init__(self, text):
        self.text = text
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self):
        # Analyze the sentiment of the text
        sentiment = self.sia.polarity_scores(self.text)
        return sentiment

    def detect_threats(self):
        # Detect threats using natural language processing
        threats = []
        for sentence in nltk.sent_tokenize(self.text):
            if self.sia.polarity_scores(sentence)['compound'] > 0.5:
                threats.append(sentence)
        return threats
