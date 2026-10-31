 MedVitals Lite - Remote Patient Monitoring Platform

**MedVitals Lite** is a lightweight, self-contained remote patient monitoring and telemedicine system built using Python and SQLite. The application tracks real-time patient metrics, manages access control for medical staff, handles automated threshold notifications, and securely updates dynamic records following robust software engineering design patterns and the Software Development Lifecycle (SDLC).

Developed as part of the software engineering sessional course requirements at **RUET**.



 Key Project Infrastructure & Modules

The platform implements five distinct functional modules across an **Incremental Process Model** lifecycle:

1. **Authentication and Roles:** Provides dynamic login validations handling Role-Based Access Control (RBAC) separating patients from medical consultants.
2. **Vital Logging:** Offers robust data parsing frameworks allowing patients to log daily metric sets persistently.
3. **Doctor Dashboard:** Generates structured visual tabular outputs tracking real-time status attributes across active patient arrays.
4. **Alerts and Notifications:** Intercepts real-time vital streams to instantly flag instances exceeding safety thresholds (>100 bpm).
5. **Prescriptions:** Allows registered consultants to append clinical medical recommendations directly to target client fields.



| **Singleton** | Creational | Prevents concurrent structural resource locking errors across the flat-file database tracking engine. | Enforces a single, globally accessible instance of the SQLite connection pool (`DatabaseConnection`). |
| **Proxy** | Structural | Blocks cross-site parameter exposure or unauthorized role evaluation checks inside administrative boundaries. | Intercepts dashboard access calls (`DoctorDashboardProxy`) to validate system authorization levels dynamically. |
| **Observer** | Behavioral | Devises asynchronous reaction pathways decoupled from transaction layers. | Automatically triggers critical target methods (`AlertNotificationService`) whenever patient metrics breach healthy limits. |

