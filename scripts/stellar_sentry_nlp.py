import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import BertTokenizer, BertModel

class StellarSentryNLP(nn.Module):
    def __init__(self, num_classes):
        super(StellarSentryNLP, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.dropout = nn.Dropout(0.1)
        self.classifier = nn.Linear(self.bert.config.hidden_size, num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        pooled_output = self.dropout(pooled_output)
        outputs = self.classifier(pooled_output)
        return outputs

def train_nlp_model(data, num_classes):
    # Create data loader
    batch_size = 32
    data_loader = torch.utils.data.DataLoader(data, batch_size=batch_size, shuffle=True)

    # Initialize model, optimizer, and loss function
    model = StellarSentryNLP(num_classes)
    optimizer = optim.Adam(model.parameters(), lr=1e-5)
    loss_fn = nn.CrossEntropyLoss()

    # Train model
    for epoch in range(5):
        model.train()
        total_loss = 0
        for batch in data_loader:
            input_ids, attention_mask, labels = batch
            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask)
            loss = loss_fn(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f'Epoch {epoch+1}, Loss: {total_loss / len(data_loader)}')

    # Evaluate model
    model.eval()
    total_correct = 0
    with torch.no_grad():
        for batch in data_loader:
            input_ids, attention_mask, labels = batch
            outputs = model(input_ids, attention_mask)
            _, predicted = torch.max(outputs, 1)
            total_correct += (predicted == labels).sum().item()
    accuracy = total_correct / len(data)
    print(f'Test Accuracy: {accuracy:.4f}')

def main():
    # Load data
    data = pd.read_csv('data/nlp_data.csv')

    # Preprocess data
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    input_ids = []
    attention_mask = []
    labels = []
    for text, label in zip(data['text'], data['label']):
        encoding = tokenizer.encode_plus(
            text,
            max_length=512,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        input_ids.append(encoding['input_ids'].flatten())
        attention_mask.append(encoding['attention_mask'].flatten())
        labels.append(torch.tensor(label))
    input_ids = torch.tensor(input_ids)
    attention_mask = torch.tensor(attention_mask)
    labels = torch.tensor(labels)

    # Train NLP model
    num_classes = 8
    train_nlp_model((input_ids, attention_mask, labels), num_classes)

if __name__ == '__main__':
    main()
