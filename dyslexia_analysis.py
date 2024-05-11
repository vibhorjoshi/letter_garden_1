def analyze_score(score, total_attempts, config):
  """Analyzes the player's score and total attempts against the dyslexia score threshold."""
  dyslexia_threshold = config["dyslexia_threshold"]
  accuracy = score / total_attempts

  dyslexia_risk = "Low" if accuracy >= dyslexia_threshold else "High"

  return {
      "accuracy": accuracy,
      "dyslexia_risk": dyslexia_risk