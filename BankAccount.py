class BankAccount: #buraya genel sistem adını yaz içeri işlevsellik ekliycen
  def __init__(self, owner, balance): #bu ana fonksiyonun ve altına temelleri atıyosun
    self.owner = owner 
    self.balance = balance

  def deposite(self, amount): #bunlar yardımcı fonksiyon gibi işlem yapıp ana fonksiyon değişkenleriyle iş yapıyor
    self.balance += amount

  def withdraw(self, amount):
    if amount > self.balance :
      print("Not enough balance")
    else:
      self.balance -= amount
    
  def __str__(self):
    return f"Owner: {self.owner}\nBalance: {self.balance}"
  
name = input("Enter your name:")
balance = int(input("Enter your balance:"))
acc = BankAccount(name, balance)

withdraw = input("Do you want to withdraw money?(y or n)")

if withdraw.lower() == "y" :
  amount = int(input("How much?"))
  acc.withdraw(amount)

deposit = input("Do you want to make a deposit?(y or n)")

if deposit.lower() == "y":
  amount = int(input("How much?"))
  acc.deposite(amount)

print(acc)
    