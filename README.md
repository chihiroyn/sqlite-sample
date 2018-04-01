Python + SQLite（エスキューライト。超簡素なローカルRDBMS）で  
簡単にSQLを自習するためのPythonスクリプト。  
  
http://www.atmarkit.co.jp/ait/articles/0508/31/news092.html  
基本情報技術者試験講座（4）：  
SQLでデータベースを操作しよう  
  
に書いてあるSQL文を試せる。  
  
■ Windows版Pythonを入れる  
参考：  
https://qiita.com/taiponrock/items/f574dd2cddf8851fb02c  
  
■ このGithubリポジトリを落とす  
  
https://github.com/chihiroyn/sqlite-sample/archive/master.zip  
を落として、  
解凍して、  
中身をホームディレクトリ（C:\Users\(アカウント名)）  
直下に置く。  
  
フォルダ名は、「sqlite-sample」に変える。  
  
■ 実行してみる  
  
コマンドプロンプトを立ち上げて  
（スタートメニュー → Windows システム ツール → コマンド プロンプト）、  
  
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
