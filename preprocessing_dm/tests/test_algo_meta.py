# -*- coding: utf-8 -*-

from .context import preprocessing_dm

import json
import unittest


class TestAlgoMeta(unittest.TestCase):
    """Basic test cases."""
    def test_get_algo4data(self):
        test_lst = [('TimeSeries', 'dataset_1',
                     {'dataSets': ['?any', 'budget-katerini-revenue-2016__235c7'], 'decision': True,
                      'dataSetPatterns': ['katerini-revenue', 'esif'], 'badDataSets': ['baddataset_x', 'baddataset_y'],
                      'badDataSetPatterns': ['bad'], 'description': 'bla bla bla about TimeSeries',
                      'name': 'TimeSeries'}),
                    ('TimeSeries', 'baddataset_x',
                     {'description': 'bla bla bla about TimeSeries', 'decision': True, 'badDataSetPatterns': ['bad'],
                      'dataSets': ['?any', 'budget-katerini-revenue-2016__235c7'],
                      'dataSetPatterns': ['katerini-revenue', 'esif'], 'name': 'TimeSeries',
                      'badDataSets': ['baddataset_x', 'baddataset_y']}),
                    ('TimeSeries', '',
                     {'description': 'bla bla bla about TimeSeries', 'dataSetPatterns': ['katerini-revenue', 'esif'],
                      'name': 'TimeSeries', 'badDataSets': ['baddataset_x', 'baddataset_y'], 'decision': True,
                      'badDataSetPatterns': ['bad'], 'dataSets': ['?any', 'budget-katerini-revenue-2016__235c7']}),
                    ('TimeSeries', 'dataset_1',
                     {'description': 'bla bla bla about TimeSeries', 'decision': True, 'badDataSetPatterns': ['bad'],
                      'dataSetPatterns': ['katerini-revenue', 'esif'], 'badDataSets': ['baddataset_x', 'baddataset_y'],
                      'dataSets': ['?any', 'budget-katerini-revenue-2016__235c7'], 'name': 'TimeSeries'}),
                    # ('dummyFunction', 'dataset_1',
                    # {'all_algorithms': ['outlierDetection_LOF', 'TimeSeries', 'sampleFunction'],
                    #  'decision': 'unknown algorithm'}),
                    ]
        for pair in test_lst:
            print(pair[0], pair[1], '*')
            print(preprocessing_dm.get_algo4data(algo=pair[0], data=pair[1]))
            assert pair[2] == preprocessing_dm.get_algo4data(algo=pair[0], data=pair[1])

    def test_get_algoIO(self):
        test_lst = [('TimeSeries', {
                                        "algorithm": {
                                            "title": "Time Series",
                                            "name": "time_series",
                                            "instance": "timeSeriesAlgorithm",
                                            "method": "POST",
                                            "endpoint": [
                                                "DAMUrl",
                                                "/library/TimeSeries.OBeu/R/open_spending.ts"
                                                ],
                                            "prompt": "Select an aggregate, a time-related drilldown " \
                                                      "and the prediction steps parameter" \
                                                      " from the left and click on the execute button on top right."
                                             },

                                        "input": {
                                            "raw_data": {
                                                "cardinality": "1",
                                                "type": "BABBAGE_AGGREGATE_URI",
                                                "name": "json_data",
                                                "title": "Data coming from an aggregation",
                                                "guess": False,
                                                "required": True
                                                },
                                            "time_dimension": {
                                                "cardinality": "1",
                                                "type": "ATTRIBUTE_REF",
                                                "name": "time",
                                                "title": "Time dimension",
                                                "guess": True,
                                                "required": True
                                                },
                                            "amount_aggregate": {
                                                "cardinality": "1",
                                                "type": "AGGREGATE_REF",
                                                "name": "amount",
                                                "title": "Amount aggregate",
                                                "guess": True,
                                                "required": True
                                            },
                                            "prediction_steps": {
                                                "cardinality": "1",
                                                "type": "PARAMETER",
                                                "name": "prediction_steps",
                                                "title": "Prediction Steps",
                                                "data_type": "number",
                                                "default_value": 4,
                                                "guess": False,
                                            "required": False
                                            }
                                        },
                                        "output": {
                                            "name": "output",
                                            "instance": "json_outout",
                                            "cardinality": "1",
                                            "type": "TABLE"
                                        }
                        }),
                    ('dummyFunction',
                     {'decision': 'unknown algorithm'}),
                    ]
        for pair in test_lst:
            print (preprocessing_dm.get_algoIO(pair[0]))
            print(pair[1])
            assert pair[1] == preprocessing_dm.get_algoIO(pair[0])

    def test_get_all_algorithms_of(self):
        all_algos = preprocessing_dm.get_all_algorithms_of('dataset_1')
        print(all_algos)
        assert 'TimeSeries' in all_algos['algos']
        assert 'sampleFunction' in all_algos['algos']


if __name__ == '__main__':
    unittest.main()