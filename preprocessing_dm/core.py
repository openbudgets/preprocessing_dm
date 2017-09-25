from .virtuoso import check_dataset_use_slice

#
# Step 1. check ttl file, whether ?s a qb:Slice
#


def get_datasets_use_slice(datasetList):
    """
    check which dataset uses 'qb:Slice'
    :param datasetList: a list of dataset names
    :return: the list of datasets which use 'qb:Slice'
    """
    rlt = []
    for dataset in datasetList:
        if check_dataset_use_slice(dataset):
            rlt.append(dataset)
    return rlt


def get_csv_table_from_dataset(dataset):
    """
    get a table from an rdf dataset
    :param dataset: an RDF datasetname
    :return:
    """
    if check_dataset_use_slice(dataset):
        pass
    else:
        pass

