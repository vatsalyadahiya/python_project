# IMPORTING REQUIRED LIBRARIES AND MODULES
import pickle

# A METHOD TO GET ALL MEMBER's DATA
def getMember():
    file = open('member.bin','rb')
    mem = {}
    try:
        while True:
            mem.update(pickle.load(file))
    except:
        pass
    file.close()
    return mem


# A METHOD TO GET ALL BOOK's DATA
def getBook():
    file = open('book.bin','rb')
    bok = {}
    try:
        while True:
            bok.update(pickle.load(file))
    except:
        pass
    file.close()
    return bok



# A METHOD TO WRITE ALL MEMBER INFORMATION INTO THE FILE
def updateMember(mem):
    file = open('member.bin','wb')
    for mid , data in mem.items():
        pickle.dump({mid:data}, file)
    file.close()

# A METHOD TO ADD A MEMBER's INFORMATION
def addMember():
    mid = input("\n\tEnter New Member ID : ")
    mname = input("\tEnter Member Name : ")
    madd = input("\tEnter Member Address : ")
    mmob = input("\tMobile Number : ")
    file = open('member.bin','ab')
    data = {mid:[mname,madd,mmob]}
    pickle.dump(data, file)
    file.close()
    print("\n\tMember Added Successfully!")

# A METHOD TO VIEW ALL MEMBER's INFORMATION
def viewMember():
    file = open('member.bin','rb')
    mem = getMember()
    for mid,data in mem.items():
        print("\n\tMember ID :",mid)
        print("\tMember Name :",data[0])
        print("\tMember Address :",data[1])
        print("\tMember Mobile :",data[2])
        print("\t---------------------------------")
    file.close()

# A METHOD TO DELETE A MEMBER
def deleteMember():
    mid = input("\n\tEnter Member ID To Delete : ")
    member = getMember()
    mem = member.get(mid,False)
    if mem:
        print("\n\tMember Name :",mem[0])
        print("\tMember Address :",mem[1])
        member.pop(mid)
        updateMember(member)
        print("\n\tMember Deleted Successfully!")
    else:
        print("\n\tMember Not Found!")

# A METHOD TO ADD BOOK INFORMATION
def addBook():
    bid = input("\n\tEnter New Book ID : ")
    bname = input("\tEnter Book Name : ")
    price = input("\tEnter Price : ")
    about = input("\tWrite About Book : ")
    data = {bid:[bname,price,about]}
    file = open('book.bin' , 'ab')
    pickle.dump(data,file)
    file.close()
    print("\n\tBook Added Successfully!")

# A METHOD TO VIEW ALL BOOKS INFORMATION
def viewBook():
    bok = getBook()
    print("\n\tBID   BNAME         PRICE   ABOUT BOOK\n")
    for bid , data in bok.items():
        print(f"\t{bid:<5}{data[0]:<12}{data[1]:<8}{data[2]}")
    print("\n\tHere is all your books!")

# A METHOD TO UPDATE THE PRICE OF A BOOK
def updatePrice():
    bid = input("\n\tEnter Book ID To Update Price : ")
    book = getBook()
    bok = book.get(bid , False)
    if bok:
        print("\n\tBook Name :",bok[0])
        print("\tBook Old Price :",bok[1])
        price = input("\n\tEnter New Price : ")
        book.update({bid:[bok[0],price,bok[2]]})
        file = open('book.bin','wb')
        for bid , data in book.items():
            pickle.dump({bid:data},file)
        file.close()
        print("\n\tPrice Updated!")
    else:
        print("\n\tBook Not Found!")

# A METHOD TO ISSUE A BOOK
def issueBook():
    mid = input("\n\tEnter Member ID To Issue Book : ")
    mem = getMember().get(mid,False)
    if mem:
        print("\n\tMember Name :",mem[0])
        print("\tMember Address :",mem[1])
        bid = input("\n\tEnter Book ID : ")
        bok = getBook().get(bid,False)
        if bok:
            print("\tBook Name :",bok[0])
            print("\tBook Price :",bok[1])
            qty = input("\tEnter Quantity : ")
            print("\tTotal Bill :",int(bok[1])*int(qty))
            data = (mid,bid,qty)
            file = open('issue.bin','ab')
            pickle.dump(data,file)
            file.close()
            print("\n\tBook Issued Successfully!")
        else:
            print("\n\tBook Not Found!")
    else:
        print("\n\tMember Not Found!")

# A METHOD TO VIEW ALL ISSUED BOOKS
def viewIssue():
    file = open('issue.bin','rb')
    try:
        i = 1000
        while True:
            i = i+1
            data = pickle.load(file)
            mem = getMember().get(data[0],False)
            if mem:
                bok = getBook().get(data[1])
                qty = data[2]
                print("\nIssue ID -",i)
                print("\tMember Name :",mem[0])
                print("\tMember Address :",mem[1])
                print("\tBook Name :",bok[0])
                print("\tBook Price :",bok[1])
                print("\tAbout Book :",bok[2])
                print("\tIssued Quantity :",qty)
                print("\tTotal Bill :",int(bok[1])*int(qty))
                print("\t---------------------------------------")
    except:
        pass
    file.close()

# A METHOD TO VIEW ALL ISSUED BOOKS BY MID
def viewIssueByMID():
    mid = input("\n\tEnter Member ID To View Issue : ")
    file = open('issue.bin','rb')
    if getMember().get(mid,False):
        try:
            i = 1000
            while True:
                i = i+1
                data = pickle.load(file)
                mem = getMember().get(data[0],False)
                if mem and data[0]==mid:
                    bok = getBook().get(data[1])
                    qty = data[2]
                    print("\nIssue ID -",i)
                    print("\tMember Name :",mem[0])
                    print("\tMember Address :",mem[1])
                    print("\tBook Name :",bok[0])
                    print("\tBook Price :",bok[1])
                    print("\tAbout Book :",bok[2])
                    print("\tIssued Quantity :",qty)
                    print("\tTotal Bill :",int(bok[1])*int(qty))
                    print("\t---------------------------------------")
        except:
            pass
        file.close()
    else:
        print("\n\tMember Not Found!")


# DASHBOARD
while True:
    print("\n\tLIBRARY MANAGEMENT SYSTEM")
    print('''
        1. Add Member
        2. View Members
        3. Delete A Member
        4. Add Book
        5. View Books
        6. Update Book Price
        7. Issue A Book
        8. View Issued Books
        9. View All Issued Books By MID
        0. Exit
    ''')
    ch = int(input("\tEnter Your Choice : "))
    if ch==0:
        print("\n\tGoodBye!")
        break
    if ch==1:
        addMember()
        input("\tPress Enter To Continue...")
    elif ch==2:
        viewMember()
        input("\tPress Enter To Continue...")
    elif ch==3:
        deleteMember()
        input("\tPress Enter To Continue...")
    elif ch==4:
        addBook()
        input("\tPress Enter To Continue...")
    elif ch==5:
        viewBook()
        input("\tPress Enter To Continue...")
    elif ch==6:
        updatePrice()
        input("\tPress Enter To Continue...")
    elif ch==7:
        issueBook()
        input("\tPress Enter To Continue...")
    elif ch==8:
        viewIssue()
        input("\tPress Enter To Continue...")
    elif ch==9:
        viewIssueByMID()
        input("\tPress Enter To Continue...")