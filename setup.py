from setuptools import setup

setup(name='preprocessing_dm',
      version='0.1',
      description='Data preprocessing for Data Mining Services',
      url='http://github.com/obeu/preprocessing_dm',
      author='Tiansi Dong',
      author_email='tian1shi2@gmail.com',
      license='MIT',
      packages=['preprocessing_dm'],
      data_files=[('',['preprocessing_dm/algo4data.json', 'preprocessing_dm/algoIO.json'])],
      zip_safe=False)