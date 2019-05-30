from flask import *
import requests
import calendar

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/rental",methods=["GET"])
def rental():
    location = request.args.get('inputlocation') 
    date = request.args.get('inputdate')

    uri = "https://api.sheety.co/311576ae-321a-43e3-9a5b-61b3ac373d85"
    try:
        response = requests.get(uri)
    except requests.ConnectionError:
        return "Connection Error"

    text_response = response.text
    data = json.loads(text_response)

    return render_template("car_details.html",temp_location=location,temp_date=date)

if __name__ == '__main__':
    app.run()