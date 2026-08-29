from pathlib import Path
from androguard.core.apk import APK


class SDKAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        apk = APK(str(self.apk_path))

        return {
            "min_sdk": apk.get_min_sdk_version(),
            "target_sdk": apk.get_target_sdk_version()
        }