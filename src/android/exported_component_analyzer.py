from pathlib import Path
from androguard.core.apk import APK


class ExportedComponentAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        apk = APK(str(self.apk_path))

        findings = []

        component_groups = {
            "activity": apk.get_activities(),
            "service": apk.get_services(),
            "receiver": apk.get_receivers(),
            "provider": apk.get_providers(),
        }

        for component_type, components in component_groups.items():
            for component in components:
                findings.append({
                    "type": component_type,
                    "name": component
                })

        return findings