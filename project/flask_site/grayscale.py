from flask import Flask, render_template

app = Flask(__name__)


# home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# # about page
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @app.route('/profile1')
# def profile():
#     return render_template('profile1.html')
#
# @app.route('/profile2')
# def profile2():
#     return render_template('profile2.html')
#
# @app.route('/profile3')
# def profile3():
#     return render_template('profile3.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
