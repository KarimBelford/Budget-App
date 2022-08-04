class Category:
  
  def __init__(self,category):
    self.ledger = []   
    self.category= category
    self.total = 0

  def check_funds(self,amount):
    if amount <= self.get_balance():
      return True
    else: 
      return False
    
  def deposit(self,amount, description = ''):  
    self.ledger.append({"amount": amount, "description": description})
    self.total += amount
    
  def withdraw(self,amount, description = ''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.total -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.total

  def transfer(self,amount,t_category):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description":"Transfer to {}".format(t_category.category)})
      self.total -= amount
      t_category.ledger.append({"amount": amount, "description":"Transfer from {}".format(self.category)})
      t_category.total += amount
      return True
    else:
      return False

  def __str__(self):
    display = ''
    display = self.category.center(30, "*") + "\n"
    for item in self.ledger:
      if (len(item['description'])>23):
        display += item['description'][0:23].ljust(23)
      else:
        display += item['description'].ljust(23)
      display += "{0:.2f}".format(item['amount']).rjust(7)
      display += '\n'
    display += 'Total: {}'.format(self.total)      
    return display
    
def create_spend_chart(categories):
  chart = 'Percentage spent by category\n'
  category_names = []
  sum=0
  withdrawl = {}
  for name in categories: 
    withdrawl[name.category] = 0
    for item in name.ledger:
      if item['amount'] < 0:
        withdrawl[name.category] += item['amount']
        category_names.append(name.category)
      withdrawl[name.category] =- withdrawl[name.category]
  for name in withdrawl:
    sum+= withdrawl[name]
  for name in withdrawl:
    withdrawl[name] = int(withdrawl[name]/sum*100)
      
      
  for label in range(100, -10, -10):
    chart += str(label).rjust(3) + '| '
    for name in categories:
      if withdrawl[name.category] >= label:
        chart += 'o  '
      else:
        chart += '   '
    chart += "\n"
  chart += ' '*4 + '-'*(1+len(categories)*3) +'\n'

  longest_name_length = 0

  for name in categories:
    if longest_name_length < len(name.category):
      longest_name_length = len(name.category)

  for i in range(longest_name_length):
    chart += ' '*5
    for name in categories:
      if len(name.category) > i:
        chart += name.category[i] + '  '
      else:
        chart += ' '*3
    chart += '\n'
    

  return chart[0:-1]
    
    
      