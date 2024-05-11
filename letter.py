import random

def generate_letter(config):
  """Generates a random letter based on game configuration."""
  available_letters = config["available_letters"]
  return random.choice(available_letters)

def is_letter_matched(received_letter, generated_letter):
  """Checks if the received letter ID matches the generated letter."""
  return received_letter == generated_letter