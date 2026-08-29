from pathlib import Path
from androguard.core.apk import APK


class CleartextAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        apk = APK(str(self.apk_path))

        manifest = apk.get_android_manifest_xml()
        application = manifest.find("application")

        cleartext = None

        if application is not None:
            cleartext = application.get(
                "{http://schemas.android.com/apk/res/android}"
                "usesCleartextTraffic"
            )

        if cleartext == "true":
            return {
                "cleartext_allowed": True,
                "risk": "WARNING: Cleartext HTTP traffic is allowed."
            }

        return {
            "cleartext_allowed": False,
            "risk": "Cleartext traffic is not explicitly allowed."
        }