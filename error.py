a = input("choose a number: ")

print(f"the table of {a} is:")


try:
    for i in range(1,11):
        print(f"{int(a)} x {int(i)} = {int(a)*i}")
except:
    print("sorry")
    
        
        
    
    
