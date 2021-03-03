"""hxlm.core.htype.sensitive

See Also
--------
GitHub Issue :https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9

TODO: create an entry on the spreadsheet
"""

# HXL Standard & other discussions related to sensitiveHType
# - About the '+sensitive'
#   - https://groups.google.com/g/hxlproject/c/N-606LwRz80/m/Q7dq88YzBAAJ

# Links (need organization)
# - https://humanitarian.atlassian.net/wiki/spaces/HDXKB/pages
#   /2132148234/Data+Loss+Prevention+on+HDX
# - https://cloud.google.com/dlp/docs/infotypes-reference

from dataclasses import dataclass

# from typing import (
#     Any
# )


@dataclass(init=True, repr=True, eq=True)
class SensitiveHtype:
    code: str = None


# Concepts __________________________________________________________________
# TODO: Community Identifiable Information: Data points that enable the
#       identification, classification, and tracking of individuals, groups,
#       or multiple groups of individuals by demographically defining factors.
#       These may include ethnicity, gender, age, occupation, and religion.
#       May also be referred to as Demographically Identifiable Information
#       “DII.”
# TODO: Personal Data: Any information relating to an identified or
#       identifiable natural person (‘data subject’); an identifiable natural
#       person is one who can be identified, directly or indirectly, in
#       particular by reference to an identifier such as a name, an
#       identification number, location data, an online identifier or
#       to one or more factors specific to the physical, physiological,
#       genetic, mental, economic, cultural or social identity of that
#       natural person.
# TODO: Sensitive Data: Data with a high sensitivity level based on the
#       magnitude and severity of potential harms and the likelihood of such
#       harm materialising.

# TEMP, remove later ________________________________________________________
# Quick links
#  - https://data.humdata.org/faq
#  - https://centre.humdata.org/wp-content/uploads/2019/03/image1-768x596.png
#  - https://mimic.physionet.org/
#  - https://physionet.org/content/mimiciii-demo/1.4/

# > https://data.humdata.org/faq
# Sensitive Data
# How does HDX define sensitive data?
# For the purpose of sharing data through HDX, we have developed the following
# categories to communicate data sensitivity:
# Non-Sensitive – This includes datasets containing country statistics,
# roadmaps, weather data and other data with no foreseeable risk associated
# with sharing.
# Uncertain Sensitivity – For this data, sensitivity depends on a number of
# factors, including other datasets collected in the same context, what
# technology is or could be used to extract insights, and the local context
# from which the data is collected or which will be impacted by use of the
# data.
# Sensitive – This includes any dataset containing personal data of affected
# populations or aid workers. Datasets containing
# demographically identifiable information (DII) or
# community identifiable information (CII)
# that can put affected populations or aid workers at risk, are also considered
# sensitive data. Depending on context, satellite imagery can also fall
# into this third category of sensitivity.
# Can I share personal data through HDX?
# HDX does not allow personal data or personally identifiable information (PII)
# to be shared in public or private datasets. All data shared through the
# platform must be sufficiently aggregated or anonymized so as to prevent
# identification of people or harm to affected people and the humanitarian
# community. We do allow private datasets to include contact information of
# aid workers if they have provided consentto the sharing of their data within
# the organisation. Read more in our Terms of Service.
# https://centre.humdata.org/wp-content/uploads/2019/03/image1-768x596.png

# How does HDX assess the sensitivity of data?
# HDX endeavors not to allow publicly shared data that includes
# community identifiable information (CII) or
# demographically identifiable information (DII)
# that may put affected people at risk. However, this type of data is more
# challenging to identify within datasets during our quality assurance process
# without deeper analysis. In cases where we suspect that survey data may have
# a high risk of re-identification of affected people, we run an internal
# statistical disclosure control process using sdcMicro. Data is made private
# while we run this process. If the risk level is found to be too high for
# public sharing on HDX given the particular context to which the data relates,
# HDX will notify the data contributor to determine a course of action.
