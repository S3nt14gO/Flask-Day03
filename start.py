from flask import Flask, render_template , url_for
from Pack import app

# app = Flask(__name__)


# @app.route('/')
# def homepage():
#     Navs={
#         '/':'homepage',
#         'about':'about',
#     }
#     return render_template('homepage.html',Navs = Navs)
#
# @app.route('/about')
# def about():
#     Navs = {
#         'homepage': 'Home Page',
#         'about': 'about Page',
#
#     }
#     return render_template('aboutpage.html',Navs = Navs)
#
# Navs = {
#         '/': 'homepage',
#         'about': 'about',
#     }
# for nav,value in Navs.items():
#     print(nav,value)