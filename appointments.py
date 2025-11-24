# appointment.py  :)
#Time for appointment module

from database import get_connection
import datetime

def add_appointment():
    print("===== ADD NEW APPOINTMENT =====")
    patient_id = int(input("Enter Patient ID: "))
    doctor_id = int(input("Enter Doctor ID: "))
    date = input("Enter date (YYYY-MM-DD): ")
    
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO appointments (patient_id, doctor_id, date) VALUES (?, ?, ?)",
                (patient_id, doctor_id, date))
    
    conn.commit()
    conn.close()
    
    print("Appointment booked successfully!")
    print("Thank you")
    input("Press Enter to continue...")

def view_appointments():
    print("\n===== ALL APPOINTMENTS LIST =====")
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT a.id, p.name, d.name, a.date 
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
    """)
    
    rows = cur.fetchall()
    conn.close()
    
    if len(rows) == 0:
        print("No appointments found ")
    else:
        print("ID   | Patient Name        | Doctor Name         | Date")
        print("----------------------------------------------------------")
        for r in rows:
            print(r[0],"  |",r[1].ljust(18),"|",r[2].ljust(18),"|",r[3])
    
    print()
    input("Press Enter to go back...")

# extra function  made for testing
def appointment_menu():
    while True:
        print("\nAppointment Menu")
        print("1. Add Appointment")
        print("2. View All Appointments")
        print("3. Back to Main Menu")
        choice = input("Choose option (1-3): ")
        
        if choice == "1":
            add_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            break
        else:
            print("Wrong choice!! Try again")