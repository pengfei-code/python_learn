#shutil copy

import  shutil


shutil.copyfile("cache","test/cache")

shutil.copytree("test","test1")

shutil.copytree("test","test2",ignore=shutil.ignore_patterns("*.html","*.txt"))