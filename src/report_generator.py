import json
import os


class ReportGenerator:

    def __init__(self, results, output_file="reports/security_report.json"):
        self.results = results
        self.output_file = output_file

    def generate(self):

        # Create reports folder if it doesn't exist
        os.makedirs(
            os.path.dirname(self.output_file),
            exist_ok=True
        )

        with open(self.output_file, "w") as file:
            json.dump(
                self.results,
                file,
                indent=4,
                default=str
            )

        return self.output_file