rooms = {
    101: "Available",
    102: "Available",
    103: "Available",
    104: "Available",
    105: "Available"
}
def show_rooms():
    print("\nRoom status:")
    for room, status in rooms.items():
        print(f"Room{room} - {status}")
def book_room():
    room_no = int(input("\nEnter room number to book: "))
    if room_no in rooms:
        if rooms[room_no] == "Available":
            rooms[room_no] = "booked"
            print(f"Room{room_no} succesfully booked!")
        else:
            print("Room already booked!")
    else:
        print("Invalid room number!")
def cancle_booking():
    room_no = int(input("\nEnter room number to cancle booking: "))
    if room_no in rooms:
        if rooms[room_no] == "booked":
            rooms[room_no] = "Available"
            print(f"booking of room {room_no} cancelled!")
        else:
            print("Room is already available!")
    else:
        print("Invalid room number!")
while True:
    print("\n==== ROOM BOOKING SYSTEM ====")
    print("1. Show room")
    print("2. Book room")
    print("3. Cancle Booking")
    print("4. Exit")
    choice = input("enter choice: ")
    if choice == "1":
        show_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        cancle_booking()
    elif choice == "4":
        print("thank you!")
        break
    else:
        print("Invalid choice!")
        
    