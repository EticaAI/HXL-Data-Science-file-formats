"""hxlm.core.model.dispatcher abstraction to HDataDispatch concept

HDataControlPanel

This file is an placeholder (both in naming conventions and how it's done),
about an equivalent of Airline Dispatch, but instead of traffic control of
aircraft, is about dispatch of data: mostly (without get too much in details,
like actually have access to data contents; they actually could be fully
encrypted!) tend to be about authorize access to data or instruct local
collaborators to mitigate (like encrypt data at rest and give keys only
to owner) common issues in name of smaller data providers.

> Note: the biggest focus (think >90%) is optimization for sensitive content
  between organizations under urgency; this is not about preparing data to be
  published for public view.

In general the drafted tools and proofs of concepts on repository tend to
draft tools and documentation that focus on point-to-point data exchange.
The closest concept related to this is delegating trusts on how data is
transferred to volunteer that work as hxlm.routing.HRouting (that is inspired
n the Routing Manifesto; see MANRS.org), but such analogy already assumes
that (even if the datasets are not HXLated or well documented; but for
routing proposes we're talking about some sort of metadata) the data
contributors are able to write well defined rules or what can be done and what
cannot. These rules themselves could still have help from the local community,
but at some point there will exist some extra challenges. For example:

- Know who to trust (an computer/server represent an individual and/or
  organization) that meets the requirements of the data contributor to allow
  sharing with much less delay
- (This is even hard) as do exist strong need to log actions need to be taken
  in name of others (both for law compliance and also to be an upgrade compared
  to alternatives) either data contributors or organizations upper in the
  control chain of data contributors may require logs
  - Please note that as the default rule (likely not just a technical rule,
    but a strong moral principle for HRouting, not just refusing to implement
    tools) data itself should not be saved, but metadata (who sent it for who?
    When? Etc) alone could be problematic because who operates as the concept
    of HRouting could do "what is right" but without one upper advice,
    this could lead to data exposure of who exchanges data themselves.
- Data exchange point-to-point, even if encrypted URN indexes become used,
  have the problem of "not scale". This still (at least for what is inferred
  via proofs of concepts) faster and more integrated with tools than
  alternatives, bit the usability of allow people encrypt URNs with
  passwords still depend on humans from data source dealing with others
  aspects that could if solved for them if do exist higher demand for such
  dataset.
    - Please also note that, like an analogy to aircraft dispatch, small
      aircraft/airlines would not know how to deal with more complex things
      (like deal with public keys of peers instead of dealing with sent
      custom passwords via private channels). Humans/servers acting like the
      concept of "HRouting" could by design implement acceptable safe
      asymmetric encryption/signing/attention, and other advanced topics,
      but if demand eventually grow up, whoever act as the concept of HRouting
      would be overwhelmed with things that would already plan ahead how to
      write instructions with YAML (or and automated how to deploy them) from
      more regionally centralized coordination could be an win-win.

NOTE: [Contextual comments as 2021-03-10]. While some sort of automated
      centralized coordination is drafted, one of the general ideas on the
      proofs of concepts of HXL-Data-Science-file-formats is also to try at
      least the bare minimum to allow real time data exchange while comply
      with laws. While the laws themselves allow for exceptions (like usage
      it data to save lives is not just allowed, but the right thing to do),
      if over the years this actually start to be used, constructive feedback
      is welcome but, at least in my honest personal opinion, both who would
      work in the field controlling sensitive data exchange (since always will
      exist things that can't be automated) and whoever donate time (or at
      least do it in good faith) to develop code and and overall infrastructure
      shouldn't aim to be perfect; I mean: is impossible (not from an technical
      point, but actually mostly because people disagree on the definition
      itself) to be perfect and the acceptance of this make things so much
      easier. Them one logical implication is to be less fearful of
      criticism that is either simply  impractical to implement with
      current time and resources or any quick-but-very-wrong-fix would make
      more damage to human lives. (Emerson Rocha, 2021-03-10 18:19 BRT)

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


class HDataDispatch:
    """Like an flight dispatcher / airline dispatcher, but for data

    This class is an draft. But in short, while the HConteiner is mostly an
    abstraction to also collention of HDataset, the HDataDispatch is meant
    to abstract routines related to authorize flow of data in name of original
    data owners.
    """

    def __init__(self):
        self.kind: str = 'HDataDispatch'
