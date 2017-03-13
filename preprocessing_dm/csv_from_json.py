
import pandas as pd
import os
from .util import down_json_content, id_generator

"""
 year , adminClass , economicClass , budgetPhase , sum ,
nom,nom,nom,nom,target,
 2013 , 25 , 6061 , executed , 0.0 ,
"""


def construct_input_csv(url, csvFile='Input.csv'):
    jsonContent = down_json_content(url)
    attributes = []
    dataLst = []
    df = []
    csvFileName = csvFile.split(".")[0]+"_"+id_generator()+".csv"

    if 'fields' in jsonContent.keys():
        attributes = jsonContent['fields']
    elif 'attributes' in jsonContent.keys():
        attributes = jsonContent['attributes']

    if 'cells' in jsonContent.keys():
        dataLst = jsonContent['cells']
        record = jsonContent['cells'][0]
    elif 'data' in jsonContent.keys():
        dataLst = jsonContent['data']
        record = jsonContent['data'][0]

    amountKey = ""
    for key in record.keys():
        if key not in attributes and not key.startswith('_'):
            amountKey = key
    if amountKey != "":
        attributes.append(amountKey)

    df.append(attributes)

    lst = ['nom'] * (len(attributes) -1)
    lst.append('target')
    df.append(lst)

    for record in dataLst:
        vLst = []
        for att in attributes:
            vLst.append(record.get(att, 'NULL'))
        df.append(vLst)

    csvDf = pd.DataFrame(df)
    csvDf.to_csv(csvFileName, index=False, header=False)

    return os.path.abspath(csvFileName)