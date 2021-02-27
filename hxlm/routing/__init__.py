"""hxlm.routing is a non-core subpackage to be used as reference to Routing

NOTE: while this may still be on the main repository
      EticaAI/HXL-Data-Science-file-formats, if eventually over the years
      be pertinent differenciate who is processing HXLated data and who is
      routing, this is were this packages kicks in!
      (Emerson Rocha, 2021-02-27 01:19 UTC)

See "Mutually Agreed Norms for Routing Security (MANRS)" (TL;DR: a global 
initiative, supported by the Internet Society, that provides crucial fixes
to reduce the most common routing threats.)

@see https://www.manrs.org/about/
@see https://www.youtube.com/watch?v=nJINk5p-HEE
@see https://www.youtube.com/watch?v=IuY6wqTm35U
"""

from hxlm.routing.main import (
    routing_info,
    get_external_ip
)