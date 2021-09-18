class atm(object):
    def __init__(self, atm_card_number, pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number

    def check_balance(self, atm_card_number, pin_number):
        print('Your balance in your account is $2')

    def cash_withdrawl(self, atm_card_number, pin_number):
        print('You have withdrawed $2 from your account')

    def cash_deposit(self, atm_card_number, pin_number):
        print('You have deposited $2 from your account')
        
atm_machine = atm(12345678, 1234)
atm_machine.check_balance(12345678, 1234)
atm_machine.cash_withdrawl(12345678, 1234)
atm_machine.cash_deposit(12345678, 1234)