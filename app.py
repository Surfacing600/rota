from flask import Flask, render_template, g, request, session, redirect, url_for
from database import get_db
from datetime import date, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = b'a~\x95EJ\x08\x8b\x97\xbc\xbb\x05\x1a\\b\xf5\xe1\xf5X\x9ei\xdd\x14u\xf5'

@app.teardown_appcontext

def close_db(error):#check if there is active database and if there is it will close it
    
    if hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur.close()
    
    if hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn.close()


@app.route('/', methods=['GET', 'POST'])
def rota():

    db = get_db()#initialise the database
    db.execute('select * from tenant1')
    name1 = db.fetchall()
    db.execute('select * from tenant2')
    name2 = db.fetchall()
    db.execute('select * from tenant3')
    name3 = db.fetchall()
    db.execute('select * from tenant4')
    name4 = db.fetchall()
    db.execute('select * from rubbish_removal')
    rubbish = db.fetchall()
    

    date1 = date.today()+ timedelta(days=11)
    date2 = date.today()+ timedelta(days=12)

    
    return render_template('update.html', name1=name1, name2=name2, name3=name3, name4=name4, date1=date1, date2=date2, rubbish=rubbish)

@app.route('/update', methods=['GET', 'POST'])
def update():

    db = get_db()#initialise the database
    db.execute('select * from tenant1')
    tenant1 = db.fetchall()
    db.execute('select * from tenant2')
    tenant2 = db.fetchall()
    db.execute('select * from tenant3')
    tenant3 = db.fetchall()
    db.execute('select * from tenant4')
    tenant4 = db.fetchall()
    db.execute('select * from rubbish_removal')
    rubbish = db.fetchall()

    if request.method == 'POST':

        return redirect(url_for('/'))
    
    return render_template('rota.html', tenant1=tenant1, tenant2=tenant2, tenant3=tenant3, tenant4=tenant4, rubbish=rubbish)


@app.route('/update/<id>', methods=['GET', 'POST'])
def update1(id):

    db = get_db()#initialise the database
    if request.method == 'POST':
        try:
            db.execute('select id, tenant_name1 from tenant1 where id = %s', (id, ))
            tenant_to_update = db.fetchone()
            name1 = request.form['tenant_1']
            db.execute('update tenant1 set tenant_name1 = %s where id = %s', (name1, id))
            db.commit()
            return redirect(url_for('update'))
        except:

            db.execute('select id, tenant_name2 from tenant2 where id = %s', (id, ))
            tenant_to_update = db.fetchone()
            name2 = request.form['tenant_2']
            db.execute('update tenant2 set tenant_name2 = %s where id = %s', (name2, id))
            db.commit()
            return redirect(url_for('update'))
    return render_template('update.html')

@app.route('/update2/<id>', methods=['GET', 'POST'])
def update2(id):

    db = get_db()#initialise the database
    if request.method == 'POST':
        try:
            db.execute('select id, tenant_name3 from tenant3 where id = %s', (id, ))
            tenant_to_update = db.fetchone()
            name3 = request.form['tenant_3']
            db.execute('update tenant3 set tenant_name3 = %s where id = %s', (name3, id))
            db.commit()
            return redirect(url_for('update'))
        except:

            db.execute('select id, tenant_name4 from tenant4 where id = %s', (id, ))
            tenant_to_update = db.fetchone()
            name4 = request.form['tenant_4']
            db.execute('update tenant4 set tenant_name4 = %s where id = %s', (name4, id))
            db.commit()
            return redirect(url_for('update'))
    return render_template('update.html')

@app.route('/update3/<id>', methods=['GET', 'POST'])
def update3(id):

    db = get_db()#initialise the database
    if request.method == 'POST':
            db.execute('select id, tenant_rubbish from rubbish_removal where id = %s', (id, ))
            tenant_to_update = db.fetchall()
            name5 = request.form['rubbish']
            db.execute('update rubbish_removal set tenant_rubbish = %s where id = %s', (name5, id))
            db.commit()
            return redirect(url_for('update'))
    return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True)