from flask import Flask, request, render_template_string, send_from_directory
import os
import sys
import json
from werkzeug.utils import secure_filename

# Allow importing main.py from the src folder
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SRC_DIR)

sys.path.insert(0, SRC_DIR)

from main import analyze_apk


app = Flask(__name__)

# Project folders
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Mobile App Security Analyzer</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #eef1f7;
            color: #1f2937;
        }

        header {
            background: #172033;
            color: white;
            padding: 18px 30px;
        }

        header h1 {
            margin: 0;
            font-size: 28px;
        }

        header p {
            margin: 6px 0 0;
            color: #cbd5e1;
        }

        .container {
            width: 900px;
            max-width: 92%;
            margin: 55px auto;
        }

        .main-card {
            background: white;
            padding: 28px;
            border-radius: 14px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        }

        h2 {
            color: #344b70;
            margin-top: 0;
        }

        .upload-box {
            border: 2px dashed #3567c8;
            padding: 30px;
            text-align: center;
            border-radius: 10px;
            margin-top: 20px;
            background: #f8faff;
        }

        input[type=file] {
            margin-bottom: 15px;
        }

        button {
            background: #315db8;
            color: white;
            border: none;
            padding: 14px 28px;
            font-size: 16px;
            border-radius: 7px;
            cursor: pointer;
        }

        button:hover {
            background: #244a94;
        }

        .success {
            margin-top: 25px;
            padding: 20px;
            background: #dff5e7;
            border-left: 4px solid #23864a;
            border-radius: 8px;
        }

        .success h3 {
            margin: 0 0 10px;
        }

        .error {
            margin-top: 20px;
            padding: 15px;
            background: #fee2e2;
            color: #991b1b;
            border-radius: 8px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-top: 20px;
        }

        .summary-cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-top: 20px;
        }

        .card {
            padding: 20px;
            border-radius: 10px;
            color: white;
            min-height: 130px;
        }

        .card-title {
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 18px;
        }

        .card-value {
            font-size: 24px;
            font-weight: bold;
            word-break: break-word;
        }

        .blue {
            background: #3565c1;
        }

        .purple {
            background: #6b35c5;
        }

        .orange {
            background: #f05a00;
        }

        .red {
            background: #df2424;
        }

        .summary {
            margin-top: 30px;
        }

        .summary h2 {
            margin-bottom: 8px;
        }

        .summary p {
            color: #64748b;
        }

        .report-buttons {
            margin-top: 25px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .report-buttons a {
            background: #172033;
            color: white;
            text-decoration: none;
            padding: 13px 20px;
            border-radius: 6px;
        }

        .report-buttons a:hover {
            background: #34435c;
        }

        footer {
            text-align: center;
            margin-top: 60px;
            color: #64748b;
        }

        @media (max-width: 800px) {

            .cards,
            .summary-cards {
                grid-template-columns: repeat(2, 1fr);
            }

        }

        @media (max-width: 500px) {

            .cards,
            .summary-cards {
                grid-template-columns: 1fr;
            }

        }

    </style>

</head>


<body>

<header>

    <h1>Mobile App Security Analyzer</h1>

    <p>APK Static Security Analysis Tool</p>

</header>


<div class="container">

    <div class="main-card">

        <h2>Analyze Android APK</h2>

        <p>
            Upload an APK file to perform a comprehensive static security analysis.
        </p>


        <form method="POST" enctype="multipart/form-data">

            <div class="upload-box">

                <input
                    type="file"
                    name="apk_file"
                    accept=".apk"
                    required
                >

                <br>

                <button type="submit">
                    Analyze APK
                </button>

            </div>

        </form>


        {% if error %}

            <div class="error">
                {{ error }}
            </div>

        {% endif %}


        {% if analyzed %}

            <div class="success">

                <h3>✓ APK Analyzed Successfully!</h3>

                <p>
                    Security analysis has been completed successfully.
                </p>

            </div>


            <div class="cards">

                <div class="card blue">

                    <div class="card-title">
                        Application
                    </div>

                    <div class="card-value">
                        {{ app_name }}
                    </div>

                </div>


                <div class="card purple">

                    <div class="card-title">
                        Package Name
                    </div>

                    <div class="card-value">
                        {{ package_name }}
                    </div>

                </div>


                <div class="card orange">

                    <div class="card-title">
                        Security Score
                    </div>

                    <div class="card-value">
                        {{ security_score }}/100
                    </div>

                </div>


                <div class="card red">

                    <div class="card-title">
                        Risk Level
                    </div>

                    <div class="card-value">
                        {{ risk_level }}
                    </div>

                </div>

            </div>


            <div class="summary">

                <h2>Analysis Summary</h2>

                <p>
                    Key security findings detected during APK analysis.
                </p>


                <div class="summary-cards">

                    <div class="card red">

                        <div class="card-title">
                            Dangerous Permissions
                        </div>

                        <div class="card-value">
                            {{ dangerous_permissions_count }}
                        </div>

                    </div>


                    <div class="card orange">

                        <div class="card-title">
                            Exported Components
                        </div>

                        <div class="card-value">
                            {{ exported_components_count }}
                        </div>

                    </div>


                    <div class="card purple">

                        <div class="card-title">
                            Security Findings
                        </div>

                        <div class="card-value">
                            {{ security_findings_count }}
                        </div>

                    </div>


                    <div class="card blue">

                        <div class="card-title">
                            Network Issues
                        </div>

                        <div class="card-value">
                            {{ network_issues_count }}
                        </div>

                    </div>

                </div>

            </div>


            <div class="report-buttons">

                <a href="/reports/security_report.html" target="_blank">
                    View HTML Report
                </a>

                <a href="/reports/security_report.pdf" target="_blank">
                    View PDF Report
                </a>

                <a href="/reports/security_report.json" target="_blank">
                    View JSON Report
                </a>

            </div>

        {% endif %}

    </div>


    <footer>
        Mobile App Security Analyzer | Internship Project
    </footer>

</div>

</body>

</html>
"""


def get_value(data, keys, default=None):
    """
    Safely search for a value using multiple possible key names.
    """

    if not isinstance(data, dict):
        return default

    for key in keys:
        if key in data and data[key] is not None:
            return data[key]

    return default


def get_count(value):

    if value is None:
        return 0

    if isinstance(value, (list, dict, tuple, set)):
        return len(value)

    if isinstance(value, int):
        return value

    return 0


@app.route("/", methods=["GET", "POST"])
def home():

    analyzed = False
    error = None
    result = {}

    # Default values
    app_name = "Unknown"
    package_name = "Unknown"

    security_score = 0
    risk_level = "UNKNOWN"

    dangerous_permissions_count = 0
    exported_components_count = 0
    security_findings_count = 0
    network_issues_count = 0


    if request.method == "POST":

        if "apk_file" not in request.files:

            error = "No APK file selected."

        else:

            apk_file = request.files["apk_file"]

            if apk_file.filename == "":

                error = "Please select an APK file."

            elif not apk_file.filename.lower().endswith(".apk"):

                error = "Please upload a valid APK file."

            else:

                try:

                    # Create safe filename
                    filename = secure_filename(apk_file.filename)

                    apk_path = os.path.join(
                        UPLOAD_FOLDER,
                        filename
                    )

                    # Save APK
                    apk_file.save(apk_path)


                    # Run analysis
                    analysis_result = analyze_apk(apk_path)


                    # Some versions of analyze_apk()
                    # return None but generate the reports.
                    if isinstance(analysis_result, dict):

                        result = analysis_result

                    else:

                        result = {}


                    # Load generated JSON report
                    json_report_path = os.path.join(
                        REPORT_FOLDER,
                        "security_report.json"
                    )


                    if os.path.exists(json_report_path):

                        try:

                            with open(
                                json_report_path,
                                "r",
                                encoding="utf-8"
                            ) as report_file:

                                json_result = json.load(report_file)


                            if isinstance(json_result, dict):

                                # Use JSON report if analyzer returned None
                                if not result:
                                    result = json_result

                                else:
                                    result.update(json_result)

                        except Exception:
                            pass


                    # If analysis completed, show results
                    if result:

                        analyzed = True

                    elif os.path.exists(json_report_path):

                        analyzed = True


                    # -----------------------------
                    # APK INFORMATION
                    # -----------------------------

                    apk_info = get_value(
                        result,
                        ["apk_info", "apk_information"],
                        {}
                    )


                    if not isinstance(apk_info, dict):
                        apk_info = {}


                    app_name = get_value(
                        apk_info,
                        ["app_name", "application_name", "name"],
                        get_value(
                            result,
                            ["app_name", "application_name"],
                            "Unknown"
                        )
                    )


                    package_name = get_value(
                        apk_info,
                        ["package_name", "package"],
                        get_value(
                            result,
                            ["package_name", "package"],
                            "Unknown"
                        )
                    )


                    # -----------------------------
                    # SECURITY SCORE
                    # -----------------------------

                    risk_data = get_value(
                        result,
                        ["risk_score", "security_score"],
                        {}
                    )


                    if isinstance(risk_data, dict):

                        security_score = get_value(
                            risk_data,
                            ["score", "security_score"],
                            0
                        )


                        risk_level = get_value(
                            risk_data,
                            ["level", "risk_level"],
                            "UNKNOWN"
                        )


                    elif isinstance(risk_data, (int, float)):

                        security_score = risk_data

                        risk_level = get_value(
                            result,
                            ["risk_level"],
                            "UNKNOWN"
                        )


                    # Also check direct keys
                    direct_score = get_value(
                        result,
                        ["score"],
                        None
                    )


                    if direct_score is not None:

                        security_score = direct_score


                    direct_level = get_value(
                        result,
                        ["risk_level", "level"],
                        None
                    )


                    if direct_level is not None:

                        risk_level = direct_level


                    # -----------------------------
                    # DANGEROUS PERMISSIONS
                    # -----------------------------

                    dangerous_permissions = get_value(
                        result,
                        [
                            "dangerous_permissions",
                            "dangerous_permission"
                        ],
                        []
                    )


                    dangerous_permissions_count = get_count(
                        dangerous_permissions
                    )


                    # -----------------------------
                    # EXPORTED COMPONENTS
                    # -----------------------------

                    exported_components = get_value(
                        result,
                        [
                            "exported_components",
                            "exported_component"
                        ],
                        []
                    )


                    exported_components_count = get_count(
                        exported_components
                    )


                    # -----------------------------
                    # SECURITY FINDINGS
                    # -----------------------------

                    findings = get_value(
                        result,
                        [
                            "security_findings",
                            "findings",
                            "security_issues"
                        ],
                        []
                    )


                    security_findings_count = get_count(findings)


                    # -----------------------------
                    # NETWORK ISSUES
                    # -----------------------------

                    network_issues = get_value(
                        result,
                        [
                            "network_issues",
                            "network_security_issues"
                        ],
                        []
                    )


                    network_issues_count = get_count(network_issues)


                    # Make score clean
                    try:
                        security_score = int(security_score)
                    except Exception:
                        security_score = 0


                    risk_level = str(risk_level).upper()


                    # Analysis succeeded if reports exist
                    if os.path.exists(json_report_path):
                        analyzed = True


                    if not analyzed:
                        error = (
                            "Analysis completed, but no result data "
                            "was returned."
                        )


                except Exception as e:

                    error = f"Error during APK analysis: {str(e)}"


    return render_template_string(

        HTML_PAGE,

        analyzed=analyzed,
        error=error,

        app_name=app_name,
        package_name=package_name,

        security_score=security_score,
        risk_level=risk_level,

        dangerous_permissions_count=dangerous_permissions_count,

        exported_components_count=exported_components_count,

        security_findings_count=security_findings_count,

        network_issues_count=network_issues_count
    )


@app.route("/reports/<path:filename>")
def view_report(filename):

    return send_from_directory(
        REPORT_FOLDER,
        filename
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )