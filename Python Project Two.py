class Account:
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
    
    def deposit(self,deposit):
        
        if(deposit < 0):
            return('Deposit needs to be positive')
        
        else:
            self.balance += deposit
        return "Deposit accepted"
    
    def withdraw(self,withdraw):
        if(withdraw < 0):
            return('withdraw needs to be positive')
        
        elif(withdraw > self.balance):
            return('Funds Unavailable')
        
        else:
            self.balance -= withdraw
            
        return "Withdraw accepted"  