from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos= [
    {'sno': 1,"title": "simple task","desc": "this is a simple task for todo list","status": "pending"}
]


@app.route('/')
def home():
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)