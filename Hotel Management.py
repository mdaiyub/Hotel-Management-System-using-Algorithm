import random
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

i = 0

def Home():
    print("\t\t\t\t\t\t WELCOME TO OUR HOTEL")
    print("\t\t\t 1 Booking")
    print("\t\t\t 2 Rooms Info")
    print("\t\t\t 3 Room Service(Menu Card)")
    print("\t\t\t 4 Record")
    print("\t\t\t 0 Exit")

    ch = int(input("->"))

    if ch == 1:
        print(" ")
        Booking()

    elif ch == 2:
        print(" ")
        Rooms_Info()

    elif ch == 3:
        print(" ")
        restaurant()

    elif ch == 4:
        print(" ")
        Record()

    else:
        exit()

# Booking function
def Booking():

    global i
    print(" BOOKING ROOMS")
    print(" ")

    while 1:
        n = str(input("Name: "))
        p1 = str(input("Phone No.: "))
        a = str(input("Address: "))

        # checks if any field is not empty
        if n != "" and p1 != "" and a != "":
            name.append(n)
            add.append(a)
            break

        else:
            print("\tName, Phone no. & Address cannot be empty..!!")

    cii = str(input("Check-In: "))
    checkin.append(cii)


    coo = str(input("Check-Out: "))
    checkout.append(coo)

    print("----SELECT ROOM TYPE----")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print(" 3. 3-Bed Non-AC")
    print(" 4. 3-Bed AC")
    print(("\t\tPress 0 for Room Prices"))

    ch = int(input("->"))

    # if-conditions to display alloted room
    # type and it's price
    if ch == 0:
        print(" 1. Standard Non-AC - Rs. 3500")
        print(" 2. Standard AC - Rs. 4000")
        print(" 3. 3-Bed Non-AC - Rs. 4500")
        print(" 4. 3-Bed AC - Rs. 5000")
        ch = int(input("->"))
    if ch == 1:
        room.append('Standard Non-AC')
        print("Room Type- Standard Non-AC")
        price.append(3500)
        print("Price- 3500")
    elif ch == 2:
        room.append('Standard AC')
        print("Room Type- Standard AC")
        price.append(4000)
        print("Price- 4000")
    elif ch == 3:
        room.append('3-Bed Non-AC')
        print("Room Type- 3-Bed Non-AC")
        price.append(4500)
        print("Price- 4500")
    elif ch == 4:
        room.append('3-Bed AC')
        print("Room Type- 3-Bed AC")
        price.append(5000)
        print("Price- 5000")
    else:
        print(" Wrong choice..!!")

    # randomly generating room no. and customer
    # id for customer
    rn = random.randrange(40) + 300
    cid = random.randrange(40) + 10

    # checks if alloted room no. & customer
    # id already not alloted
    while rn in roomno or cid in custid:
        rn = random.randrange(60) + 300
        cid = random.randrange(60) + 10

    rc.append(0)
    p.append(0)

    if p1 not in phno:
        phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 1:
                    phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 0:
                    print("\tPhone no. already exists and payment yet not done..!!")
                    name.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()
    print("")
    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
    print("Room No. - ", rn)
    print("Customer Id - ", cid)
    roomno.append(rn)
    custid.append(cid)
    i = i + 1
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()


# ROOMS INFO
def Rooms_Info():
    print("		 ------ HOTEL ROOMS INFO ------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()


# RESTAURANT FUNCTION
def restaurant():
    ph = int(input("Customer Id: "))
    global i
    f = 0
    r = 0
    for n in range(0, i):
        if custid[n] == ph and p[n] == 0:
            f = 1
            print("-------------------------------------------------------------------------")
            print("						 Menu Card")
            print("-------------------------------------------------------------------------")
            print("\n")
            print(" 1 Regular Tea............. 20.00")
            print(" 2 Masala Tea.............. 25.00")
            print(" 3 Coffee.................. 25.00")
            print(" 4 Cold Drink.............. 25.00")
            print(" 5 Bread Butter............ 30.00")
            print(" 6 Bread Jam............... 30.00")
            print(" 7 Veg. Sandwich........... 50.00")
            print(" 8 Veg. Toast Sandwich..... 50.00")
            print(" 9 Cheese Toast Sandwich... 70.00")
            print(" 10 Grilled Sandwich........ 70.00")

            ch = 1
            while (ch != 0):

                ch = int(input(" -> "))

                # if-elif-conditions to assign item
                # prices listed in menu card
                if ch == 1:
                    rs = 20
                    r = r + rs
                elif ch <= 4 and ch >= 2:
                    rs = 25
                    r = r + rs
                elif ch <= 6 and ch >= 5:
                    rs = 30
                    r = r + rs
                elif ch <= 8 and ch >= 7:
                    rs = 50
                    r = r + rs
                elif ch <= 10 and ch >= 9:
                    rs = 70
                    r = r + rs

                elif ch == 0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ", r)

            r = r + rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Invalid Customer Id")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()


# RECORD FUNCTION
def Record():
    # checks if any record exists or not
    if phno != []:
        print("	 *** HOTEL RECORD ***\n")
        print("| Name	 | Phone No. | Address	 | Check-In | Check-Out	 | Room Type	 | Price	 ")
        print(
            "----------------------------------------------------------------------------------------------------------------------")

        def sort(a, b, c, d, e, f, g):
            name = a
            phno = b
            add = c
            checkin = d
            checkout = e
            room = f
            price = g
            for y in range(1, len(name)):
                key = name[y]
                key1 = phno[y]
                key2 = add[y]
                key3 = checkin[y]
                key4 = checkout[y]
                key5 = room[y]
                key6 = price[y]
                a = y
                while (name[a - 1] > key) and a > 0:
                    z = name[a - 1]
                    name[a] = z

                    h = phno[a - 1]
                    phno[a] = h

                    i = add[a - 1]
                    add[a] = i

                    j = checkin[a - 1]
                    checkin[a] = j

                    k = checkout[a - 1]
                    checkout[a] = k

                    l = room[a - 1]
                    room[a] = l

                    m = price[a - 1]
                    price[a] = m

                    a = a - 1
                    name[a] = key
                    phno[a] = key1
                    add[a] = key2
                    checkin[a] = key3
                    checkout[a] = key4
                    room[a] = key5
                    price[a] = key6

        x = sort(name, phno, add, checkin, checkout, room, price)
        for n in range(0, i):
            print("|", name[n], "\t |", phno[n], "\t|", add[n], "\t|", checkin[n], "\t|", checkout[n], "\t|", room[n],
                  "\t|", price[n])

        print(
            "----------------------------------------------------------------------------------------------------------------------")
        print("\n1- Search customer")

    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 1:
        key = str(input("input customer name\n ->"))
        start_point = 0
        end_point = len(name) - 1
        found = 0
        while start_point <= end_point:
            mid_point = (start_point + end_point) // 2
            if name[mid_point] == key:
                x = mid_point
                found = 1
                break
            elif key > name[mid_point]:
                start_point = mid_point + 1
            else:
                end_point = mid_point - 1
        if found == 0:
            print("can't found customer")
        if found == 1:
            print("| Name	 | Phone No. | Address	 | Check-In | Check-Out	 | Room Type	 | Price	 ")
            print(
                "----------------------------------------------------------------------------------------------------------------------")

            print("|", name[x], "\t |", phno[x], "\t|", add[x], "\t|", checkin[x], "\t|", checkout[x], "\t|", room[x],
              "\t|", price[x])

            n = int(input("\n\n0-BACK\n ->"))
            if n == 0:
                Home()

            else:
                exit()

    if n == 0:
        Home()
    else:
        exit()

# Driver Code
Home()
