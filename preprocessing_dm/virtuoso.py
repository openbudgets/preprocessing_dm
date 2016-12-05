
import os
import requests
import json
from SPARQLWrapper import SPARQLWrapper, JSON


try:
    SPARQLEndPoint = os.environ['VIRTUOSO_ENDPOINT']
    FILE_OF_GRAPH_NAMES = os.environ['FILE_OF_GRAPH_NAMES']
except Exception:
    SPARQLEndPoint = "http://eis-openbudgets.iais.fraunhofer.de/virtuoso/sparql"
    FILE_OF_GRAPH_NAMES = "GRAPH_NAMES.txt"


sparql = SPARQLWrapper(SPARQLEndPoint)


###
#  query virtuoso
#
def query_virtuoso(sqlStr):
    """
    send SPARQL string sqlStr to virtuoso server, and return result in json format
    :param sqlStr:
    :return:
    """
    sparql.setQuery(sqlStr)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()
#
#  List all names of named-graphs
###


def get_all_names_of_named_graph(db, GraphName, use_cache='True'):
    nlst = []
    names = ""
    if use_cache == 'True':
        nlst=[]
        print('use db cache')
        try:
            for record in db.session.query(GraphName):
                nlst.append(record.gname)
        except:
            print('Error by querying graph names from DB')
        return nlst
    else:
        errors = []
        query_NameOfGraphs = "SELECT Distinct(?g) WHERE { graph ?g {?s ?p ?o .} }"
        sparql.setQuery(query_NameOfGraphs)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        recordId = 0
        for result in results["results"]["bindings"]:
            nm = str(result['g']['value'])
            recordId += 1
            if nm.startswith('http'):
                nlst.append(nm)
                names += nm+"\n"
                try:
                    cur_list = []
                    for record in db.session.query(GraphName):
                        cur_list.append(record.gname)
                    if nm not in cur_list:
                        graphname = GraphName(
                            id= recordId,
                            gname= nm
                        )
                        db.session.add(graphname)
                        db.session.commit()
                    else:
                        print(nm, ' found in da')
                except:
                    errors.append('Unable to add item to GraphNames table')

        with open(FILE_OF_GRAPH_NAMES, 'w') as fh:
            fh.writelines(names)
        return nlst


def get_all_codelists_of_named_graph(db, GraphName, use_cache='True'):
    nlst = get_all_names_of_named_graph(db, GraphName, use_cache = use_cache)
    codelist = []
    for nm in nlst:
        if 'codelist' in nm:
            codelist.append(nm)
    return codelist


def get_all_dataset_of_named_graph(db, GraphName, use_cache='True'):
    nlst = get_all_names_of_named_graph(db, GraphName, use_cache = use_cache)
    datasets = []
    for nm in nlst:
        if 'dataset' in nm:
            datasets.append(nm)
    return datasets


###
#  list content of a named graph
##

def get_dimensions_from_rdfrecord(dataset, record=''):
    """
    get all dimensions *used* in Slice or Observation
    :param dataset:
    :return:
    """
    sqlStr = ""
    if record == 'Slice':
        sqlStr = "PREFIX qb:  <http://purl.org/linked-data/cube#> SELECT ?p FROM {} \
        WHERE {{?s a qb:Slice; ?p ?o .filter(contains(str(?p), 'dimension')).}} group by ?p".format(dataset)
    elif record == 'Observation':
        sqlStr = "PREFIX qb:  <http://purl.org/linked-data/cube#> SELECT ?p FROM {} \
        WHERE {{?s a qb:Observation; ?p ?o .filter(contains(str(?p), 'dimension')).}} group by ?p".format(dataset)
    elif record == '':
        sqlStr = "SELECT ?p FROM {} WHERE {{?s ?p ?o . filter(contains(str(?p), 'dimension'))}}  group by ?p".format(dataset)
    result = query_virtuoso(sqlStr)
    lst = []
    for record in result['results']['bindings']:
        lst.append(record['p']['value'])
    return lst


def get_dimensions_from_dataset(dataset):
    """
    get all dimensions *used* in an RDF dataset
    :param dataset:
    :return: a list of all dimensions used for observations
    """
    return get_dimensions_from_rdfrecord(dataset, record='')


def get_dimensions_of_observation(dataset):
    """
    get all dimensions *used* in observation
    :param dataset:
    :return: a list of all dimensions used for observations
    """
    return get_dimensions_from_rdfrecord(dataset, record='Observation')


def get_dimensions_of_slice(dataset):
    """
    get all dimensions *used* in slice
    :param dataset:
    :return: a list of all dimensions used for observations
    """
    return get_dimensions_from_rdfrecord(dataset, record='Slice')


def get_slice_function(dataset):
    """
    get the function of slice
    :param dataset:
    :return: function
    """
    sqlStr = ""
    sqlStr = "PREFIX qb:  <http://purl.org/linked-data/cube#> SELECT ?o FROM {}\
     WHERE {{?s qb:sliceStructure ?o}}  group by ?o".format(dataset)
    result = query_virtuoso(sqlStr)
    lst = []
    for record in result['results']['bindings']:
        lst.append(record['o']['value'])
    return lst


def get_all_observations_from_sliced_dataset(dataset):
    """
    :param dataset:
    :return:
    """
    sqlStr = "PREFIX qb:  <http://purl.org/linked-data/cube#>\n"
    sqlStr += "PREFIX obeu-measure: <http://data.openbudgets.eu/ontology/dsd/measure/>\n"
    whereClause = ""
    whereSliceFunction = "?s qb:sliceStructure ?sfunc .\n"
    selectClause = "?s ?sfunc ?amount"
    dimensionInSlice = get_dimensions_of_slice(dataset)
    dimensionInObservation = get_dimensions_of_observation(dataset)

    whereSliceDimension = ""
    for i in range(len(dimensionInSlice)):
        column = dimensionInSlice[i].split('/')[-1]
        whereSliceDimension += "?s <{0}> ?{1} . \n".format(dimensionInSlice[i], column)
        selectClause += " ?{0}".format(column)

    obsrevationClause = "?s qb:observation ?observation .\n"
    selectClause += " ?observation"
    whereObservationDimension = ""
    for i in range(len(dimensionInObservation)):
        column = dimensionInObservation[i].split('/')[-1]
        whereObservationDimension += "?observation <{0}> ?{1} . \n".format(dimensionInObservation[i], column)
        selectClause += " ?{0}".format(column)
    whereClause += " ?observation obeu-measure:amount ?amount . \n"
    whereClause += whereSliceFunction + whereSliceDimension + obsrevationClause + whereObservationDimension
    sqlStr += "Select {0}\n From {1}\n WHERE {{ {2} }}".format(selectClause, dataset, whereClause)
    print(sqlStr)
    result = query_virtuoso(sqlStr)
    return result['results']['bindings']


def list_dataset_name():
    endpoint = "http://eis-openbudgets.iais.fraunhofer.de/api/3/cubes/"
    r = requests.get(endpoint)
    if r.status_code == requests.codes.ok:
        dic = json.loads(r.text)
        return [ dataset_name['name'] for dataset_name in dic['data']]
    else:
        return ['not found!']


def check_dataset_use_slice(dataset):
    """
    check whether a dataset uses 'qb:Slice'
    :param dataset:  dataset name
    :return: true if it uses qb:Slice, otherwise, return false
    """
    sqlStr = "PREFIX qb:  <http://purl.org/linked-data/cube#>  ASK FROM {} WHERE {{ ?s a qb:Slice . }} ".format(dataset)
    result = query_virtuoso(sqlStr)
    return result['boolean']
