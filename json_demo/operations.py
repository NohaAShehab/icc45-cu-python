from inputs_module import  askforInt, askforString
from fileoperations import save_book, read_all_books, generate_id
def addbook():
    print("addbook")
    no_of_pages = askforInt("Enter number of pages")
    title = askforString("Enter title")
    bookdata = {
        "id": generate_id(),
        "title": title,
        "no_of_pages": no_of_pages
    }
    # print(bookdata)
    ## title , no_of_pages
    # I need to save the data to a file
    saved = save_book(bookdata)
    if saved:
        print("----------books saved----------")


def editbook():
    print("editbook")


def deletebook():
    print("deletebook")

def listbook():
    print("listbook")
    allbooks = read_all_books()
    for book in allbooks:
        print(f"{book['title']}: {book['no_of_pages']}")
        print("----------------------------------------")
