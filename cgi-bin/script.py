import cgi
import cgitb
cgitb.enable()
# from menu_item import MenuItem
from food import Food
from drink import Drink

print("Content-Type: text/html")
print()   

form = cgi.FieldStorage()



food1 = Food('サンドイッチ',400,300)
food2 = Food('チョコケーキ',500,600)
food3 = Food('シュークリーム',300,500)
foods = [food1,food2,food3]



drink1 = Drink('コーヒー',200,200)
drink2 = Drink('オレンジジュース',150,300)
drink3 = Drink('エスプレッソ',250,200)
drinks = [drink1,drink2,drink3]

 
order = int(form["number"].value)
count = int(form["count"].value)
set_count = int(form["set"].value)


# if order < 0 or order > len(foods) - 1:
#   print('正しい値を入力してください')
# elif count < 0 or count > len(drinks) - 1:
#   print('正しい値を入力してください')
# else:
#   result = selected_food.get_total_price(set_count) + selected_drink.get_total_price(set_count)
#   print('合計は'+str(result)+'円です')

# ０～２以外の数字を入れられた時の処理
try:
  selected_food = foods[order]
  selected_drink = drinks[count]
  # 変更部分
  selected_food.food_register(set_count)
  selected_drink.drink_register(set_count)
  result = selected_food.get_total_price(set_count) + selected_drink.get_total_price(set_count)
  print('合計は'+str(result)+'円です')
except IndexError:
  print('エラー！正しく値を入力してください')

