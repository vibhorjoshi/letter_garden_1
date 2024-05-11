import cv2
import socket
import threading
from hand_tracking import start_hand_tracking

def main():
  # Replace with actual values based on your Letter Garden communication protocol
  host = "localhost"  # Replace with the IP of the Letter Garden application
  port = 12345  # Replace with the port used in Letter Garden for receiving data

  # Start hand tracking thread
  hand_tracking_thread = threading.Thread(target=start_hand_tracking, args=(host, port))
  hand_tracking_thread.start()

  # ... (optional: add code for other companion app features)

  # Wait for hand tracking thread to finish (optional)
  hand_tracking_thread.join()

if __name__ == "__main__":
  main()