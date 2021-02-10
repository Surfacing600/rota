from flask import Flask, render_template, g, request, session, redirect, url_for
from database import get_db
from datetime import date, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = b'a~\x95EJ\x08\x8b\x97\xbc\xbb\x05\x1a\\b\xf5\xe1\xf5X\x9ei\xdd\x14u\xf5'

@app.teardown_appcontext

def close_db(error):#check if there is active database and if there is it will close it
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/', methods=['GET', 'POST'])
def rota():

    db = get_db()#initialise the database
    cursor1 = db.execute('select * from tenant1')
    name1 = cursor1.fetchall()
    cursor2 = db.execute('select * from tenant2')
    name2 = cursor2.fetchall()
    cursor3 = db.execute('select * from tenant3')
    name3 = cursor3.fetchall()
    cursor4 = db.execute('select * from tenant4')
    name4 = cursor4.fetchall()
    cursor5 = db.execute('select * from rubbish_removal')
    rubbish = cursor5.fetchall()
    

    date1 = date.today()+ timedelta(days=11)
    date2 = date.today()+ timedelta(days=12)

    
    return render_template('update.html', name1=name1, name2=name2, name3=name3, name4=name4, date1=date1, date2=date2, rubbish=rubbish)

@app.route('/update', methods=['GET', 'POST'])
def update():

    db = get_db()#initialise the database
    cursor1 = db.execute('select * from tenant1')
    tenant1 = cursor1.fetchall()
    cursor2 = db.execute('select * from tenant2')
    tenant2 = cursor2.fetchall()
    cursor3 = db.execute('select * from tenant3')
    tenant3 = cursor3.fetchall()
    cursor4 = db.execute('select * from tenant4')
    tenant4 = cursor4.fetchall()
    cursor5 = db.execute('select * from rubbish_removal')
    rubbish = cursor5.fetchall()

    if request.method == 'POST':

        return redirect(url_for('/'))
    
    return render_template('rota.html', tenant1=tenant1, tenant2=tenant2, tenant3=tenant3, tenant4=tenant4, rubbish=rubbish)


@app.route('/update/<id>', methods=['GET', 'POST'])
def update1(id):

    db = get_db()#initialise the database
    if request.method == 'POST':
        try:
            
            db.execute('update tenant1 set tenant_name1 = ? where id = ?', [request.form['tenant_1'], id])
            db.commit()
            return redirect(url_for('update'))
        except:

            db.execute('update tenant2 set tenant_name2 = ? where id = ?', [request.form['tenant_2'], id])
            db.commit()
            return redirect(url_for('update'))
    return render_template('update.html')

@app.route('/update2/<id>', methods=['GET', 'POST'])
def update2(id):

    db = get_db()#initialise the database
    if request.method == 'POST':
        try:
            
 
            db.execute('update tenant3 set tenant_name3 = ? where id = ?', [request.form['tenant_3'], id])
            db.commit()
            return redirect(url_for('update'))
        except:

            
            db.execute('update tenant4 set tenant_name4 = ? where id = ?', [request.form['tenant_4'], id])
            db.commit()
            return redirect(url_for('update'))
    return render_template('/update2/<id>')

@app.route('/update3/<id>', methods=['GET', 'POST'])
def update3(id):

    db = get_db()#initialise the database
    if request.method == 'POST':
            

            name5 = request.form['rubbish']
            db.execute('update rubbish_removal set tenant_rubbish = ? where id = ?', [name5, id])
            db.commit()
            return redirect(url_for('update'))
    return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True)