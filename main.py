import random
import json
from selenium import webdriver

# ---- Load json file ---- #
with open("madlibs.json", "r", encoding="utf-8") as f:
    user_input = json.load(f)

template_list = user_input["templates"]
nouns = user_input["values"]["adjectives"]
verbs = user_input["values"]["nouns"]
adjectives = user_input["values"]["verbs"]

# ---- Generate random stories ---- #
def generate_story():
    template = random.choice(template_list)
    filled = template.format(
        adjective=random.choice(adjectives),
        noun=random.choice(nouns),
        verb=random.choice(verbs)
    )
    return filled

# ---- Generate and print one story ---- #
story = generate_story()
print(f"The story is: {story}")

# ---- Generate and print multiple stories ---- #
#for i in range(5):
#   print(f"Story {i+1}: {generate_story()}\n")