import json
import os


search_path = [
        os.path.dirname(__file__),
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..'))
        ]


def get_data_in_paths(dfile, paths):
    """
    return the first data file in the path list
    :param dfile:
    :param paths:
    :return:
    """
    for pth in paths:
        for f in os.listdir(pth):
            if f == dfile:
                return os.path.abspath(os.path.join(pth, dfile))


def get_algo4data(algo='', data=''):
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
    global search_path
    algo4dataFile = get_data_in_paths("algo4data.json", search_path)
    with open(algo4dataFile) as algo4data:
        algo4dataDic = json.load(algo4data)
        if algo in algo4dataDic.keys():
            dic = algo4dataDic[algo]
            data = data.lower()
            if data in dic["dataSets"]:
                return {'decision': True}
            else:
                for pat in dic["dataSetPatterns"]:
                    if pat in data:
                        return {'decision': True}
                if data in dic["badDataSets"]:
                    return {'decision': False}
                for pat in dic["badDataSetPatterns"]:
                    if pat in data:
                        return {'decision': False}
            return dic
        else:
            algos = list(algo4dataDic.keys())
            return {'decision': 'unknown algorithm', 'all_algorithms': algos}


def get_all_algorithms_of(data):
    """
    return json {'algos': <a list of algorithms which can be applied for dataset>}
    :param data:
    :return: json
    """
    global search_path
    algo4dataFile = get_data_in_paths("algo4data.json", search_path)
    rlt = []
    with open(algo4dataFile) as algo4data:
        algo4dataDic = json.load(algo4data)
        for algo in algo4dataDic.keys():
            dic = algo4dataDic[algo]
            data = data.lower()
            if data in dic["dataSets"]+ dic["dataSetPatterns"]:
                rlt.append(algo)
    return {'algos': rlt}



def get_algoIO(algo):
    """
    given an algorithm name, return the detailed input/output of this algorithm
    :param algo:
    :return: json, if algo not found, return {'decision': 'unknown algorithm'}
    """
    algoIOFile = get_data_in_paths('algoIO.json', search_path)
    with open(algoIOFile) as algoIO:
        algoIODic = json.load(algoIO)
        if algo in algoIODic.keys():
            return algoIODic[algo]
        else:
            return {'decision': 'unknown algorithm'}
