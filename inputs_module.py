
def askforInt(message='please enter an integer'):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("----plz enter valid integer----")

# askforInt("plEasw enter salary")

"""these lines will run only if this file run """

if __name__ == '__main__':
    ##
    print("*************** welcome to inputs module **********************")
