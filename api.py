from flask import Flask,request,json,render_template,jsonify,make_response
from src.main import kaiseki
from flask_cors import CORS
import ssl


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
  return {"key":"hello world"}

@app.route("/api",methods=["POST"])
def kanjou():
  output=''
  if request.method == 'POST':
    req = request.json
    text = req["text"]
    # print(text)
    output = kaiseki(text)  
  else:
    output = "a"
  print(jsonify(output))
  return jsonify(out=output)

@app.route("/example")
def example():
  return("こんにちは！")

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()