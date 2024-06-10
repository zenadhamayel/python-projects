class user:
    def __init__(self,user_name):
        self.name=user_name
        self.account_balance=0


    def get_name(self):
        result=self.name
        return result
    def make_deposit(self,amount):
        self.account_balance +=amount
        return self
    def make_withdraw(self,amount):
        self.account_balance -=amount
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -=amount
        self.other_user +=amount
        return self
    def display_user_balance(self):
       display=self.name+" " +str(self.account_balance) 
       return display                







zenad=user("Zenad_Hamayel")
mohammad=user("moh hamayel")
print(zenad.get_name())
print(zenad.make_deposit(200).make_deposit(200).make_withdraw(50).make_deposit(200).display_user_balance())
print(mohammad.make_deposit(200).make_deposit(200).make_withdraw(50).make_deposit(200).display_user_balance())
print(mohammad.display_user_balance())
            