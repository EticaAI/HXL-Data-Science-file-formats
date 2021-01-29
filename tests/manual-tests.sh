#!/bin/sh

hxl2tab tests/files/iris_hxlated-csv.csv temp/iris.tab
hxl2tab https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=245471857 data-mining-projects/output/hxl2tab-spec.tab
hxl2tab https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833 data-mining-projects/output/HXL-CPLP-Exemplar_iris.tab
hxl2tab https://docs.google.com/spreadsheets/d/1sYqhbAcwLe7hnwAJk7Qljlq-YH31DZT3GNVqPIBykV4/edit#gid=1357271284 data-mining-projects/output/HXL-CPLP-Exemplar_golf-weather_nominal.tab

hxlquickimport hxlquickimport_samples/covid19mexico_10itens.csv
hxlquickimport hxlquickimport_samples/covid19mexico_10itens.csv temp/covid19mexico_10itens.hxl.csv

# With this command, an non-HXLated dataset can be converted directly to hxl2tab
# (including poorly non human reviewed tags)
hxlquickimport hxlquickimport_samples/covid19mexico_10itens.csv | hxl2tab

hxlquickimport https://drive.google.com/file/d/1nQAu6lHvdh2AV7q6aewGBQIxFz7VrCF9/view?usp=sharing| hxl2tab > temp/mx.gob.dados_dataset_informacion-referente-a-casos-covid-19-en-mexico_2020-06-01.hxl.csv