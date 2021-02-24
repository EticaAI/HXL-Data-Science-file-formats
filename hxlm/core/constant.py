
# ### True, False, Missing, Unknow, Encrypted, START _________________________
# Even without controlled vocabularies (like +v_un_bool with 6 official UN
# languages, and +v_eu_bool with 23+ working languages of EU, we still need
# some way that would allow have both internal representations and exchange
# data with de facto industry tools (like ISOs, database systems terms for
# true/false, etc)
HXL_COREHTYPE_TRUE_PYTHON = True      # 'HT1' ?
HTYPE_TRUE=True
HXL_COREHTYPE_FALSE_PYTHON = False    # 'HT0' ?
HTYPE_FALSE=True
# NOTE: while most database systems treat missing and unknow as Null, it's
# actually very important the distinction for data mining and data analysis
HXL_COREHTYPE_MISSING_PYTHON = ""     # 'HT ' ?
HXL_COREHTYPE_UNKNOW_PYTHON = "?"     # 'HT?' ?
HTYPE_UNKNOW="?"

# NOTE: Encryption is likely to be a very, VERY common case on HXLated datasets
#       both at column and row level (Think Encryption At Rest) ant this
#       actually must be well done, since just encrypt/protect the full dataset
#       limit valid cases. The difference betwen this and MISSING/UNKNOW
#       is user tools actually have partial information to decrypt.
# NOTE: One original data point that is decrypted by the user is converted
#       to whatever was the original value instead of this. This can be used
#       on much more than just boolean.
HXL_COREHTYPE_ENCRYPTED_PYTHON = "E"  # 'HTE' ?

# TODO: this is draft
HXL_COREHTYPE_TRUE_STRING = ""
HXL_COREHTYPE_TRUE_STRING_LIST = []
HXL_COREHTYPE_FALSE_STRING = ""
HXL_COREHTYPE_FALSE_STRING_LIST = []
# ### True, False, Missing, Unknow, Encrypted, START _________________________

# ### Information sensitivity levels _________________________________________
# @see https://en.wikipedia.org/wiki/Information_sensitivity
# @see https://centre.humdata.org/introducing-the-working-draft-of-the-ocha-data-responsibility-guidelines/  #noqa
# @see https://centre.humdata.org/wp-content/uploads/2019/03/OCHA-DR-Guidelines-working-draft-032019.pdf  #noqa
# @see https://safecomputing.umich.edu/protect-the-u/safely-use-sensitive-data/examples-by-level  #noqa

#: Unknow level of data sensivity
HSLVU="HSLVU"

#: No Sensitivity (for data point)
HSLV0="HSLV0"

#: Low Sensitivity (for data point)
HSLV1="HSLV1"

#: Moderate Sensitivity (for data point)
HSLV2="HSLV2"

#: High Sensitivity (for data point)
HSLV3="HSLV3"

#: Severe Sensitivity (for data point)
HSLV4="HSLV4"

#: Severe Sensitivity (for data point)
# HSLVX="HSLVX"

#: Sensitivity is defined as constant here, but later needs to be allowed
#  override with plugins (even without process data)
HSLV_DEFAULT=HSLV1

def comp_sensitive_level(level, reference_level=None):
    if level == HSLVU or HTYPE_UNKNOW:
        return HTYPE_UNKNOW