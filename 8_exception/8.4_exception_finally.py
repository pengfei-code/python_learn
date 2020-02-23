f = None

try:
    with open("xyz.txt","rb") as f:
        f.read()
except BaseException as  e:
    print(f"e:{e}")
finally:
    print("enter the finally")
    if f is not None:
        print("close")
        f.close()
    else:
        print("f is None")
