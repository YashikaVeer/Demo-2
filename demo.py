fn= input("Input the Filename: ")
f = fn.split(".")
if f[-1] == "py":
    print("The extension of file name is:'python'")
else:
    print("invalid")

