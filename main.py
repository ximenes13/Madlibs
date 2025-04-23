import random
from selenium import webdriver

# ---- TEMPLATES ---- #
templates = ["Today, I saw {adjective} {noun} trying to {verb} at the park.",
    "My best friend is a {adjective} {noun} who loves to {verb} on weekends.",
    "In the future, {noun}s will {verb} all over the {adjective} cities."]

# ---- Word Pools ---- #
nouns = ["dragon", "teacher", "banana", "robot", "pirate"]
verbs = ["dance", "sing", "scream", "teleport", "cook"]
adjectives = ["fuzzy", "gigantic", "creepy", "sassy", "blue"]

# ---- Generate random stories ----#
def generate_story():
    template = random.choice(templates)
    filled = template.format(
        adjective=random.choice(adjectives),
        noun=random.choice(nouns),
        verb=random.choice(verbs))

    return filled

story = generate_story()
print(f"The story is: {story}")