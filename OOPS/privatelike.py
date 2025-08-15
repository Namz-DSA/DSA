class Email:
    def __init__(self, mailid, pwd):
        self.mailid = mailid
        self.__pwd = pwd
    
    def __retreive_pwd(self):
        print(f"My password is {self.__pwd}")
    

e1 = Email("abc@gmail.com", "abc@123")

print(e1.mailid)
# print(e1.__pwd)
e1._Email__retreive_pwd()
print(e1._Email__pwd)