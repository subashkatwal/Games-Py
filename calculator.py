import math 

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b


def main():
    while True:
        print("Choices \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Exit \n")
        choice=int(input("Enter your choice :\n"))
        if (choice==1):
            a,b=map(int,input("Enter two numbers : ").split(" "))
            print("Result is : ",add(a,b))
    
        elif (choice==2):
            a,b=map(int,input("Enter two numbers : ").split(" "))
            print("Result is : ",subtract(a,b))
        
        elif(choice==3):
            a,b=map(int,input("Enter two numbers : ").split(" "))
            print("Result is : ",multiply(a,b))
    
        elif(choice==4):
            a,b=map(int,input("Enter two numbers : ").split(" "))
            print("Result is : ",divide(a,b))
        elif(choice==5):
            print("Choose a valid input,Exiting .....")
            break
        else:
            print("Choose number between 1 and 5 ...")
            
    
if __name__=="__main__":
    main()