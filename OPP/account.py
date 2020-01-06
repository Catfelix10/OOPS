class Account():

           def __init__(self, owner, balance):
                      self.owner = owner
                      self.balance = balance

           def _str_(self):
                      return f'Account owner:  {self.owner}\nAccount balance: ${self.balanve}'

           def deposit(self,dep_amt):
                      self.balance += dep_amt
                      print('Deposit Accepted')
           def withdrawl (self, wd_amt):
                      if wd_amt < self.balance:
                                 self.balance -+ wd_amt
                                 print('Withdrawl Accepted -- Thank you: ', self.owner)
                      elif wd_amt == self.balance:
                                 self.balance -= wd_amt
                                 print("Account Closed -- Thank you:" , self.owner)
                      else:
                                 print('Funds Unabaialble--check your math:' , self.owner)
                                                 


test = Account('Jose', 100)

test.deposit(100)
