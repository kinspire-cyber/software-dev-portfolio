# 🔍 PC Health & Temp Junk Inspector

> A lightweight, zero-dependency Python diagnostic tool that checks operating system specifications, monitors real-time disk storage health, and calculates exact megabytes of hidden Windows temporary junk.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-v1.0%20Released-brightgreen.svg)
![Ecosystem](https://img.shields.io/badge/Project-KinspireFix%20AI%20Module%201-purple.svg)

---

## 🎯 What It Does

**PC Health & Temp Junk Inspector** is Module 1 of the **KinspireFix AI** IT diagnostics ecosystem. It provides instant hardware/OS telemetry, monitors drive capacity thresholds, and safely scans Windows `%TEMP%` directories to uncover reclaimable disk space without risking system stability.

- 🖥️ **OS & Hardware Telemetry** — Extracts OS release, build version, architecture, CPU model, and hostname.
- 💾 **Drive Health & Utilization** — Calculates total, used, free gigabytes, and drive utilization percentage.
- 🧹 **Temp Junk Audit** — Recursively scans temporary folders and computes exact reclaimable megabytes.
- 🛡️ **Fault-Tolerant Scanning** — Handles locked/in-use Windows system files gracefully with zero crashes.
- ⚡ **Zero External Dependencies** — Built 100% on standard Python libraries (`platform`, `shutil`, `pathlib`, `tempfile`).

---

## 📊 Live Sample Output

```text
============================================================
   🔍 KINSPIRE PC HEALTH & TEMP JUNK INSPECTOR v1.0   
============================================================

[+] SYSTEM SPECIFICATIONS:
    • OS            : Windows
    • Release       : 11
    • Version       : 10.0.26300
    • Architecture  : AMD64
    • Processor     : AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD
    • Hostname      : KinspireTech

[+] STORAGE HEALTH (C:\):
    • Total Space   : 237.39 GB
    • Used Space    : 190.05 GB (80.06%)
    • Free Space    : 47.34 GB

[+] SCANNING TEMPORARY JUNK FILES...
    • Temp Location : C:\Users\KINGSL~1\AppData\Local\Temp
    • Junk Files    : 9,024 files
    • Reclaimable   : 1,554.08 MB

============================================================
   ✅ HEALTH INSPECTION COMPLETE
============================================================
```

---

## 🚀 How to Run

### Method 1: Command Line
1. Clone the portfolio repository:
   ```bash
   git clone https://github.com/kinspire-cyber/software-dev-portfolio.git
   cd software-dev-portfolio/PCHealthInspector
   ```
2. Run the script:
   ```bash
   python main.py
   ```

### Method 2: Double-Click Execution (Windows / macOS / Linux)
* Simply double-click `main.py` in your file explorer.
* The script contains an integrated pause guard (`input(...)`), keeping the terminal open until you press Enter.

---

## 🧠 Architectural Design & OOP Principles

This module demonstrates key production software engineering standards:

1. **Separation of Concerns:** 
   Telemetry retrieval (`get_system_info`), storage math (`get_disk_usage`), and disk scanning (`scan_temp_junk`) return pure data structures (`dict`). None of them are coupled to console printing.
2. **Encapsulation & Abstraction:** 
   The complex logic of byte-to-GB conversions, Windows path normalizations, and locked-file exception handling is cleanly encapsulated inside class methods.
3. **Presentation Layer:** 
   `display_report()` acts as the consumer/renderer. When integrated into the future KinspireFix GUI dashboard or NLP tool router, the core logic remains 100% reusable without modification.

---

## 🗺️ Roadmap & Ecosystem Alignment

- [x] **v1.0** — CLI OS specs, disk usage %, and temp junk scanner ✅ *(Released)*
- [ ] **v1.1** — 1-click safe temp cleaner action with user confirmation
- [ ] **v2.0** — Integration into **KinspireFix AI** Dark-Mode Dashboard (Tkinter / CustomTkinter)
- [ ] **v3.0** — Natural Language Intent Routing (`"check_system_specs"`, `"clean_temp_junk"`)

---

## 👨‍💻 Developer & Project Context

Developed by **Kingsley Onyema** ([@kinspiretech](https://youtube.com/@kinspiretech)) as part of the **13-Week NOUN AI IT Support Research Project** and Software Dev Portfolio.

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute!

