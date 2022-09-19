class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        if(self.balance-amount) >=0:
            self.balance-=amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -=5
        return self
        # your code here
    def display_account_info(self):
        print(f"Balance: $ {self.balance}")
        return self
        # your code here
    def yield_interest(self):
        if self.balance >0:
            self.balance += (self.balance * self.int_rate)
        return self
        # your code here
checking = BankAccount(.01, 100)
savings = BankAccount(.03, 2500)    

checking.deposit(300).deposit(256).deposit(42).withdraw(17).yield_interest().display_account_info()

savings.deposit(800).deposit(1500).withdraw(450).withdraw(50).withdraw(20).withdraw(100).yield_interest().display_account_info()


class User:	
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0
        self. account = BankAccount(int_rate=0.02, balance=0)

    def display_info(self):
        print(self.first_name,self.last_name,self.age,self.email,self.is_rewards_member,self.gold_card_points)

    def enroll(self):
        is_rewards_member = True

    def spend_points(self, amount):
        gold_card_points = gold_card_points - amount

    def make_deposit(self, amount):
        self.account.balance+=amount
        return self

    def make_withdraw(self, amount):
        self.account.balance-=amount
        return self

    def display_account_info(self):
        print(f"Balance: $ {self.account.balance}")
        return self


User_mia = User("Mia", "Thermopolis", 32, "princessofgenovia@gmail.com")
User_scott = User("Scott", "Styles", 17, "wolffriend@yahoo.com")
User_ted = User("Ted", "Lasso", 46, "englishfootbal@crumpet.com")


User_mia.enroll()
User_mia.spend_points(50)

User_scott.enroll()
User_scott.spend_points(80)

User_mia.display_info()
User_scott.display_info()