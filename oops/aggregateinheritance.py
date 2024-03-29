class Author:
    def __init__(self, name, birth_year):
        self.name=name
        self.birth_year=birth_year


    def get_author_info(self):
        return f"{self.name} (born in {self.birth_year})"
    


class Book:
    def __init__(self, title, publication_year, author:Author):
        self.title=title
        self.publication_year=publication_year
        self.author=author
    
    def get_book_info(self):
        return f"Book is {self.title} by Author {self.author.get_author_info()}, published in {self.publication_year}"
    

author_obj=Author("APJ Abdul Kalam", 1942)
book_obj=Book("Wings of fire", 2000, author_obj)

print(book_obj.get_book_info())


