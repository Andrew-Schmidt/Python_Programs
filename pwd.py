import os
print(os.path.abspath(os.curdir))
os.chdir("../../..")
print(os.path.abspath(os.curdir))
