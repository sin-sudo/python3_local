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
        <meta charset="utf-8">
  <title>乾真一朗のポートフォリオサイト</title>
  <!-- <link href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" rel="stylesheet"> -->
  <link href="https://use.fontawesome.com/releases/v5.0.10/css/all.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link rel="stylesheet" href="../styles.css">
  <link rel="stylesheet" href="../responsive.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
      </head>
      <body>
        <header>

    <ul>
      <li><a href="#my-story">経歴</a></li>
      <li><a href="#my-hobby">趣味</a></li>
      <li><a href="#my-strong">自分の強み</a></li>
      <li><a href="#my-contact">コンタクト</a></li>
    </ul>
    
    <!-- <span class="fa fa-bars menu-icon"></span> -->
  </header>

  <div class="top-wrapper">
    <div class="wrapper">
      
      <div class="icon">
        <img src="../img/1454740.jpg" width="200" height="200">
      </div>

      <div class="info">
        <h1>乾真一朗</h1>
        <p>京都工芸繊維大学　工芸科学部　一回生</p>
        <p>プログラミング初心者です。</p>
      </div>
    


    </div>
  </div>

  <div class="history" id="my-story">
    <h1>経歴</h1>
    <div class="container">
      <div class="time">
        <p>2013年　中学校に入学</p>
        <p>2016年　京都の高校に入学</p>
        <p>2019年　京都工芸繊維大学に入学</p>
        <p>2019年　プログラミングに出会う</p>
        <p>2020年　未来電子に入社</p>
      </div>
      <div class="detail">
        <p>勉強に打ち込んで学年一位をもぎ取る</p>
        <p>継続して勉強に打ち込み校外模試で学年十四位を獲得</p>
        <p>主に大学の授業に時間を使っていたが、他のこともやりたくなる</p>
        <p>プログラミングを紹介している動画をyoutubeで発見</p>
        <p>切磋琢磨して成長したいと思い、入社</p>
      </div>
    </div>
  </div>

  <div class="hobbies" id="my-hobby">
    <h1>趣味</h1>
    <div class="hobby hobby1">
      <div class="hobby-wrapper">
        <h2>海外サッカー観戦</h2>
        <p>私は幼いころからサッカーをしていたこともあり、サッカー観戦することがすごい好きです。日本代表のサッカーも見ていてすごく応援したくなるのですが、なんといってもイングランドプレミアリーグ所属のアーセナルというチームが大好きです。もちろんサッカーするのも大好きです！</p>
      </div>
      <img src="../img/gahag-0078061838.jpg">
    </div>

    <div class="hobby hobby2">
      <div class="hobby-wrapper">
        <h2>YouTube</h2>
        <p>最近は「ダンビラムーチョ」という芸人の動画にはまっています。「野球部あるある」シリーズが自分のツボにはまり、何十回も見返す動画もあるほどです。ほとんど一分前後という短時間の動画なのですが、すごく楽しめます。</p>
      </div>
      <img src="../img/動画再生ボタン.jpeg">
    </div>

    <div class="hobby hobby3">
      <div class="hobby-wrapper">
        <h2>スマホゲーム</h2>
        <p>授業の空き時間などの隙間時間にスマホゲームするのにはまっています。おすすめはSlither.io、ミルクチョコ、ドラゴンクエストウォーク！特にドラゴンクエストウォークは外に出歩かないとモンスターが出てこない仕組みになっているので、過度に没頭する心配なしです！
        </p>
      </div>
      <img src="../img/gahag-0110580641.jpg">
    </div>
  </div>

  <!-- 変更部分 -->
  <div class="achievement">
    <h1>作品集</h1>
    <p>ここでは料理注文システムとじゃんけんゲームの機能を提供しています。私のアウトプットをどんどんこのサイトにアップしていきたいと思います！</p>
    <a href="janken.py" target="_blank" class ="app">じゃんけんゲームへ</a>
    <a href="menu.py" target="_blank" class="app">料理注文システムへ</a>
  </div>
  
  <section id="my-strong">
    <h1>自分の強み</h1>
    <div class="strong-point">
      <div class="strong">
        <h3>一度始めたことを継続努力できる</h3>
        <p>私は大学生になってからいろんなことに挑戦してきました。大学生になってから挑戦した大きなことの一つにプログラミングがありますが、2019年の8月の中旬からはじめて2020年2月の現在まで継続して学習してきました。これからも継続努力する耐久力に磨きをかけていこうと思います。</p>
      </div>
  
      <div class="strong">
        <h3>新しい環境に一人で飛び込める</h3>
        <p>私は意識的にいろんなことに挑戦することを心がけています。それによって新しい発見が必ずあるからです。実際未来電子のインターンに参加してから、マーケティングにも興味がわきました。プログラミングとWEBマーケティングを掛け合わせて、自分にしかできないことを今後できたらと思います。</p>
      </div>
      
    </div>
    <div class="modal">
      <span class="fa fa-2x fa-times"></span>
      <h1>ありがとうございます！</h1>
      <a href="https://twitter.com/inushin2" class="btn2" target="_blank">コンタクト</a>
    </div>
  </section>

  <div class="message-wrapper" id="my-contact">
    <div class="message-container">
      <h2>乾真一朗とコンタクトをとってみませんか？</h2>
    </div>
    <a class="btn">コンタクト</a>
  </div>

  <i class="fas fa-arrow-up"></i>
  <p id="scroll">トップへ</p>
  
  <script src="../script.js"></script>
      </body>
    </html>
     """
)
