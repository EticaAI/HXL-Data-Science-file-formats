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

To implementers:
- While hxlm.core.htype.routing (and hxlm.routing) are early-drafts/
  working-drafts, the idea behind RoutingHtype (that professionals who work
  with internet routing) can help to protect sites who serve public HXLated
  content.
    - For "just" cache, you actually do not need at all to implement  this
      code or automate with other tools. In the middle of urgencies, do you
      think and make it work.
- The concept of a ideal of an HRouting work to proxy/filter data between
  different private networks require both knowledge of HXL and how to exchange
  data with very sensitive content. This means that even if implementations do
  become more than proof of concept, this may not become public.
    - At least not until do exist huge demand to a point of divide
      responsability of computers 'who route' from the ones 'who undestand'
      the HXL.


Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

from hxlm.routing.main import (
    routing_info,
    get_external_ip,
    request_cache_resource,
    request_priority_access
)