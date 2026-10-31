import sqlite3

# --- SINGLETON PATTERN (Database Connection Helper) ---
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def get_connection(self):
        return sqlite3.connect('medvitals.db')


# --- OBSERVER PATTERN (Mod 4: Alerts & Notifications) ---
class VitalObserver:
    def update(self, patient_name, heart_rate):
        pass

class AlertNotificationService(VitalObserver):
    def __init__(self):
        self.alert_triggered = False

    def update(self, patient_name, heart_rate):
        if heart_rate > 100:
            self.alert_triggered = True
            print(f"\n[ALERT 🚨] Critical Notification: {patient_name}'s Heart Rate is dangerously high: {heart_rate} bpm!")


class VitalTracker:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

  
    def log_vitals(self, patient_name, heart_rate, blood_pressure):
     
        if isinstance(heart_rate, str) or not isinstance(heart_rate, (int, float)):
            raise ValueError("Heart rate must be a numeric value.")
        if heart_rate < 0:
            raise ValueError("Heart rate cannot be negative.")

  
        
        db = DatabaseConnection()
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vital_logs (patient_name, heart_rate, blood_pressure) VALUES (?, ?, ?)", 
                       (patient_name, heart_rate, blood_pressure))
        conn.commit()
        conn.close()
        
        
        for observer in self._observers:
            observer.update(patient_name, heart_rate)


# --- PROXY PATTERN (Mod 1 & Mod 3: Authentication & Dashboard Access) ---
class DashboardAccess:
    def view_dashboard(self):
        pass

class RealDoctorDashboard(DashboardAccess):
    def view_dashboard(self):
        db = DatabaseConnection()
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vital_logs")
        logs = cursor.fetchall()
        conn.close()
        
        output = "\n--- 🩺 Doctor Dashboard (Patient Vitals Table) ---\n"
        output += f"{'ID':<5}{'Patient Name':<15}{'Heart Rate':<12}{'Blood Pressure':<15}\n"
        output += "-" * 50 + "\n"
        for log in logs:
            alert_flag = "🚨 [HIGH ALERT]" if log[2] > 100 else "Normal"
            output += f"{log[0]:<5}{log[1]:<15}{log[2]:<12}{log[3]:<15} {alert_flag}\n"
        return output

class DoctorDashboardProxy(DashboardAccess):
    def __init__(self, username, user_role):
        self.username = username
        self.user_role = user_role
        self.real_dashboard = RealDoctorDashboard()

    def view_dashboard(self):
       
        

        if self.user_role.lower() == "doctor":
            return self.real_dashboard.view_dashboard()
        else:
            return f"\n[ACCESS DENIED]: User '{self.username}' is not authorized to view the Doctor Dashboard."


# --- MOD 5: PRESCRIPTION ENGINE ---
class PrescriptionEngine:
    @staticmethod
    def write_prescription(doctor_name, patient_name, medicine_note):
        db = DatabaseConnection()
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO prescriptions (patient_name, doctor_name, notes) VALUES (?, ?, ?)", 
                       (patient_name, doctor_name, medicine_note))
        conn.commit()
        conn.close()
        return f"[SUCCESS] Prescription saved successfully for {patient_name}."
