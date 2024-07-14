# services/alert_system.py
import os
import requests
from twilio.rest import Client

class AlertSystem:
    def __init__(self, config):
        self.config = config
        self.client = Client(self.config['TWILIO_ACCOUNT_SID'], self.config['TWILIO_AUTH_TOKEN'])

    def send_alert(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.config['TWILIO_PHONE_NUMBER'],
            to=self.config['STAKEHOLDER_PHONE_NUMBER']
        )
        return message.sid
