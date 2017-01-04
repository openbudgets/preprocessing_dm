# -*- coding: utf-8 -*-

from .context import preprocessing_dm

import json
import unittest


class TestAlgoMeta(unittest.TestCase):
    """Basic test cases."""
    def test_get_algo4data(self):
        test_lst = [('dummyTimeSeries', 'dataset_1', '',
                     {'decision': True}),
                    ('dummyTimeSeries', 'baddataset_x', '',
                     {'decision': False}),
                    ('dummyTimeSeries', '', 'bad',
                     {'decision': False}),
                    ('dummyTimeSeries', 'dataset_1', 'dataset',
                     {'decision':True}),
                    ('dummyTimeSeries', '', '',
                     {
                                            "description": "bla bla bla about dummyTimeSeries",
                                            "dataSets": ["dataset_1", "dataset_2"],
                                            "dataSetPatterns": ["athen", "esif"],
                                            "badDataSets": ["baddataset_x", "baddataset_y"],
                                            "badDataSetPatterns": ["bad"]
                    }),
                    ('dummyFunction', 'dataset_1', 'dataset',
                     {'decision': 'unknown algorithm'}),
                    ]
        for pair in test_lst:
            print(pair)
            print(preprocessing_dm.get_algo4data(algo=pair[0], data=pair[1], dataPat=pair[2]))
            assert pair[3] == preprocessing_dm.get_algo4data(algo=pair[0], data=pair[1], dataPat=pair[2])

    def test_get_algoIO(self):
        test_lst = [('dummyTimeSeries', {
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


if __name__ == '__main__':
    unittest.main()