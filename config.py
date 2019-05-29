# ----------------------
# Imports & configs
# ----------------------

import pyrebase

config = {
    "apiKey": "AIzaSyBCaBJIKkBZc0Q_Seq4D_PaqIIxuTDIG8M",
    "authDomain": "siftery-test.firebaseapp.com",
    "databaseURL": "https://siftery-test.firebaseio.com",
    "projectId": "siftery-test",
    "storageBucket": "siftery-test.appspot.com",
    "messagingSenderId": "430977697255",
    "appId": "1:430977697255:web:4669125f8bf534b7"
}

# ----------------------
# Globals
# ----------------------

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db   = firebase.database()
