import time
import random
import os
import sys
import nltk
from nltk.corpus import words
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

os.system("taskkill /F /IM msedge.exe >nul 2>&1")

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")
  return os.path.join(base_path, relative_path)

nltk.download("words")
all_words = words.words()
random.shuffle(all_words)

def getRandomNames():
    path = resource_path("random_names.txt")
    with open(path, "r") as f:
      names = [line.strip() for line in f if line.strip()]
    return random.choice(names)

def unique_word_generator():
  for word in all_words:
    yield word

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Read from config.json to get the profile name
exe_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
config_path = os.path.join(exe_dir, "config.json")
with open(config_path, "r") as config_file:
  config = json.load(config_file)
profile_name = config.get("profile", "Default")
print("Browser profile: ", profile_name)

# user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data")
# options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_name}")

print("Edge Browser start kar raha hu...")
service = EdgeService(log_path=os.devnull) 
driver = webdriver.Edge(service=service, options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
word_gen = unique_word_generator()

search_count = config.get("search_count", 10)
for i in range(search_count):
  search_term = next(word_gen) + " " + getRandomNames()
  print(f"Searching for: {search_term}")
  search_url = "https://www.bing.com/search?q=" + search_term.replace(" ", "+")
  driver.get(search_url)
  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.NAME, "q"))
    )
    time.sleep(0.5)
  except Exception:
    print(f"Timeout while loading search page for: {search_term}")

  time.sleep(0.5)

print("Performed:", search_count, "searches.")

driver.quit()
