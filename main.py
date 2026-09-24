from pathlib import Path

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

    report = generate_report(system_info)

    print(report)

    report_path = Path("reports/system_report.txt")

    report_path.parent.mkdir(parents=True, exist_ok=True)

    report_path.write_text(report)

    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()