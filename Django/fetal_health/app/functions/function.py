import joblib
#import uuid

#unique_filename = str(uuid.uuid4())
def handle_uploaded_file(f,fname):  
    with open(f'app/upload/{fname}.txt', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def rfPrediction(data):
    model=joblib.load('app/ml_models/ml_rf_fetal_health_model.joblib')
    try:
        pred=model.predict(data)
        val = ""
        if pred[0]==1.0:
            val = 'Normal'
        elif pred[0]==2.0:
            val='Suspect'
        else:
            val='Pathological'
        return val
    except:
        return 'Error in Readings'



    