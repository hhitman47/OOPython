class Bank(object):


    def __init__(self , account_name = "Current", balance = 1000):
        self.__account_name = account_name
        self.__balance    = balance
        self.__bank_name = "HBL"
       # self.mobile = 563464536

    def __Client_info(self):
        print("Ishtiaq , accunt number : 4584 6434 1234 8584")

    def Balance_getter(self):
        Bank.__Client_info(self)
        return self.__balance

    def Balance_Setter(self, value):
         if self.__balance > (value) :
            self.__balance -= value
            print ("Current Update Balance is : ",self.__balance,"\nAccount type is : ",self.__account_name)
         else :
             print("You dont have enough Fund.....!")


