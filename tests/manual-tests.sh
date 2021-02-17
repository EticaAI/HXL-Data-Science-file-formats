#!/bin/sh


#### Requisites ________________________________________________________________
pip3 install libhxl
pip3 install hug

# If you plan to use ngrok to proxy for external world, use something like
sudo snap install ngrok

#### The tests _________________________________________________________________

### hxl2example ----------------------------------------------------------------

hxl2example tests/files/iris_hxlated-csv.csv | head
hxl2example tests/files/iris_hxlated-csv.csv temp/iris.tab
hxl2example https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833 | head
hxl2example https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833 data-mining-projects/output/HXL-CPLP-Exemplar_iris.tab

## hug -f bin/hxl2example ......................................................
#@see https://hugapi.github.io/hug/
#@see https://github.com/hugapi/hug/
hug -f bin/hxl2example

curl --silent http://localhost:8000/hxl2example.csv?source_url=https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833 | head
# HXLStandard_HXLCoreSchema_CoreHashtags
curl --silent http://localhost:8000/hxl2example.csv?source_url=https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=319251406 | head

### hxl2tab --------------------------------------------------------------------

hxl2tab tests/files/iris_hxlated-csv.csv temp/iris.tab
hxl2tab https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=245471857 data-mining-projects/output/hxl2tab-spec.tab
hxl2tab https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833 data-mining-projects/output/HXL-CPLP-Exemplar_iris.tab
hxl2tab https://docs.google.com/spreadsheets/d/1sYqhbAcwLe7hnwAJk7Qljlq-YH31DZT3GNVqPIBykV4/edit#gid=1357271284 data-mining-projects/output/HXL-CPLP-Exemplar_golf-weather_nominal.tab

hxl2tab https://docs.google.com/spreadsheets/d/1Vqv6-EAdSHMSZvZtE426aXkDiwP8Mdrpft3tiGQ1RH0/edit#gid=0 temp/example-ebola-dataset-1_HXLated+tab.tab
hxl2tab https://docs.google.com/spreadsheets/d/1Vqv6-EAdSHMSZvZtE426aXkDiwP8Mdrpft3tiGQ1RH0/edit#gid=0 temp/example-ebola-dataset-1_HXLated+tab_hxltabv15.tab
hxl2tab https://docs.google.com/spreadsheets/d/1Vqv6-EAdSHMSZvZtE426aXkDiwP8Mdrpft3tiGQ1RH0/edit#gid=0 temp/example-ebola-dataset-1_HXLated+tab_hxltabv15_b.tab
hxl2tab https://docs.google.com/spreadsheets/d/1Vqv6-EAdSHMSZvZtE426aXkDiwP8Mdrpft3tiGQ1RH0/edit#gid=0 temp/example-ebola-dataset-1_HXLated+tab_hxltabv16.tab

## hug -f bin/hxl2tab ..........................................................
#@see https://hugapi.github.io/hug/
#@see https://github.com/hugapi/hug/
hug -f bin/hxl2tab

# See something like
#    - http://localhost:8000/hxl2tab.tab?source_url=https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833

# This will allow use hxl2tab via http. With ngrok could be used to quick allow
# others to use your computer as quick interface

### hxlquickmeta ---------------------------------------------------------------

hxlquickmeta tests/files/iris_hxlated-csv.csv | head
hxlquickmeta tests/files/iris_hxlated-csv.csv temp/iris.tab
hxlquickmeta https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833 | head
hxlquickmeta https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833 data-mining-projects/output/HXL-CPLP-Exemplar_iris.tab

## hug -f bin/hxlquickmeta ......................................................
#@see https://hugapi.github.io/hug/
#@see https://github.com/hugapi/hug/
hug -f bin/hxlquickmeta

curl --silent http://localhost:8000/hxlquickmeta.csv?source_url=https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833 | head
# HXLStandard_HXLCoreSchema_CoreHashtags
curl --silent http://localhost:8000/hxlquickmeta.csv?source_url=https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=319251406 | head


### hxlquickimport -------------------------------------------------------------

hxlquickimport hxlquickimport_samples/covid19mexico_10itens.csv
hxlquickimport hxlquickimport_samples/covid19mexico_10itens.csv temp/covid19mexico_10itens.hxl.csv

# With this command, an non-HXLated dataset can be converted directly to hxl2tab
# (including poorly non human reviewed tags)
hxlquickimport hxlquickimport_samples/covid19mexico_10itens.csv | hxl2tab

hxlquickimport https://drive.google.com/file/d/1nQAu6lHvdh2AV7q6aewGBQIxFz7VrCF9/view?usp=sharing | hxl2tab > temp/mx.gob.dados_dataset_informacion-referente-a-casos-covid-19-en-mexico_2020-06-01.hxl.csv
hxlquickimport https://docs.google.com/spreadsheets/d/1GQVrCQGEetx7RmKaZJ8eD5dgsr5i1zNy_UJpX3_AgrE/edit#gid=1715408033 > 'temp/hxlquickimport(v1.0)+hxl2tab(v1.4)__br.einstein_dataset_covid-pacientes-hospital-albert-einstein-anonimizado_2020-03-28.hxl.tab'
hxlquickimport https://docs.google.com/spreadsheets/d/1GQVrCQGEetx7RmKaZJ8eD5dgsr5i1zNy_UJpX3_AgrE/edit#gid=1715408033 | hxl2tab > 'temp/hxlquickimport(v1.0)+hxl2tab(v1.4)__br.einstein_dataset_covid-pacientes-hospital-albert-einstein-anonimizado_2020-03-28.hxl.tab'

hxlselect tests/files/iris_hxlated-csv+meta.hxl

### hxlquickimporttab ----------------------------------------------------------

hxlquickimporttab tests/files/iris_hxlated-tab.tab temp/iris_hxlated-csv-from-tab.csv
hxlquickimporttab tests/files/iris_hxlated-tab.tab temp/iris_hxlated-csv-from-tab.csv | head
hxl2tab https://docs.google.com/spreadsheets/d/1Vqv6-EAdSHMSZvZtE426aXkDiwP8Mdrpft3tiGQ1RH0/edit#gid=0 | head

hxlquickimporttab temp/titanic.tab | head


#### Ignore after this part ___________________________________________________
# fititnt@bravo:/workspace/data/brasil_inep_microdados-enem-2019/DADOS$ head -n 1000 MICRODADOS_ENEM_2019.csv > MICRODADOS_ENEM_2019_head-n-1000.csv
hxlquickimport hxlquickimport_samples/MICRODADOS_ENEM_2019_head-n-1000.csv | hxl2tab

head -n 3 hxlquickimport_samples/MICRODADOS_ENEM_2019_head-n-1000_quick-utf8-bom.csv | hxltag --map NU_INSCRICAO#item+incricao --default-tag='#item' 
head -n 3 hxlquickimport_samples/MICRODADOS_ENEM_2019_head-n-1000_quick-utf8.csv | hxltag --map NU_INSCRICAO#item+incricao --default-tag='#item' 
head -n 3 hxlquickimport_samples/MICRODADOS_ENEM_2019_head-n-1000.csv | hxltag --map NU_INSCRICAO#item+incricao --default-tag='#item' 