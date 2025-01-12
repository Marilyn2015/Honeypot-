import socket
import os
import datetime

# Configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 8080       # Port to simulate the service
LOG_DIR = './logs'
LOG_FILE = f'{LOG_DIR}/honeypot.log'

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def log_connection(client_ip, client_data):
    """Log the IP and data of incoming connections."""
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.datetime.now()}] Connection from {client_ip}: {client_data}\n")

def start_honeypot():
    """Start the honeypot server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Honeypot listening on {HOST}:{PORT}...")

        while True:
            client, address = server.accept()
            client_ip, _ = address
            print(f"Connection from {client_ip}")
            
            # Simulate interaction
            client.sendall(b"Welcome to the honeypot!\n")
            client_data = client.recv(1024).decode('utf-8').strip()
            log_connection(client_ip, client_data)
            client.sendall(b"Goodbye!\n")
            client.close()

if __name__ == "__main__":
    print("Starting honeypot...")
    start_honeypot()
