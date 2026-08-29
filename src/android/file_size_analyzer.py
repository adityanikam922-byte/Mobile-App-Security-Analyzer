from pathlib import Path


class FileSizeAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = Path(apk_path)

    def analyze(self):
        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        size_bytes = self.apk_path.stat().st_size
        size_mb = size_bytes / (1024 * 1024)

        return {
            "bytes": size_bytes,
            "mb": round(size_mb, 2)
        }