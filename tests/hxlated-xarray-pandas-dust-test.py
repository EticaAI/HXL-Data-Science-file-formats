#!/usr/bin/env python3

# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ ./tests/hxlated-xarray-pandas-test.py

import numpy as np
import pandas as pd

df = pd.read_csv("tests/files/iris_hxlated-csv.csv", header=1)
df.info()
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ ./tests/hxlated-xarray-pandas-test.py
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 150 entries, 0 to 149
# Data columns (total 5 columns):
#  #   Column                             Non-Null Count  Dtype  
# ---  ------                             --------------  -----  
#  0   #item+eng_sepal+eng_length+number  150 non-null    float64
#  1   #item+eng_sepal+eng_width+number   150 non-null    float64
#  2   #item+eng_petal+eng_length+number  150 non-null    float64
#  3   #item+eng_petal+eng_width+number   150 non-null    float64
#  4   #item+class+vt_class               150 non-null    object 
# dtypes: float64(4), object(1)
# memory usage: 6.0+ KB


# Huge dataset ______________________________________________________________
# @see https://stackoverflow.com/questions/25962114/how-do-i-read-a-large-csv-file-with-pandas
# @see https://pt.stackoverflow.com/questions/392787/manipulando-dataset-de-3-gb-com-pandas-usando-chunks
# 3.2GB dataset
## This will crash the computer, can use more than 10GB of RAM
# df = pd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019.csv", sep=";")
# df.info()

# This will not crash (if 1.000.000 fit on memory)
chunksize = 1000000
with pd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019.csv",
                 sep=";", chunksize=chunksize) as reader:
    for chunk in reader:
        # process(chunk)
        chunk.info()
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ ./tests/hxlated-xarray-pandas-test.py
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000000 entries, 0 to 999999
# Columns: 136 entries, NU_INSCRICAO to Q025
# dtypes: float64(24), int64(71), object(41)
# memory usage: 1.0+ GB
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000000 entries, 1000000 to 1999999
# Columns: 136 entries, NU_INSCRICAO to Q025
# dtypes: float64(24), int64(71), object(41)
# memory usage: 1.0+ GB
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000000 entries, 2000000 to 2999999
# Columns: 136 entries, NU_INSCRICAO to Q025
# dtypes: float64(24), int64(71), object(41)
# memory usage: 1.0+ GB
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000000 entries, 3000000 to 3999999
# Columns: 136 entries, NU_INSCRICAO to Q025
# dtypes: float64(24), int64(71), object(41)
# memory usage: 1.0+ GB
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000000 entries, 4000000 to 4999999
# Columns: 136 entries, NU_INSCRICAO to Q025
# dtypes: float64(24), int64(71), object(41)
# memory usage: 1.0+ GB
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 95270 entries, 5000000 to 5095269
# Columns: 136 entries, NU_INSCRICAO to Q025
# dtypes: float64(24), int64(71), object(41)
# memory usage: 98.9+ MB



# TODO: add test with xarray (XArray requires complex formating, CSV is not engouth)
# TODO: add test with dust