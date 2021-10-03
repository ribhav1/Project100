class atm(object):
    def __init__(self, atm_card_number, pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
        
    balance = 0

    def check_balance(self, atm_card_number, pin_number):
        print(self.balance)

    def cash_withdrawl(self, atm_card_number, pin_number, amount):
        if self.balance > 0:
            if self.balance - amount < 0:
                print('You cannot withdraw $' + amount + ' because you do not have enough money in your account')
            else:
                self.balance = self.balance - amount
                print('You have withdrawed ' + str(amount) + ' from your account')
                print('Your account balance is now: ' + str(self.balance))
        else:
            print('You have no money in your account')

    def cash_deposit(self, atm_card_number, pin_number, amount):
        self.balance = self.balance + amount
        print('You have deposited ' + str(amount) + ' into your account')
        print('Your account balance is now: ' + str(self.balance))

atm_card_number = input('Enter ATM card number: ')
pin_number = input('Enter Pin number: ')

atm_machine = atm(atm_card_number, pin_number)
atm_machine.check_balance(atm_card_number, pin_number)
atm_machine.cash_withdrawl(atm_card_number, pin_number, 5)
atm_machine.cash_deposit(atm_card_number, pin_number, 5)
