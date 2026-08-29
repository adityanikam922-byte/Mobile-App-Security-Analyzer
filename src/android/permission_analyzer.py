class PermissionAnalyzer:
    SENSITIVE_PERMISSIONS = {
        "android.permission.INTERNET": "Internet access",
        "android.permission.READ_EXTERNAL_STORAGE": "Read external storage",
        "android.permission.WRITE_EXTERNAL_STORAGE": "Write external storage",
        "android.permission.CAMERA": "Camera access",
        "android.permission.RECORD_AUDIO": "Microphone access",
        "android.permission.ACCESS_FINE_LOCATION": "Precise location access",
        "android.permission.ACCESS_COARSE_LOCATION": "Approximate location access",
        "android.permission.READ_CONTACTS": "Read contacts",
        "android.permission.SEND_SMS": "Send SMS",
    }

    def __init__(self, permissions):
        self.permissions = permissions

    def analyze(self):
        findings = []

        for permission in self.permissions:
            if permission in self.SENSITIVE_PERMISSIONS:
                findings.append({
                    "permission": permission,
                    "risk": self.SENSITIVE_PERMISSIONS[permission]
                })

        return findings