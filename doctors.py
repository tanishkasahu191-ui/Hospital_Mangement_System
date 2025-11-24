# doctors.py file



from database import get_connection
import os   # for clear screen

def add_doctor():
    os.system('cls')   # i like clear screen
    print("          ADD NEW DOCTOR          ")
    print("===================================")
    name = input("Enter Doctor Name : ")
    spec = input("Enter Specialization : ")
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO doctors (name, specialization) VALUES (?, ?)", (name, spec))
    conn.commit()
    conn.close()
    
    print("Doctor added successfully!")
    print("Welcome Dr.", name, "to our hospital")
    input("\nPress Enter to continue...")

def view_doctors():
    os.system('cls')
    print("              ALL DOCTORS LIST              ")
    print("==============================================")
    print("ID   | Doctor Name            | Specialization")
    print("----------------------------------------------")
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctors")
    data = cur.fetchall()
    conn.close()
    
    if len(data) == 0:
        print("     No doctors in hospital yet ")
    else:
        for d in data:
            print(d[0]," |", d[1].ljust(22),"|", d[2])
    
    print()
    input("Press Enter to go back...")

def delete_doctor():
    os.system('cls')
    print("           DELETE DOCTOR           ")
    print("===================================")
    view_doctors()   # show list first
    print()
    did = int(input("Enter Doctor ID to delete: "))
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM doctors WHERE id=?", (did,))
    
    if cur.rowcount > 0:
        print("Doctor deleted successfully!")
    else:
        print("No doctor found with that ID ")
    
    conn.commit()
    conn.close()
    input("Press Enter to continue...")

# menu for doctor section
def doctor_menu():
    while True:
        os.system('cls')
        print("==================================")
        print("       DOCTOR MANAGEMENT MENU       ")
        print("==================================")
        print("1. Add New Doctor")
        print("2. View All Doctors")
        print("3. Delete Doctor")
        print("4. Back to Main Menu")
        print("==================================")
        
        ch = input("Enter your choice (1-4): ")
        
        if ch == "1":
            add_doctor()
        elif ch == "2":
            view_doctors()
        elif ch == "3":
            delete_doctor()
        elif ch == "4":
            print("Going back...")
            break
        else:
            print("Invalid choice! Try again")
            input("Press Enter...")