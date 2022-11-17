from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


#------minimal aplicatin----
""" @app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




#------------Routing------------

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'



#---------variable Routing----------

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'hii this is User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'users id is  {post_id}'


if __name__=='__main__':
    app.run()   """






#----------escape-------

""" from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!" """



""" #-----------url_for url building------

from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__=='__main__':
    app.run()   

 """



@app.route("/")

def home():

    return render_template("home.html")

   
@app.route("/index")

def index():

    return render_template("index.html")


if __name__=='__main__':

    app.run(debug = True)