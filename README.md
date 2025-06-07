## 🔍 Edge Automation
This Python application automates Microsoft Edge to simulate typing and searching random name-word combinations using a mix of dictionary words and preloaded names. It uses `pyautogui` for keyboard control, `pygetwindow` for detecting when Edge is open, and can be optionally adapted to run in headless mode via Selenium.

---

### 📦 Features

* Launches Microsoft Edge
* Waits until the Edge window is ready
* Focuses on the address bar using `F4`
* Types a random name + dictionary word and presses `Enter`
* Repeats the process 10 times
* Uses `nltk` corpus and a `random_names.txt` file
* Compatible with PyInstaller packaging via `resource_path()`

---

### 🛠️ Requirements

```bash
pip install pyautogui pygetwindow nltk
```

Additionally, if using Selenium in headless mode (optional):

Also install `msedgedriver` from: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

---

### 📁 File Structure
```
project/
├── main.py               # Your main automation script
├── random_names.txt      # Text file with 1000+ random names
└── README.md             # This file
```
---

### 📄 `random_names.txt`

Place this file in the same directory. It should contain one name per line:

```
Olivia
Liam
Emma
Noah
Ava
...
```

---

### 🚀 How to Run

```bash
python main.py
```

If packaged with PyInstaller:

```bash
pyinstaller --onefile main.py
dist/main.exe
```

---

### 🧠 How It Works

1. Downloads the NLTK `words` corpus if not already available.
2. Loads random names from `random_names.txt`.
3. Opens Edge using `subprocess`.
4. Waits until a window with "Edge" in its title appears.
5. Types name + word into the address bar and presses Enter.
6. Repeats the search 10 times with a 3-second interval.

---

### ⚙️ Optional Headless Mode

To avoid showing the browser, consider using **Selenium with Edge in headless mode**. Replace the `pyautogui` and `subprocess` logic with a headless driver.

```python
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Edge(options=options)
driver.get("https://www.google.com")
```

---

### 📌 Notes

* On first run, `nltk.download("words")` will download the word list.
* Ensure Microsoft Edge is installed and on your system path.
* This script is for automation/testing purposes only — do not use it to spam search engines or scrape sites against their terms of service.

---

### 🧾 License

MIT License

---
