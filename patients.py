# patients.py


import os
from database import get_connection

def add_patient():
    os.system('cls')
    print("=====================================")
    print("         ADD NEW PATIENT         ")
    print("=====================================")
    
    name = input("Enter Patient Name       : ")
    age = int(input("Enter Patient Age        : "))
    gender = input("Enter Gender (M/F/Other) : ")
    disease = input("Enter Disease/Problem    : ")
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO patients (name, age, gender, disease) VALUES (?, ?, ?, ?)", 
                (name, age, gender, disease))
    conn.commit()
    conn.close()
    
    print("\nPatient added successfully!")
    print("Get well soon", name, "!")
    input("\nPress Enter to continue...")

def view_patients():
    os.system('cls')
    print("===============================================")
    print("              ALL PATIENTS LIST              ")
    print("===============================================")
    print("ID | Name                 | Age | Gender | Disease")
    print("------------------------------------------------")
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    all_patients = cur.fetchall()
    conn.close()
    
    if len(all_patients) == 0:
        print("         No patients admitted yet ")
    else:
        for p in all_patients:
            print(p[0], "|", p[1].ljust(20), "|", str(p[2]).center(3), "|", p[3].center(6), "|", p[4])
    
    print()
    input("Press Enter to go back...")

def delete_patient():
    os.system('cls')
    print("           DELETE PATIENT           ")
    print("====================================")
    view_patients()   # show list first so easy to choose
    print()
    pid = int(input("Enter Patient ID to delete: "))
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM patients WHERE id=?", (pid,))
    
    if cur.rowcount > 0:
        print("Patient record deleted successfully!")
    else:
        print("No patient found with that ID")
    
    conn.commit()
    conn.close()
    input("Press Enter to continue...")

def update_patient():
    os.system('cls')
    print("           UPDATE PATIENT INFO           ")
    print("=========================================")
    view_patients()
    print()
    pid = int(input("Enter Patient ID to update: "))
    
    print("\nEnter new details (leave blank to keep old):")
    name = input("New Name     : ") or None
    age_input = input("New Age      : ")
    gender = input("New Gender   : ") or None
    disease = input("New Disease  : ") or None
    
    conn = get_connection()
    cur = conn.cursor()
    
    if name and age_input and gender and disease:
        age = int(age_input)
        cur.execute("UPDATE patients SET name=?, age=?, gender=?, disease=? WHERE id=?", 
                    (name, age, gender, disease, pid))
    else:
        print("You must fill all fields to update!")
    
    if cur.rowcount > 0:
        print("Patient information updated!")
    else:
        print("Patient not found!")
        
    conn.commit()
    conn.close()
    input("Press Enter...")

# Patient Menu - called from main.py
def patient_menu():
    while True:
        os.system('cls')
        print("=======================================")
        print("         PATIENT MANAGEMENT MENU        ")
        print("=======================================")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Back to Main Menu")
        print("=======================================")
        
        choice = input("Choose option (1-5): ")
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("WRONG CHOICE::: TRY AGAIN")
            input("Press Enter...")