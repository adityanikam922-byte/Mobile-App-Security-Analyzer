# Mobile App Security Analyzer

## Project Overview

Mobile App Security Analyzer is a Python-based cybersecurity tool designed to perform static security analysis on Android APK files.

The tool analyzes an APK and identifies potential security vulnerabilities, insecure configurations, dangerous permissions, exported components, hardcoded secrets, insecure network URLs, and other security issues.

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
- HTML
- CSS
- JSON


## Installation

Create and activate a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate


## Running the Web Application

Run:

```bash
python src/web_app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

Upload an Android APK file and click **Analyze APK**.


## Reports

After analyzing an APK, the project generates three types of security reports:

### JSON Report

Contains structured security analysis results.

### HTML Report

Provides a browser-friendly security report.

### PDF Report

Provides a downloadable security assessment report.


## Security Analysis Performed

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


## Sample Result

The project was tested using the DIVA Android application.

Example result:

```text
Security Risk Score: 80/100
Risk Level: CRITICAL
```





## Disclaimer

This project is intended for educational purposes and authorized security testing only.

Only analyze applications that you own or have permission to test.

## Author

Aditya 

Cybersecurity Project