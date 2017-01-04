# -*- coding: utf-8 -*-

from .context import preprocessing_dm

import json
import unittest


class DataPreprocessingForOutlierDetectionLOF(unittest.TestCase):
    """Basic test cases."""

    @unittest.skip("testing skipping")
    def test_create_csv_for_LOF(self):
        input_cols = ["observation", "amount", "economicClass", "adminClass", "year", "budgetPhase"]
        input_dict_cols2aggr = {"observation": "MIN", "amount": "SUM"}
        input_datasets = ["<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012>",
                          "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2013>",
                          "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2014>"]
        sparql_helper_ce = preprocessing_dm.SparqlCEHelper()
        txt = sparql_helper_ce.create_csv_as_text(input_datasets, input_cols, input_dict_cols2aggr, limit=100)
        assert len(txt) > 0
        assert type(txt) == str

    @unittest.skip("testing skipping")
    def test_list_dataset_name(self):
        datasetNames = preprocessing_dm.list_dataset_name()
        print('totally ', len(datasetNames), ' data names')
        assert len(datasetNames) > 212


if __name__ == '__main__':
    unittest.main()