# nlu/advanced_nlu/language_understanding.py
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class LanguageUnderstanding:
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=2, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, input_ids):
        embeddings = self.embedding(input_ids)
        output, _ = self.lstm(embeddings)
        output = self.fc(output[:, -1, :])
        return output

    def train(self, input_ids, labels):
        self.zero_grad()
        output = self.forward(input_ids)
        loss = nn.CrossEntropyLoss()(output, labels)
        loss.backward()
        self.optimizer.step()
        return loss.item()

    def evaluate(self, input_ids, labels):
        output = self.forward(input_ids)
        loss = nn.CrossEntropyLoss()(output, labels)
        return loss.item()
