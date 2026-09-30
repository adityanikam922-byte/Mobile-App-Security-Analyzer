Mobile App Security Analyzer
Project Overview

Mobile App Security Analyzer is a Python-based cybersecurity tool designed to perform static security analysis on Android APK files.

The tool analyzes an APK and identifies potential security vulnerabilities, insecure configurations, dangerous permissions, exported components, hardcoded secrets, insecure network URLs, and other security issues.

The project generates security reports in JSON, HTML, and PDF formats and provides a web-based interface for uploading and analyzing APK files.

Features
APK Information Analysis
File Size Analysis
SDK Version Analysis
Android Manifest Security Analysis
Permission Analysis
Dangerous Permission Detection
Resource Analysis
Hardcoded Secret Detection
Storage Security Analysis
Component Analysis
Exported Component Detection
Exported Component Risk Analysis
Network Security Analysis
Debuggable APK Detection
Backup Security Analysis
Cleartext Traffic Analysis
Certificate Analysis
APK Hash Generation
Native Library Detection
Security Risk Score Calculation
Security Recommendations
JSON Report Generation
HTML Report Generation
PDF Report Generation
Web-Based APK Upload Interface
Technologies Used
Python
Flask
Androguard
ReportLab
HTML
CSS
JSON
Requirements

The following software is required:

Python 3
pip
Git

The required Python packages are listed in:

requirements.txt
Installation and Usage
Windows

Open PowerShell and run:

git clone https://github.com/adityanikam922-byte/Mobile-App-Security-Analyzer.git
cd Mobile-App-Security-Analyzer
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python src\web_app.py

After the application starts, open:

http://127.0.0.1:5000
macOS

Open Terminal and run:

git clone https://github.com/adityanikam922-byte/Mobile-App-Security-Analyzer.git
cd Mobile-App-Security-Analyzer
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 src/web_app.py

After the application starts, open:

http://127.0.0.1:5000
Linux / Kali Linux

Open Terminal and run:

git clone https://github.com/adityanikam922-byte/Mobile-App-Security-Analyzer.git
cd Mobile-App-Security-Analyzer
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 src/web_app.py

After the application starts, open:

http://127.0.0.1:5000
Using the Analyzer
Start the Flask web application.
Open http://127.0.0.1:5000 in a web browser.
Upload an Android APK file.
Start the APK analysis.
Review the security analysis results.
Generate the available security reports.
Reports

After analyzing an APK, the project can generate:

JSON Report

Contains structured security analysis results.

HTML Report

Provides a browser-friendly security report.

PDF Report

Provides a downloadable security assessment report.

Generated reports are stored in:

reports/
Security Analysis Performed

The analyzer checks for potential security issues including:

Dangerous Android permissions
Debuggable applications
Application backup configuration
Hardcoded passwords and API keys
Possible security tokens
Insecure HTTP URLs
Insecure data storage patterns
Exported Android components
Exposed content providers
Native libraries
APK hashes
Application certificates
Project Structure
Mobile-App-Security-Analyzer/
│
├── .gitignore
├── README.md
├── requirements.txt
│
└── src/
    │
    ├── main.py
    ├── web_app.py
    │
    ├── android/
    │   ├── apk_analyzer.py
    │   ├── manifest_analyzer.py
    │   ├── manifest_security_analyzer.py
    │   ├── permission_analyzer.py
    │   ├── dangerous_permission_analyzer.py
    │   ├── resource_analyzer.py
    │   ├── security_analyzer.py
    │   ├── native_library_analyzer.py
    │   ├── storage_analyzer.py
    │   ├── component_analyzer.py
    │   ├── exported_component_analyzer.py
    │   ├── exported_component_risk_analyzer.py
    │   ├── network_analyzer.py
    │   ├── debuggable_analyzer.py
    │   ├── backup_analyzer.py
    │   ├── cleartext_analyzer.py
    │   ├── certificate_analyzer.py
    │   ├── hash_analyzer.py
    │   ├── file_size_analyzer.py
    │   ├── sdk_analyzer.py
    │   ├── risk_score_analyzer.py
    │   └── recommendation_analyzer.py
    │
    ├── ios/
    │   └── ipa_analyzer.py
    │
    ├── report_generator.py
    ├── html_report_generator.py
    └── pdf_report_generator.py
Sample Result

The project was tested using the DIVA Android application.

Example result:

Security Risk Score: 80/100
Risk Level: CRITICAL
Disclaimer

This project is intended for educational purposes and authorized security testing only.

Only analyze applications that you own or have permission to test.

Author

Aditya Nikam

Cybersecurity Project


