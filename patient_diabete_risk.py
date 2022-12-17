print('***** Starting patient_diabete_risk.py  V 000 *****')

import numpy as npy
import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

print('*** Import completed ***')

class Patient(BaseModel):
    highbp: int 
    highchol: int 
    cholcheck: int
    bmi: int
    smoker: int
    stroke: int
    heartdiseaseorattack: int
    physactivity: int
    fruits: int
    veggies: int
    hvyalcoholconsump: int
    anyhealthcare: int
    nodocbccost: int
    genhlth: int
    menthlth: int
    physhlth: int
    diffwalk: int
    sex: int
    age: int
    education: int
    income: int

print('*** Get model ***')
modBnt = bentoml.xgboost.get("patient_diabete_risk:4ngty4d4wcbjynht")
dvt = modBnt.custom_objects['dictVectorizer']

print('*** Run mmodel ***')
modBntRun = modBnt.to_runner()
svc = bentoml.Service("patient_diabete_risk_service", runners=[modBntRun])

@svc.api(input=JSON(), output=JSON())

async def classify(patient):
    print('\n\n*** in classify ***')

    # should be a dict
    print('*** type(patient) :' , type(patient)) 
    # "must be like { "val1" : val1 , ...}"
    print('*** patient :' , patient)

    print('*** parsing patient with pydantc Class')
    try:
        booOK = False
        Patient.parse_obj(patient)
        print('*** parsing patient OK')
        booOK = True
    except Exception as err:
        strErr = str(err).replace('\n' , ' : ')
        print("*** parsing patient NOT OK *** Error: \n" , strErr )
    

    if booOK:
        X_pat = dvt.transform(patient)
        print('*** X:' , X_pat)

        print('*** predict... beg' )
        prd = await modBntRun.predict.async_run( X_pat )
        print('*** predict... end' )

        if prd > 0.5:
            strPrd = 'Diabete probable'
        else:
            strPrd = 'Diabete NOT probable' 
    else:
        # in case of error return -1
        prd = -1
        strPrd = strErr
    
    print('>*** prd = ' , prd , ' - interpret :' , strPrd  )
    return( { "prediction" : prd , "interpret" : strPrd  })