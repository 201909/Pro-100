from cmath import pi

from traitlets import CaselessStrEnum


class Atm():
    def __init__(self,user, card_no, pin_no, balance):
        self.user = user
        self.card_no = card_no
        self.pin_no = pin_no
        self.balance = balance

    
    def CashWithdrawl(self, wd_amount):
        if (self.balance>=wd_amount):
            net_balance=self.balance-wd_amount
            print("Balance: {}".format(net_balance))
        else:
            print("Sorry balance in not enough")
    
rishan = Atm("Rishan", '122345','1234',1200)
pin = input("Please enter your pin number ")
if(pin == rishan.pin_no):
    print("New balance: {}".format(rishan.balance))
    wish= input("Do you want to withdraw (yes/no) ")
    if wish.lower() == 'yes':
        wdamount = int(input("How much do you want to withdraw £ "))
        rishan.CashWithdrawl(wdamount)
    else:
        exit
else:
    print("pin number is wrong")

