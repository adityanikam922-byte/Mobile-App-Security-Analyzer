from pathlib import Path
from androguard.core.apk import APK


class ManifestSecurityAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        apk = APK(str(self.apk_path))
        findings = []

        # Check debuggable configuration
        try:
            application = apk.get_android_manifest_xml().find("application")

            if application is not None:
                debuggable = application.get(
                    "{http://schemas.android.com/apk/res/android}debuggable"
                )

                if debuggable == "true":
                    findings.append({
                        "type": "debuggable_enabled",
                        "risk": "HIGH",
                        "message": "Application debugging is enabled."
                    })

                allow_backup = application.get(
                    "{http://schemas.android.com/apk/res/android}allowBackup"
                )

                if allow_backup == "true":
                    findings.append({
                        "type": "backup_enabled",
                        "risk": "MEDIUM",
                        "message": "Application backups are enabled."
                    })

        except Exception:
            pass

        return findings