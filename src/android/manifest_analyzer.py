from pathlib import Path
from androguard.core.apk import APK


class ManifestAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        apk = APK(str(self.apk_path))

        activities = apk.get_activities()
        services = apk.get_services()
        receivers = apk.get_receivers()

        return {
            "package_name": apk.get_package(),
            "permissions": apk.get_permissions(),
            "activities": activities,
            "services": services,
            "receivers": receivers,
        }