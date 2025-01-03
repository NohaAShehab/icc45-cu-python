

"""1- import the module """

import  inputs_module
#
# num= inputs_module.askforInt("please enter age: ")
# print(num, type(num))

""" import part of the module """
# from inputs_module import askforInt
# print(askforInt())

""" import from package"""
# from devops.greeting import saywelcome
# saywelcome("Ahmed")

# import devops.greeting
#
# devops.greeting.saywelcome("wr")
#######################

""" ---- Alias the block .. /// module you import ?? """

# import inputs_module as inn

# from inputs_module import askforInt as getnum

""" *****************packages with __init__ ****************"""

# import  iti.validation
#
# print(iti.validation.validate_int("fsdf"))

""" ------------ """
from iti import validate_int

print(validate_int('jkh'))


from iti import hii
hii()
