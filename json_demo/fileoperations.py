"""

    any operation with files --
"""


""" if you have json file --> architecture --> array of object  [{},{}, {}]
    and you need to add new object to the file ??
    it is better to read the file data into a list 
    save new object to the list 
    then write the list the file 

"""
import json

def read_all_books():
    try:
        fileobject = open('books.json', 'r')
        # read data from json ??
        books_list = json.load(fileobject) # parse file content to valid json {}, [{}, {}]
    except Exception as e:
        return []
    return books_list


def save_all_books(books_list):
    try:
        fileobject= open("books.json","w")
    except Exception as e:
        print(e)
        return False
    else:
        json.dump(books_list,fileobject, indent=4)
        fileobject.close()
        return True

def save_book(book):
    old_data  =read_all_books()  # list
    print(old_data)
    old_data.append(book) # add the new book to the list
    saved = save_all_books(old_data)
    return saved


#######################################

def generate_id():
    try:
        fileobject = open('id', 'r')
        id = fileobject.read()
        id = int(id)
        id +=1
        fileobject.close()
        fileobject = open('id', 'w')
        fileobject.write(str(id))
        fileobject.close()
    except Exception as e:
        return 1
    else:
        return id








