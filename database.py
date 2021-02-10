from flask import g
import sqlite3
import psycopg2
from psycopg2.extras import DictCursor


def connect_db():
    conn = psycopg2.connect('postgres://rtjgqpqkpvwezu:04eadcbdd549c1a51e7d79bba2d695a4a4eddc98f19c708335d20874b08b8db4@ec2-52-205-3-3.compute-1.amazonaws.com:5432/d46prc73pddqj5', cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()
    return conn, sql

def get_db():
    db = connect_db()

    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur

def init_db():
    db = connect_db()

    db[1].execute(open('schema.sql', 'r').read())
    db[1].close()

    db[0].close()

