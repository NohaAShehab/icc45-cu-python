""" How can the function deals with the variables within
python module === .py file """


course = 'python'  # global variable


def say_hi():
    # any variable defined inside a function local variable
    name= input('What is your name?')  # local
    print(f'Hi {name}')


# say_hi()

# print(name)




"""
    ************ Access global variables  from inside function *************
"""

meal="Grilled-chicken"

def printTodayMeal():
    print(f"my lunch today is {meal}")

# printTodayMeal()



def printNohaMeal():
    meal = "BashaMeal"  # local variable
    print(f"my lunch today is {meal}")

# printNohaMeal()
# print(f"meal is {meal}")

"""*****************Modify global variable from inside the function  """

def defaultMeal():
    global meal
    meal = "vegetables"  # please don't create newone, just use the global
    print(f"my lunch today is {meal}")

# defaultMeal()




names = []

def askforStudents(stds:list):
    for i in range(5):
        stds.append(input(f"What is your name?"))


# askforStudents(names)
# print(names)
#
# sddd = []
# askforStudents(sddd)



infoo = []
def askforStudents():
    global infoo
    for i in range(5):
        infoo.append(input(f"What is your name?"))


"""******************************* Local scopes *******************************"""

def outerFunction():
    track = "Devops"# local variable


    print(f"track = {track}")

# outerFunction()

"----------******************* ----"
def outerFunction():
    track = "Devops"# local variable can be accessed anywhere inside the function
    def printTrack():
        print(f"from the printfunction {track}")

    printTrack()
    print(f"track = {track}")


# outerFunction()

"***************************************"

def outerFunction():
    track = "Devops"# local variable can be accessed anywhere inside the function
    def printTrack():
        print(f"from the printfunction {track}")

    def modifyTrack():
        track = input("What is your track name ?") # create new local variable
        print(f"track after updated  = {track}")

    printTrack()
    modifyTrack()
    print(f"track = {track}")


# outerFunction()
"""********************************"""
def outerFunction():
    track = "Devops"# local variable can be accessed anywhere inside the function
    def printTrack():
        print(f"from the printfunction {track}")

    def modifyTrack():
        nonlocal track  # please don't create new, use the parents' one
        track = input("What is your track name ?") # create new local variable
        print(f"track after updated  = {track}")

    printTrack()
    modifyTrack()
    print(f"track = {track}")


# outerFunction()





def A():
    track = "Devops"
    print(f"before calling the B {track}")
    def B():
       def C():
           track = "MMMMMMMM"
           def D():
               def E():
                   nonlocal track
                   print(f"from E {track}")
                   track = "Updated"
               E()
           D()
       C()
    B()
    print(f"after calling the B {track}")


A()








