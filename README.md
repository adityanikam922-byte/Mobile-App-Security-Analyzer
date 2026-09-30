# Mobile App Security Analyzer
## Project Overview

Mobile App Security Analyzer is a Python-based cybersecurity tool designed to perform static security analysis on Android APK files.

The tool analyzes APK files and identifies potential security vulnerabilities, insecure configurations, dangerous permissions, exported components, hardcoded secrets, insecure network URLs, and other security issues.

The project generates security reports in JSON, HTML, and PDF formats and provides a web-based interface for uploading and analyzing APK files.

## Features

- APK Information Analysis
- File Size Analysis
- SDK Version Analysis
- Android Manifest Security Analysis
- Permission Analysis
- Dangerous Permission Detection
- Resource Analysis
- Hardcoded Secret Detection
- Storage Security Analysis
- Component Analysis
- Exported Component Detection
- Exported Component Risk Analysis
- Network Security Analysis
- Debuggable APK Detection
- Backup Security Analysis
- Cleartext Traffic Analysis
- Certificate Analysis
- APK Hash Generation
- Native Library Detection
- Security Risk Score Calculation
- Security Recommendations
- JSON Report Generation
- HTML Report Generation
- PDF Report Generation
- Web-Based APK Upload Interface

## Technologies Used

- Python
- Flask
- Androguard
- ReportLab
- HTML
- CSS
- JSON

## Requirements

- Python 3
- pip
- Git

Python dependencies are listed in:

`requirements.txt`

## Installation and Usage

### Windows

Open PowerShell and run:

```powershell
git clone https://github.com/adityanikam922-byte/Mobile-App-Security-Analyzer.git
cd Mobile-App-Security-Analyzer
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python src\web_app.py

Then open:

http://127.0.0.1:5000

### macOS
git clone https://github.com/adityanikam922-byte/Mobile-App-Security-Analyzer.git
cd Mobile-App-Security-Analyzer
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 src/web_app.py

Then open:
127.0.0.1:5000

### Linux / Kali Linux

Open Terminal and run:
git clone https://github.com/adityanikam922-byte/Mobile-App-Security-Analyzer.git
cd Mobile-App-Security-Analyzer
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 src/web_app.py
Then open:

http://127.0.0.1:5000

## Using the Analyzer

1. Start the Flask web application.
2. Open `http://127.0.0.1:5000` in a web browser.
3. Upload an Android APK file.
4. Start the APK analysis.
5. Review the security analysis results.
6. Generate the available security reports.

## Security Analysis

The analyzer checks for potential security issues including:

- Dangerous Android permissions
- Debuggable applications
- Application backup configuration
- Hardcoded passwords and API keys
- Possible security tokens
- Insecure HTTP URLs
- Insecure data storage patterns
- Exported Android components
- Exposed content providers
- Native libraries
- APK hashes
- Application certificates

## Reports

After analyzing an APK, the project can generate:

### JSON Report

Contains structured security analysis results.

### HTML Report

Provides a browser-friendly security report.

### PDF Report

Provides a downloadable security assessment report.

## Sample Result

The project was tested using the DIVA Android application.

Example result:

- **Security Risk Score:** 80/100
- **Risk Level:** CRITICAL

## Disclaimer

This project is intended for educational purposes and authorized security testing only.

Only analyze applications that you own or have permission to test.

## Author

**Aditya Nikam**
