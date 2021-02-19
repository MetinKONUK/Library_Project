import sqlite3
from time import sleep
class Book():
    def __init__(self,name,author,owner,kind,press):
        self.name = name
        self.author = author
        self.owner = owner
        self.kind = kind
        self.press = press
    def __str__(self):
        return "Name: {}\nAuthor{}\nOwner:{}\nKind:{}\nPress:{}".format(self.name,self.author,self.owner,self.kind,self.press)

class Library():
    def __init__(self):
        self.connect()
    def connect(self):
        self.connection = sqlite3.connect("kütüphane.db")
        self.cursor = self.connection.cursor()
        query = "CREATE TABLE IF NOT EXISTS books (name TEXT,author TEXT,owner TEXT,kind TEXT,press INT)"
        self.cursor.execute(query)
        self.connection.commit()
    def kill_connection(self):
        self.connection.close()
    def display_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        if len(data):
            for i in data:
                book = Book(i[0], i[1],i[2],i[3],i[4])
                print(book)
        else:
            print("There are no books in library :(")
            
    def query_books(self,name):
        query = "SELECT * FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))
        data = self.cursor.fetchall()
        if len(data):
            for i in data:
                book = Book(i[0], i[1],i[2],i[3],i[4])
                print(book)      
        else:
            print("There is no book named {} in this library :(".format(name))
            
    def add_book(self,book):
        query = "INSERT INTO books Values(?,?,?,?,?)"
        self.cursor.execute(query,(book.name,book.author,book.owner,book.kind,book.press))
        self.connection.commit()
    def delete_book(self,name):
        query = "DELETE FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))
        self.connection.commit()
    def increase_press_count(self,name):
        query = "SELECT * FROM books WHERE name = ?"
        self.cursor.execute(query,(name,))
        data = self.cursor.fetchall()
        if len(data):
            press = data[0][4]
            press += 1
            query_second = "UPDATE books SET press = ? WHERE name = ?"
            self.cursor.execute(query_second,(press,name))
            self.connection.commit()
        else:
            print("No such book")









        
    
    
        
