#Project 4 : Guest House Management System(CRUD+Additional functionalities)
bookings={}
RoomStatus={
    101:"Available",102:"Available",103:"Available",104:"Available",105:"Available",
    106:"Available",107:"Available",108:"Available",109:"Available",110:"Available"
    }
RoomPrices={'single nonac':1000,'single ac':1500,'double nonac':1800,'double ac':2500}
def mainMenu():
    while True:
        print('''\nGuest House Management Menu\n
              1.create booking
              2.view all bookings
              3.update booking
              4.delete bookings
              5.check room availability
              6.generate bill
              7.search bookings by name
              8.Exit
              ''')
        print("="*100)
        ch=input("choose options : ")
        if ch=='1':
            createB()
        elif ch=='2':
            viewB()
        elif ch=="3":
            updateB()
        elif ch=='4':
            deleteB()
        elif ch=='5':
            checkAvailability()
        elif ch=='6':
            generateBill()
        elif ch=="7":
            searchBookings()
        elif ch=='8':
            print("Exiting...")
            break
        else:
            print("Invald choice try again.")
def createB():
    name=input("Enter name :")
    age=int(input("Enter age: "))
    room_type=input("Enter Room type (single nonac/single ac/double Ac/double nonac): ")
    checkin=input("Enter check in date: ")
    checkout=input("Enter Checkout date: ")
    nights=int(input("Enter no. of nights: "))
    
    room_number=None
    for i in RoomStatus:
        if RoomStatus[i]=="Available":
            room_number=i
            break
    if room_number is None:
        print("No rooms available")
        return
    RoomStatus[room_number]="Booked"
    bookings[room_number]={
        'name':name,
        'age':age,
        'room_type':room_type,
        'checkin':checkin,
        'checkout':checkout,
        'nights':nights
    }
    print(f"Room {room_number} booked successfully for{name}")
    print('-'*100)
def viewB():
    if not bookings:
        print("No bookings yet.")
        return 
    print("\nCurrent Bookings: ")
    for key ,value in bookings.items():
        print(f'Room {key} : {value}')
    print('-'*100)  
def updateB():
    room=int(input("Enter Room number to update : "))
    if room in bookings:
        name=input("Enter new customer name:")
        bookings[room]['name']=name
        print("Bookings Updated.")
    else:
        print("Bookings not Found.")
def deleteB():
    room=int(input("Enter Room number to delete: "))
    if room in bookings:
        del bookings[room]
        RoomStatus[room]="Available"
        print("Booking Deleted.")
    else:
        print("Bookings not found.")
    print("-"*100)
def checkAvailability():
    print("\nRoom Availability: ")
    for i in RoomStatus:
        print(f"Room {i} : {RoomStatus[i]}")
    print("-"*100)
def generateBill():
    room=int(input("Enter Room Number for Bill: "))
    if room in bookings:
        nights=bookings[room]['nights']
        rtype=bookings[room]['room_type']
        price=RoomPrices.get(rtype,1000)
        total=nights*price
        print(f"\n\tBill for Room {room}")
        print(f"\tCustomer :{bookings[room]['name']} ")
        print(f"\tRoom Type:{rtype}")
        print(f"\tNights Stayed : {nights}\n")
        #print("-"*20)
        print(f"\tTotal Bill : Rs.{total}")
    else:
        print("Bookings not found")
    print("="*100)
def searchBookings():
    name=input("Enter the customer name to search: ")
    found=False
    for key,value in bookings.items():
        if value['name']==name:
            print(f"Booking Found: Room {key}, Details {value}")
            found=True
        if not found:
            print("No bookings found for that name.")
        print("-"*100)       
    
mainMenu()