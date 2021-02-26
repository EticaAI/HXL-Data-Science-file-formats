#!/usr/bin/env python3

# TODO: move to some other place. Or maybe just delete it.

# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ ./tests/hxlated-xarray-pandas-test.py

import numpy as np
import pandas as pd
import dask.dataframe as dd

#### quick test, pandas _______________________________________________________

# df = pd.read_csv("tests/files/iris_hxlated-csv.csv", header=1)
# df.info()
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


#### Huge dataset ______________________________________________________________
        # @see https://stackoverflow.com/questions/25962114/how-do-i-read-a-large-csv-file-with-pandas
        # @see https://pt.stackoverflow.com/questions/392787/manipulando-dataset-de-3-gb-com-pandas-usando-chunks
        # 3.2GB dataset
        ## This will crash the computer, can use more than 10GB of RAM
        # df = pd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019.csv", sep=";")
        # df.info()

# This will not crash (if 1.000.000 fit on memory)
# chunksize = 1000000
# with pd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019.csv",
#                  sep=";", chunksize=chunksize) as reader:
#     for chunk in reader:
#         # process(chunk)
#         chunk.info()
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

#### dask ____________________________________________________________________
# @see https://examples.dask.org/dataframes/01-data-access.html
# pip3 install dask[dataframe]
# import dask.dataframe as dd

# df = dd.read_csv("tests/files/iris_hxlated-csv.csv", header=1)
# df.info()

### dask dashboard! ---------------------------------------------------------
# @see https://docs.dask.org/en/latest/diagnostics-distributed.html


# pip3 install "dask[distributed]
from dask.distributed import Client
client = Client()  # start distributed scheduler locally.  Launch dashboard
# http://localhost:8787/status

# @see https://stackoverflow.com/questions/49039750/how-to-see-progress-of-dask-compute-task
# @see https://docs.dask.org/en/latest/diagnostics-local.html
from dask.diagnostics import ProgressBar
ProgressBar().register()


# df = dd.read_csv("tests/files/iris_hxlated-csv.csv", header=1, blocksize=10000)
# df = dd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019.csv", sep=";", blocksize=10000)
        # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 1893: invalid continuation byte

# df = dd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019_knime-utf8.csv", sep=";", blocksize=10000)
# df.info()
# df.head()
# print('')
        # fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ ./tests/hxlated-xarray-pandas-dask-test.py 
        # <class 'dask.dataframe.core.DataFrame'>
        # Columns: 1 entries, NU_INSCRICAO,"NU_ANO","CO_MUNICIPIO_RESIDENCIA","NO_MUNICIPIO_RESIDENCIA","CO_UF_RESIDENCIA","SG_UF_RESIDENCIA","NU_IDADE","TP_SEXO","TP_ESTADO_CIVIL","TP_COR_RACA","TP_NACIONALIDADE","CO_MUNICIPIO_NASCIMENTO","NO_MUNICIPIO_NASCIMENTO","CO_UF_NASCIMENTO","SG_UF_NASCIMENTO","TP_ST_CONCLUSAO","TP_ANO_CONCLUIU","TP_ESCOLA","TP_ENSINO","IN_TREINEIRO","CO_ESCOLA","CO_MUNICIPIO_ESC","NO_MUNICIPIO_ESC","CO_UF_ESC","SG_UF_ESC","TP_DEPENDENCIA_ADM_ESC","TP_LOCALIZACAO_ESC","TP_SIT_FUNC_ESC","IN_BAIXA_VISAO","IN_CEGUEIRA","IN_SURDEZ","IN_DEFICIENCIA_AUDITIVA","IN_SURDO_CEGUEIRA","IN_DEFICIENCIA_FISICA","IN_DEFICIENCIA_MENTAL","IN_DEFICIT_ATENCAO","IN_DISLEXIA","IN_DISCALCULIA","IN_AUTISMO","IN_VISAO_MONOCULAR","IN_OUTRA_DEF","IN_GESTANTE","IN_LACTANTE","IN_IDOSO","IN_ESTUDA_CLASSE_HOSPITALAR","IN_SEM_RECURSO","IN_BRAILLE","IN_AMPLIADA_24","IN_AMPLIADA_18","IN_LEDOR","IN_ACESSO","IN_TRANSCRICAO","IN_LIBRAS","IN_TEMPO_ADICIONAL","IN_LEITURA_LABIAL","IN_MESA_CADEIRA_RODAS","IN_MESA_CADEIRA_SEPARADA","IN_APOIO_PERNA","IN_GUIA_INTERPRETE","IN_COMPUTADOR","IN_CADEIRA_ESPECIAL","IN_CADEIRA_CANHOTO","IN_CADEIRA_ACOLCHOADA","IN_PROVA_DEITADO","IN_MOBILIARIO_OBESO","IN_LAMINA_OVERLAY","IN_PROTETOR_AURICULAR","IN_MEDIDOR_GLICOSE","IN_MAQUINA_BRAILE","IN_SOROBAN","IN_MARCA_PASSO","IN_SONDA","IN_MEDICAMENTOS","IN_SALA_INDIVIDUAL","IN_SALA_ESPECIAL","IN_SALA_ACOMPANHANTE","IN_MOBILIARIO_ESPECIFICO","IN_MATERIAL_ESPECIFICO","IN_NOME_SOCIAL","CO_MUNICIPIO_PROVA","NO_MUNICIPIO_PROVA","CO_UF_PROVA","SG_UF_PROVA","TP_PRESENCA_CN","TP_PRESENCA_CH","TP_PRESENCA_LC","TP_PRESENCA_MT","CO_PROVA_CN","CO_PROVA_CH","CO_PROVA_LC","CO_PROVA_MT","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","TX_RESPOSTAS_CN","TX_RESPOSTAS_CH","TX_RESPOSTAS_LC","TX_RESPOSTAS_MT","TP_LINGUA","TX_GABARITO_CN","TX_GABARITO_CH","TX_GABARITO_LC","TX_GABARITO_MT","TP_STATUS_REDACAO","NU_NOTA_COMP1","NU_NOTA_COMP2","NU_NOTA_COMP3","NU_NOTA_COMP4","NU_NOTA_COMP5","NU_NOTA_REDACAO","Q001","Q002","Q003","Q004","Q005","Q006","Q007","Q008","Q009","Q010","Q011","Q012","Q013","Q014","Q015","Q016","Q017","Q018","Q019","Q020","Q021","Q022","Q023","Q024","Q025" to NU_INSCRICAO,"NU_ANO","CO_MUNICIPIO_RESIDENCIA","NO_MUNICIPIO_RESIDENCIA","CO_UF_RESIDENCIA","SG_UF_RESIDENCIA","NU_IDADE","TP_SEXO","TP_ESTADO_CIVIL","TP_COR_RACA","TP_NACIONALIDADE","CO_MUNICIPIO_NASCIMENTO","NO_MUNICIPIO_NASCIMENTO","CO_UF_NASCIMENTO","SG_UF_NASCIMENTO","TP_ST_CONCLUSAO","TP_ANO_CONCLUIU","TP_ESCOLA","TP_ENSINO","IN_TREINEIRO","CO_ESCOLA","CO_MUNICIPIO_ESC","NO_MUNICIPIO_ESC","CO_UF_ESC","SG_UF_ESC","TP_DEPENDENCIA_ADM_ESC","TP_LOCALIZACAO_ESC","TP_SIT_FUNC_ESC","IN_BAIXA_VISAO","IN_CEGUEIRA","IN_SURDEZ","IN_DEFICIENCIA_AUDITIVA","IN_SURDO_CEGUEIRA","IN_DEFICIENCIA_FISICA","IN_DEFICIENCIA_MENTAL","IN_DEFICIT_ATENCAO","IN_DISLEXIA","IN_DISCALCULIA","IN_AUTISMO","IN_VISAO_MONOCULAR","IN_OUTRA_DEF","IN_GESTANTE","IN_LACTANTE","IN_IDOSO","IN_ESTUDA_CLASSE_HOSPITALAR","IN_SEM_RECURSO","IN_BRAILLE","IN_AMPLIADA_24","IN_AMPLIADA_18","IN_LEDOR","IN_ACESSO","IN_TRANSCRICAO","IN_LIBRAS","IN_TEMPO_ADICIONAL","IN_LEITURA_LABIAL","IN_MESA_CADEIRA_RODAS","IN_MESA_CADEIRA_SEPARADA","IN_APOIO_PERNA","IN_GUIA_INTERPRETE","IN_COMPUTADOR","IN_CADEIRA_ESPECIAL","IN_CADEIRA_CANHOTO","IN_CADEIRA_ACOLCHOADA","IN_PROVA_DEITADO","IN_MOBILIARIO_OBESO","IN_LAMINA_OVERLAY","IN_PROTETOR_AURICULAR","IN_MEDIDOR_GLICOSE","IN_MAQUINA_BRAILE","IN_SOROBAN","IN_MARCA_PASSO","IN_SONDA","IN_MEDICAMENTOS","IN_SALA_INDIVIDUAL","IN_SALA_ESPECIAL","IN_SALA_ACOMPANHANTE","IN_MOBILIARIO_ESPECIFICO","IN_MATERIAL_ESPECIFICO","IN_NOME_SOCIAL","CO_MUNICIPIO_PROVA","NO_MUNICIPIO_PROVA","CO_UF_PROVA","SG_UF_PROVA","TP_PRESENCA_CN","TP_PRESENCA_CH","TP_PRESENCA_LC","TP_PRESENCA_MT","CO_PROVA_CN","CO_PROVA_CH","CO_PROVA_LC","CO_PROVA_MT","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","TX_RESPOSTAS_CN","TX_RESPOSTAS_CH","TX_RESPOSTAS_LC","TX_RESPOSTAS_MT","TP_LINGUA","TX_GABARITO_CN","TX_GABARITO_CH","TX_GABARITO_LC","TX_GABARITO_MT","TP_STATUS_REDACAO","NU_NOTA_COMP1","NU_NOTA_COMP2","NU_NOTA_COMP3","NU_NOTA_COMP4","NU_NOTA_COMP5","NU_NOTA_REDACAO","Q001","Q002","Q003","Q004","Q005","Q006","Q007","Q008","Q009","Q010","Q011","Q012","Q013","Q014","Q015","Q016","Q017","Q018","Q019","Q020","Q021","Q022","Q023","Q024","Q025"
        # dtypes: object(1)

# with dd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019_knime-utf8.csv", sep=";", blocksize=10000) as reader:
#     for chunk in reader:
#         print(chunk)
#         # chunk.info()
#         # df.head()
#         print('')
        # Traceback (most recent call last):
        #   File "./tests/hxlated-xarray-pandas-dask-test.py", line 106, in <module>
        #     with dd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019_knime-utf8.csv", sep=";", blocksize=10000) as reader:
        # AttributeError: __enter__

# df = dd.read_csv("tests/files/iris_hxlated-csv.csv", header=1)
# print('df', df)
        # df Dask DataFrame Structure:
        #               #item+eng_sepal+eng_length+number #item+eng_sepal+eng_width+number #item+eng_petal+eng_length+number #item+eng_petal+eng_width+number #item+class+vt_class
        # npartitions=1                                                                                                                                                           
        #                                         float64                          float64                           float64                          float64               object
        #                                             ...                              ...                               ...                              ...                  ...
        # Dask Name: read-csv, 1 tasks

df = dd.read_csv("/workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019_knime-utf8.csv", sep=";", blocksize=10000)
print('df', df)
print('df.info()')
df.info()
print('df.describe()')
        # df.describe()
        # df Dask DataFrame Structure:
        #                    NU_INSCRICAO,"NU_ANO","CO_MUNICIPIO_RESIDENCIA","NO_MUNICIPIO_RESIDENCIA","CO_UF_RESIDENCIA","SG_UF_RESIDENCIA","NU_IDADE","TP_SEXO","TP_ESTADO_CIVIL","TP_COR_RACA","TP_NACIONALIDADE","CO_MUNICIPIO_NASCIMENTO","NO_MUNICIPIO_NASCIMENTO","CO_UF_NASCIMENTO","SG_UF_NASCIMENTO","TP_ST_CONCLUSAO","TP_ANO_CONCLUIU","TP_ESCOLA","TP_ENSINO","IN_TREINEIRO","CO_ESCOLA","CO_MUNICIPIO_ESC","NO_MUNICIPIO_ESC","CO_UF_ESC","SG_UF_ESC","TP_DEPENDENCIA_ADM_ESC","TP_LOCALIZACAO_ESC","TP_SIT_FUNC_ESC","IN_BAIXA_VISAO","IN_CEGUEIRA","IN_SURDEZ","IN_DEFICIENCIA_AUDITIVA","IN_SURDO_CEGUEIRA","IN_DEFICIENCIA_FISICA","IN_DEFICIENCIA_MENTAL","IN_DEFICIT_ATENCAO","IN_DISLEXIA","IN_DISCALCULIA","IN_AUTISMO","IN_VISAO_MONOCULAR","IN_OUTRA_DEF","IN_GESTANTE","IN_LACTANTE","IN_IDOSO","IN_ESTUDA_CLASSE_HOSPITALAR","IN_SEM_RECURSO","IN_BRAILLE","IN_AMPLIADA_24","IN_AMPLIADA_18","IN_LEDOR","IN_ACESSO","IN_TRANSCRICAO","IN_LIBRAS","IN_TEMPO_ADICIONAL","IN_LEITURA_LABIAL","IN_MESA_CADEIRA_RODAS","IN_MESA_CADEIRA_SEPARADA","IN_APOIO_PERNA","IN_GUIA_INTERPRETE","IN_COMPUTADOR","IN_CADEIRA_ESPECIAL","IN_CADEIRA_CANHOTO","IN_CADEIRA_ACOLCHOADA","IN_PROVA_DEITADO","IN_MOBILIARIO_OBESO","IN_LAMINA_OVERLAY","IN_PROTETOR_AURICULAR","IN_MEDIDOR_GLICOSE","IN_MAQUINA_BRAILE","IN_SOROBAN","IN_MARCA_PASSO","IN_SONDA","IN_MEDICAMENTOS","IN_SALA_INDIVIDUAL","IN_SALA_ESPECIAL","IN_SALA_ACOMPANHANTE","IN_MOBILIARIO_ESPECIFICO","IN_MATERIAL_ESPECIFICO","IN_NOME_SOCIAL","CO_MUNICIPIO_PROVA","NO_MUNICIPIO_PROVA","CO_UF_PROVA","SG_UF_PROVA","TP_PRESENCA_CN","TP_PRESENCA_CH","TP_PRESENCA_LC","TP_PRESENCA_MT","CO_PROVA_CN","CO_PROVA_CH","CO_PROVA_LC","CO_PROVA_MT","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","TX_RESPOSTAS_CN","TX_RESPOSTAS_CH","TX_RESPOSTAS_LC","TX_RESPOSTAS_MT","TP_LINGUA","TX_GABARITO_CN","TX_GABARITO_CH","TX_GABARITO_LC","TX_GABARITO_MT","TP_STATUS_REDACAO","NU_NOTA_COMP1","NU_NOTA_COMP2","NU_NOTA_COMP3","NU_NOTA_COMP4","NU_NOTA_COMP5","NU_NOTA_REDACAO","Q001","Q002","Q003","Q004","Q005","Q006","Q007","Q008","Q009","Q010","Q011","Q012","Q013","Q014","Q015","Q016","Q017","Q018","Q019","Q020","Q021","Q022","Q023","Q024","Q025"
        # npartitions=358762                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                object
        #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ...
        # ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ...
        #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ...
        #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ...
        # Dask Name: read-csv, 358762 tasks
        # df.info()
        # <class 'dask.dataframe.core.DataFrame'>
        # Columns: 1 entries, NU_INSCRICAO,"NU_ANO","CO_MUNICIPIO_RESIDENCIA","NO_MUNICIPIO_RESIDENCIA","CO_UF_RESIDENCIA","SG_UF_RESIDENCIA","NU_IDADE","TP_SEXO","TP_ESTADO_CIVIL","TP_COR_RACA","TP_NACIONALIDADE","CO_MUNICIPIO_NASCIMENTO","NO_MUNICIPIO_NASCIMENTO","CO_UF_NASCIMENTO","SG_UF_NASCIMENTO","TP_ST_CONCLUSAO","TP_ANO_CONCLUIU","TP_ESCOLA","TP_ENSINO","IN_TREINEIRO","CO_ESCOLA","CO_MUNICIPIO_ESC","NO_MUNICIPIO_ESC","CO_UF_ESC","SG_UF_ESC","TP_DEPENDENCIA_ADM_ESC","TP_LOCALIZACAO_ESC","TP_SIT_FUNC_ESC","IN_BAIXA_VISAO","IN_CEGUEIRA","IN_SURDEZ","IN_DEFICIENCIA_AUDITIVA","IN_SURDO_CEGUEIRA","IN_DEFICIENCIA_FISICA","IN_DEFICIENCIA_MENTAL","IN_DEFICIT_ATENCAO","IN_DISLEXIA","IN_DISCALCULIA","IN_AUTISMO","IN_VISAO_MONOCULAR","IN_OUTRA_DEF","IN_GESTANTE","IN_LACTANTE","IN_IDOSO","IN_ESTUDA_CLASSE_HOSPITALAR","IN_SEM_RECURSO","IN_BRAILLE","IN_AMPLIADA_24","IN_AMPLIADA_18","IN_LEDOR","IN_ACESSO","IN_TRANSCRICAO","IN_LIBRAS","IN_TEMPO_ADICIONAL","IN_LEITURA_LABIAL","IN_MESA_CADEIRA_RODAS","IN_MESA_CADEIRA_SEPARADA","IN_APOIO_PERNA","IN_GUIA_INTERPRETE","IN_COMPUTADOR","IN_CADEIRA_ESPECIAL","IN_CADEIRA_CANHOTO","IN_CADEIRA_ACOLCHOADA","IN_PROVA_DEITADO","IN_MOBILIARIO_OBESO","IN_LAMINA_OVERLAY","IN_PROTETOR_AURICULAR","IN_MEDIDOR_GLICOSE","IN_MAQUINA_BRAILE","IN_SOROBAN","IN_MARCA_PASSO","IN_SONDA","IN_MEDICAMENTOS","IN_SALA_INDIVIDUAL","IN_SALA_ESPECIAL","IN_SALA_ACOMPANHANTE","IN_MOBILIARIO_ESPECIFICO","IN_MATERIAL_ESPECIFICO","IN_NOME_SOCIAL","CO_MUNICIPIO_PROVA","NO_MUNICIPIO_PROVA","CO_UF_PROVA","SG_UF_PROVA","TP_PRESENCA_CN","TP_PRESENCA_CH","TP_PRESENCA_LC","TP_PRESENCA_MT","CO_PROVA_CN","CO_PROVA_CH","CO_PROVA_LC","CO_PROVA_MT","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","TX_RESPOSTAS_CN","TX_RESPOSTAS_CH","TX_RESPOSTAS_LC","TX_RESPOSTAS_MT","TP_LINGUA","TX_GABARITO_CN","TX_GABARITO_CH","TX_GABARITO_LC","TX_GABARITO_MT","TP_STATUS_REDACAO","NU_NOTA_COMP1","NU_NOTA_COMP2","NU_NOTA_COMP3","NU_NOTA_COMP4","NU_NOTA_COMP5","NU_NOTA_REDACAO","Q001","Q002","Q003","Q004","Q005","Q006","Q007","Q008","Q009","Q010","Q011","Q012","Q013","Q014","Q015","Q016","Q017","Q018","Q019","Q020","Q021","Q022","Q023","Q024","Q025" to NU_INSCRICAO,"NU_ANO","CO_MUNICIPIO_RESIDENCIA","NO_MUNICIPIO_RESIDENCIA","CO_UF_RESIDENCIA","SG_UF_RESIDENCIA","NU_IDADE","TP_SEXO","TP_ESTADO_CIVIL","TP_COR_RACA","TP_NACIONALIDADE","CO_MUNICIPIO_NASCIMENTO","NO_MUNICIPIO_NASCIMENTO","CO_UF_NASCIMENTO","SG_UF_NASCIMENTO","TP_ST_CONCLUSAO","TP_ANO_CONCLUIU","TP_ESCOLA","TP_ENSINO","IN_TREINEIRO","CO_ESCOLA","CO_MUNICIPIO_ESC","NO_MUNICIPIO_ESC","CO_UF_ESC","SG_UF_ESC","TP_DEPENDENCIA_ADM_ESC","TP_LOCALIZACAO_ESC","TP_SIT_FUNC_ESC","IN_BAIXA_VISAO","IN_CEGUEIRA","IN_SURDEZ","IN_DEFICIENCIA_AUDITIVA","IN_SURDO_CEGUEIRA","IN_DEFICIENCIA_FISICA","IN_DEFICIENCIA_MENTAL","IN_DEFICIT_ATENCAO","IN_DISLEXIA","IN_DISCALCULIA","IN_AUTISMO","IN_VISAO_MONOCULAR","IN_OUTRA_DEF","IN_GESTANTE","IN_LACTANTE","IN_IDOSO","IN_ESTUDA_CLASSE_HOSPITALAR","IN_SEM_RECURSO","IN_BRAILLE","IN_AMPLIADA_24","IN_AMPLIADA_18","IN_LEDOR","IN_ACESSO","IN_TRANSCRICAO","IN_LIBRAS","IN_TEMPO_ADICIONAL","IN_LEITURA_LABIAL","IN_MESA_CADEIRA_RODAS","IN_MESA_CADEIRA_SEPARADA","IN_APOIO_PERNA","IN_GUIA_INTERPRETE","IN_COMPUTADOR","IN_CADEIRA_ESPECIAL","IN_CADEIRA_CANHOTO","IN_CADEIRA_ACOLCHOADA","IN_PROVA_DEITADO","IN_MOBILIARIO_OBESO","IN_LAMINA_OVERLAY","IN_PROTETOR_AURICULAR","IN_MEDIDOR_GLICOSE","IN_MAQUINA_BRAILE","IN_SOROBAN","IN_MARCA_PASSO","IN_SONDA","IN_MEDICAMENTOS","IN_SALA_INDIVIDUAL","IN_SALA_ESPECIAL","IN_SALA_ACOMPANHANTE","IN_MOBILIARIO_ESPECIFICO","IN_MATERIAL_ESPECIFICO","IN_NOME_SOCIAL","CO_MUNICIPIO_PROVA","NO_MUNICIPIO_PROVA","CO_UF_PROVA","SG_UF_PROVA","TP_PRESENCA_CN","TP_PRESENCA_CH","TP_PRESENCA_LC","TP_PRESENCA_MT","CO_PROVA_CN","CO_PROVA_CH","CO_PROVA_LC","CO_PROVA_MT","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","TX_RESPOSTAS_CN","TX_RESPOSTAS_CH","TX_RESPOSTAS_LC","TX_RESPOSTAS_MT","TP_LINGUA","TX_GABARITO_CN","TX_GABARITO_CH","TX_GABARITO_LC","TX_GABARITO_MT","TP_STATUS_REDACAO","NU_NOTA_COMP1","NU_NOTA_COMP2","NU_NOTA_COMP3","NU_NOTA_COMP4","NU_NOTA_COMP5","NU_NOTA_REDACAO","Q001","Q002","Q003","Q004","Q005","Q006","Q007","Q008","Q009","Q010","Q011","Q012","Q013","Q014","Q015","Q016","Q017","Q018","Q019","Q020","Q021","Q022","Q023","Q024","Q025"
        # dtypes: object(1)df.describe()


# @see https://stackoverflow.com/questions/60889399/debug-why-dask-dataframe-operation-is-doing-nothing

#### TODOs ____________________________________________________________________

# TODO: do some quick test on dask dashboard https://docs.dask.org/en/latest/diagnostics-distributed.html
# TODO: add test with xarray (XArray requires complex formating, CSV is not engouth)
