#!/usr/bin/env python

import sqlite3

def create_table(conn, cur):
    cur.execute('''
CREATE TABLE IF NOT EXISTS
    社員 (
        社員番号       text,
        社員名         text,
        給与          integer,
        部署番号        text
        )
    ''')

    cur.execute('''
CREATE TABLE IF NOT EXISTS
    部署 (
        部署コード       text,
        部署名         text,
        所在地         text
        )
    ''')

    # 過去データ削除処理
    cur.execute(" \
DELETE FROM 社員 \
    ")

    cur.execute(" \
DELETE FROM 部署 \
    ")

def insert_data(conn, cur):
    cur.execute(" \
INSERT INTO 社員 (社員番号, 社員名, 給与, 部署番号) VALUES ( \
    '100010', \
    '沢木翔一', \
    210000, \
    '302' \
)")

    cur.execute(" \
INSERT INTO 社員 (社員番号, 社員名, 給与, 部署番号) VALUES ( \
    '100011', \
    '野田奈央子', \
    330000, \
    '301' \
)")

    cur.execute(" \
INSERT INTO 社員 (社員番号, 社員名, 給与, 部署番号) VALUES ( \
    '100012', \
    '黒沢さおり', \
    270000, \
    '202' \
)")

    cur.execute(" \
INSERT INTO 社員 (社員番号, 社員名, 給与, 部署番号) VALUES ( \
    '100013', \
    '野村雅也', \
    320000, \
    '301' \
)")

    cur.execute(" \
INSERT INTO 社員 (社員番号, 社員名, 給与, 部署番号) VALUES ( \
    '100014', \
    '児玉亮', \
    350000, \
    '101' \
)")

    cur.execute(" \
INSERT INTO 部署 (部署コード, 部署名, 所在地) VALUES ( \
    '101', \
    '人事', \
    '東京' \
)")

    cur.execute(" \
INSERT INTO 部署 (部署コード, 部署名, 所在地) VALUES ( \
    '201', \
    '総務', \
    '東京' \
)")

    cur.execute(" \
INSERT INTO 部署 (部署コード, 部署名, 所在地) VALUES ( \
    '202', \
    '総務', \
    '大阪' \
)")

    cur.execute(" \
INSERT INTO 部署 (部署コード, 部署名, 所在地) VALUES ( \
    '301', \
    '経理', \
    '東京' \
)")

    cur.execute(" \
INSERT INTO 部署 (部署コード, 部署名, 所在地) VALUES ( \
    '302', \
    '経理', \
    '大阪' \
)")

    conn.commit()

def select_data(cur):
    # ここにSELECT文をいろいろ書いて、動作を確認してみよう。
    # ただし、行の最後には「\」を付けてね。

    print('問題4のSELECT結果')
    cur.execute(" \
SELECT 社員番号 FROM 社員 \
WHERE 部署番号 > 300 AND 給与 <= 320000 ; \
")
    print(cur.fetchall())

    print('問題5のSELECT結果')
    cur.execute(" \
SELECT 社員番号, 社員名, 部署番号 FROM 社員 \
WHERE 社員名 LIKE '%沢%' ; \
")
    print(cur.fetchall())

    print('問題6のSELECT結果')
    cur.execute(" \
SELECT 社員名 FROM 社員, 部署 \
WHERE 部署番号 = 部署コード AND 所在地 = '東京' ; \
")
    print(cur.fetchall())

    print('問題7のSELECT結果')
    cur.execute(" \
SELECT 部署番号, 社員番号, 社員名 FROM 社員 \
ORDER BY 部署番号, 社員番号 ; \
")
    print(cur.fetchall())
