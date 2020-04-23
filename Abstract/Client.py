from Abstract.Bank import Bank

class Clinet(Bank):
 pass


 def Get_slip(self):
       print("Thanks for using our services .... !")


client_1 = Clinet()
#client_1.Get_slip()

#print(client_1.Bank__Client_info())

#print(client_1._Bank__bank_name)


while True:
    print("1. Check Account Balance ")
    print("2. Withdraw Funds ")
    menu_option = int(input())

    if menu_option == 1:
       print("Your Current Balance is : ",client_1.Balance_getter())

    elif menu_option == 2:
        value = int(input("How much would you like to withdreaw : "))
        client_1.Balance_Setter(value)
        client_1.Get_slip()

    else:
        print("Wrong menu choice ....")



