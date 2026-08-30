z=int(input("enter your marks: "))

match z :
    case _ if z>=90 and z<=100:
        print("excellent job buddy")
        print("you're a topper now")
    case _ if z>=75 and z<=89:
        print("very good")
    case _ if z>=60 and z<=74:
        print('good')
    case _ if z>=40 and z<=59:
        print("pass")
    case _ if z < 40:
        print("fail")
    case _ if z>100 or z<0:
        print("invaild")