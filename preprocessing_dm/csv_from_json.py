
import pandas as pd
import os
from .util import down_content, id_generator
import json
import ast

"""
 year , adminClass , economicClass , budgetPhase , sum ,
nom,nom,nom,nom,target,
 2013 , 25 , 6061 , executed , 0.0 ,
"""


def construct_input_csv(url, csvFile='Input.csv'):
    jsonContent, result_type = down_content(url)
    attributes = []
    dataLst = []
    df = []
    csvFileName = csvFile.split(".")[0]+"_"+id_generator()+".csv"

    if result_type == 'json':
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

        #this code is only for test, comment out when deploy
        '''
        Flag = False
        for att in attributes:
            if("fiscalPeriod" in att):
                Flag = True
                break
        if(Flag==False):
            dataLst = test_data_with_year(dataLst)
            attributes.insert(0, 'year')
            record["year"] = 2017


                print("test~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if ('year' not in attributes):
            dataLst = test_data_with_year(dataLst)
            attributes.insert(0,'year')
            record["year"] = 2017
        '''
        # this code is only for test,comment out when deploy

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
                val=record.get(att, 'NULL')
                if(type(val) is str):
                    if(',' in val):
                        val=val.replace(","," ")
                vLst.append(val)
            df.append(vLst)

        csvDf = pd.DataFrame(df)
        csvDf.to_csv(csvFileName, index=False, header=False)

        return os.path.abspath(csvFileName)

    if result_type == 'sparql':
        """
        {'results': {'ordered': True, 'distinct': False, 'bindings':
        [{'s': {'type': 'uri', 'value': 'http://data.openbudgets.eu/resource/dataset/aragon-2006-expenditure/observation/10'}},
        {'s': {'type': 'uri', 'value': 'http://data.openbudgets.eu/resource/dataset/aragon-2006-expenditure/observation/100'}}
        ]}}
        """
        records = jsonContent.get('results', {}).get('bindings', [])
        attributes = list(records[0].keys())
        df.append(attributes)

        lst = ['nom'] * (len(attributes) - 1)
        lst.append('target')
        df.append(lst)

        for record in records:
            vLst = []
            for att in attributes:
                vLst.append(record.get(att, {'value':'NULL'}).get('value', 'NULL'))
            df.append(vLst)
        csvDf = pd.DataFrame(df)
        csvDf.to_csv(csvFileName, index=False, header=False)

        return os.path.abspath(csvFileName)


def construct_uep_input_csv(url, csvFile='Input.csv'):
    jsonContent, result_type = down_content(url)
    attributes = []
    dataLst = []
    df = []
    csvFileName = csvFile.split(".")[0]+"_"+id_generator()+".csv"

    if result_type == 'json':
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

        # this code is only for test, comment out when deploy
        '''
        Flag = False
        for att in attributes:
            if("fiscalPeriod" in att):
                Flag = True
                break
        if(Flag==False):
            dataLst = test_data_with_year(dataLst)
            attributes.insert(0, 'year')
            record["year"] = 2017


                print("test~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if ('year' not in attributes):
            dataLst = test_data_with_year(dataLst)
            attributes.insert(0,'year')
            record["year"] = 2017
        '''
        # this code is only for test,comment out when deploy

        amountKey = ""
        for key in record.keys():
            if key not in attributes and not key.startswith('_'):
                amountKey = key
        if amountKey != "":
            attributes.append(amountKey)

        df.append(attributes)


        for record in dataLst:
            vLst = []
            for att in attributes:
                vLst.append(record.get(att, 'NULL'))
            df.append(vLst)

        csvDf = pd.DataFrame(df)
        csvDf.to_csv(csvFileName, index=False, header=False)

        return os.path.abspath(csvFileName)

    if result_type == 'sparql':
        """
        {'results': {'ordered': True, 'distinct': False, 'bindings':
        [{'s': {'type': 'uri', 'value': 'http://data.openbudgets.eu/resource/dataset/aragon-2006-expenditure/observation/10'}},
        {'s': {'type': 'uri', 'value': 'http://data.openbudgets.eu/resource/dataset/aragon-2006-expenditure/observation/100'}}
        ]}}
        """
        records = jsonContent.get('results', {}).get('bindings', [])
        attributes = list(records[0].keys())
        df.append(attributes)


        for record in records:
            vLst = []
            for att in attributes:
                vLst.append(record.get(att, {'value':'NULL'}).get('value', 'NULL'))
            df.append(vLst)
        csvDf = pd.DataFrame(df)
        csvDf.to_csv(csvFileName, index=False, header=False)

        return os.path.abspath(csvFileName)

def test_data_with_year(input):
    import random
    for row in input:
        year = random.randint(2014, 2017)
        row["year"] = year
    return input

def cached_file(filename):
    json_url = os.path.join(os.getenv("CACHE_FILE_PATH"), filename)

    data = json.load(open(json_url))
    json_data = json.dumps(data)


    print(data)
    return json_data