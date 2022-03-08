"""
Define a Book class with the following attributes: Title, Author (Full name), Price.
2. Define a constructor used to initialize the attributes of the method with values entered by the user.
3. Set the View() method to display information for the current book.
4. Write a program to testing the Book class.
"""



class Book:
     
     def __init__(self , Title , Author , Price):
          self.Title    =  Title
          self.Author   =  Author
          self.Price    =  Price
          
    
     def view(self ):
          return ("Book Title: " , self.Title ,  "Book Author: " , self.Author, "Book Price: " , self.Price)
          

MyBook = Book("Python Crash Course" , "Eric Matthes" , "23 $")          
print( MyBook.view())