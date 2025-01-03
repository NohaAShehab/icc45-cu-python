

def askforInt(message="please enter number of pages"):
    try:
        numm = int(input(message))
    except Exception as e :
        return askforInt(message)
    else:
        return numm


def askforString(message="please enter string"):
    while True:
        strr = input(message)
        if strr.isalpha():
            return strr

        print("--- please enter a string --- ")

