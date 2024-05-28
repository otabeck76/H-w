# class Bankaccount:
#     def __init__(self):
#         self.balance=0
#         self.__all_balans={}
       

#     def deposit(self,__account_number,amount):
#         self.__all_balans[__account_number]=amount+self.balance
#         self.balance+=amount
#     def withdraw(self,__account_number,amount):
#         self.__all_balans[__account_number]=self.balance-amount
#         self.balance-=amount
#     def get_balance(self,__account_number):
#         return f'нынешний Баланс:{self,__account_number[__all_balans]}'
#     def get_account_number(self,__account_number):
#         return f'Номер счёта: {__account_number}'
    
# a=Bankaccount()
# a.deposit (1,47)
# a.withdraw(1,30)
# print(a.get_account_number(1))
# print(a.get_balance(1))