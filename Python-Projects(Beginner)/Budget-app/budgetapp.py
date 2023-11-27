class Category:
  def __init__(self, label):
    self.label  = label
    self.ledger = []

  def get_balance(self):
    c = 0
    for item in self.ledger:
      c += item['amount']
    return c

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True

    return False

  def transfer(self, amount, obj):
    if self.withdraw(amount, "Transfer to " + obj.label):
      obj.deposit(amount, "Transfer from " + self.label)
      return True

    return False

  def __str__(self):
    output = ""
    output += self.label.center(30,"*") + "\n"

    total = 0
    for item in self.ledger:
      total += item['amount']

      output += item['description'].ljust(23, " ")[:23]
      output += "{0:>7.2f}".format(item['amount'])
      output += "\n"

    output += "Total: " + "{0:.2f}".format(total)
    return output

def create_spend_chart(categories):
  output = "Percentage spent by category\n"

  # Retrieve total expense of each category
  total      = 0
  expenses   = []
  labels     = []
  len_labels = 0

  for item in categories:
    expense    = sum([-x['amount'] for x in item.ledger if x['amount'] < 0])
    total     += expense

    if len(item.label) > len_labels:
      len_labels = len(item.label)

    expenses.append(expense)
    labels.append(item.label)

  # Convert to percent + pad labels
  expenses = [(x/total)*100 for x in expenses]
  labels   = [label.ljust(len_labels, " ") for label in labels]

  # Format output
  for c in range(100,-1,-10):
    output += str(c).rjust(3, " ") + '|'
    for x in expenses:
      output += " o " if x >= c else "   "
    output += " \n"

  # Add each category name
  output += "    " + "---"*len(labels) + "-\n"

  for i in range(len_labels):
    output += "    "
    for label in labels:
      output += " " + label[i] + " "
    output += " \n"

  return output.strip("\n")