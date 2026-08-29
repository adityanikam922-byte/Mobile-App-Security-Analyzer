from pathlib import Path
from androguard.core.apk import APK


class DebuggableAnalyzer:
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

        debuggable = False

        if application is not None:
            value = application.get(
                "{http://schemas.android.com/apk/res/android}debuggable"
            )

            if value == "true":
                debuggable = True

        return {
            "debuggable": debuggable
        }