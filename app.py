# ----------------------
# Imports & requirements
# ----------------------

from flask import Flask, request, render_template, session, redirect, url_for
from config import firebase, auth, db
from config_secret import ConfigSecret
from form import SignupForm, LoginForm

application = Flask(__name__)
application.config.from_object(ConfigSecret)

# ----------------------
# Handy methods
# ----------------------

# Utility
def logged_in():
    if 'user' in session:
        return True
    else:
        return False

# Log in an existing user
def login(email, password):
    if not logged_in():
        try:
            user = auth.sign_in_with_email_and_password(email, password);
            session['user'] = user['idToken']
            return True
        except:
            return False

# Sign up a new user
def handle_new_user(interests, email, password):
    if not logged_in():
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user['idToken']
            interests_array = interests.split(",")
            extra_data = {
                "interests": interests_array
            }
            db.child("users").push(extra_data, user['idToken'])
            return True
        except Exception as e:
            print(e)
            return False
    return False

# ----------------------
# Route handling
# ----------------------

@application.route('/')
def handle_entry():
  if logged_in():
      return redirect(url_for('handle_listing'))
  else:
      return redirect(url_for('handle_signup'))

# Sign up a new user
@application.route('/signup', methods=['GET', 'POST'])
def handle_signup():
  if logged_in():
      return redirect(url_for('handle_listing'))
  else:
      signup_form = SignupForm()
      if signup_form.validate_on_submit():
          success = handle_new_user(signup_form.interests.data, signup_form.email.data, signup_form.password.data)
          if success:
              return redirect(url_for('handle_listing'))
          else:
              return render_template('signup.html', title = 'Sign up', form=signup_form)
      return render_template('signup.html', title = 'Sign up', form=signup_form)

# Log in an existing user
@application.route('/login', methods=['GET', 'POST'])
def handle_login():
  if logged_in():
      return redirect(url_for('handle_listing'))
  else:
      login_form = LoginForm()
      if login_form.validate_on_submit():
          success = login(login_form.email.data, login_form.password.data)
          if success:
              return redirect(url_for('handle_listing'))
          else:
              return render_template('login.html', title = 'Login', form = login_form)
      return render_template('login.html', title = 'Login', form=login_form)

# Listing of products
@application.route('/list')
def handle_listing():
    return "Hello list"

@application.route('/signout')
def signout():
    session.clear()
    return redirect('/')

# ----------------------
# Running
# ----------------------

if __name__ == "__main__":
    application.run(port=5000)
