from flask import Flask, jsonify, request
import math
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
  """
  Returns the string "Hello, world" to the caller
  """
  return "Hello, world"

@app.route("/name", methods=["GET"])
def getName():
  """
  Returns the data dictionary below to the caller as JSON
  """
  data = {
    "name": "Cole"
  }
  return jsonify(data) # respond to the API caller with a JSON representation of data

@app.route("/name/<name>", methods=["GET"])
def getCustomName(name):
  """
  Returns the data dictionary below to the caller as JSON
  """
  # data = {
  #   "name": "Cole"
  # }
  data = {
    "message": "Hello there, {0}".format(name)
  }
  return jsonify(data) # respond to the API caller with a JSON representation of data

@app.route("/distance", methods=["POST"])
def calcDistance():
  """
  Returns the data dictionary below to the caller as JSON
  """
  r = request.get_json() # parses the POST request body as JSON
  # print(r)
  distance = math.hypot(r["b"][0] - r["a"][0], r["b"][1] - r["a"][1])
  data = {
    "distance": distance,
    "a": r["a"],
    "b": r["b"]
  }
  return jsonify(data) # respond to the API caller with a JSON representation of data

# if __name__ == "__main__":
#     app.run(host="127.0.0.1")
