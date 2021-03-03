"""hxlm.core.htype.actor

TODO: revew names used to classify actors/agents (think Data processor,
      Data consumer, Data contributor, ...)

See Also
--------
GitHub Issue: https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/9
"""


from dataclasses import dataclass

# from typing import (
#     Any
# )


@dataclass(init=True, repr=True, eq=True)
class ActorHtype:
    code: str = None


# @see https://data.humdata.org/dataset/2048a947-5714-4220-905b-e662cbcd14c8
#      /resource/c7053042-fd68-44c7-ae24-a57890a48235/download
#      /ocha-dr-guidelines-working-draft-032019.pdf

# TODO: Data processor: A person or organization that processes and adds value
#       to raw data, e.g. by cleaning it, loading it into a searchable
#       database, or combining it with data from other sources.

# TODO: Data consumer: A person or organization that uses data to make
#       decisions, take actions, or increase awareness.

# TODO:  Data subject: A natural person (i.e. an individual) whose personal
#        data is subject to processing, and who can be identified, either
#        directly or indirectly, by reference to this data and reasonably
#        likely measures. The nomination as a data subject is linked to a
#        set of specific data subject rights to which this natural person is
#        entitled with regards to his/her personal data, even when this data
#        is gathered, collected or otherwise processed by others).
#        Although data may also relate to organizations, rather than
#        individuals, organizations would not be considered ‘data subjects’
#         under the recognized legal definition.
