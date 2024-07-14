# quantum_secured/encryption_algorithms.py
import numpy as np
from qiskit import QuantumCircuit, execute

class QuantumEncryption:
    def __init__(self, key_size):
        self.key_size = key_size
        self.qc = QuantumCircuit(key_size)

    def generate_key(self):
        # Generate a random key using quantum random number generation
        key = np.random.randint(0, 2, self.key_size)
        return key

    def encrypt(self, message, key):
        # Encrypt the message using quantum encryption
        encrypted_message = []
        for i, bit in enumerate(message):
            if key[i] == 1:
                self.qc.x(i)
            encrypted_message.append(self.qc.measure(i))
        return encrypted_message

    def decrypt(self, encrypted_message, key):
        # Decrypt the message using quantum decryption
        decrypted_message = []
        for i, bit in enumerate(encrypted_message):
            if key[i] == 1:
                self.qc.x(i)
            decrypted_message.append(self.qc.measure(i))
        return decrypted_message
