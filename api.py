from flask import Flask,request,json,render_template,jsonify,make_response
from src.main import kaiseki
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
  return {"key":"hello world"}

@app.route("/api",methods=["POST"])
def kanjou():
  if request.method == 'POST':
    name = request
    print(name)
  else:
    name = "no name."
  return("こんにちは！")

@app.route("/example")
def example():
  return("こんにちは！")

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()