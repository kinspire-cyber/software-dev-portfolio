# 💻 Software Development Portfolio

> **Production-grade Python utilities, system diagnostics, automation engines, and offline AI solutions.**  
> Built by **Kingsley Onyema** | Tech Educator & Developer | 🎥 [@kinspiretech](https://youtube.com/@kinspiretech)

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Engineering-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Ecosystem](https://img.shields.io/badge/Ecosystem-KinspireFix%20AI-purple?style=for-the-badge)

---

## 👋 Welcome to My Software Portfolio

Hi, I'm **Kingsley Onyema**! I build tools that solve practical problems in IT support, system administration, automation, and applied artificial intelligence.

This repository serves as the centralized monorepo for my **Software Engineering Portfolio**, built with rigorous engineering standards:
* **Object-Oriented Design & Encapsulation** — Clean abstractions separating data ingestion from presentation layers.
* **Standard Library First** — Zero-bloat, highly portable code relying on battle-tested standard libraries (`pathlib`, `shutil`, `platform`, `hashlib`, `sqlite3`).
* **Fault-Tolerant Architecture** — Defensive programming that gracefully bypasses OS permission locks and filesystem race conditions.
* **Real-World Impact** — Every utility directly serves daily user workflows and integrates into the **KinspireFix AI** autonomous support ecosystem.

---

## 🗂️ Project Directory & Roadmap

| # | Project | Focus / Category | Status | Primary Toolkit | Description |
|---|---------|------------------|--------|-----------------|-------------|
| 01 | [**FileOrganizerPro**](./FileOrganizerPro/) | File Automation | ✅ **v1.0 Live** | `pathlib`, `shutil` | Automatically sorts chaotic downloads and folders into 7 categorized directories in seconds. |
| 02 | [**PCHealthInspector**](./PCHealthInspector/) | System Diagnostics | ✅ **v1.0 Live** | `platform`, `shutil`, `tempfile` | Real-time OS telemetry, storage health percentages, and recursive Windows Temp junk auditor. |
| 03 | **DuplicateFileFinder** | Storage Optimization | 🔜 In Pipeline | `hashlib (SHA-256)`, `pathlib` | Fast duplicate file detection using cryptographic hashing rather than superficial filenames. |
| 04 | **BulkFileRenamer** | Batch Automation | 📋 Planned | `re`, `pathlib`, `Tkinter` | High-speed batch renaming engine supporting complex regex patterns and metadata extraction. |
| 05 | **LocalBackupManager** | Data Protection | 📋 Planned | `sqlite3`, `cryptography` | Automated, encrypted local backup engine designed for SME data recovery and offline archiving. |
| 06 | **NetworkScannerDashboard** | Network Engineering | 📋 Planned | `socket`, `scapy`, `ipaddress` | LAN host discovery, open port diagnostics, and rogue device network auditor. |
| 07 | **SoftwareInventoryAuditor**| IT Asset Management | 📋 Planned | `winreg`, `csv` | Windows Registry scanner auditing installed software, version drift, and publisher signatures. |
| 08 | **SystemEventLogAnalyzer** | Fault Diagnostics | 📋 Planned | `win32evtlog`, `pandas` | Parses Windows Event Viewer crash logs and translates cryptic error IDs into actionable root causes. |
| 09 | **AutomatedReportGenerator** | Business Intelligence | 📋 Planned | `pandas`, `reportlab` | Converts diagnostic spreadsheets and metrics into publication-ready executive PDF reports. |
| 10 | **KinspireFix AI** | Applied AI / Thesis | 👑 **Flagship** | `local LLM`, `CustomTkinter`, `SQLite` | Master offline AI IT support assistant with intent classification and autonomous diagnostic tool routing. |

---

## 🌟 Featured Projects

### 1. 🔍 [PC Health & Temp Junk Inspector](./PCHealthInspector/)
A zero-dependency diagnostic module that monitors system specifications, tracks disk capacity thresholds, and safely measures hundreds of megabytes of hidden Windows temporary junk.

```text
============================================================
   🔍 KINSPIRE PC HEALTH & TEMP JUNK INSPECTOR v1.0   
============================================================
[+] SYSTEM SPECIFICATIONS:
    • OS            : Windows 11 (AMD64)
    • Hostname      : KinspireTech
[+] STORAGE HEALTH (C:\):
    • Total / Used  : 237.39 GB / 190.05 GB (80.06% Used)
    • Free Space    : 47.34 GB
[+] TEMPORARY JUNK AUDIT:
    • Junk Files    : 9,024 files
    • Reclaimable   : 1,554.08 MB
============================================================
```

### 2. 📁 [File Organizer Pro](./FileOrganizerPro/)
A smart Python CLI tool that automatically cleans disorganized download directories into organized category folders (`Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Code`, `Others`) with interactive path validation and summary reports.

---

## 🛠️ Engineering Standards & Best Practices

All modules in this portfolio adhere to these development rules:
1. **Type Annotations (PEP 484):** All functions and methods include strict type hints for maintainability and IDE static analysis.
2. **Defensive Error Handling:** Filesystem operations handle `PermissionError`, `FileNotFoundError`, and `OSError` to prevent runtime crashes.
3. **Execution Guards:** Scripts implement `if __name__ == "__main__":` to support both standalone CLI runs and clean programmatic imports.
4. **Interactive Pause Guards:** Windows double-click executions are preserved with terminal pause listeners to ensure output visibility.

---

## 🚀 Quick Start & Installation

To run any module locally:

```bash
# 1. Clone this portfolio repository
git clone https://github.com/kinspire-cyber/software-dev-portfolio.git

# 2. Navigate to your target project folder
cd software-dev-portfolio/PCHealthInspector

# 3. Execute the module directly (No external pip install required)
python main.py
```

---

## 📬 Connect & Collaborate

* 🎥 **YouTube:** [@kinspiretech](https://youtube.com/@kinspiretech) — Tutorials on Robotics, Python, and Applied AI
* 🐙 **GitHub:** [@kinspire-cyber](https://github.com/kinspire-cyber)
* 💼 **Focus:** Software Development, IoT & Robotics, IT Systems Automation, and Applied NLP

---

## 📜 License

This portfolio repository is licensed under the [MIT License](LICENSE) — open for educational use, adaptation, and collaboration.
