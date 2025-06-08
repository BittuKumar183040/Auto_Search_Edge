## 🚀 Edge Search Automation (Keystroke Version)

This Python script automates opening Microsoft Edge, typing randomized search terms (name + dictionary word), and repeating this process for a user-defined number of times. It simulates human keystrokes using `pyautogui` and closes the browser after each search.

---

### 🧩 Features

* Opens Microsoft Edge using `subprocess`
* Waits for the Edge window using `pygetwindow`
* Simulates user actions using `pyautogui` (like pressing `F4`, typing, Enter)
* Searches for random combinations of dictionary words and names
* Closes Edge after each search
* Uses `random_names.txt` and `nltk` word corpus
* Compatible with PyInstaller packaging

---

### ⚙️ Requirements

Install the required Python packages:

```bash
pip install pyautogui pygetwindow nltk
```

Also install `Edge` browser and ensure it's available in system path.

---

### 📁 Project Structure

```
project/
├── main.py               # Main script
├── random_names.txt      # List of names (1 per line)
└── README.md             # This documentation
```

---

### 📄 `random_names.txt`

Provide a list of names (one per line):

```
Olivia
Liam
Emma
Noah
Ava
...
```

---

### 💻 How to Run

```bash
python main.py
```

You will be prompted:

```text
How many searches need to perform? (10 by default):
```

Each search opens Edge, performs the search, and closes the browser.

---

### 📦 PyInstaller Packaging

To compile it into an `.exe`:

```bash
pyinstaller --onefile --add-data "random_names.txt;." main.py
```

To run without a visible console window (GUI mode):

```bash
pyinstaller --onefile --noconsole --add-data "random_names.txt;." main.py
```

> 💡 Note: Avoid using `input()` if you're using `--noconsole`. Replace with a fixed number or config file.

---

### 📌 Notes

* On first run, `nltk.download("words")` downloads the dictionary word list.
* The script uses `taskkill` to force-close Edge after each search.
* Avoid overusing this script on search engines to prevent rate-limiting or bans.

---

### ❓ Troubleshooting

**Edge not found?**

* Ensure Edge is installed and accessible via `start msedge` in CMD.

**PermissionError when running `pyinstaller`?**

* Make sure the output folder is writable.
* Run your terminal with Administrator privileges if needed.
