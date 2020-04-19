# m5LineTracer


# ハードウェア

以下の３つを購入します

- m5stickC
- beetleC
- センサ

上記の３つを組み合わせて以下のようなm5lineTracerをつくります。

# ソフトウェア

## UIFlow-Desktop-IDEのインストール

どこからかUIFlow-Desktop-IDEを入手しインストールします

## ファームウェアの書き込み

- m5lineTracerをPCにusb接続します

- UIFlow-Desktop-IDEを起動し、以下の設定をします
    - COM:ｍ5stickCがつながっているポート番号
    - 言語:日本語
    - Device:Stick-C
- Firewareの書き込み
    - メニューからFirewareBurnerを選択
    - 以下の内容で書き込み(burn)
        - UIFlow-v1.4.5
        - Baudrate:115200
        - Series:StickC
        - SSID:任意、入れるとネットワーク越しで更新可能
        - Password:任意、入れるとネットワーク越しで更新可能

## プログラムの書き込み

- m5stickcの左側面ボタンをおして再起動し、起動中にm5ボタンを押しっぱなしにします
- 選択画面で右側面画面でsettignを選択しm5ボタンで選択、usbmodeを選択します
- m5stickcをusb接続した状態でUIFlowのアプリ本体の右下の接続状況の更新を行うと「disconnect」から「接続済み」になります
- アプリ本体のpythonタブに切り替えてmain.m5fを張り付けてrunボタンを押します

# 動作

白い紙に黒いマジックで塗った円の上を走ります。カーブが急すぎると曲がり切れません




    - トラブルシューティング
        - 書き込めない場合は、USB抜き差しやボーレートを変えてみる

- プログラムの書き込み