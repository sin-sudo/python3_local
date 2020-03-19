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
  <title>料理注文システム</title>     
</head>
<style>
  form {
    display: flex;
    flex-direction: column;
  }
  input {
    width: 30%;
  }
  ul {
    list-style: none;
  }
</style>
     <body>
       <h1>料理注文システム</h1>
<p>三セット以上購入で一割引きです。それぞれ番号で選んでください。</p>
<h2>食べ物メニュー</h2>
<ul>
  <li>0.サンドイッチ:¥400(300kcal)</li>
  <li>1.チョコケーキ:¥500(600kcal)</li>
  <li>2.シュークリーム:¥300(500kcal)</li>
</ul>
<h2>飲み物メニュー</h2>
<ul>
  <li>0.コーヒー:¥200(200ml)</li>
  <li>1.オレンジジュース:¥150(300ml)</li>
  <li>2.エスプレッソ:¥250(200ml)</li>
</ul>
<form action="/cgi-bin/script.py" method="POST">
  <input type="number" name="number" id="food"><label for="food">食べ物（０～２）</label>
  <input type="number" name="count" id="drink"><label for="drink">飲み物（０～２）</label>
  <input type="number" name="set" id="count"><label for="count">セット数</label>
  <input type="submit">
</form>
     </body>
     </html>
     """
)

