# nlp/advanced_nlp/language_model.py
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class LanguageModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super(LanguageModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=2, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, input_ids):
        embeddings = self.embedding(input_ids)
        output, _ = self.lstm(embeddings)
        output = self.fc(output[:, -1, :])
        return output

class LanguageModelTrainer:
    def __init__(self, model, optimizer, criterion):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion

    def train(self, input_ids, labels):
        self.model.zero_grad()
        output = self.model(input_ids)
        loss = self.criterion(output, labels)
        loss.backward()
        self.optimizer.step()
        return loss.item()

    def evaluate(self, input_ids, labels):
        output = self.model(input_ids)
        loss = self.criterion(output, labels)
        return loss.item()
