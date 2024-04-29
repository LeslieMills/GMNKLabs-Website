from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
  return "<p>Welcome to GLabs</p>"


if __name__ == "__main__":
  print("I am here now!")
  app.run(host="0.0.0.0", port=8080, debug=True)
