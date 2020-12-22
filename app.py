from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('cv.html')

@app.route('/contactL')
def contactL():
    return render_template('contactList.html')

@app.route('/assignment8')
def ass():
    hobbies = ['Dancing', 'Netflix', 'Sport']
    return render_template('ass8.html', hobbies=hobbies, language='Paython', lang=False, framework='flask' , name="user")

if __name__ == '__main__':
    app.run(DEBUG=True)
