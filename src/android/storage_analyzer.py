from pathlib import Path
from zipfile import ZipFile


class StorageAnalyzer:
    KEYWORDS = [
        "SharedPreferences",
        "getSharedPreferences",
        "openFileOutput",
        "getExternalStorageDirectory",
        "Environment.getExternalStorage",
    ]

    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        findings = []

        with ZipFile(self.apk_path, "r") as apk:
            for file_name in apk.namelist():
                if not file_name.endswith(".dex"):
                    continue

                content = apk.read(file_name).decode(
                    "utf-8",
                    errors="ignore"
                )

                for keyword in self.KEYWORDS:
                    if keyword in content:
                        findings.append({
                            "type": "possible_insecure_storage",
                            "keyword": keyword,
                            "file": file_name
                        })

        return findings