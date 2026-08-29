class DangerousPermissionAnalyzer:
    def __init__(self, permissions):
        self.permissions = permissions

        self.dangerous_permissions = {
            "android.permission.CAMERA": "Camera access",
            "android.permission.RECORD_AUDIO": "Microphone access",
            "android.permission.ACCESS_FINE_LOCATION": "Precise location access",
            "android.permission.ACCESS_COARSE_LOCATION": "Approximate location access",
            "android.permission.READ_CONTACTS": "Read contacts",
            "android.permission.WRITE_CONTACTS": "Modify contacts",
            "android.permission.READ_SMS": "Read SMS messages",
            "android.permission.SEND_SMS": "Send SMS messages",
            "android.permission.READ_CALL_LOG": "Read call logs",
            "android.permission.CALL_PHONE": "Make phone calls",
            "android.permission.READ_EXTERNAL_STORAGE": "Read external storage",
            "android.permission.WRITE_EXTERNAL_STORAGE": "Write external storage",
        }

    def analyze(self):
        findings = []

        for permission in self.permissions:
            if permission in self.dangerous_permissions:
                findings.append({
                    "permission": permission,
                    "risk": self.dangerous_permissions[permission]
                })

        return findings