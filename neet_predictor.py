a=int(input("enter your neet score: "))
b=(input("what is your category: "))
if (a<500):
    print("sorry you cannot get any medical college")
    print("try again next year")
elif(a>=500 and a<=599 and (b=="gen")):
    print("you can try for private medical college")
elif(a>=500 and a<=599 and (b=="obc")):
    print("You may get a decent private college.")
elif(a>=500 and a<=599 and (b=="SC" or b=="ST")):
    print("You have a chance at some government colleges.")
elif(a>=600 and a<=649 and (b=="gen")):
    print("Government college possible.")
elif(a>=600 and a<=649 and (b=="obc")):
    print("Good chance for government college.") 
elif(a>=600 and a<=649 and (b=="SC" or b=="ST")):
    print("Strong chance for government college.")
elif(a>=650 and a<=699 and (b=="gen")):
    if(a>=680 and (b=="gen")):
        print("Top government colleges may be possible.")
    if(a<680 and (b=="gen")):
        print("Good government college options.")
elif(a>=650 and a<=699 and (b=="obc" or b=="SC" or b=="ST")):
    print("Very strong government college chances.")    
else:
    print("Excellent score! Top government colleges are possible.")

