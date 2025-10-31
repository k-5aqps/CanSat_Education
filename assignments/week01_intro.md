# 第1週 概要/環境構築/Pythonの復習
## 概要
6週間をかけて，入門編CanSatの機体制御プログラムを作成します．流れは以下の通りです．
<ul>
    <li>[1週目]：イントロダクション</li>
    <li>[2週目]：モータ制御実装</li>
    <li>[3週目]：画像処理入門/実装</li>
    <li>[4週目]：ログ出力/実装</li>
    <li>[5週目]：全モジュール結合&走行プログラム実装</li>
    <li>[6週目]：模擬大会&模擬発表</li>
</ul>

模擬大会/模擬発表の仕方は` assignments/week06_competition.md` を参考に(決まり次第，随時情報を追加していきます)．

## 環境構築

### 1. PC側の準備

 - [Visal Studio Code](https://code.visualstudio.com/download)，[PiImager](https://www.raspberrypi.com/software/)，[TeraTerm](https://teratermproject.github.io/)をインストール．<br>
それぞれの指示に従う．

 - MicrosoftStoreからPythonをインストール．バージョンは何でもOK．

### 2. RaspberryPiの準備
 - マイクロSDカードをPCに挿入(必要に応じて変換器を使用)
 - PiImagerを起動
 - デバイスは「 **RaspberryPiZERO** 」，OSは「 **32bit Legacy Lite** 」を選択
 - 設定を編集するを選択．以下のように設定

 |項目|内容|
 |---|---|
 |ホスト名|raspberrypi|
 |ユーザ名|pi|
 |パスワード|raspberrypi|
 |SSID|スマホのテザリング設定を入力|
 |パスワード|同上|
 |WiFiを使う国|JP|
 |タイムゾーン|ASIA/Tokyo|
 |キーボード配置|JP|
 |SSHを有効化する|☑|
 |パスワード認証を使う|☑|

  - 保存⇒書き込み
  - 書き込み終了次第，RaspberryPiZEROにマイクロSDを挿入．
  - PCをスマホのテザリングに接続し，RaspberryPiに電源を接続．
  - スマホのテザリングにRaspberryPiが接続されたら，TeraTermを起動し，以下のように入力する

|項目|内容|
|---|---|
|TCP/IP|☑|
|ホスト|pi@raspberrypi.local|
|SSH|☑|
|ポート番号|22|

 - OKをクリックし，接続．
 - 以下のように入力

|項目|内容|
|---|---|
|ユーザ名|pi|
|パスフレーズ|raspberry|
|ブレインパスワードを使う|☑|
<br>
 - OKをクリックし，以下のように表示されたら成功
 ```
 pi@raspberrypi.local:~$
 ```
 <br>

 - 次のコマンドを実行
```
sudo apt-get update
```
```
sudo apt-get upgrade
```

<br>

 - RaspberryPiに`example\00-intro\intro.py`をコピーし，`python3 intro.py`と実行する．
 ```
 Hello,World!!
 ```
 と出力されることを確認する．

 - RaspberryPiをシャットダウンする．`sudo shutdown now`

## Pythonの復習
以下の問題に合う，プログラムを作成し，その動作結果を確認せよ．

### 1. 標準入出力
```math
y = x^2+x+10
``` 
について，任意のxを与えた時，yの値を出力するプログラムを作成せよ．ただし，以下は出力例である．
```
y = x^2 + x + 10
x = 5[ユーザ入力]
答えはy = 40です．
```
### 2. 条件分岐

ジャンケンの勝敗判定を行うプログラムを作成せよ．ただし，以下は出力例である．
```
A：グー[ユーザ入力]
B：チョキ[ユーザ入力]
判定結果 >>> Aさんの勝ち
```
### 3. 繰り返し文

1の問題について，xが-10から10までの範囲について，yの値を出力するプログラムを作成せよ．ただし，xは1ずつ大きくなると考えてよい．また，for文を使うこと．
```
y = x^2 + x + 10
| x | y |
|-10|100|
|-9 |82 |
|-8 |66 |
以下略
```

### 4. 関数
任意の個数のフィボナッチ数列を出力するプログラムを関数の再帰呼び出しによって作成せよ．
```
0,1,1,2,3,5,8,......
```

### 5. リスト
CUIの簡易単語テストを作成せよ．英単語の訳を回答させる形式であり，毎回，出題される英単語はランダムにすること．
<br>ヒント1：英単語リストと訳リストを作る．
<br>ヒント2：`random`モジュール使う．