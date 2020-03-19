class MenuItem:
  def __init__(self,name,price):
    # インスタンスが生成された瞬間にインスタンス変数に値が代入される
    self.name = name
    self.price = price
    # menu_item1.name = 'サンドイッチ'
    # menu_item1.price = 500  これらとほぼ同じ記述

  def info(self):
    return self.name + ': ¥' + str(self.price)

  def get_total_price(self,count):
    # countにselfがつかないのはインスタンス変数が定義されていないから
    total_price = self.price * count
    if count >= 3:
      total_price *= 0.9

    return round(total_price)