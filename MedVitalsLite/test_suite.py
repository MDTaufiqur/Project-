import unittest
from app import DatabaseConnection, VitalTracker, AlertNotificationService, DoctorDashboardProxy, PrescriptionEngine

class TestMedVitalsLiteTDD(unittest.TestCase):

    def setUp(self):
        self.tracker = VitalTracker()
        self.notifier = AlertNotificationService()
        self.tracker.attach(self.notifier)

    def testHeartRateThresholdTriggersWarning(self):
        """Original TDD Test: Critical heart rate (>100) triggers warning"""
        self.tracker.log_vitals("John Doe", 115, "135/85")
        self.assertTrue(self.notifier.alert_triggered)

    def testHeartRateExactlyOneHundredDoesNotAlert(self):
        """Boundary Test: 100 bpm must NOT trigger alert"""
        self.tracker.log_vitals("John Doe", 100, "120/80")
        self.assertFalse(self.notifier.alert_triggered)

    def testHeartRateOneHundredAndOneAlerts(self):
        """Boundary Test: 101 bpm MUST trigger alert"""
        self.tracker.log_vitals("John Doe", 101, "122/81")
        self.assertTrue(self.notifier.alert_triggered)

    def testNegativeHeartRateIsRejected(self):
        """Boundary Test: Negative vital inputs must raise a ValueError"""
        with self.assertRaises(ValueError):
            self.tracker.log_vitals("John Doe", -5, "120/80")

    def testNonNumericHeartRateIsRejected(self):
        """Boundary Test: Non-numeric strings must raise a ValueError"""
        with self.assertRaises(ValueError):
            self.tracker.log_vitals("John Doe", "high", "120/80")

if __name__ == "__main__":
    unittest.main()
