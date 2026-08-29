from pathlib import Path
from androguard.core.apk import APK


class APKAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        if self.apk_path.suffix.lower() != ".apk":
            raise ValueError(
                "The selected file is not an APK file."
            )

        apk = APK(str(self.apk_path))

        return {
            "app_name": apk.get_app_name(),
            "package_name": apk.get_package(),
            "version_name": apk.get_androidversion_name(),
            "version_code": apk.get_androidversion_code(),
        }