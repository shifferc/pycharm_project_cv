from flask import Flask, render_template, redirect, url_for
from flask import request
from flask import session
app = Flask(__name__)
app.secret_key='123'

@app.route('/')
def hello_world():
    return render_template('cv.html')

@app.route('/contactL')
def contactL():
    return render_template('contactList.html')

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

@app.route('/assignment8')
def ass():
    hobbies = ['Dancing', 'Netflix', 'Sport']
    return render_template('ass8.html', hobbies=hobbies, language='Paython', lang=False, framework='flask' , name="user")

if __name__ == '__main__':
    app.run(DEBUG=True)
