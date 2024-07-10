def main():
    bookList=[]
    choice=-1
    while choice!=0:
        print("****Books Menu****")
        print("1. Add Books .")
        print("2. Display Books")
        print("3. Search For a Book")
        print("4.Exit")
        
        choice=int(input("Enter your choice "))
        if choice==1:
            while True:
                book=(input("Enter the name of the Books ('Type done when you are finished'): "))
                if book.lower()=="done":
                    break
                bookList.append(book)
                print(f'Book {book} added to your list')
            
        elif choice==2:
            print("Total number of present books ")
            for book in bookList:
                print(book)
            
        elif choice==3:
            search=input("Enter the name of book you want to search ").lower()
            if search in bookList:
                    print(f'Book {search} found in the list')
            else:
                print("Error while finding the book ")
        else:
            print("Exiting.....")
            exit()
        
    
if __name__=="__main__":
    main()