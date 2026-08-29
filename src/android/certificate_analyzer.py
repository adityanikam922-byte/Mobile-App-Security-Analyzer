from pathlib import Path
from zipfile import ZipFile


class CertificateAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        certificates = []

        with ZipFile(self.apk_path, "r") as apk:
            for file_name in apk.namelist():

                if file_name.startswith("META-INF/"):

                    if (
                        file_name.endswith(".RSA")
                        or file_name.endswith(".DSA")
                        or file_name.endswith(".EC")
                    ):
                        certificates.append(file_name)

        return certificates