# Write a function to replace word with another word and another function to replace only alphabet


class Replace:
    def __init__(self,str1):
        self.str1 = str1.lower()

    def replaceWord(self):
        word = input("\nEnter a word to replace : ")
        rep = input("Enter a replacement word : ")
        list1 = self.str1.split()

        for i in range(len(list1)):
            if list1[i] == word:
                list1[i] = rep

        self.str1 = " ".join(list1)
        return self.str1



    def replaceChar(self):
        char = input("\nEnter a character to replace : ")
        rep = input("Enter a replacement character : ")
        
        revstr=""

        for i in range(len(self.str1)):
            if self.str1[i] == char:
                revstr += rep
            else:
                revstr += self.str1[i]

        self.str1 = revstr
        return self.str1


s1 = input("Enter a String : ")


obj1 =Replace(s1)
print("String after replacing word : ",obj1.replaceWord())


print("String After replacing Character : ",obj1.replaceChar())