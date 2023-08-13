from flask import Flask, render_template, request, jsonify
from pytz import timezone
from datetime import datetime


app = Flask(__name__)

#app.route("*"), * is http route

@app.route("/")
def hello():
    #To render a web page using render_template(), 
    #the corresponding HTML must be stored in the "/templates" directory
    return render_template("index.html")
#Test
@app.route("/get_json", methods=['GET'])
def get_json():
    data = {"name" : "TEST", "context" : 1234}
    return jsonify(data)

@app.route("/sensor_data")
def sensor_data():
    sensor_data = "a"

#Test
@app.route("/page/now")
def page_now():
    KST = timezone('Asia/Seoul')
    now = datetime.now()
    now = now.astimezone(KST)
    return render_template("page_test.html", now = now)


if __name__ == '__main__':
    app.run(debug=False)
