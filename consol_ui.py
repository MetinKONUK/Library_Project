from experimental_v2 import *
import time
print("""
******Welcome******
Operations:
1. Display Books
2. Query Book
3. Add Book
4.Delete Book
5. Increase Press Count
Q to EXIT
*******************
""")
library = Library()
while True:
    p = input("Select an operation")
    if p == "Q":
       break
    elif p == "1":
        library.display_books()
    elif p == "2":
        name = input("Book Name: ")
        time.sleep(2)
        library.query_books(name)
    elif p == "3":
        a,b,c,d,e = input("Name"),input("Author"),input("Owner"),input("Kind"),int(input("Press:")),
        new_book = Book(a,b,c,d,e)
        time.sleep(2)
        library.add_book(new_book)
        print("Book Added")
    elif p == "4":
        name = input("Book Name: ")
        time.sleep(2)
        library.delete_book(name)
        print("Book has been deleted")
    elif p == "5":
        name = input("Book Name: ")
        time.sleep(1)
        library.increase_press_count(name)
        print("Press enhanced!")
    else:
        print("Invalid Operation Selection!")
        
