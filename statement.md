# Project Statement – Hospital Management System

## ● Problem Statement
- Hospitals often manage patient details, doctor information, and appointments manually, which leads to errors, delays, and difficulty in maintaining records.  
- A simple computerized system is required to store, update, and retrieve hospital data efficiently.

## ● Scope of the Project
- Manage patient records (add, view, update, delete)
- Manage doctor records (add, view, update, delete)
- Manage appointments between patients and doctors
- Store all data using using ***SQLite*(relational databases)
- Provides a simple, menu driven interface.
- Primary Scope
To provide a simple, lightweight, and fully functional system for managing basic hospital records (patients, doctors, and appointments) using Python and SQLite.
To demonstrate the practical application of core programming concepts such as functions, modules, file handling, database connectivity, and SQL queries in a real-world scenario.

- Current Functional Scope
Complete management of patient records (Add, View, Update, Delete)
Management of doctor records (Add, View, Delete)
Appointment scheduling and viewing with proper linking of patient and doctor names using SQL JOIN
Permanent storage of all data in a local database file
User-friendly console interface with clean navigation and informative messages

- Target Environment
Small clinics, nursing homes, charitable hospitals, and private practitioners
Rural or low-resource healthcare setups where expensive licensed software cannot be afforded
Educational institutions for teaching database programming concepts



## ● Target Users
- Beginners learning modular programming  
- Small clinics needing a basic, offline record-management demonstration
- Receptionist / Front-Desk Staff
The primary user who will register new patients, book appointments, and view/update records on a daily basis.
Hospital Administrator
Can add/delete doctors, view all patient and appointment records, and maintain the overall database.
- Small Clinic or Nursing Home Owner
A single person running a small clinic who needs a simple, zero-cost system to manage daily operations without hiring extra IT staff.
- College Lab Demonstrators / Students
Easy to run and demonstrate in Python lab practicals and viva – no installation or internet required.
- Doctors (limited use)
Can quickly check their appointment schedule from the “View Appointments” section (though full doctor login is not implemented in this basic version).

## ● High-level Features
- Patient Management Module  
- Doctor Management Module  
- Appointment Management Module  
- Persistent storage using SQLite(hospital.db)  
- Error handling & input validation
- Fully Menu-Driven Console Application – Easy navigation using simple numbered menus.
- Three Core Modules – Complete management of Patients, Doctors, and Appointments.
- Permanent Data Storage – Uses SQLite database (hospital.db) – data never gets lost on restart.
- Automatic Database Creation – Tables are created automatically on first run – no manual setup needed.
- Clean & Attractive Interface – Screen clears after every action, bordered headings, aligned tables, and friendly messages.
- Real SQL JOIN Query – View Appointments shows actual Patient Name + Doctor Name instead of just IDs.
- Full CRUD Operations – Add, View, Update, Delete for patients; Add, View, Delete for doctors.
- User-Friendly Experience – Success messages, “Get well soon”, “Welcome Dr.”, “Thank you”, and “Press Enter to continue…” after every step.
- 100% Portable – Only uses built-in Python libraries – runs anywhere without installation.
- Modular & Clean Code – Separate files for each module – easy to understand and extend.
- Zero External Dependencies – No pip install, no internet, no extra software required

