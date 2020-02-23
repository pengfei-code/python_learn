#if you want to catch the multiple Exceptions ,the order of exception you'd better
#except from  sonclass to inherited class
try:
    a=1/0
    pass
# except:
#     pass
except ZeroDivisionError as e:
    print(f"e:{e}")
except ArithmeticError as ae:
    print(f"ae:{ae}")

except Exception as ex:
    print(f"ex:{ex}")

except BaseException as be:
    print(f"be:{be}")

except :
    
    pass



