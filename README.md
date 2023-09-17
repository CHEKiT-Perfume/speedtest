# ツール・ライブラリの名前

SpeedTest on fast.com

## 簡単な説明

fast.comのサイトにChromeでアクセスしてその時の回線速度を取得します。<br>
実行したフォルダにout.csvができますのでタスクスケジューラなり、Cronなりで定期実行してください<br>

## 必要要件

- Python
- Selenium 
- webdriver_manager

## 使い方

以下をインストールしてください<br>
■Pythonのインストール<br>
https://www.python.jp/install/windows/install.html<br>
■PowerShellの環境設定<br>
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force<br>
■Seleniumのインストール<br>
pip install selenium<br>
■webdriver_managerのインストール<br>
pip install webdriver_manager<br>

## Windows EXEファイルへの変換

pip install pyinstaller<br>
pyinstaller speedtest.py –onefile -noconsole<br>

## インストール

```
$ git clone https://github.com/TomoakiTANAKA/awesome-tool
$ cd awesome-tool
$ sh setup.sh
$ ~do anything~
```

## 作者

[@GOETAN_GOETAN(https://twitter.com/GOETAN_GOETAN)<br>
mail to: h.kawagoe@it-guardian.jp<br>
