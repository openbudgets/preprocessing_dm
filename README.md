# PREPROCESSING_DM
A Python module for data pre-processing of data-mining tasks

# Quick start
```
$ git clone https://github.com/openbudgets/preprocessing_dm.git
$ cd preprocessing_dm
preprocessing_dm $ make init
```

# Run test
```
preprocessing_dm $ make test
```

# Generate documentation
```
preprocessing_dm $ ./make_docu
```
Documentation is located at docs/html/

# Access PREPROCESSING_DM within iPython

```
$ iPython

In [1]: import preprocessing_dm as ppdm
In [2]: ppdm.get_all_observations_from_nonsliced_dataset("<http://data.openbudgets.eu/resource/dataset/aragon-expenditure-2010>")
PREFIX qb:  <http://purl.org/linked-data/cube#>
PREFIX obeu-measure: <http://data.openbudgets.eu/ontology/dsd/measure/>
Select ?observation ?amount ?administrativeClassification ?functionalClassification ?economicClassification ?fundingClassification
 From <http://data.openbudgets.eu/resource/dataset/aragon-expenditure-2010>
 WHERE {  ?observation obeu-measure:amount ?amount .
?observation a qb:Observation .
?observation <http://data.openbudgets.eu/ontology/dsd/aragon-budget-exp-2010/dimension/administrativeClassification> ?administrativeClassification .
?observation <http://data.openbudgets.eu/ontology/dsd/aragon-budget-exp-2010/dimension/functionalClassification> ?functionalClassification .
?observation <http://data.openbudgets.eu/ontology/dsd/aragon-budget-exp-2010/dimension/economicClassification> ?economicClassification .
?observation <http://data.openbudgets.eu/ontology/dsd/aragon-budget-exp-2010/dimension/fundingClassification> ?fundingClassification .
 }
Out[2]:
[{'administrativeClassification': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/codelist/estructura_organica_aragon_2010/01010'},
  'amount': {'datatype': 'http://www.w3.org/2001/XMLSchema#decimal',
   'type': 'typed-literal',
   'value': '610051.68'},
  'economicClassification': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/codelist/estructura_economica_g_aragon_2010/121001'},
  'functionalClassification': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/codelist/estructura_funcional_aragon_2010/1111'},
  'fundingClassification': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/codelist/estructura_financiacion_g_aragon_2010/91002'},
  'observation': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/dataset/aragon-2010-expenditure/observation/10'}},
 {'administrativeClassification': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/codelist/estructura_organica_aragon_2010/01010'},
  'amount': {'datatype': 'http://www.w3.org/2001/XMLSchema#decimal',
   'type': 'typed-literal',
   'value': '150'},
  'economicClassification': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/codelist/estructura_economica_g_aragon_2010/206000'},
  'functionalClassification': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/codelist/estructura_funcional_aragon_2010/1113'},
  'fundingClassification': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/codelist/estructura_financiacion_g_aragon_2010/91002'},
  'observation': {'type': 'uri',
   'value': 'http://data.openbudgets.eu/resource/dataset/aragon-2010-expenditure/observation/100'}},
 ...
 ]
```
