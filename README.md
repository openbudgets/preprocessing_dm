# PREPROCESSING_DM
A Python module for data pre-processing of data-mining tasks

# Quick start
```
$ git clone https://github.com/openbudgets/processing_dm.git
$ cd preprocessing_dm
preprocessing_dm $ source venv/bin/activate
(venv) okfgr_dm $ make init
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
In [2]: preprocessing_dm.list_dataset_name()
Out[2]:
['budget-katerini-revenue-2016__235c7',
 'budget-kalamaria-revenue-2004__e5589',
 'aragon-2010-expenditure__7fc66',
 'budget-heraklion-expenditure-2013__2c4eb',
 'budget-heraklion-expenditure-2010__4c7cc',
 'budget-heraklion-expenditure-2015__a9652',
 'budget-athens-revenue-2004__220e3',
 ...
 ]
 ```
