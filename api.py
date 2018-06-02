from flask import Flask,request,json,render_template
from src.main import kaiseki

app = Flask(__name__)

@app.route("/")
def hello():
  return {"key":"hello world"}

@app.route("/api",methods=["POST"])
def kanjou():
  if request.method == 'POST':
    name = request.form['name']
  else:
    name = "no name."
  return kaiseki(name)

@app.route("/example")
def example():
  return("こんにちは！")

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()