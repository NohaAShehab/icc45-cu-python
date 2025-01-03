

def divnums():
    try:
        num = int(input("please enter number : "))
        num2 = int(input("please enter number : "))
        res = num / num2
        print(res)
    except Exception as e:
        print(f"----- problem happpened : {e}")
        return False
    else:
        return res
    finally:
        # finally block preceeds the return
        print("************************THE END*************************")

print(divnums())