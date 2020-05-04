from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
import table as t

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    data = t.return_all_users_data()
    return render_template(
        'dashboard.html'
    )

@app.route('/accounts', methods=["GET", "POST"])
def accounts():
    data = t.return_all_users_data()
    return render_template(
        'accounts.html',
        data=data
    )

@app.route('/currencies', methods=["GET", "POST"])
def currencies():
    data = t.return_all_users_data()
    return render_template(
        'currencies.html'
    )

@app.route("/accounts/<user_id>", methods=["GET", "POST"])
def user(user_id):
    data = t.return_user_data(user_id)
    return render_template(
        'user.html',
        data=data
    )

if __name__ == '__main__':
    app.run(debug=True)
