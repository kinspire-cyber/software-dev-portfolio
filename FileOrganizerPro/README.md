# 📁 File Organizer Pro

> A smart Python tool that automatically sorts messy folders into organized category folders — by file type, in seconds.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-v1.0%20Released-brightgreen.svg)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-success.svg)

---

## 🎯 What It Does

Tired of drowning in a messy Downloads folder? File Organizer Pro scans any folder and automatically moves files into neat category folders:

- 📂 **Images** — jpg, png, gif, svg, and more
- 📄 **Documents** — pdf, docx, txt, xlsx, and more
- 🎬 **Videos** — mp4, mov, avi, mkv, and more
- 🎵 **Audio** — mp3, wav, flac, aac, and more
- 📦 **Archives** — zip, rar, 7z, tar, and more
- 💻 **Code** — py, js, html, css, java, and more
- 📁 **Others** — anything that doesn't match above

---

## ✨ Features

- ✅ **7 smart categories** — Automatically detects file types by extension
- ✅ **Safe by default** — Built-in error handling won't crash on bad files
- ✅ **Detailed summary** — See exactly what was moved and where
- ✅ **No external dependencies** — Uses only Python standard library
- ✅ **Cross-platform** — Works on Windows, Mac, and Linux
- ✅ **Lightweight** — Single file, no installation needed

---

## 📦 Installation

1. Make sure you have **Python 3.8 or higher** installed
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/file-organizer-pro.git
   ```
3. Navigate to the project folder:
   ```bash
   cd file-organizer-pro
   ```

That's it! No `pip install` needed — it uses only built-in Python libraries.

---

## 🚀 Usage

1. **Create a folder** with files you want to organize (or use the included `test_folder/`)
2. **Edit `main.py`** and change `"test_folder"` to your folder name on the last line
3. **Run the program:**
   ```bash
   python main.py
   ```
4. **Watch the magic happen!** ✨

### Example Output:

```
Moving backup.zip → Archives/
Moving movie.mp4 → Videos/
Moving photo.jpg → Images/
Moving random.xyz → Others/
Moving report.pdf → Documents/
Moving script.py → Code/
Moving song.mp3 → Audio/

========================================
📊 ORGANIZATION COMPLETE!
========================================
✅ Total files moved: 7
📁 Categories used: 7

Breakdown:
   • Archives: 1 file(s)
   • Videos: 1 file(s)
   • Images: 1 file(s)
   • Others: 1 file(s)
   • Documents: 1 file(s)
   • Code: 1 file(s)
   • Audio: 1 file(s)
========================================
```

---

## 📁 Project Structure

```
FileOrganizerPro/
├── main.py              # Main program (all the magic happens here)
├── README.md            # You are here!
├── test_folder/         # Sample folder for testing
│   ├── photo1.jpg
│   ├── photo2.png
│   ├── report.pdf
│   ├── script.py
│   ├── song.mp3
│   ├── movie.mp4
│   ├── backup.zip
│   └── random.xyz
└── LICENSE              # MIT License
```

---

## 🧠 How It Works (For the Curious)

The program uses a simple but powerful approach:

1. **Dictionary Lookup** — A predefined map connects categories to file extensions
2. **Path Scanning** — Uses Python's `pathlib` to scan the target folder
3. **Extension Matching** — Each file's extension is matched against the dictionary
4. **Smart Moving** — Files are moved using `shutil.move()` with error handling
5. **Tracking** — Counts are kept in a dictionary for the final summary

No fancy AI, no heavy dependencies — just clean Python code solving a real problem.

---

## 🗺️ Roadmap

- [x] **v1.0** — Type-based organization ✅ *(Released)*
- [ ] **v1.1** — Date-based organization (Year/Month folders)
- [ ] **v1.2** — Custom rules & configuration file (JSON)
- [ ] **v1.3** — Dry-run mode (preview before moving)
- [ ] **v2.0** — Desktop GUI with Tkinter
- [ ] **v2.1** — Convert to standalone .exe (PyInstaller)
- [ ] **v3.0** — Cloud sync & plugin system

---

## 👨‍💻 About the Developer

Hi, I'm **Kingsley Onyema** — a Python developer and tech educator passionate about building tools that solve real problems. I teach robotics, AI, and software development across Africa.

🎥 **YouTube:** [kinspiretech](https://youtube.com/@kinspiretech)
🚀 **Mission:** Building tools that make life easier, one script at a time.

---

## 🤝 Contributing

Found a bug? Have a feature idea? Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute!

---

## ⭐ Show Your Support

If this project helped you, please **give it a star** ⭐ on GitHub! It motivates me to keep building and sharing.

---

### 💡 Tips for Users

- **Always test on a copy** of your folder first (just in case!)
- **Backup important files** before running on large folders
- **Check the summary report** to verify everything moved correctly

Made with ❤️ by Kingsley Onyema | kinspiretech
