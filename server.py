from flask import Flask, app, render_template, request, redirect
from flask.wrappers import Request
from user import User
app = Flask (__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def readALL():
    users = User.get_all_users()
    return render_template("read(all).html", all_users = users)

@app.route('/users/new')
def new_user():
    return render_template('create.html')

@app.route('/create', methods =['POST'])
def create_user():
     User.create_user(request.form)
     return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    print(user_id)
    data = {
        'id': user_id
    }

    User.delete_user(data)
    return redirect('/users')

@app.route('/users/<int:id>/userspage')
def selected_user(id):

    data = {
        'id': id
    }

    return render_template('userspage.html', user =  User.get_single_user(data))

@app.route('/users/<int:user_id>/edit')
def edit(user_id):

    data ={
        "id": user_id,
        'first_name' : request.form ['first_name'],
        'last_name' : request.form ['last_name'],
        'email' : request.form ['email'],
    }

    return render_template("edit_user.html", user=User.edit_user(data))


if __name__ == "__main__":
    app.run(debug=True)