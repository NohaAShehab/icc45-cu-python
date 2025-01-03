

# program --> menu
"""
    1- add book
    2- edit book
    3- delete book
    4- list book
"""
from json_demo.operations import  addbook, editbook, deletebook, listbook

def main():
    while True:
        choice = input(""" please enter your choice:
                1- add book 
                2- edit book 
                3- delete book 
                4- list book 
                5- exit
                """)
        if choice == '1':
            addbook()
        elif choice == '4':
            listbook()
        elif choice == '5':
            exit()
        else:
            print("--- please enter a valid choice ---")

if __name__ == '__main__':
    main()

