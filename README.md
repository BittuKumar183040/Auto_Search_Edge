## 🔍 Edge Search Automation with Selenium

This Python application automates Microsoft Edge browser searches using the user's logged-in profile. It performs keyword + name-based search using real dictionary words (`nltk`) and names from a file (`random_names.txt`). The profile used is configurable via a `config.json` file placed beside the executable.

---

### 📦 Features

* Uses **your actual Edge browser profile** (bookmarks, search history, etc. preserved)
* Searches **realistic phrases** like `"eclipse Amelia"` or `"quantum Noah"`
* Reads names from `random_names.txt`
* Configurable **profile name** via `config.json`
* Uses `nltk` for English words
* Optionally packable using `PyInstaller` for one-file `.exe`

---

### 🛠️ Requirements

Install the required Python packages:

```bash
pip install selenium nltk
```

Also install [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) compatible with your Edge version, and ensure it's in your system PATH.

---

### 📁 File Structure

```
project/
├── main.py             # Your automation script
├── random_names.txt    # File with 1000+ names (1 per line)
├── config.json         # External config file for profile selection
└── README.md           # This file
```

---

### 📄 `random_names.txt`

Each line should be a name (used for pairing with dictionary words):

```
Olivia
Liam
Emma
Noah
Ava
...
```

---

### ⚙️ `config.json`

This file **must be placed next to the compiled `.exe`** (or in the same folder during development). Example:

```json
{
  "profile": "Profile 1"
}
```

To use the **default profile**, set:

```json
{
  "profile": "Default"
}
```

---

### 🚀 How to Run

```bash
python main.py
```

If you're building a `.exe` with PyInstaller, run:

```bash
pyinstaller --onefile --add-data "random_names.txt;." main.py
```

> ⚠️ Do **not** include `config.json` in the bundle — it stays **outside** so users can edit it.

---

### 💡 How It Works

1. Prompts for number of searches (`10` default)
2. Kills existing Edge processes (to avoid profile lock issues)
3. Reads `random_names.txt` and `nltk` word list
4. Loads Edge using the logged-in user profile (from `config.json`)
5. For each search:

   * Creates a search phrase (`word + name`)
   * Opens Bing search with that term
   * Waits for page to fully load
6. Exits automatically after all searches

---

### ✅ Example Output

```
All existing Edge tabs will be closed. Press Enter to proceed...
Browser profile: Profile 1
Edge Browser start kar raha hu...
Searching for: quantum Ava
Searching for: gravity Liam
...
Performed: 10 searches.
```

---

### 🧾 License

MIT License

---
