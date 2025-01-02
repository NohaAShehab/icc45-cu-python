#
# logged_in = False
# for t in range(3):
#     password = input("Enter Password: ")
#     if password == "1234":
#         print("Password is OK")
#         logged_in = True
#         break
#
#     print("--- invalid password please try again ---")
#
#
# ####
# if not logged_in:
#     print("--- account is locked ----")


### I need to lock the account only if loop reached its end

for t in range(3):
    password = input("Enter Password: ")
    if password == "1234":
        print("Password is OK")
        break

    print("--- invalid password please try again ---")

else:
    print('---- loop reached its end ')
    print("--- account is locked ----")

name=  ""
if name=="beshoy":
    pass

"""
    pass_stmt ::=  "pass"
pass is a null operation — when it is executed, nothing happens. 
It is useful as a placeholder when a statement is required syntactically, 
but no code needs to be executed, for example:
"""
