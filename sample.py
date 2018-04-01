import sys
import os
import sqlite3

import database

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

def main():
    database.create_table(conn, cur)

    database.insert_data(conn, cur)

    database.select_data(cur)

if __name__ == "__main__":
    main()
