

"""
grade=float(input("Enter the grade of your exam"))
if (grade<35):
    print("D",grade)
elif(grade<45 and grade >35):
    print("C",grade)
elif(grade<60 and grade >45):
    print("C+",grade)
elif(grade<70 and grade >60):
    print("B",grade)
elif(grade<80 and grade >70):
    print("B",grade)
elif(grade<90 and grade >80):
    print("A",grade)
elif(grade<100 and grade >90):
    print("A",grade)
else:
    exit()
    """
 

time=int(input("Enter the time period to give bonus "))
salary=int(input("Enter the salary of the employee "))
bonus=0
if (time > 10):
    bonus=salary+0.10*salary
    print(bonus)
elif(time>=6 and time>= 10):
    bonus=salary+0.8*salary
    print(bonus)
elif(time<6):
    bonus=salary+0.05*salary
    print(bonus)
else:
    print("Exiting...")
    exit()
print("Total salary is ",salary)
    

