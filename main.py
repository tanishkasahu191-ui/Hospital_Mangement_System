
# HOSPITAL MANAGEMENT SYSTEM
# Name     : Tanishka Sahu
# Roll No   : 25BCE10056
# Class     : First Year B.Tech
# Submitted to: Respected  DR AVR MAYURI Mam/Sir
# Date      : 24TH November 2025

import os
from database import connect
import patients
import doctors
import appointments

# First time running = create database
connect()
print("Database connected successfully!")

def main():
    while True:
        os.system('cls')  
        print("=====================================================")
        print("     HOSPITAL MANAGEMENT SYSTEM")
        print("=====================================================")
        print("1. Manage Patients")
        print("2. Manage Doctors") 
        print("3. Manage Appointments")
        print("4. Exit System")
        print("=====================================================")
        
        choice = input("  Enter your choice (1-4): ")
        
        if choice == "1":
            patients.patient_menu()        # #### calling from patients.py
        elif choice == "2":
            doctors.doctor_menu()          # #### doctor menu
        elif choice == "3":
            appointments.appointment_menu() # appointment menu
        elif choice == "4":
            os.system('cls')
            print("\n\n\tThank You for using our System!")
            print("\tProject by: Tanishka Sahu")
            print("\tHave a nice day")
            input("\n\tPress Enter to exit...")
            break
        else:
            print("  Wrong choice ! Please try again")
            input("  Press Enter to continue...")

# WORKS ONLY WHEN hum direct file run karte hain
if __name__ == "__main__":
    print("Starting Hospital System...")
    main()