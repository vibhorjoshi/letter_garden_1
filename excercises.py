def get_relaxation_exercise(exercise_type, config):
  """Returns relaxation exercise instructions based on type."""
  instructions = None

  if exercise_type == "progressive_muscle_relaxation":
    instructions = """
    Tense and relax muscle groups starting from your toes and working your way up.
    Hold each tense for a few seconds, then release and feel the relaxation.
    Repeat for each muscle group.
    """
  elif exercise_type == "hand_stretching":
    # Not used in Letter Garden, as hand data isn't received directly
    instructions = "Perform gentle stretches for your fingers and wrist."  # Generic instructions

  return instructions

def get_exercise_duration(config):
  """Returns the exercise duration based on configuration."""
  return config["exercise_duration"]