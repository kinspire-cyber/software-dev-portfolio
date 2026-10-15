#!/usr/bin/env python3
import platform
import shutil
import tempfile
from pathlib import Path
from typing import Any, Dict

class PCHealthInspector:
    """Diagnostic tool for monitoring OS health, disk usage, and temp junk."""
    def __init__(self, target_drive: str = "C:") -> None:
        self.target_drive = target_drive
        self.temp_dir = Path(tempfile.gettempdir())

    def get_system_info(self) -> Dict[str,str]:
        """Collect core operating system and hardware specifications."""
        return {
            "OS": platform.system(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Architecture": platform.machine(),
            "Processor": platform.processor(),
            "Hostname": platform.node(),
        }

    def get_disk_usage(self) -> Dict[str,Any]:
        """Calculate total, used, free space, and usage percentage for the target drive."""
        # Ensure path format is drive root like 'C:\' on Windows
        drive_path = f"{self.target_drive[0]}:\\" if platform.system() == "Windows" else "/"
        usage = shutil.disk_usage(drive_path)

        gb_factor = 1024 ** 3
        total_gb = round(usage.total / gb_factor, 2)
        used_gb = round(usage.used / gb_factor, 2)
        free_gb = round(usage.free / gb_factor, 2)
        percent_used = round((usage.used / usage.total) * 100, 2)

        return {
            "Drive": drive_path,
            "Total_GB": total_gb,
            "Used_GB": used_gb,
            "Free_GB": free_gb,
            "Percent_Used": percent_used,
        }

    def scan_temp_junk(self) -> Dict[str, Any]:
        """Scan system temp folder and calculate total junk files and size in MB."""
        total_bytes = 0
        file_count = 0
        locked_count = 0

        if not self.temp_dir.exists():
            return {"Temp_Path": str(self.temp_dir), "File_Count": 0, "Total_MB": 0.0, "Locked_Skipped": 0}
        for item in self.temp_dir.rglob("*"):
            try:
                if item.is_file():
                    total_bytes += item.stat().st_size
                    file_count += 1
            except (PermissionError, FileNotFoundError, OSError):
                locked_count += 1
                continue
        total_mb = round(total_bytes / (1024 ** 2), 2)
        return {
            "Temp_Path": str(self.temp_dir),
            "File_Count": file_count,
            "Total_MB": total_mb,
            "Locked_Skipped": locked_count,
        }

    def display_report(self) -> None:
        """Run all diagnostic checks and display a formatted health summary."""
        print("=" * 60)
        print("   KINSPIRE PC HEALTH & TEMP JUNK INSPECTOR v1.0   ")
        print("=" * 60)

        # 1. System Info
        sys_info = self.get_system_info()
        print("\n[+] SYSTEM SPECIFICATIONS:")
        for key, val in sys_info.items():
            print(f"    • {key:<14}: {val}")

        # 2. Disk Health
        disk_info = self.get_disk_usage()
        print(f"\n[+] STORAGE HEALTH ({disk_info['Drive']}):")
        print(f"    • Total Space   : {disk_info['Total_GB']} GB")
        print(f"    • Used Space    : {disk_info['Used_GB']} GB ({disk_info['Percent_Used']}%)")
        print(f"    • Free Space    : {disk_info['Free_GB']} GB")

        # 3. Temp Junk Status
        print("\n[+] SCANNING TEMPORARY JUNK FILES...")
        temp_info = self.scan_temp_junk()
        print(f"    • Temp Location : {temp_info['Temp_Path']}")
        print(f"    • Junk Files    : {temp_info['File_Count']:,} files")
        print(f"    • Reclaimable   : {temp_info['Total_MB']:,} MB")
        if temp_info['Locked_Skipped'] > 0:
            print(f"    • Locked/In-Use : {temp_info['Locked_Skipped']} (safely skipped)")

        print("\n" + "=" * 60)
        print("   HEALTH INSPECTION COMPLETE")
        print("=" * 60)

if __name__ == "__main__":
    inspector = PCHealthInspector()
    inspector.display_report()
    input("\nPress Enter to exit...")