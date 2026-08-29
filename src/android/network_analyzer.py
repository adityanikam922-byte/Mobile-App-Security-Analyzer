from pathlib import Path
from zipfile import ZipFile
import re


class NetworkAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        findings = []

        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        found_urls = set()

        with ZipFile(self.apk_path, "r") as apk:
            for file_name in apk.namelist():

                try:
                    content = apk.read(file_name).decode(
                        "utf-8",
                        errors="ignore"
                    )

                    urls = re.findall(
                        r'http://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s"\'<>]*)?',
                        content
                    )

                    for url in urls:

                        if "schemas.android.com" in url:
                            continue

                        if url not in found_urls:
                            found_urls.add(url)

                            findings.append({
                                "type": "insecure_http_url",
                                "file": file_name,
                                "url": url
                            })

                except Exception:
                    continue

        return findings