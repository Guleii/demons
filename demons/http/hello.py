from flask import Flask, request, make_response, jsonify, redirect, url_for, session, abort
import os
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')  # 获取参数查询参数name的值
    if name is None:
        name = request.cookies.get('name', 'Human')  # 从Cookie获取name值
        response = '<h1>Hello, %s</h1>' % name
        # 根据用户不同状态返回不同内容
        if 'logged_in' in session:
            response += '[Authenticated]'
        else:
            response += '[Not Authenticated]'

        return response


# @app.route('/foo')
# def foo():
#     data = {
#         'name': 'Guleii',
#         'gender': 'male'
#     }
#     response = make_response(json.dumps(data))
#     response.mimetype = 'application/json'
#     return response
# def foo():
#     return jsonify(name='Guleii', gender='male')
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/login')
def login():
    session['logged_in'] = True  # 写入session
    return redirect(url_for('hello'))


@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page.'


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">Do Something and redirect</a>' % url_for('do_something', next=request.full_path)


@app.route('/bar')
def bar():
    return '<h1>Bar page</h1><a href="%s">Do Something</a>' % url_for('do_something')


@app.route('/do_something_and_redirect')
@app.route('/do_something')
def do_something():
    # do something
    # return redirect(url_for('hello'))
    # return redirect(request.referrer)
    # return redirect(request.args.get('next', url_for('hello')))
    return redirect_back()


def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if target:
            return redirect(target)
    return redirect(url_for(default, **kwargs))


if __name__ == '__main__':
    app.run(debug=True)
