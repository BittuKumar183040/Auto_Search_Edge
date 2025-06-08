import subprocess
import pyautogui
import pygetwindow as gw
import time
import random
import nltk
from nltk.corpus import words
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

nltk.download("words")
all_words = words.words()
random.shuffle(all_words)

try:
    os.system('cls' if os.name == 'nt' else 'clear')
    user_input = input("How many searches need to perform? (10 by default): ").strip()
    search_count = int(user_input) if user_input else 10
except ValueError:
    print("Invalid input. Using default value of 10.")
    search_count = 10

def getRandomNames():
    path = resource_path("random_names.txt")
    with open(path, "r") as f:
        names = [line.strip() for line in f if line.strip()]
    return random.choice(names)

def unique_word_generator():
    for word in all_words:
        yield word

word_gen = unique_word_generator()

for i in range(search_count):
    print(f"\nOpening browser for search {i+1}/{search_count}...")
    subprocess.Popen(["start", "msedge"], shell=True)
    
    edge_window = None
    for _ in range(20):
        windows = gw.getWindowsWithTitle("Edge")
        for win in windows:
            if "Edge" in win.title:
                edge_window = win
                break
        if edge_window:
            break
        time.sleep(0.5)
    
    if edge_window:
        print("Edge is ready. Performing search...")
        edge_window.activate()
        time.sleep(1)
        pyautogui.hotkey("f4")
        time.sleep(0.5)
        search_query = next(word_gen) + " " + getRandomNames()
        print(f"Searching for: {search_query}")
        pyautogui.write(search_query, interval=0.01)
        pyautogui.press("enter")
        time.sleep(3)
        subprocess.call("taskkill /IM msedge.exe /F", shell=True)
        print("Closed browser.")
    else:
        print("Edge window not found. Skipping this iteration.")

print("\n✅ All searches completed.")
