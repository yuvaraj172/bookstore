class NoteBook:

    def __init__(self,companyname,type,isbn, price = 0 ):
        self.companyname = companyname
        self.type= type
        self.isbn = isbn
        self.price = price

class Notebook:

    books = []
    selectedBook = []

    def __init__(self, companyname, type, isbn, price ):
        b = NoteBook(companyname,type,isbn = isbn, price = price)
        self.books.append(b)
    
    def show(self):
        print("============== AVAILBALE NOTEBOOKS ==========")
        
        pos=0

        for book in self.books:
            print("============ ", pos, " ==========") 
            pos += 1   
            self.display(book)
            
    
    def select(self):
        print("========== SELECT A NOTEBOOK ========")
        print("====== HOW MANY BOOKS YOU WANT? ======")
        neededBooks = int(input())

        for i in range(0, neededBooks ):
            print("====== INPUT THE NOTEBOOK NO ======")
            selectedBook = int(input())
            print("========== SELECTED A NOTEBOOK =======")
            b = self.getBookById(selectedBook - 1)
            self.selectedBook.append(b)
            print(self.display(b))

    def getBookById(self, position):
        return self.books[position]

    def display(self, book):
        print("Book name : ", book.companyname)
        print("Book ISBN : ", book.isbn)
        print("Book Price : ", book.price)
        print("Book Type : ",book.type)

    def selectedBooks(self):
        return self.selectedBook


class BillCounter:

    books = []
    def __init__(self, myBooks):
        self.books = myBooks
    
    def display(self):
        pos = 0
        for book in self.books:
            print("============ BILL COUNTER BOOKS ========")
            pos += 1
            print("============ BOOK NO", pos,"========")
            print("Book name : ", book.companyname)
            print("Book ISBN : ", book.isbn)
            print("Book Price : ", book.price)
            print("Book Type : ",book.type)

    def getTotal(self):
        total = sum(map(lambda b : b.price, self.books))
        print("=========== TOTAL PRICE =======")
        print(total)
    
    def getMax(self):
        total = max(map(lambda b : b.price, self.books))
        print("=========== MAX PRICE =======")
        print(total)

    def getMin(self):
        total = min(map(lambda b : b.price, self.books))
        print("=========== MIN PRICE =======")
        print(total)

    def getType(self):
        print("================== TYPE =============")
        type = map(lambda t : t.type, self.books)
        for type in type:
            print(type)
    

    def delete(self):
        print("=========== DO YOU WANT DELETE? 1 = YES, 0 = NO")
        choice = int(input())
        if (choice == 1):
            print("=========== ENTER BOOK NUMBER =======")
            position = int(input())
            self.books.remove(self.getBookById(position))
        else:
            print("=========== NO BOOKS =========")

    def getBookById(self, position):
        return self.books[position - 1]

    
if "__MAIN__":

    print("========== WELCOME TO BOOK STORE ==========")

    nb = Notebook("CLASSMATE UNRULED", "100 PAGES", "ABC123", 199)
    nb = Notebook("BHASKAR", "200 PAGES", "XYZ123", 399)
    nb = Notebook("TILDA UNRULED", "300 PAGES", "ABC567", 299)
    
    
    nb.show()

    nb.select()

    selectedBooks = nb.selectedBooks()
    
    print(selectedBooks)

    bc = BillCounter(selectedBooks)

    bc.display()

    bc.delete()

    bc.getTotal()

    bc.getMax()

    bc.getMin()

    bc.getType()
