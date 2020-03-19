from menu_item import MenuItem

class Food(MenuItem):
  def __init__(self,name,price,calorie):
    super().__init__(name,price)
    self.calorie = calorie

  def info(self):
    return self.name + ': ¥' + str(self.price) + '(' + str(self.calorie) + 'kcal)'

  def calorie_info(self):
    print(str(self.calorie) + 'kcalです')

# 変更部分
  def food_register(self,count):
    total = self.price * count
    print(self.name + 'を' + str(count) + '個ですね？食べ物は合計で' + str(total) + '円になります。') 
    if count >= 3:
      print('さらに' + str(count) + '個ご購入いただいたので一割引きで' + str(round(total * 0.9)) + '円です。')
     
