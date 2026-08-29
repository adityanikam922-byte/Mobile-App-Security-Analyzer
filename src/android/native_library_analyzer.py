from pathlib import Path
from zipfile import ZipFile


class NativeLibraryAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        libraries = []

        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        with ZipFile(self.apk_path, "r") as apk:
            for file_name in apk.namelist():
                if file_name.startswith("lib/") and file_name.endswith(".so"):
                    libraries.append(file_name)

        return libraries