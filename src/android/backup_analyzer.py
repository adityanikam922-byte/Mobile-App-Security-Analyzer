from pathlib import Path
from androguard.core.apk import APK


class BackupAnalyzer:
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

        allow_backup = None

        if application is not None:
            allow_backup = application.get(
                "{http://schemas.android.com/apk/res/android}allowBackup"
            )

        if allow_backup == "false":
            return {
                "allow_backup": False,
                "risk": "Backup is disabled."
            }

        return {
            "allow_backup": True,
            "risk": "WARNING: APK backups may be allowed."
        }