"""
    File name: preprocessing/util.py
    Author: Tiansi Dong, Maik Lukasche
    Date created: 9/14/2016
    Date last modified: 9/14/2016
    Python Version: 3.5
"""
import os
import httplib2
import json
import string
import random
from .virtuoso import query_virtuoso
from .send_request import SparqlCEHelper


def down_file(url=None):
    h = httplib2.Http(".cache")
    resp, content = h.request(url, "GET")
    return content


def is_json(jstr):
    try:
        json.loads(jstr)
        return True
    except ValueError:  # includes JSONDecodeError
        return False


def is_sparql(jstr):
    jstr = jstr.strip().lower()
    if 'select' in jstr and 'where' in jstr:
        return True
    else:
        return False


def do_sparql_query(urlContent, output_format='json'):
    return query_virtuoso(urlContent, output_format=output_format)


def down_content(url=None):
    print('url', url)
    urlContent = down_file(url)
    urlContent = str(urlContent.decode("utf-8"))
    if is_json(urlContent):
        return json.loads(urlContent), 'json'
    elif is_sparql(urlContent):
        jsonStruc = do_sparql_query(urlContent, output_format='json')
        return jsonStruc, 'sparql'


def down_json_content(url=None):
    print('url', url)
    jsonBytes = down_file(url)
    jsonString = jsonBytes.decode("utf-8")
    return json.loads(jsonString)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def ce_from_file_names_query_fuseki_output_csv(filenames, dataPath, debug=False):
    """
    if debug=True, we just use the already exising csv file
    Parameters
    ----------
    filenames
    debug

    Returns
    -------

    """
    if debug:
        if os.path.isdir(dataPath):
            csvFile = os.path.join(dataPath, 'Kilkis_neu.csv')
            print(csvFile)
            return csvFile
        else:
            print('no such path ', dataPath)
            return False
    else:
        fileNamesLst = filenames.split('+')[1:]
        input_cols = ["observation", "amount", "economicClass", "adminClass", "year", "budgetPhase"]
        input_dict_cols2aggr = {"observation": "MIN", "amount": "SUM"}
        input_datasets = ["<http://data.openbudgets.eu/resource/dataset/"+fn+">" for fn in fileNamesLst]

        SparqlHelperCE = SparqlCEHelper()
        csvFile = SparqlHelperCE.create_csv_as_file(input_datasets, input_cols,
                                                    input_dict_cols2aggr, dataPath, limit=10000)

        return csvFile