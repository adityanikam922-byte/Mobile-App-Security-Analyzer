class RiskScoreAnalyzer:
    def __init__(
        self,
        dangerous_permissions,
        security_findings,
        storage_findings,
        exported_components,
        network_findings,
        debuggable_result,
        backup_result
    ):
        self.dangerous_permissions = dangerous_permissions
        self.security_findings = security_findings
        self.storage_findings = storage_findings
        self.exported_components = exported_components
        self.network_findings = network_findings
        self.debuggable_result = debuggable_result
        self.backup_result = backup_result

    def analyze(self):
        score = 0

        score += len(self.dangerous_permissions) * 5
        score += len(self.security_findings) * 5
        score += len(self.storage_findings) * 5
        score += len(self.network_findings) * 10

        if self.debuggable_result["debuggable"]:
            score += 15

        if backup_result_allowed(self.backup_result):
            score += 10

        if score >= 70:
            level = "CRITICAL"
        elif score >= 40:
            level = "HIGH"
        elif score >= 20:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "score": min(score, 100),
            "level": level
        }


def backup_result_allowed(backup_result):
    return "WARNING" in backup_result.get("risk", "")