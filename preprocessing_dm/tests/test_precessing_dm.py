# -*- coding: utf-8 -*-

from .context import preprocessing_dm

import json
import unittest
import random


class DataPreprocessingForOutlierDetectionLOF(unittest.TestCase):
    """Basic test cases."""

    @unittest.skip("testing skipping")
    def test_create_csv_for_LOF(self):
        input_cols = ["observation", "amount", "economicClass", "adminClass", "year", "budgetPhase"]
        input_dict_cols2aggr = {"observation": "MIN", "amount": "SUM"}
        input_datasets = ["<http://data.openbudgets.eu/resource/dataset/budget-karpenisi-revenue-2015>",
            "<http://data.openbudgets.eu/resource/dataset/budget-karpenisi-expenditure-2016>",
            "<http://data.openbudgets.eu/resource/dataset/budget-karpenisi-revenue-2014>" ]
#            "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012>",
#                          "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2013>",
#                          "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2014>"
            # ]
        sparql_helper_ce = preprocessing_dm.SparqlCEHelper()
        txt = sparql_helper_ce.create_csv_as_text(input_datasets, input_cols, input_dict_cols2aggr, limit=100)
        assert len(txt) > 0
        assert type(txt) == str

    @unittest.skip("testing skipping")
    def test_list_dataset_name(self):
        datasetNames = preprocessing_dm.list_dataset_name()
        print('totally ', len(datasetNames), ' data names')
        assert len(datasetNames) > 212

    @unittest.skip("testing skipping")
    def test_batch_same_city_create_csv_for_LOF(self):
        allDataSets = preprocessing_dm.get_all_names_of_named_graph('', '', use_cache=False)
        keywords = set()
        gnameLst = []
        for dname in allDataSets:
            lst = dname.split('-')
            if len(lst) > 1:
                dnameEnd = lst[-1]
                if dname.startswith('http://data.openbudgets.eu/resource/dataset') and 'codelist' not in dname \
                        and "1900" < dnameEnd < "3000":
                    gnameLst.append(dname)
                    keywords = keywords | set([dname.split('/')[-1].split('-')[1]])
        print(keywords)

        count = 0
        while count < 20:
            city = random.choice(list(keywords))
            candidates = [name for name in gnameLst if city in name and city not in ['draft']]
            random.shuffle(candidates)
            N = min(len(candidates), 3)
            sNames = candidates[0:N]

            input_cols = ["observation", "amount", "economicClass", "adminClass", "year", "budgetPhase"]
            input_dict_cols2aggr = {"observation": "MIN", "amount": "SUM"}
            input_datasets = ["<"+name+">" for name in sNames]
            sparql_helper_ce = preprocessing_dm.SparqlCEHelper()
            txt = sparql_helper_ce.create_csv_as_text(input_datasets, input_cols, input_dict_cols2aggr, limit=100)

            print('====', sNames)
            assert len(txt) > 300
            count += 1


if __name__ == '__main__':
    unittest.main()