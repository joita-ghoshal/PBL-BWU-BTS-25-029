
appointment = []
def book_appointment ():
    name = input ("Enter Patient Name:")
    age = input ("Enter age:")
    doctor = input ("Enter doctor's name:")
    date = input (" Enter appointment date:")

    appointment. append ([name, age, doctor, date])
    print (" Appointment booked Successfully")
def view ():
    if len (appointment) == 0:
        print (" No appointments found")
    else:
        for i in appointment:
            print (" Patient:", i[0])
            print (" Age:", i[1])
            print (" Doctor:", i[2])
            print (" Date:", i[3])
while True:
    print (" Hospital Appointment System")
    print (" 1. Book Appointment")
    print (" 2. View Appointment")
    print ("3. Exit")
    ch= input ("Enter choice:")
    if ch == "1":
        book_appointment ()
    elif ch == "2":
        view ()
    elif ch == "3":
        print (" Thank you...!")
        break
    else:
        print (" Invalid choice")


# Hospital Appointment Management System