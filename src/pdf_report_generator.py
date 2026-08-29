import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


class PDFReportGenerator:

    def __init__(
        self,
        results,
        output_file="reports/security_report.pdf"
    ):
        self.results = results
        self.output_file = output_file

    def generate(self):

        os.makedirs(
            os.path.dirname(self.output_file),
            exist_ok=True
        )

        document = SimpleDocTemplate(
            self.output_file,
            pagesize=A4
        )

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "Mobile App Security Analysis Report",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 20))

        apk = self.results["apk_information"]

        elements.append(
            Paragraph(
                "<b>APK Information</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"App Name: {apk.get('app_name')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Package Name: {apk.get('package_name')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Version: {apk.get('version_name')}",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 15))

        risk = self.results["risk_score"]

        elements.append(
            Paragraph(
                "<b>Overall Security Risk</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Risk Score: {risk.get('score')}/100",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Risk Level: {risk.get('level')}",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 15))

        elements.append(
            Paragraph(
                "<b>Security Recommendations</b>",
                styles["Heading2"]
            )
        )

        for number, recommendation in enumerate(
            self.results["recommendations"],
            start=1
        ):
            elements.append(
                Paragraph(
                    f"{number}. {recommendation}",
                    styles["Normal"]
                )
            )

            elements.append(Spacer(1, 5))

        document.build(elements)

        return self.output_file