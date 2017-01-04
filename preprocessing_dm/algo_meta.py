import json
import os


def get_algo4data(algo='', data='', dataPat=''):
    """
    1) given an algorithm, return description of the algorithm and the list of datasets which the algorithm
       can be applied;
    2) given an algorithm and a dataset, decide whether the algorithm can be applied for this dataset;
    3) given an algorithm and a dataset pattern, decide whether the algorithm can be applied for all datasets
       having this pattern;
    :param algo:
    :param data:
    :param dataPat:
    :return: json in 1), json {'decision': True/False/'unknown'} in case 2) and 3)
    """
    algo4dataFile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'algo4data.json'))
    with open(algo4dataFile) as algo4data:
        algo4dataDic = json.load(algo4data)
        if algo in algo4dataDic.keys():
            dic = algo4dataDic[algo]
            if data in dic["dataSets"] or dataPat in dic["dataSetPatterns"]:
                return {'decision' : True}
            elif data in dic["badDataSets"] or dataPat in dic["badDataSetPatterns"]:
                return {'decision': False}
            else:
                return dic
        else:
            return {'decision': 'unknown algorithm'}


def get_algoIO(algo):
    """
    given an algorithm name, return the detailed input/output of this algorithm
    :param algo:
    :return: json, if algo not found, return {'decision': 'unknown algorithm'}
    """
    algoIOFile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'algoIO.json'))
    with open(algoIOFile) as algoIO:
        algoIODic = json.load(algoIO)
        if algo in algoIODic.keys():
            return algoIODic[algo]
        else:
            return {'decision': 'unknown algorithm'}
