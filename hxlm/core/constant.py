"""hxlm.core.constant

# TODO: consider create new constants based on
#       https://reliefweb.int/sites/reliefweb.int/files/resources/data.pdf
"""
import os

HXLM_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

HDATUM_EXEMPLUM = 'file://' + HXLM_ROOT + '/data/exemplum/'
HDATUM_HXL = 'file://' + HXLM_ROOT + '/data/hxl/'
HDATUM_UDHR = 'file://' + HXLM_ROOT + '/data/udhr/'

# TODO: 'ontologia' (ontology) seems to be not classical Latin, but somewhat
#       recent (1600). We will for now use HOntologia as term
#       (Emerson Rocha, 2021-03-23 08:48 UTC)
# https://en.wikipedia.org/wiki/Jacob_Lorhard
# 'He uses "Ontologia" synonymously with "Metaphysica".'
HONTOLOGIA_LKG = 'file://' + HXLM_ROOT + '/ontologia/core.lkg.yml'
HONTOLOGIA_VKG = 'file://' + HXLM_ROOT + '/ontologia/core.vkg.yml'

# _HXLM_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# HXLM_UDUR = _HXLM_ROOT + '/data/udhr'

# TODO: path to test folder is deprecated.
HXLM_TESTS_ROOT = os.path.dirname(HXLM_ROOT) + '/tests'


# ### True, False, Missing, Unknow, Encrypted, START _________________________
# Even without controlled vocabularies (like +v_un_bool with 6 official UN
# languages, and +v_eu_bool with 23+ working languages of EU, we still need
# some way that would allow have both internal representations and exchange
# data with de facto industry tools (like ISOs, database systems terms for
# true/false, etc)
# HXL_COREHTYPE_TRUE_PYTHON = True      # 'HT1' ?
HTYPE_TRUE = "TRUE"
# HXL_COREHTYPE_FALSE_PYTHON = False    # 'HT0' ?
HTYPE_FALSE = "FALSE"
# NOTE: while most database systems treat missing and unknow as Null, it's
# actually very important the distinction for data mining and data analysis
# HXL_COREHTYPE_MISSING_PYTHON = ""     # 'HT ' ?
# HXL_COREHTYPE_UNKNOW_PYTHON = "?"     # 'HT?' ?
HTYPE_UNKNOW = "?"

# NOTE: Encryption is likely to be a very, VERY common case on HXLated datasets
#       both at column and row level (Think Encryption At Rest) ant this
#       actually must be well done, since just encrypt/protect the full dataset
#       limit valid cases. The difference betwen this and MISSING/UNKNOW
#       is user tools actually have partial information to decrypt.
# NOTE: One original data point that is decrypted by the user is converted
#       to whatever was the original value instead of this. This can be used
#       on much more than just boolean.
# Note: the "!" different from HTYPE_UNKNOW="?" that
# actually can be stored explicitly as ?, is an
# pseudo representation. Encryption-aware tools could
# choose to print "!" while internally have the real
# value. Also, if exported tables do have "!" as value
# Encryption-aware tools could still label the data as
# encrypted while don't offer how to decrypt (since they
# technically could not do it)
HTYPE_ENCRYPTED = "!"

HTYPE_TRUE_LIST = ["TRUE", "true", "1"]
HTYPE_FALSE_LIST = ["FALSE", "false", "0"]

# ### True, False, Missing, Unknow, Encrypted, START _________________________

# ### Information sensitivity levels _________________________________________
# Group H(XLm) D(ata) S(ensitivity) L(evel)
# Statistical data type: Ordinal data
# For compare, see hxlm.core.util.cmp_sensitive_level()

# @see https://en.wikipedia.org/wiki/Information_sensitivity
# @see https://centre.humdata.org
#    /introducing-the-working-draft-of-the-ocha-data-responsibility-guidelines/
# @see https://centre.humdata.org/wp-content/uploads/2019/03
#      /OCHA-DR-Guidelines-working-draft-032019.pdf
# @see https://safecomputing.umich.edu/protect-the-u
#      /safely-use-sensitive-data/examples-by-level

#: Unknow level of data sensivity
HDSLU = "HDSLU"

#: No Sensitivity (for data point)
HDSL0 = "HDSL0"

#: Low Sensitivity (for data point)
HDSL1 = "HDSL1"

#: Moderate Sensitivity (for data point)
HDSL2 = "HDSL2"

#: High Sensitivity (for data point)
HDSL3 = "HDSL3"

#: Severe Sensitivity (for data point)
HDSL4 = "HDSL4"

#: Severe Sensitivity (for data point)
# HDSLX="HDSLX"

#: Sensitivity is defined as constant here, but later needs to be allowed
#  override with plugins (even without process data)
HDSL_DEFAULT = HDSL1

# ### Security Clearance level ________________________________________________
# @see https://www.ors.od.nih.gov/ser/dpsac/services/other-services
#      /security-clearance/Pages/default.aspx
# @see https://en.wikipedia.org/wiki/Level_of_measurement

# ### Data Trust Level ________________________________________________________
# >> This is a draft to see good naming conventions. May not be implemented <<
# >> This draft may be moved to compliance example extension <<
# The concept of 'Data Trust Level' (if implemeted) is not meant to be exposed
# to end user. (TODO: explain or remove)
# HDTLU="HDTLU"
# HDTL0="HDTL0"
# HDTL1="HDTL1"
# HDTL2="HDTL2"
# HDTL3="HDTL3"
# HDTL4="HDTL4"

# ### Data Processor (human, organization) Trust Level ________________________
# >> This is a draft to see good naming conventions. May not be implemented <<
# Reasoning to consider add:
#   some type of scale to measure infered trust on
#   the current natural person and organization makes sense
#   Note that this type of check could be ignored if the data is managed by
#   infrastruture without release sensitive information to the human.
HPTLU = "HPTLU"
HPTL1 = "HPTL1"  # Default ?
HPTL2 = "HPTL2"
HPTL3 = "HPTL3"
HPTL4 = "HPTL4"

# ### Data Infrastruture Trust Level _________________________________________
# >> This is a draft to see good naming conventions. May not be implemented <<
# Note: maybe is necessary break this note in more than one group.
# Reasoning to consider add:
#   Do exist cases were an combination of underlining hardware infrastruture
#   plus the way the software is used have an higher trust level than the
#   current Data Processor (the human or organization).
#   While on averange cases, is very likely that users implement rules that
#   require both HITL_ and HPTL_ have a minimum, special rules could be made
#   upfront, (think something like elections) were groups that do not trust
#   each other but the infrasctuture is homologated
HITLU = "HITLU"
HITL0 = "HITL0"
HITL1 = "HITL1"  # Default ?
HITL2 = "HITL2"
HITL3 = "HITL3"
HITL4 = "HITL4"
