# -*- coding: utf-8 -*-

from .context import preprocessing_dm

import json
import unittest


class CheckDataSets(unittest.TestCase):
    """Basic test cases."""
    def test_check_dataset_use_slice(self):
        input_dataset1 = "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012>"
        input_dataset2 = "<http://data.openbudgets.eu/resource/dataset/aragon-2006-expenditure>"
        ref = True
        result = preprocessing_dm.check_dataset_use_slice(input_dataset1)
        print(result)
        assert ref == result
        ref = False
        result = preprocessing_dm.check_dataset_use_slice(input_dataset2)
        assert ref == result

    def test_get_datasets_use_slice(self):
        input_datasets = ["<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012>",
                          "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2013>",
                          "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2014>",
                          "<http://data.openbudgets.eu/resource/dataset/aragon-2006-expenditure>"]
        ref = ['<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012>',
               '<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2013>',
               '<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2014>']
        result = preprocessing_dm.get_datasets_use_slice(input_datasets)
        assert result == ref


if __name__ == '__main__':
    unittest.main()