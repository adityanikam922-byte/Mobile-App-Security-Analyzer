class RecommendationAnalyzer:
    def __init__(
        self,
        manifest_security_results,
        dangerous_permission_results,
        security_results,
        exported_component_risk_results,
        network_results,
        debuggable_result,
        backup_result
    ):
        self.manifest_security_results = manifest_security_results
        self.dangerous_permission_results = dangerous_permission_results
        self.security_results = security_results
        self.exported_component_risk_results = exported_component_risk_results
        self.network_results = network_results
        self.debuggable_result = debuggable_result
        self.backup_result = backup_result

    def analyze(self):
        recommendations = []

        if self.debuggable_result.get("debuggable"):
            recommendations.append(
                "Disable android:debuggable in production builds."
            )

        if "WARNING" in self.backup_result.get("risk", ""):
            recommendations.append(
                "Disable application backups if sensitive data is stored."
            )

        if self.dangerous_permission_results:
            recommendations.append(
                "Review dangerous permissions and remove unnecessary permissions."
            )

        if self.security_results:
            recommendations.append(
                "Avoid hardcoded passwords, API keys, tokens, and secrets."
            )

        if self.network_results:
            recommendations.append(
                "Use HTTPS instead of insecure HTTP connections."
            )

        high_risk_components = [
            component
            for component in self.exported_component_risk_results
            if component.get("risk") == "HIGH"
        ]

        if high_risk_components:
            recommendations.append(
                "Secure exported content providers with proper permissions."
            )

        medium_risk_components = [
            component
            for component in self.exported_component_risk_results
            if component.get("risk") == "MEDIUM"
        ]

        if medium_risk_components:
            recommendations.append(
                "Review exported components and restrict unnecessary access."
            )

        return recommendations