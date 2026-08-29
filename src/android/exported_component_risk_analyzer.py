class ExportedComponentRiskAnalyzer:
    def __init__(self, exported_components):
        self.exported_components = exported_components

    def analyze(self):
        findings = []

        for component in self.exported_components:
            component_type = component.get("type")
            component_name = component.get("name")

            if component_type == "activity":
                risk = "MEDIUM"
                message = (
                    "Exported activity may be accessible "
                    "by other applications."
                )

            elif component_type == "provider":
                risk = "HIGH"
                message = (
                    "Exported content provider may expose "
                    "application data to other applications."
                )

            elif component_type in ["service", "receiver"]:
                risk = "MEDIUM"
                message = (
                    f"Exported {component_type} may be accessible "
                    "by other applications."
                )

            else:
                risk = "LOW"
                message = "Exported component detected."

            findings.append({
                "type": component_type,
                "name": component_name,
                "risk": risk,
                "message": message
            })

        return findings