math = int(input("Enter the number for Math : "))
english = int(input("Enter the number for English : "))
bangla = int(input("Enter the number for Bangla : "))
science = int(input("Enter the number for Science : "))
history = int(input("Enter the number for History : "))
religion = int(input("Enter the number for Religion : "))

avg = (math+english+bangla+science+history+religion)//6

if avg>79 and avg<=100:
    print("Your grade by the given numbers is A+.")
elif avg>74 and avg<=79:
    print("Your grade by the given numbers is A.")
elif avg>69 and avg<=74:
    print("Your grade by the given numbers is A-.")
elif avg>64 and avg<=69:
    print("Your grade by the given numbers is B+.")
elif avg>59 and avg<=64:
    print("Your grade by the given numbers is B.")
elif avg>54 and avg<=59:
    print("Your grade by the given numbers is B-.")
elif avg>49 and avg<=54:
    print("Your grade by the given numbers is C+.")
elif avg>44 and avg<=49:
    print("Your grade by the given numbers is C.")
elif avg>39 and avg<=44:
    print("Your grade by the given numbers is D.")
elif avg>=0 and avg<=39:
    print("Your grade by the given numbers is F.")
else:
    print("You inputted wrong numbers.")