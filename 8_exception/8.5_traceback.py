import  traceback
try:
    a = 1/0
except BaseException as e:
    traceback.print_exc()
    print(f"e:{e}")
    pass
finally:
    traceback.print_exc()
    pass


