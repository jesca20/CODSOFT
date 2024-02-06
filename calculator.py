while True:
    num1=float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))

    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.EXIT")

    choice = input("Enter the operation to perform:")

    if choice == '1':
        print("Answer :",num1+num2)
        
    elif choice == '2':
        print("Answer :",num1-num2)    
        
    elif choice == '3':
        if(num1==0 or num2 ==0):
            print("Answer : 0")
        else:
            print("Answer:",num1*num2)    
            
    elif choice =='4':
        if(num2==0):
         print("Mathematical Error.")
        else:
          print("Answer:",num1/num2)   
          
    elif choice=='5':
       exit

    option = input("Do you want to continue other operation?(y/n)").lower()
    if (option == "n"):
        break     

