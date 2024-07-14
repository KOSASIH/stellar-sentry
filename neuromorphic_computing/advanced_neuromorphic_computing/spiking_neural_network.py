# neuromorphic_computing/advanced_neuromorphic_computing/spiking_neural_network.py
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class SpikingNeuralNetwork:
    def __init__(self, num_inputs, num_hidden, num_outputs):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs
        self.input_layer = nn.Linear(num_inputs, num_hidden)
        self.hidden_layer = nn.Linear(num_hidden, num_hidden)
        self.output_layer = nn.Linear(num_hidden, num_outputs)
        self.spike_function = nn.ReLU()

    def forward(self, input_spike_train):
        hidden_spike_train = self.spike_function(self.input_layer(input_spike_train))
        hidden_spike_train = self.spike_function(self.hidden_layer(hidden_spike_train))
        output_spike_train = self.spike_function(self.output_layer(hidden_spike_train))
        return output_spike_train

    def train(self, input_spike_train, target_spike_train):
        self.zero_grad()
        output_spike_train = self.forward(input_spike_train)
        loss = nn.MSELoss()(output_spike_train, target_spike_train)
        loss.backward()
        self.optimizer.step()
        return loss.item()

    def evaluate(self, input_spike_train, target_spike_train):
        output_spike_train = self.forward(input_spike_train)
        loss = nn.MSELoss()(output_spike_train, target_spike_train)
        return loss.item()
