def get_relaxation_exercise(exercise_type, hand_data, config):
  """Returns relaxation exercise instructions based on type and hand data (optional)."""
  instructions = None

  if exercise_type == "progressive_muscle_relaxation":
    instructions = """
    Tense and relax muscle groups starting from your toes and working your way up.
    Hold each tense for a few seconds, then release and feel the relaxation.
    Repeat for each muscle group.
    """
  elif exercise_type == "hand_stretching":
    # Access hand data (if available) to provide hand-specific stretching instructions
    if hand_data:
      # ... (replace with logic to analyze hand data and provide targeted instructions)
      instructions = f"""
      Based on your hand position ({hand_data}), perform gentle stretches for your fingers and wrist.
      """
    else:
      instructions = "Perform gentle stretches for your fingers and wrist."

  return instructions

def get_exercise_duration(config):
  """Returns the exercise duration based on configuration."""
  return config["exercise_duration"]python run