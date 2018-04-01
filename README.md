Python + SQLite（エスキューライト。超簡素なローカルRDBMS）で  
簡単にSQLを自習するためのPythonスクリプト。  
  
http://www.atmarkit.co.jp/ait/articles/0508/31/news092.html  
基本情報技術者試験講座（4）：
SQLでデータベースを操作しよう

に書いてあるSQL文を試せる。

■ Windows版Pythonを入れる
参考：
https://qiita.com/taiponrock/items/f574dd2cddf8851fb02c

■ Git for Windows版Gitを入れる
https://gitforwindows.org/

■ このGithubリポジトリを自分のPCに取り込む

コマンドプロンプトを立ち上げて
（スタートメニュー → Windows システム ツール → コマンド プロンプト）、

git clone https://github.com/chihiroyn/sqlite-sample.git

たったこれだけでOK！

■ 実行してみる

コマンドプロンプトで、
cd sqlite-sample

python sample.py

正しくセットアップできていれば、これで結果が得られる。

■ SQLをいろいろいじってみる

「sqlite-sample」フォルダの中の
「database.py」
の、一番後ろ、「select_data」メソッドの中に、
SELECT文がいろいろ書いてあります。

ここをいろいろ触って、

python sample.py

してから、動作を確認してみよう。

以上

がんばれ！
