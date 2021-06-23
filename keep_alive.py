from flask import Flask, render_template
from threading import Thread
import os.path
app = Flask(  # Create a flask app
	__name__,
	template_folder='',  # Name of html file folder
	static_folder=''  # Name of directory for static files
)

def plural(number):
  if int(number) == 1:
    return ""
  else:
    return "s"

#idk what this is i just copy pasted it and it worked
def root_dir():  # pragma: no cover
  return os.path.abspath(os.path.dirname(__file__))
def get_file(filename):  # pragma: no cover
  try:
    src = os.path.join(root_dir(), filename)
    # Figure out how flask returns static files
    # Tried:
    # - render_template
    # - send_file
    # This should not be so non-obvious
    return open(src).read()
  except IOError as exc:
    return str(exc)

@app.route('/')
def home():
	return "Yo mama."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()