class Book:
    def __init___(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def get_details(self):
        return f"title : {self.title} , author : {self.author} , isbn : {self.isbn} , available : {self.is_available}"

