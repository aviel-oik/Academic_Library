class Library:
    max_borrow_days = 14
    def __init__(self):
        self.books = {}
        self.users = {}

    def register_user(self, user):
        self.users[user.user_id] = user

    def add_book(self, book):
        self.books[book.isbn] = book

    def perform_borrow(self, user_id, isbn):
        if user_id not in self.users:
            raise
        if isbn not in self.books:
            raise
        if self.books[isbn].is_available == True:
            self.books[isbn].is_available = False
            self.users[user_id].borrow_book(self.books[isbn])
            Logger.log_action("BORROW", {user_id, isbn})
            SystemAdmin.update_transactions_count()

    def perform_return(self,user_id, isbn):
        if user_id not in self.users:
            raise
        if isbn not in self.books:
            raise
        if self.books[isbn].is_available == False:
            self.books[isbn].is_available = True
            self.users[user_id].return_book(self.books[isbn])
            Logger.log_action("RETURN", {user_id, isbn})
            SystemAdmin.update_transactions_count()
        else:
            print("we have a problem")

