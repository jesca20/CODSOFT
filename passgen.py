while True : 
 import random
 import string

 print("This is the password generator made using python.")
 print("-------------------------------------------------")
 passlength = int(input("Enter the length for your password:"))

 def passgen():
    ucase = string.ascii_uppercase
    lcase = string.ascii_lowercase
    digit = string.digits
    splchar = string.punctuation

    all = ucase+lcase+digit+splchar

    if(passlength<8):
        print("The password length should not be less than 8 characters.")
        pass        
    else:
        password = ''.join(random.sample(all,passlength))
        return password

 password = passgen()
 print("The password is :",password)
 option= input("Do you want to generate another password?(y/n)").lower()
 if(option == 'n'):
  break   
        
 