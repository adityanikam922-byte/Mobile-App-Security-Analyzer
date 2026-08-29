import os


class HTMLReportGenerator:

    def __init__(
        self,
        results,
        output_file="reports/security_report.html"
    ):
        self.results = results
        self.output_file = output_file

    def generate(self):

        os.makedirs(
            os.path.dirname(self.output_file),
            exist_ok=True
        )

        apk = self.results["apk_information"]
        file_size = self.results["file_size"]
        sdk = self.results["sdk_information"]
        risk = self.results["risk_score"]
        recommendations = self.results["recommendations"]

        html = f"""
<!DOCTYPE html>
<html>

<head>

<title>Mobile Security Report</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background-color: #f4f6f9;
    margin: 40px;
}}

h1 {{
    color: #1f2937;
}}

h2 {{
    color: #2563eb;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 5px;
}}

.card {{
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
}}

.critical {{
    color: red;
    font-weight: bold;
}}

.high {{
    color: orange;
    font-weight: bold;
}}

table {{
    width: 100%;
    border-collapse: collapse;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}}

th {{
    background-color: #2563eb;
    color: white;
}}

</style>

</head>

<body>

<h1>Mobile App Security Analysis Report</h1>

<div class="card">

<h2>APK Information</h2>

<table>

<tr>
<th>Property</th>
<th>Value</th>
</tr>

<tr>
<td>App Name</td>
<td>{apk.get("app_name")}</td>
</tr>

<tr>
<td>Package Name</td>
<td>{apk.get("package_name")}</td>
</tr>

<tr>
<td>Version</td>
<td>{apk.get("version_name")}</td>
</tr>

<tr>
<td>File Size</td>
<td>{file_size.get("mb")} MB</td>
</tr>

<tr>
<td>Minimum SDK</td>
<td>{sdk.get("min_sdk")}</td>
</tr>

<tr>
<td>Target SDK</td>
<td>{sdk.get("target_sdk")}</td>
</tr>

</table>

</div>


<div class="card">

<h2>Overall Security Risk</h2>

<p>
Security Score:
<strong>{risk.get("score")}/100</strong>
</p>

<p>
Risk Level:
<span class="critical">
{risk.get("level")}
</span>
</p>

</div>


<div class="card">

<h2>Dangerous Permissions</h2>

<ul>
"""

        for permission in self.results["dangerous_permissions"]:

            html += f"""
<li>
<strong>{permission["permission"]}</strong>
— {permission["risk"]}
</li>
"""

        html += """
</ul>

</div>


<div class="card">

<h2>Security Findings</h2>

<ul>
"""

        for finding in self.results["security_findings"]:

            html += f"""
<li>
<strong>{finding["type"]}</strong>
— Found in {finding["file"]}
</li>
"""

        html += """
</ul>

</div>


<div class="card">

<h2>Security Recommendations</h2>

<ol>
"""

        for recommendation in recommendations:

            html += f"""
<li>{recommendation}</li>
"""

        html += """
</ol>

</div>

</body>

</html>
"""

        with open(
            self.output_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        return self.output_file