import random
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Load JSON data
with open("madlibs.json", "r", encoding="utf-8") as f:
    user_input = json.load(f)

# Set up Chrome with options
options = Options()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Load the HTML file from the local server
driver.get("http://localhost:8000/madlib_page.html")

sleep(1)  # Let the page load for a second

# Pull data from JSON
template_list = user_input["templates"]
nouns = user_input["values"]["nouns"]
verbs = user_input["values"]["verbs"]
adjectives = user_input["values"]["adjectives"]

# Generate the story
def generate_story():
    template = random.choice(template_list)
    return template.format(
        adjective=random.choice(adjectives),
        noun=random.choice(nouns),
        verb=random.choice(verbs)
    )

madlib_story = generate_story()

# ---- Check if the element is found and then inject the story ---- #
try:
    madlib_story_element = driver.find_element(By.ID, "madlib-story")
    driver.execute_script("arguments[0].textContent = arguments[1];", madlib_story_element, madlib_story)
    print("Story injected successfully.")  # Confirm successful injection
except Exception as e:
    print("Error:", e)  # Print error if there's an issue

input("Press Enter to close the browser...")