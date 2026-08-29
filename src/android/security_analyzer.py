from pathlib import Path
from zipfile import ZipFile
import re


class SecurityAnalyzer:
    PATTERNS = {
        "possible_api_key": r"(?i)(api[_-]?key)",
        "possible_password": r"(?i)(password|passwd)",
        "possible_token": r"(?i)(token|secret)",
    }

    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        findings = []

        with ZipFile(self.apk_path, "r") as apk:
            for file_name in apk.namelist():

                try:
                    content = apk.read(file_name).decode(
                        "utf-8",
                        errors="ignore"
                    )

                    for finding_type, pattern in self.PATTERNS.items():
                        if re.search(pattern, content):
                            findings.append({
                                "type": finding_type,
                                "file": file_name
                            })

                except Exception:
                    continue

        return findings