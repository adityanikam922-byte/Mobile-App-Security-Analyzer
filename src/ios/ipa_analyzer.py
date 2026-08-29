from pathlib import Path
from zipfile import ZipFile


class IPAAnalyzer:
    def __init__(self, ipa_path):
        self.ipa_path = Path(ipa_path)

    def analyze(self):
        if not self.ipa_path.exists():
            raise FileNotFoundError(
                f"IPA file not found: {self.ipa_path}"
            )

        if self.ipa_path.suffix.lower() != ".ipa":
            raise ValueError(
                "The selected file is not an IPA file."
            )

        files = []

        with ZipFile(self.ipa_path, "r") as ipa:
            for file_name in ipa.namelist():
                files.append(file_name)

        return {
            "total_files": len(files),
            "payload_files": [
                file_name for file_name in files
                if file_name.startswith("Payload/")
            ]
        }