from config import *
import json 
from flask import Flask
from flask import request
#location the api functions live 
from  helpers.api import * 


#configs pulled from config.py 
# apiKEY


app = Flask(__name__)


def generateResponse(Status, Data):
    responseString = {'status':f"{Status}", 'data': f"{Data}"}
    return json.dumps(responseString)


@app.route("/test")
def test():
    val = testAPI()
    return val

# test function 
@app.route('/api/ping', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        return generateResponse("Succsess", "GET- PONG")
    elif request.method == 'POST':
        data = request.get_json()
        val = data["somekey"]
        return generateResponse("Succsess", f"POST somekey with val {val}")
    else:
        return generateResponse("FAILURE", "Something went wrong")



# run the application 
if __name__ == "__main__": 
    app.run(debug=True)


