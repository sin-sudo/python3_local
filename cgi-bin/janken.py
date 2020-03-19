#! /usr/bin/env python3

import sys
import io

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print("Content-type: text/html; charset=utf-8")

# print(“””  “””)で囲んだ部分にhtmlを書く。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。
print(
   """
     <html>
       <head>
           <meta http-equiv=\"Content-Type\" content=\ "text/html
           charset=utf-8\" / >       
           <title>じゃんけんゲーム</title>
</head>
     <body>
       <h1>じゃんけんゲーム</h1>
  <p>名前と出す手を決めてください（０：グー、１：チョキ、２：パー）</p>
  <form action="/cgi-bin/sample.py" method="POST">
   <input type="text" name="name" placeholder="名前">
   <input type="number" name="hand" placeholder="0~2">
   <input type="submit">
  </form>
     </body>
     </html>
     """
)

