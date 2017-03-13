# -*- coding: utf-8 -*-

from .context import preprocessing_dm

import json
import unittest


class CheckDataSets(unittest.TestCase):
    """Basic test cases."""

    def test_check_dataset_use_slice(self):
        link1 = "http://ws307.math.auth.gr/rudolf/public/api/3/cubes/aragon-2008-income__568a8/facts"
        link2 = "http://ws307.math.auth.gr/rudolf/public/api/3/cubes/global/aggregate?drilldown=global__administrativeClassification__854d0.notation%7Cglobal__administrativeClassification__854d0.prefLabel&order=global__amount__0397f.sum:desc&pagesize=30"
        link3 = "http://ws307.math.auth.gr/rudolf/public/api/3/cubes/budget-kilkis-expenditure-2015__74025/aggregate?drilldown=administrativeClassification.prefLabel%7CeconomicClassification.prefLabel%7CbudgetPhase.prefLabel&aggregates=amount.sum"

        result = preprocessing_dm.construct_input_csv(link3)
        assert '/Input_' in result


if __name__ == '__main__':
    unittest.main()