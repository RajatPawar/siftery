# ----------------------
# Imports & requirements
# ----------------------

from flask import Flask, request, render_template
from config import firebase, auth, db

application = Flask(__name__)

# ----------------------
# Route handling
# ----------------------

@application.route('/')
def method():
  if firebase:
      return "Hello"
  else:
      return "No"

# ----------------------
# Running
# ----------------------

if __name__ == "__main__":
    application.run(port=5000)
