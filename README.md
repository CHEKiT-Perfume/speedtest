# ツール・ライブラリの名前

SpeedTest on fast.com

## 簡単な説明

fast.comのサイトにChromeでアクセスしてその時の回線速度を取得します。<br>
実行したフォルダにout.csvができますのでタスクスケジューラなり、Cronなりで定期実行してください<br>

## 実行環境

- Python 3.11.5
- Selenium 4.12.0
- webdriver-manager 4.0.0

## 使い方

以下をインストールしてください<br>
■Pythonのインストール<br>
https://www.python.jp/install/windows/install.html<br><br>
■PowerShellの環境設定<br>
```
$ Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```
■Seleniumのインストール<br>
```
$ pip install selenium
```
■webdriver_managerのインストール<br>
```
$ pip install webdriver_manager
```


## 使い方

リポジトリをクローンしてspeedtest.pyを実行してください

```
$ git clone git@github.com:CHEKiT-Perfume/speedtest.git
$ cd speedtest
$ python speedtest.py
```

## exeファイルへの変換

exeに変換したい場合speedtest.pyがあるフォルダで下記コマンドを実行してください<br>
distのフォルダの中にexeファイルが作成されます<br>

```
$ pip install pyinstaller
$ pyinstaller speedtest.py –onefile -noconsole
```

## 作者

[@GOETAN_GOETAN(https://twitter.com/GOETAN_GOETAN)]<br>
mail to: h.kawagoe@it-guardian.jp<br>
