import cgi
import cgitb
cgitb.enable()
import utils
# randomモジュールを読み込んでください
import random

print("Content-Type: text/html")
print()   

form = cgi.FieldStorage()

player_name = form["name"].value
player_hand = int(form["hand"].value)

# 名前が入力されなかったときの対処
# if player_name == '':
#     print_hand('グー')
# else:
#     print_hand('グー',player_name)

if utils.validate(player_hand):
# try:
    # randintを用いて0から2までの数値を取得し、変数computer_handに代入してください
    computer_hand = random.randint(0,2)
    
    if player_name == '':
        utils.print_hand(player_hand)
    else:
        utils.print_hand(player_hand, player_name)

    utils.print_hand(computer_hand, 'コンピューター')
    
    result = utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
# except TypeError:
    print('エラー！')
    print('正しい数値を入力してください')
