# About the os.path mudules
import os

print(os.getcwd())


print(f"the a.txt is exists:{os.path.exists('a.txt')}")

print(os.path.isabs("a.txt"))

print(os.path.isdir("test"))

#the file must exists
print(os.path.isfile("cache"))

print(os.path.abspath("cache"))


print(os.path.getsize("cache"))

print(os.path.dirname("/users/songpengfei"))

ctime =os.path.getctime("1.6_iter.py")
mtime = os.path.getmtime("1.6_iter.py")
atime = os.path.getatime("1.6_iter.py")

import datetime


# now_time =datetime.datetime.now()
# times = datetime.datetime(2019,12,23,23,12,54)
# print(now_time)
# print(times)

times = datetime.datetime.now()
print(times.timestamp())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

ctime_date = datetime.datetime.fromtimestamp(ctime)
atime_date = datetime.datetime.fromtimestamp(atime)
mtime_date = datetime.datetime.fromtimestamp(mtime)


print(ctime_date)
print(atime_date)
print(mtime_date)


cache_abs = os.path.abspath("cache")

print(f"cache_path is {cache_abs}")

print(os.path.split(cache_abs))

#os.path.join  keep adding the string after the specified path

print(os.path.join("/users","songpengfei","downloads"))
print(os.path.join(cache_abs,"subdirs"))


# Use the  list expression to implemet list all the files in a specified dir

file_list = [file_name for file_name in  os.listdir(".") if os.path.isfile(file_name)]

print(file_list)








