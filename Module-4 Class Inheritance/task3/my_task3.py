# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 07:54:40 2023

@author: Nico
"""

## Super class

class Book():
    
    # Keeptrack of created objects
    books = [] #class variable
    
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.books.append(self) # append book object to books class variable
        
    def display_info(self):
        print(f'{self.title}, {self.author}, {self.year}')
        
    
    

class FictionBook(Book):
    def __init__(self,title,author,year,genre):
        super().__init__(title,author,year)
        self.genre = genre
        
    def display_info(self):
        print(f'{self.title}, {self.author}, {self.year}, {self.genre}')
        


class NonFictionBook(Book):
    def __init__(self,title,author,year,topic):
        super().__init__(title,author,year)
        self.topic = topic
        
    def display_info(self):
        print(f'{self.title}, {self.author}, {self.year}, {self.topic}')


class Library():
    def __init__(self):
        self.list_of_books = []
        
    def add_book(self,book):
        self.list_of_books.append(book)
    
    def display_all_books(self):
        for book in self.list_of_books:
            book.display_info()

    def search_book(self,author):
        book_search = [book for book in self.list_of_books 
                       if book.author == author]
        for bk in book_search:
            bk.display_info()
            
    def search_book_by_year_range(self,year1,year2):
        book_search = [book for book in self.list_of_books if (book.year > year1 and book.year < year2)]
        for bk in book_search:
            bk.display_info()




book1 = Book("Big Adventure", "Gerald", 1998)
book2 = Book("The blood bath", "Cartener", 2001)
book3 = FictionBook("Lapinou lapinou", "kalel", 2020, "fiction")
book4 = NonFictionBook("Great", "Cartener", 2015, "nonfiction")
print(Book.books)
print()

my_lib = Library()
for book in Book.books:
    my_lib.add_book(book)
    
print("All books")
my_lib.display_all_books()

print("\nBook search")
my_lib.search_book("Cartener")

print("\nBook search by year range")
my_lib.search_book_by_year_range(1999,2016)