# Hebrew Braille Auto-Translator

A Python-based utility for **bidirectional translation** between **Hebrew text** and **Unicode Braille**.  
The script runs in a continuous loop and **automatically detects** whether the input is Hebrew or Braille.

Built according to **Israeli Grade 1 Braille** conventions.

---

## ✨ Features

- 🔁 **Bidirectional Translation**
  - Hebrew → Braille
  - Braille → Hebrew
- 🔍 **Automatic Detection**
  - Detects Braille input using Unicode range `U+2800–U+28FF`
- 🔢 **Number Support**
  - Uses the Braille number prefix `⠼`
- ✍️ **Hebrew Final Letters**
  - Correctly normalizes ך ם ן ף ץ
- 🧠 **Continuous Interactive Mode**
  - No need to restart the script
- ⛔ **Exit Commands**
  - `exit`, `quit`, `יציאה`

---

## 📦 Installation

Make sure Python **3.x** is installed.

```bash
git clone https://github.com/yourusername/hebrew-braille-translator.git
cd hebrew-braille-translator
python he_braille_translator.py

