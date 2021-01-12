from flask import Flask, render_template, redirect, url_for, jsonify
from flask import request
from flask import session
import mysql.connector


app = Flask(__name__)
app.secret_key='123'

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='mydb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # changes in db= commit
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # take all data that sumnu. list of uesrs
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
@app.route('/')
def hello_world():
    return render_template('cv.html')

@app.route('/contactL')
def contactL():
    return render_template('contactList.html')

@app.route('/assignment11/users', methods=['get'])
def ass11():
    query = "SELECT * FROM users "
    query_result = interact_db(query, query_type='fetch')
    return jsonify(users=query_result)

    return jsonify(userss)

@app.route('/assignment11/users/selected/id/', defaults={'id':None})
@app.route('/assignment11/users/selected/id/<int:id>')

def get_user(id=None):
    if id:
        query = "SELECT * FROM users WHERE id='%s'" % id
        query_result = interact_db(query, query_type='fetch')
        return jsonify( users=query_result)
    else:
        return jsonify({'sucsess':False})

@app.route('/assignment9', methods=['GET','POST'])
def ass9():
    first_name = request.args.get('first_name')

    users={'chen':['shiffer','0504776625'],'linoy':['lutati','0523443325'],
           'liran':['bass','0544444325'],'gal':['shapira','05587663823']}


    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        session['logged_in'] = True


    return render_template('assignment9.html', request_method=request.method,
                           users=users,first_name=first_name)

@app.route('/assignment10', methods=['POST','GET'])
def ass10():
    query = "SELECT * FROM users"
    query_result=interact_db(query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)

@app.route('/assignment8')
def ass():
    hobbies = ['Dancing', 'Netflix', 'Sport']
    return render_template('ass8.html', hobbies=hobbies, language='Paython', lang=False, framework='flask' , name="user")

@app.route('/delete_user', methods=['GET','POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        query ="DELETE FROM users WHERE id='%s';" % user_id
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return 'deleteddd'

@app.route('/update_user', methods=['GET','POST'])
def update_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        user_id = request.form['user_id']
        query ="UPDATE users set first_name='%s',last_name='%s', phone_number='%s'  WHERE id='%s'  " % (first_name,last_name,phone,user_id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return 'updatedddd'

@app.route('/insert_user', methods=['GET','POST'])
def insert_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        query = " INSERT INTO users(first_name, last_name, phone_number) VALUES ('%s','%s','%s')" % (
        first_name, last_name, phone)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return 'inserted'





if __name__ == '__main__':
    app.run(DEBUG=True)
