from flask import Flask,redirect, session, url_for, request, render_template
from urllib.parse import urlparse, urljoin
from jinja2.utils import generate_lorem_ipsum
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)  # 生产两端随机文本
    return '''
           <h1>A very long post</h1>
           <div class="body">%s</div>
           <button id="load">Load More</button>
           <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
           <script type="text/javascript">
           $function() {
                $('#load').click(function() {
                    $.ajax(
                        {
                            url:'/more', //目标URL
                            type:'get',  //请求方法
                            success:function(data){
                                //返回2XX响应后出发的回调函数
                                $('.body').append(data); //将返回的响应插入到页面中
                            }
                        }
                    )
                }
            )
        }
           </script> 
    ''' % post_body


@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)


@app.route('/students')
def bobby_table():
    password = request.args.get('password')
    cur = db.execute("SELECT * FROM students WHERE password='%s';" % password)
    results = cur.fetchall()
    return results


@app.route('/watchlist')
def watchlist():
    render_template('watchlist.html', user=user, movies=movies)



if __name__ == '__main__':
    app.run(debug=True)
