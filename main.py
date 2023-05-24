from flask import Flask,request,render_template
from flask import Response
import os
from flask_cors import CORS,cross_origin
from Prediction_validatoion import Pred
from trainmodel import training
from predictfrommodel import predictfrom_model
from Training_validation import Training_validation
import requests
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)
CORS(app)


response = requests.post('http://localhost:5000/', headers={'Content-Type': 'application/json'})
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
@cross_origin()
def predict_route():
    try:
       if request.json is not None:
           path=request.json['filepath']
           prediction_validation=Pred(path)
           prediction_validation.predic()
           predic_model=predictfrom_model(path)
           predic_model.predict()
           return Response('Prediction file created at Prediction_Output_File',headers={'Content-Type': 'application/json'})
       elif request.form is not None:
            path = request.form['filepath']
            prediction_validation = Pred(path)
            prediction_validation.predic()
            predic_model = predictfrom_model(path)
            predic_model.predict()
            return Response('Prediction file created at Prediction_Output_File',headers={'Content-Type': 'application/json'})
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)


@app.route("/train", methods=['POST'])
@cross_origin()
def trainroute():
    try:
        if request.json['folderpath'] is not None:
            path=request.json['folderpath']
            trainobj=Training_validation(path)
            trainobj.validation()
            train_model=training()
            train_model.train()

    except ValueError:

        return Response("Error Occurred! %s" % ValueError,headers={'Content-Type': 'application/json'})

    except KeyError:

        return Response("Error Occurred! %s" % KeyError,headers={'Content-Type': 'application/json'})

    except Exception as e:

        return Response("Error Occurred! %s" % e,headers={'Content-Type': 'application/json'})
    return Response("Training successfull!!",headers={'Content-Type': 'application/json'})





port = int(os.getenv("PORT",5000))
if __name__ == "__main__":
    app.run(port=port,debug=True,host="0.0.0.0")





