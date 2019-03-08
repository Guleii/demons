from flask import Flask
app = Flask(__name__)


user = {
    'username': 'Guleii',
    'bio': 'A boy who loves movies and music.',
}
movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'The Matrix', 'year': '1997'},
    {'name': 'Perfect Blue', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'}
]


@app.route('/')
@app.route('/hi')
@app.route('/hello')
def index():
    return '<h1>Hello Flask!</h1>'


@app.route('/greet',
           defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


@app.cli.command()
def hello():
    click.echo('Hello, Human!')


if __name__ == '__main__':
    app.run(debug=True)
