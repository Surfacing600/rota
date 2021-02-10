from flask import g
import sqlite3


def connect_db(): #connects to the database
    sql = sqlite3.connect('postgres://jspcxodfhzzyhf:390459475d7d8fe4ed4825fa3cb45fc36e035665762122112cee83a90e1d2e9e@ec2-3-222-11-129.compute-1.amazonaws.com:5432/d8gn9j0gp84qm0')
    sql.row_factory = sqlite3.Row #to get dictionaries instead of tuples when you access the rows
    return sql


def get_db():
    if not hasattr(g, 'sqlite3_db'):#checks if global object 'sqlite3_db' is in the database
        g.sqlite_db = connect_db()
    return g.sqlite_db

