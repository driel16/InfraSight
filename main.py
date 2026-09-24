from pathlib import Path

from infrasight.system.disk_monitor import format_bytes, get_disk_usage
from infrasight.system.system_info import get_system_info


def generate_report(system_info):
    report = f"""
===================================
        INFRASIGHT SYSTEM REPORT
===================================

Operating System : {system_info['operating_system']}
Hostname         : {system_info['hostname']}
Python Version   : {system_info['python_version']}
Architecture     : {system_info['architecture']}
Kernel           : {system_info['kernel']}
Current User     : {system_info['current_user']}
Home Directory   : {system_info['home_directory']}
Working Directory: {system_info['working_directory']}

===================================
"""
    return report


def main():
    system_info = get_system_info()
    disk_info = get_disk_usage()

    # Print System Report
    report = generate_report(system_info)
    print(report)

    # Print Disk Status
    print("===== DISK MONITORING =====")
    print(f"Total Disk : {format_bytes(disk_info['total'])}")
    print(f"Used Disk  : {format_bytes(disk_info['used'])}")
    print(f"Free Disk  : {format_bytes(disk_info['free'])}")
    print(f"Usage      : {disk_info['percent']}%")

    if disk_info["percent"] >= 90:
        print("Disk Status : CRITICAL")
    elif disk_info["percent"] >= 80:
        print("Disk Status : WARNING")
    else:
        print("Disk Status : HEALTHY")

    # Save report
    report_path = Path("reports/system_report.txt")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()