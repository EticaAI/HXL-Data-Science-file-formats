#!/bin/sh
echo "Read me, not execute-me. Usage:"
echo "  cat manual-tests.sh"
exit

#### Automated tests __________________________________________________________

### tox ------------------------------------------------------------------------
# @see https://tox.readthedocs.io/en/latest/
tox

### GitHub actions local debug (nektos/act) ------------------------------------
# @see https://github.com/nektos/act
act
# sudo act

## Extra commands for debug and delete all images
## (DO NOT use these if you use docker for anything else)
# List all containers (include stopped)
#    sudo docker ps -a
# Show all local images
#    sudo docker image ls
# Stop running conteiners
#    sudo docker stop $(sudo docker ps -a -q)
# Delete all stoppend conteiners
#    sudo docker rm $(sudo docker ps -a -q)

## doctest
# @see https://docs.python.org/3/library/doctest.html
pytest -vv hxlm/ --doctest-modules

#### Requisites ________________________________________________________________
pip3 install libhxl
pip3 install hug

# If you plan to use ngrok to proxy for external world, use something like
sudo snap install ngrok


#### Build JSON Knowledge Graph from YAML ______________________________________

### Installation of requisites -------------------------------------------------
# @see https://kislyuk.github.io/yq/
sudo apt install jq
pip3 install jq yq

### Filter YAML (useful if need to build subsets) ------------------------------

## Filter groups, like .attr.datum from core.vkg.yml

# cat hxlm/ontologia/core.vkg.yml | yq .attr.datum
yq .attr.datum < hxlm/ontologia/core.vkg.yml
#  This will output json

yq .attr.datum --yaml-output < hxlm/ontologia/core.vkg.yml
# This will output YAML

### YAML to JSON ---------------------------------------------------------------

# Generate hxlm/ontologia/json/core.vkg.json
yq < hxlm/ontologia/core.vkg.yml > hxlm/ontologia/json/core.vkg.json

# Generate hxlm/ontologia/json/core.lkg.json
yq < hxlm/ontologia/core.lkg.yml > hxlm/ontologia/json/core.lkg.json

#### localization ______________________________________________________________

### Enviroment checks ----------------------------------------------------------
locale
echo "$LANGUAGE"
echo "$LC_ALL"
echo "$LC_MESSAGES"
echo "$LANG"
echo "$LC_NUMERIC"
echo "$LC_MONETARY"

# To force run hdpcli with an different locale, can prefix with enviroment
# variables, like
LANG=en.UTF-8 LANGUAGE=en.UTF-8 hdpcli --help

### Extract keywords -----------------------------------------------------------
xgettext hxlm/core/bin/hdpcli.py

# Generate pot file
xgettext hxlm/core/bin/hdpcli.py --output=hxlm/locale/hdp.pot --language=Python --package-name='hxlm' --package-version="0.8.3" --default-domain=hdp  --add-comments --no-location --indent

# Example of how generate an specific translation file
xgettext hxlm/core/bin/hdpcli.py --output=hxlm/locale/pt/LC_MESSAGES/hdp.po --language=Python --package-name='hxlm' --package-version="0.8.3" --default-domain=hdp  --add-comments --no-location --inden --join-existing

#### The tests _________________________________________________________________

### hdpcli ---------------------------------------------------------------------
./hxlm/core/bin/hdpcli.py --debug --hdp-init-data /tmp/hdp-test --please
./hxlm/core/bin/hdpcli.py --debug --hdp-init-data /tmp/hdp-test

### hdpcli --export-to-hxl-json-processing-specs ...............................

# remote access
hdpcli --export-to-hxl-json-processing-specs tests/hxl-processing-specs/hxl-processing-specs-test-01.mul.hdp.yml --debug
hdpcli --export-to-hxl-json-processing-specs https://raw.githubusercontent.com/EticaAI/HXL-Data-Science-file-formats/main/tests/hxl-processing-specs/hxl-processing-specs-test-01.mul.hdp.yml --debug
hdpcli https://raw.githubusercontent.com/EticaAI/HXL-Data-Science-file-formats/main/tests/hxl-processing-specs/hxl-processing-specs-test-01.mul.hdp.yml 


# To inspect the result (pretty print)
hdpcli --export-to-hxl-json-processing-specs tests/hxl-processing-specs/hxl-processing-specs-test-01.mul.hdp.yml
# To pipe the result direct to hxlspec (first item of array, use jq '.[0]')
hdpcli --export-to-hxl-json-processing-specs tests/hxl-processing-specs/hxl-processing-specs-test-01.mul.hdp.yml | jq '.[0]' | hxlspec
# To pipe the result direct to hxlspec (first item of array, use jq '.[1]')
hdpcli --export-to-hxl-json-processing-specs tests/hxl-processing-specs/hxl-processing-specs-test-01.mul.hdp.yml | jq '.[1]' | hxlspec

### hdpcli --non-(*) / --verum-(*) (filters) ...................................
# This allow filter the HDP internal dictionary

# Returns empty:
hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --non-grupum salve-mundi

# Returns something
hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --verum-grupum salve-mundi

# Retuns something
hdpcli tests/hrecipe/yemen-01.hrecipe.mul.hdp.yml --verum-urn yemen

# Retuns something
hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --verum-urn salve-mundi --verum-grupum salve-mundi

# export languages
hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --objectivum-linguam RUS
hdpcli tests/hrecipe/salve-mundi.hrecipe.rus.hdp.yml --objectivum-linguam POR
hdpcli tests/hrecipe/salve-mundi.hrecipe.rus.hdp.yml --fontem-linguam=RUS --objectivum-linguam POR

### hdpcli --objectivum-linguam ZZZ (export to language) .......................
# this will export to a new know language
hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --objectivum-linguam ARA
hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --objectivum-linguam POR
hdpcli tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml --objectivum-linguam RUS

# hdpcli --export-to-hxl-json-processing-specs tests/hxl-processing-specs/hxl-processing-specs-test-01.mul.hdp.yml | jq '.[0]' | hxlspec | tabulate
jsonschema -i temp/salve-mundi.hrecipe.mul.hdp.json hxlm/core/schema/hdp.json-schema.json
# jsonschema tests/hrecipe/salve-mundi.hrecipe.mul.hdp.yml hxlm/core/schema/hdp.json-schema.json

### jsonschema .................................................................
# TODO: maybe?
#       - https://github.com/Julian/jsonschema
#       - https://python-jsonschema.readthedocs.io/en/stable/

# https://raw.githubusercontent.com/HXLStandard/libhxl-python/master/profile/data/unhcr_popstats_export_persons_of_concern_all_data.hxl
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
hxlquickmeta --hxlquickmeta-hashtag="#adm2+code" --hxlquickmeta-value="BR3106200"

hxlquickmeta tests/files/iris_hxlated-csv.csv
hxlquickmeta https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833
hxlquickmeta https://docs.google.com/spreadsheets/u/1/d/1l7POf1WPfzgJb-ks4JM86akFSvaZOhAUWqafSJsm3Y4/edit#gid=634938833
hxlquickmeta https://data.humdata.org/dataset/2d058968-9d7e-49a9-b28f-2895d7f6536f/resource/a12bad12-f5ea-493c-9faa-66cb3f3e9ca7/download/fts_incoming_funding_bra.csv

# Non HXLated CSV, use hxlquickimport
hxlquickimport tests/files/iris.csv | hxlquickmeta

# HXL-CPLP-Vocab_Bool; @see https://github.com/HXL-CPLP/forum/issues/49
hxlquickmeta https://docs.google.com/spreadsheets/d/1hGUxMN2ywWNv8ONQ59Pp9Q4nG-eTRnAs0SyWunFZUDg/edit#gid=214068544

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

### hxl2encryption -------------------------------------------------------------
hxl2encryption tests/files/iris_hxlated-csv.csv | head
### hxl2decryption -------------------------------------------------------------
hxl2decryption tests/files/iris_hxlated-csv.csv | head

### urnresolver ----------------------------------------------------------------
hxlselect "$(urnresolver urn:data:xz:hxl:standard:core:hashtag)" --query 'release_status=Released'
hxlquickimport "$(urnresolver urn:data:xz:hxl:standard:core:hashtag)"
urnresolver urn:data:xz:hxlcplp:fod:lang --no-urn-vendor-defaults --no-urn-user-defaults

head /home/fititnt/Downloads/brasil-covid.csv | hxlquickimport | hxlselect --query="#item+paciente_racacor_valor=PARDA"

head "$(urnresolver urn:data:br:saude.gov.br:vacinacao:covid-19-vacinacao)"


urnresolver urn:data:xz:hxlcplp:fod:lang --no-urn-vendor-defaults --no-urn-user-defaults --urn-index-remote="https://raw.githubusercontent.com/EticaAI/HXL-Data-Science-file-formats/main/tests/urnresolver/all-in-same-dir/urn.csv"

# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ wc -l "$(urnresolver urn:data:br:saude.gov.br:vacinacao:covid-19-vacinacao)"
# 8580433 /home/fititnt/.local/var/hxlm/data/br/saude.gov.br/vacinacao/covid-19-vacinacao/covid-19-vacinacao.csv

#### [meta issue] HXL and data directly from and to SQL databases #10 __________
# @see https://docs.sqlalchemy.org/en/13/dialects/
# @see https://github.com/wireservice/csvkit/blob/master/csvkit/utilities/csvsql.py

# TODO: Create an local PostgreSQL database
# @see https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html
# createdb hxltest

# Generate create schema
csvsql tests/files/iris_hxlated-csv.csv --dialect postgresql --skip-lines 1
csvsql tests/files/iris_hxlated-csv.csv --dialect mysql --skip-lines 1
# CREATE TABLE "iris_hxlated-csv" (
# 	"#item+eng_sepal+eng_length+number" DECIMAL NOT NULL, 
# 	"#item+eng_sepal+eng_width+number" DECIMAL NOT NULL, 
# 	"#item+eng_petal+eng_length+number" DECIMAL NOT NULL, 
# 	"#item+eng_petal+eng_width+number" DECIMAL NOT NULL, 
# 	"#item+class+vt_class" VARCHAR NOT NULL
# );
csvsql tests/files/iris_hxlated-csv.csv --dialect mysql --skip-lines 1
# CREATE TABLE `iris_hxlated-csv` (
# 	`#item+eng_sepal+eng_length+number` DECIMAL(38, 1) NOT NULL, 
# 	`#item+eng_sepal+eng_width+number` DECIMAL(38, 1) NOT NULL, 
# 	`#item+eng_petal+eng_length+number` DECIMAL(38, 1) NOT NULL, 
# 	`#item+eng_petal+eng_width+number` DECIMAL(38, 1) NOT NULL, 
# 	`#item+class+vt_class` VARCHAR(15) NOT NULL
# );
csvsql tests/files/iris_hxlated-csv.csv --dialect sqlite --skip-lines 1
# CREATE TABLE "iris_hxlated-csv" (
# 	"#item+eng_sepal+eng_length+number" FLOAT NOT NULL, 
# 	"#item+eng_sepal+eng_width+number" FLOAT NOT NULL, 
# 	"#item+eng_petal+eng_length+number" FLOAT NOT NULL, 
# 	"#item+eng_petal+eng_width+number" FLOAT NOT NULL, 
# 	"#item+class+vt_class" VARCHAR NOT NULL
# );
csvsql tests/files/iris_hxlated-csv.csv --dialect mssql --skip-lines 1
# CREATE TABLE [iris_hxlated-csv] (
# 	[#item+eng_sepal+eng_length+number] DECIMAL(38, 1) NOT NULL, 
# 	[#item+eng_sepal+eng_width+number] DECIMAL(38, 1) NOT NULL, 
# 	[#item+eng_petal+eng_length+number] DECIMAL(38, 1) NOT NULL, 
# 	[#item+eng_petal+eng_width+number] DECIMAL(38, 1) NOT NULL, 
# 	[#item+class+vt_class] VARCHAR(max) NOT NULL
# );

# Insert data directly on the server
csvsql tests/files/iris_hxlated-csv.csv --db 'postgresql://postgres:password@localhost/hxltest' --skip-lines 1

#### Build hxlmeta local storage _______________________________________________
# @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc
# Note: these hxlmeta examples may not actually be used by the HXLMeta Class
#       but could at least be used to test importing/exporting from databases

# @see https://github.com/harelba/q/blob/master/test/BENCHMARK.md

# TODO hxl2example --remove-headers example.com/dataset hxlmeta-data/HXLMeta_DataType.hxl.csv

### HXLMeta_DataType, HXLMeta_StorageType, HXLMeta_StatisticalType
hxl2example https://docs.google.com/spreadsheets/d/1hGUxMN2ywWNv8ONQ59Pp9Q4nG-eTRnAs0SyWunFZUDg/edit#gid=214068544 hxlmeta-data/HXLMeta_DataType.hxl.csv
hxl2example https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=211012023 hxlmeta-data/HXLMeta_StorageType.hxl.csv
hxl2example https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1566300457 hxlmeta-data/HXLMeta_StatisticalType.hxl.csv
hxl2example https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1053765950 hxlmeta-data/HXLMeta_LevelType.hxl.csv
hxl2example https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=617579056 hxlmeta-data/HXLMeta_UsageType.hxl.csv

### HXL-CPLP-Vocab_Bool --------------------------------------------------------
# @see https://github.com/HXL-CPLP/forum/issues/49
hxl2example https://docs.google.com/spreadsheets/d/1hGUxMN2ywWNv8ONQ59Pp9Q4nG-eTRnAs0SyWunFZUDg/edit#gid=214068544 hxlmeta-data/HXL-CPLP-Vocab_Bool.hxl.csv

### UNOCHA-countries-territories -----------------------------------------------
# https://vocabulary.unocha.org/
hxl2example https://docs.google.com/spreadsheets/d/1NjSI2LaS3SqbgYc0HdD8oIb7lofGtiHgoKKATCpwVdY/edit#gid=1088874596 hxlmeta-data/UNOCHA_countries-territories.hxl.csv

### HXL-CPLP-FOD_languages -----------------------------------------------------
hxl2example https://docs.google.com/spreadsheets/d/12k4BWqq5c3mV9ihQscPIwtuDa_QRB-iFohO7dXSSptI/edit#gid=0 hxlmeta-data/HXL-CPLP-FOD_languages.hxl.csv

### HXLStandard_Data-types --------------------------------------------------
hxl2example https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=1881622062 hxlmeta-data/HXLStandard_Data-types.hxl.csv

### HXLStandard_Core-hashtags --------------------------------------------------
hxl2example https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=319251406 hxlmeta-data/HXLStandard_Core-hashtags.hxl.csv

### HXLStandard_Core-attributes ------------------------------------------------
hxl2example https://docs.google.com/spreadsheets/d/1En9FlmM8PrbTWgl3UHPF_MXnJ6ziVZFhBbojSJzBdLI/edit#gid=1810309357 hxlmeta-data/HXLStandard_Core-attributes.hxl.csv

#### Ignore after this part ___________________________________________________
# fititnt@bravo:/workspace/data/brasil_inep_microdados-enem-2019/DADOS$ head -n 1000 MICRODADOS_ENEM_2019.csv > MICRODADOS_ENEM_2019_head-n-1000.csv
hxlquickimport hxlquickimport_samples/MICRODADOS_ENEM_2019_head-n-1000.csv | hxl2tab

head -n 3 hxlquickimport_samples/MICRODADOS_ENEM_2019_head-n-1000_quick-utf8-bom.csv | hxltag --map NU_INSCRICAO#item+incricao --default-tag='#item' 
head -n 3 hxlquickimport_samples/MICRODADOS_ENEM_2019_head-n-1000_quick-utf8.csv | hxltag --map NU_INSCRICAO#item+incricao --default-tag='#item' 
head -n 3 hxlquickimport_samples/MICRODADOS_ENEM_2019_head-n-1000.csv | hxltag --map NU_INSCRICAO#item+incricao --default-tag='#item' 

#### hxlspec __________________________________________________________________
# /workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/yemen_hno_2021_clusters-intersectoral-severity_dataset.xlsx
# @source https://data.humdata.org/dataset/yemen-humanitarian-needs-overview
# @source https://data.humdata.org/dataset/yemen-humanitarian-needs-overview/resource/eb4e597c-a969-4b77-b9ef-94c55c216dbf

#### frictionless tests ________________________________________________________
# @see https://framework.frictionlessdata.io/docs/guides/basic-examples/
# @see https://developers.google.com/public-data/docs/schema/dspl9

pip3 install frictionless
# cd temp/
# wget https://raw.githubusercontent.com/frictionlessdata/frictionless-py/master/data/countries.csv
frictionless describe countries.csv

frictionless describe countries.csv
frictionless describe /workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019_head-n-1000.csv
frictionless describe /workspace/data/brasil_inep_microdados-enem-2019/DADOS/MICRODADOS_ENEM_2019.csv
frictionless describe /home/fititnt/Downloads/ven_adminboundaries_tabulardata.xlsx

#### dask tests ______________________________________________________________
# @see https://docs.dask.org/en/latest/install.html
# python -m pip install "dask[complete]"    # Install everything
pip3 install dask                # Install only core parts of dask
# pip3 install dask[dataframe]     # we need dataframe even for simple tests
pip3 install "dask[complete]"    # Install everything

#### xarray tests ____________________________________________________________
pip3 install xarray
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ pip3 install xarray
# Collecting xarray
#   Downloading xarray-0.16.2-py3-none-any.whl (736 kB)
#      |████████████████████████████████| 736 kB 4.1 MB/s 
# Requirement already satisfied: setuptools>=38.4 in /usr/lib/python3/dist-packages (from xarray) (45.2.0)
# Requirement already satisfied: pandas>=0.25 in /home/fititnt/.local/lib/python3.8/site-packages (from xarray) (1.2.1)
# Requirement already satisfied: numpy>=1.15 in /usr/lib/python3/dist-packages (from xarray) (1.17.4)
# Requirement already satisfied: pytz>=2017.3 in /usr/lib/python3/dist-packages (from pandas>=0.25->xarray) (2019.3)
# Requirement already satisfied: python-dateutil>=2.7.3 in /usr/lib/python3/dist-packages (from pandas>=0.25->xarray) (2.7.3)
# Installing collected packages: xarray
# Successfully installed xarray-0.16.2

#### antlr ____________________________________________________________________
# @see https://github.com/antlr/antlr4/blob/master/doc/getting-started.md
# cd /usr/local/lib
$ curl -O https://www.antlr.org/download/antlr-4.9-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.9.1-complete.jar:$CLASSPATH"

# I will not add alias to bash_profile; needs to run this everytime
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
# url.g4 from https://github.com/antlr/grammars-v4/tree/master/url

# cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/url-python
antlr4 -Dlanguage=Python3 /workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/url-python/url.g4

# https://pypi.org/project/antlr4-python3-runtime/#files
# pip3 install antlr4-python3-runtime

#### instantparse _____________________________________________________________
clojure -X tests/grammar/instaparse-abnf_test.cljc

# TODO: https://stackoverflow.com/questions/25136463/how-print-parse-tree-using-python2-runtime-with-antlr4?rq=1#comment39129827_25137278
# TODO: https://github.com/antlr/grammars-v4/tree/master/doiurl
# TODO: https://github.com/antlr/antlr4/blob/master/doc/python-target.md

#### keying python tests ______________________________________________________
# pip3 install keyring
# keyring --help
# keyring --list-backends
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ keyring set system username
# Password for 'username' in 'system': (type here: teste)
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ keyring get system username
# teste
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ python3 -c "import keyring.util.platform_; print(keyring.util.platform_.config_root())"
# /home/fititnt/.local/share/python_keyring
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats$ python3 -c "import keyring.util.platform_; print(keyring.util.platform_.data_root())"
# /home/fititnt/.local/share/python_keyring


#### Rocha's local development notes _________________________________________
# VSCode python code suggestion is wonderful, but have some issues with
# namespaced packages when doing local development. So this trick is how Rocha
# do: a bunch of symlinks

# mv /home/fititnt/.local/lib/python3.8/site-packages/hxlm /home/fititnt/.local/lib/python3.8/site-packages/hxlm-old
# ln -s /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm  /home/fititnt/.local/lib/python3.8/site-packages/hxlm
# ln -s /workspace/git/EticaAI/hxlm-compliance-bra-eticaai/hxlm/compliance /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/compliance
# ln -s /workspace/git/EticaAI/hxlm-crypto-eticaai/hxlm/crypto /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/crypto
# ln -s /workspace/git/EticaAI/hxlm-crypto-eticaai/hxlm/plugin/xe_cryptoexample /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm/plugin/xe_cryptoexample


# ### On termux
# pip install git+https://github.comEticaAI/HXL-Data-Science-file-formats.git#egg=hxlm-base-eticaai
