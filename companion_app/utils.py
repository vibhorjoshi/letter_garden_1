Python
import socket

def send_data_over_socket(host, port, data):
  """Sends data over a socket connection."""
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((host, port))
  sock.sendall(data.encode())  # Assuming data is string-like
  sock.close()