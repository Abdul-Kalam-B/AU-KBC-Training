from flask import Flask 

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>ABDUL KALAM B</h1> <p>Welcome to Flask</p>'
@app.route('/about')
def about():
    return '<h1>This is about page hello 333</h1>'

@app.route('/users/<name>')
def users(name):
    return  '<h1>Welcome {}</h1>'.format(name.upper())

if __name__ == '__main__':
    app.run(debug=True)
