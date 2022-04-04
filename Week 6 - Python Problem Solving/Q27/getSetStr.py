# Define a class/function which has at least two methods: getString: to get a string from console
# input printString: to print the string in upper case.


class getSetStr:
    def __init__(self):
        self.str1 = ""


    def setString(self):
        self.str1 = input("Enter a String : ")
        

    def getString(self):
        print("Output : ",self.str1.upper())



obj = getSetStr()
obj.setString()
obj.getString()