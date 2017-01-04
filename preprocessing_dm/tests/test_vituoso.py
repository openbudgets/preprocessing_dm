# -*- coding: utf-8 -*-

from .context import preprocessing_dm

import json
import unittest


class TestVituoso(unittest.TestCase):
    """Basic test cases."""
    def test_check_dataset_use_slice(self):
        input_dataset1 = "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012>"
        input_dataset2 = "<http://data.openbudgets.eu/resource/dataset/aragon-2006-expenditure>"
        ref = ['http://data.openbudgets.eu/ontology/dsd/dimension/fiscalYear',
               'http://data.openbudgets.eu/ontology/dsd/dimension/operationCharacter',
               'http://data.openbudgets.eu/ontology/dsd/dimension/organization',
               'http://data.openbudgets.eu/ontology/dsd/greek-municipalities/dimension/budgetPhase',
               'http://data.openbudgets.eu/ontology/dsd/budget-kilkis-expenditure-2012/dimension/functionalClassification',
               'http://data.openbudgets.eu/ontology/dsd/greek-municipalities/dimension/economicClassification',
               'http://data.openbudgets.eu/ontology/dsd/greek-municipalities/dimension/administrativeClassification']
        result = preprocessing_dm.get_dimensions_from_dataset(input_dataset1)
        print(result)
        assert result == ref

    def test_get_all_observations_from_sliced_dataset(self):
        dataset1 = "<http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012>"
        reflst = [{'s': {'value': 'http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012/slice/00.6031', 'type': 'uri'},
                   'functionalClassification':
                       {'value': 'http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012/codelist/00/6031', 'type': 'uri'},
                   'budgetPhase': {'value': 'http://data.openbudgets.eu/resource/codelist/budget-phase/draft', 'type': 'uri'},
                   'administrativeClassification': {'value': 'http://data.openbudgets.eu/resource/codelist/kae-ota-administration-2014/00',
                                                    'type': 'uri'}, 'economicClassification':
                       {'value': 'http://data.openbudgets.eu/resource/codelist/kae-ota-exodwn-2014/6031', 'type': 'uri'},
                   'sfunc': {'value': 'http://data.openbudgets.eu/ontology/dsd/budget-kilkis-expenditure-2012/slice/slice-by-functionalCode',
                             'type': 'uri'},
                   'observation': {'value': 'http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012/observation/00.6031/draft', 'type': 'uri'},
                   'amount': {'datatype': 'http://www.w3.org/2001/XMLSchema#decimal', 'value': '123600', 'type': 'typed-literal'}},
                  {'s': {'value': 'http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012/slice/00.6031', 'type': 'uri'},
                   'functionalClassification': {'value': 'http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012/codelist/00/6031',
                                                'type': 'uri'},
                   'budgetPhase': {'value': 'http://data.openbudgets.eu/resource/codelist/budget-phase/executed', 'type': 'uri'},
                   'administrativeClassification': {'value': 'http://data.openbudgets.eu/resource/codelist/kae-ota-administration-2014/00', 'type': 'uri'},
                   'economicClassification': {'value': 'http://data.openbudgets.eu/resource/codelist/kae-ota-exodwn-2014/6031', 'type': 'uri'},
                   'sfunc': {'value': 'http://data.openbudgets.eu/ontology/dsd/budget-kilkis-expenditure-2012/slice/slice-by-functionalCode', 'type': 'uri'},
                   'observation': {'value': 'http://data.openbudgets.eu/resource/dataset/budget-kilkis-expenditure-2012/observation/00.6031/executed', 'type': 'uri'},
                   'amount': {'datatype': 'http://www.w3.org/2001/XMLSchema#decimal', 'value': '123548.47', 'type': 'typed-literal'}}]
        item1 = reflst[0]
        item2 = reflst[1]
        result = preprocessing_dm.get_all_observations_from_sliced_dataset(dataset1)
        assert item1 in result
        assert item2 in result

    def test_get_all_observations_from_nonsliced_dataset(self):
        dataset1 = "<http://data.openbudgets.eu/resource/dataset/aragon-expenditure-2010>"
        reflst = [
            {'observation': {
                'value': 'http://data.openbudgets.eu/resource/dataset/aragon-2010-expenditure/observation/10',
                'type': 'uri'}, 'amount': {'datatype': 'http://www.w3.org/2001/XMLSchema#decimal', 'value': '610051.68',
                                           'type': 'typed-literal'}, 'economicClassification': {
                'value': 'http://data.openbudgets.eu/resource/codelist/estructura_economica_g_aragon_2010/121001',
                'type': 'uri'}, 'fundingClassification': {
                'value': 'http://data.openbudgets.eu/resource/codelist/estructura_financiacion_g_aragon_2010/91002',
                'type': 'uri'}, 'administrativeClassification': {
                'value': 'http://data.openbudgets.eu/resource/codelist/estructura_organica_aragon_2010/01010',
                'type': 'uri'}, 'functionalClassification': {
                'value': 'http://data.openbudgets.eu/resource/codelist/estructura_funcional_aragon_2010/1111',
                'type': 'uri'}}
        ]
        result = preprocessing_dm.get_all_observations_from_nonsliced_dataset(dataset1)
        print(result[0])
        assert reflst[0] in result


if __name__ == '__main__':
    unittest.main()