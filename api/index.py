from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World", 200

@app.route('/image',methods=['POST'])
def process_image():
    try:
        data = request.json
        crop = data["type"]
        name = data["name"]

        input_image = preprocess_base64_image(data["filebase64"][23:])
      
        return {"status":"true", "name":name}
    except error:
        return {"status:":"false","error":error}

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404