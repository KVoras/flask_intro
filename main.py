"""
-Flask
-path/query parameters
-GET/POST methods
-forms
-render_template
-extend_template
"""
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST']) #decorator
def hello_world():
    print(request.method)
    print(request.form.get('username'))
    return render_template('form.html')

app.run()


