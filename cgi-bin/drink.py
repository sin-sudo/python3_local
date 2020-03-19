from menu_item import MenuItem

class Drink(MenuItem):
  def __init__(self,name,price,amount):
    super().__init__(name,price)
    self.amount = amount

  def info(self):
    return self.name + ': ¥' + str(self.price) + '(' + str(self.amount) + 'ml)'

  def drink_register(self,count):
    total = self.price * count
    print(self.name + 'を' + str(count) + '個ですね？飲み物は合計で' + str(total) + '円になります。') 
    if count >= 3:
      print('さらに' + str(count) + '個ご購入いただいたので一割引きで' + str(round(total * 0.9)) + '円です。')
     