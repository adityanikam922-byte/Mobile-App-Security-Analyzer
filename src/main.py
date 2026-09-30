import argparse
from pathlib import Path

from android.apk_analyzer import APKAnalyzer
from android.manifest_analyzer import ManifestAnalyzer
from android.manifest_security_analyzer import ManifestSecurityAnalyzer
from android.permission_analyzer import PermissionAnalyzer
from android.dangerous_permission_analyzer import DangerousPermissionAnalyzer
from android.resource_analyzer import ResourceAnalyzer
from android.security_analyzer import SecurityAnalyzer
from android.native_library_analyzer import NativeLibraryAnalyzer
from android.storage_analyzer import StorageAnalyzer
from android.component_analyzer import ComponentAnalyzer
from android.exported_component_analyzer import ExportedComponentAnalyzer
from android.exported_component_risk_analyzer import ExportedComponentRiskAnalyzer
from android.network_analyzer import NetworkAnalyzer
from android.debuggable_analyzer import DebuggableAnalyzer
from android.backup_analyzer import BackupAnalyzer
from android.cleartext_analyzer import CleartextAnalyzer
from android.certificate_analyzer import CertificateAnalyzer
from android.hash_analyzer import HashAnalyzer
from android.file_size_analyzer import FileSizeAnalyzer
from android.sdk_analyzer import SDKAnalyzer
from android.risk_score_analyzer import RiskScoreAnalyzer
from android.recommendation_analyzer import RecommendationAnalyzer

from report_generator import ReportGenerator
from html_report_generator import HTMLReportGenerator
from pdf_report_generator import PDFReportGenerator
from ios.ipa_analyzer import IPAAnalyzer


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "reports"

# Create reports directory automatically if it does not exist
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def analyze_apk(file_path):

    apk_results = APKAnalyzer(file_path).analyze()
    manifest_results = ManifestAnalyzer(file_path).analyze()

    manifest_security_results = ManifestSecurityAnalyzer(
        file_path
    ).analyze()

    permission_results = PermissionAnalyzer(
        manifest_results["permissions"]
    ).analyze()

    dangerous_permission_results = DangerousPermissionAnalyzer(
        manifest_results["permissions"]
    ).analyze()

    resource_results = ResourceAnalyzer(file_path).analyze()
    security_results = SecurityAnalyzer(file_path).analyze()
    storage_results = StorageAnalyzer(file_path).analyze()
    component_results = ComponentAnalyzer(file_path).analyze()

    exported_components = ExportedComponentAnalyzer(
        file_path
    ).analyze()

    exported_component_risk_results = ExportedComponentRiskAnalyzer(
        exported_components
    ).analyze()

    network_results = NetworkAnalyzer(file_path).analyze()
    debuggable_result = DebuggableAnalyzer(file_path).analyze()
    backup_result = BackupAnalyzer(file_path).analyze()
    cleartext_result = CleartextAnalyzer(file_path).analyze()
    certificate_results = CertificateAnalyzer(file_path).analyze()
    hash_results = HashAnalyzer(file_path).analyze()
    file_size_results = FileSizeAnalyzer(file_path).analyze()
    sdk_results = SDKAnalyzer(file_path).analyze()
    native_libraries = NativeLibraryAnalyzer(file_path).analyze()

    risk_results = RiskScoreAnalyzer(
        dangerous_permission_results,
        security_results,
        storage_results,
        exported_components,
        network_results,
        debuggable_result,
        backup_result
    ).analyze()

    recommendation_results = RecommendationAnalyzer(
        manifest_security_results,
        dangerous_permission_results,
        security_results,
        exported_component_risk_results,
        network_results,
        debuggable_result,
        backup_result
    ).analyze()

    report_data = {
        "apk_information": apk_results,
        "file_size": file_size_results,
        "sdk_information": sdk_results,
        "manifest_security": manifest_security_results,
        "permissions": permission_results,
        "dangerous_permissions": dangerous_permission_results,
        "resources": resource_results,
        "security_findings": security_results,
        "storage_findings": storage_results,
        "components": component_results,
        "exported_components": exported_components,
        "exported_component_risks": exported_component_risk_results,
        "network_security": network_results,
        "debuggable": debuggable_result,
        "backup_security": backup_result,
        "cleartext_traffic": cleartext_result,
        "certificates": certificate_results,
        "hashes": hash_results,
        "risk_score": risk_results,
        "recommendations": recommendation_results,
        "native_libraries": native_libraries
    }

    # Generate reports
    report_path = ReportGenerator(
        report_data,
        str(REPORT_DIR / "security_report.json")
    ).generate()

    html_report_path = HTMLReportGenerator(
        report_data,
        str(REPORT_DIR / "security_report.html")
    ).generate()

    pdf_report_path = PDFReportGenerator(
        report_data,
        str(REPORT_DIR / "security_report.pdf")
    ).generate()

    print("\nAPK Analysis Results")
    print("-" * 30)

    for key, value in apk_results.items():
        print(f"{key}: {value}")

    print("\nAPK File Size Analysis Results")
    print("-" * 30)
    print(f"Size: {file_size_results['bytes']} bytes")
    print(f"Size: {file_size_results['mb']} MB")

    print("\nSDK Analysis Results")
    print("-" * 30)
    print(f"Minimum SDK Version: {sdk_results['min_sdk']}")
    print(f"Target SDK Version: {sdk_results['target_sdk']}")

    print("\nManifest Security Analysis Results")
    print("-" * 30)

    if manifest_security_results:
        for finding in manifest_security_results:
            print(
                f"Type: {finding['type']} | "
                f"Risk: {finding['risk']} | "
                f"Message: {finding['message']}"
            )
    else:
        print("No manifest security issues detected.")

    print("\nPermission Analysis Results")
    print("-" * 30)

    for finding in permission_results:
        print(f"{finding['permission']}: {finding['risk']}")

    print("\nDangerous Permission Analysis Results")
    print("-" * 30)

    if dangerous_permission_results:
        for finding in dangerous_permission_results:
            print(
                f"Permission: {finding['permission']} | "
                f"Risk: {finding['risk']}"
            )
    else:
        print("No dangerous permissions detected.")

    print("\nAPK Resource Analysis Results")
    print("-" * 30)
    print("XML files:", len(resource_results["xml_files"]))
    print("Image files:", len(resource_results["image_files"]))
    print("Asset files:", len(resource_results["asset_files"]))

    print("\nSecurity Analysis Results")
    print("-" * 30)

    for finding in security_results:
        print(f"Type: {finding['type']} | File: {finding['file']}")

    print("\nStorage Security Analysis Results")
    print("-" * 30)

    for finding in storage_results:
        print(f"Keyword: {finding['keyword']} | File: {finding['file']}")

    print("\nComponent Analysis Results")
    print("-" * 30)

    for component_type, components in component_results.items():
        print(f"{component_type.capitalize()}: {len(components)}")

    print("\nExported Component Analysis Results")
    print("-" * 30)

    for component in exported_components:
        print(
            f"Type: {component['type']} | "
            f"Name: {component['name']}"
        )

    print("\nExported Component Risk Analysis Results")
    print("-" * 30)

    for finding in exported_component_risk_results:
        print(
            f"Type: {finding['type']} | "
            f"Name: {finding['name']} | "
            f"Risk: {finding['risk']}"
        )

    print("\nNetwork Security Analysis Results")
    print("-" * 30)

    if network_results:
        for finding in network_results:
            print(
                f"Type: {finding['type']} | "
                f"File: {finding['file']} | "
                f"URL: {finding['url']}"
            )
    else:
        print("No insecure HTTP URLs detected.")

    print("\nDebuggable APK Analysis Results")
    print("-" * 30)

    if debuggable_result["debuggable"]:
        print("WARNING: APK is debuggable.")
    else:
        print("APK debugging is disabled.")

    print("\nBackup Security Analysis Results")
    print("-" * 30)
    print(backup_result["risk"])

    print("\nCleartext Traffic Analysis Results")
    print("-" * 30)
    print(cleartext_result["risk"])
