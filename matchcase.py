x=int(input("enter a number: "))
match x:
    case 0:
        print("the number is 0")
    case 4:
        print("this is not that number")
    case _ if x>4 and x<=6:
        print("close yet so far")
    case 7:
        print("yeah this is the number")
    case _:
        print("this is greater than 7")

