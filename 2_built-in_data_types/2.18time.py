from datetime import datetime
timenow = datetime.now()
print(timenow)

#aquire the specify time
dt = datetime(2019,12,21,23,54,23)
print(dt)
print(dt.timestamp())
print(type(timenow))#class datetime
print(type(dt))#class datetime
# get the time  year month  day  hour minute  second 
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)


print(datetime(800,1,1,0,0).timestamp())

#   about ocd 
# I dont care  but  the  sentiment  you can have ，
# I‘ll never guess it this is not  scope of my ability


dtStrF = dt.strftime("%Y-%m-%d: %H:%M:%S")
print(dtStrF)



