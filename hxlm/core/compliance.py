"""Core facade to policy, standard or law compliance-like methods

TL;DR: check if user is authorized to do something based on context and then
       take an decision (from just remove/anonymize the sensitive content for
       the human who is processing the data now or maybe who is defined to
       receive the data to raise warnings)

Typical usage
-------------

While most automated tools that do compliance checks tend to be about
technical standards or conventions on files ("does this file have this
attribute?" "Does this field is the right date type?")" the main goal of
this module is focused on more police/law for common tasks related to
process the data.

Please note that do exist limitations on automated checks:

- The quality of the checks are based on how the input data was HXLated
- The number of false positives is likely to be high even if you use rules
  from one domain (like education) for people who work on healthcare.
- Consider implement additional features, like require user credentials, or
  maybe allow reduce severity based on infrastruture (like if be aware that
  someone granted that the data would be deleted).

Notes:
- While the core library will not enforce these functions, the documentation
  serve as hint for implementers.
- Also note that, if eventually HXLm becomes used, part of the rules would not
  be public outside your organization.


Advanced usage (requires coordination)
--------------------------------------
TODO: explain ways based on the Data processor (the natural person) that
      can receive additional (preferable also some fake ones, just to always
      have noise) list of hashes that are not authorized to see.

Author: 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""

import sys

# TODO: add check_compliance_on_after_decrypt_row and
#       check_compliance_on_before_decrypt_row and document how to optimize
#       the loops. This may need some real testing
#       (fititnt, 2021-02-25 07:57)


def check_compliance_on_after_decrypt_column(
        Tolerance: int, Verbose: int = 0, **kwargs):
    """Check compliance with policy/law/standard after column decryption

    Even if the current context the decryption of an column is allowed, this is
    the step were after actually know what each data point represent, the
    program can choose to not only block this column decryption, but mark the
    entire row as protected.

    One simple example could be (TODO: add examples)

    Parameters
    ----------
    Tolerance: int
        Description of parameter `x`.
    Verbose: int, default=0
        Verbose is recommended to be used as an way to help debug errors.
        But some implementers of the compliance extension to literaly
        return True while doing other checks without warn the user.

    Returns
    -------
    bool
        True means 100% compliant on the context. False may return instead of
        exception based on Tolerance.
    """

    # TODO: implement plugin-like feature, while use this as facade
    # TODO: consider strerr for verbose; but this depends on how we would
    #       test https://docs.pytest.org/en/stable/capture.html
    return True


def check_compliance_on_before_decrypt_column(
        Tolerance: int, Verbose: int = 0, **kwargs):
    """Check compliance with policy/law/standard before try decrypt a column

    This check is not about if a column COULD, but if SHOULD, be decrypted in
    the current context. The semantics here are very important: while the
    program may try the default decryption strategy (like a key that the user
    or the well controlled data proxy may actually have, but will not tell to
    user) if the user is not authorized to decrypt this type of column, the
    software should not offer this feature.

    Also, the implementers use the Tolerance as a hint to not trow Exception
    if you are doing a quick check on all the table the user just opened, but
    be less tolerant if the user explicitly ask to decrypt.

    Parameters
    ----------
    Tolerance: int
        Give a numeric hint about tolerance if the computed result is not 100%
        compliant. While compilance extensions may use this value for
        customized implementations, implementators should assume that 0 may
        break the program imediatelly (like raise an exception)
    Verbose: int, default=0
        Verbose is recommended to be used as an way to help debug errors.
        But some implementers of the compliance extension to literaly
        return True while doing other checks without warn the user.

    Returns
    -------
    bool
        True means 100% compliant on the context. False may return instead of
        exception based on Tolerance.
    """

    # TODO: implement plugin-like feature, while use this as facade
    # TODO: consider strerr for verbose; but this depends on how we would
    #       test https://docs.pytest.org/en/stable/capture.html
    return True


def check_compliance_on_after_decrypt_row(
        Tolerance: int, Verbose: int = 0, **kwargs):
    """Check compliance with policy/law/standard after a HXLRow decryption

    If for some reason before decryption the program was allowed to decrypt,
    this check can be used to, based on new evidence, take some action.
    This could be used to validate if the user (or the destinatary, if is
    preparing data) should see the end result.

    The averange usage for this routine is validate the end result before
    show to contents for the current user. While this could be the chance to
    apply simpler rules (like 'if the program now is aware that the data
    represent people and generic rules don't allow this type of user see
    people from specific region were it works'), advanced usage could be
    allow to re-encrypt for others.

    TODO: improve/correct this text. I

    See
    ---
        hxlm.core.HXLRow

    Advanced usage
    --------------
    One advanced usage of this method is to allow the program to re-encrypt
    (think like the current user is very skilled


    data to
    send to a new data consumer while the current person

    Parameters
    ----------
    Tolerance: int
        Give a numeric hint about tolerance if the computed result is not 100%
        compliant. While compilance extensions may use this value for
        customized implementations, implementators should assume that 0 may
        break the program imediatelly (like raise an exception)
    Verbose: int, default=0
        Verbose is recommended to be used as an way to help debug errors.
        But some implementers of the compliance extension to literaly
        return True while doing other checks without warn the user.

    Returns
    -------
    bool
        True means 100% compliant on the context. False may return instead of
        exception based on Tolerance.
    """

    # TODO: implement plugin-like feature, while use this as facade
    # TODO: consider strerr for verbose; but this depends on how we would
    #       test https://docs.pytest.org/en/stable/capture.html
    return True


def check_compliance_on_before_decrypt_row(
        Tolerance: int, Verbose: int = 0, **kwargs):
    """Check compliance with policy/law/standard before try decrypt a HXLRow

    TODO: explain more.

    See
    ---
        hxlm.core.HXLRow

    Parameters
    ----------
    Tolerance: int
        Give a numeric hint about tolerance if the computed result is not 100%
        compliant. While compilance extensions may use this value for
        customized implementations, implementators should assume that 0 may
        break the program imediatelly (like raise an exception)
    Verbose: int, default=0
        Verbose is recommended to be used as an way to help debug errors.
        But some implementers of the compliance extension to literaly
        return True while doing other checks without warn the user.

    Returns
    -------
    bool
        True means 100% compliant on the context. False may return instead of
        exception based on Tolerance.
    """

    # TODO: implement plugin-like feature, while use this as facade
    # TODO: consider strerr for verbose; but this depends on how we would
    #       test https://docs.pytest.org/en/stable/capture.html
    return True


def check_compliance_on_initialization(
        Tolerance: int, Verbose: int = 0, **kwargs):
    """Check compliance with policy/law/standard at initialization.

    This function is recommended at very early stage of any program run
    before even do a request (like open a local or remove file).

    Parameters
    ----------
    Tolerance: int
        Give a numeric hint about tolerance if the computed result is not 100%
        compliant. While compilance extensions may use this value for
        customized implementations, implementators should assume that 0 may
        break the program imediatelly (like raise an exception)
    Verbose: int, default=0
        Verbose is recommended to be used as an way to help debug errors.
        But some implementers of the compliance extension to literaly
        return True while doing other checks without warn the user.

    Returns
    -------
    bool
        True means 100% compliant on the context. False may return instead of
        exception based on Tolerance.
    """

    # TODO: implement plugin-like feature, while use this as facade
    # TODO: consider strerr for verbose; but this depends on how we would
    #       test https://docs.pytest.org/en/stable/capture.html
    return True


def check_compliance_on_termination(
        Tolerance: int, Verbose: int = 0, **kwargs):
    """Check compliance with policy/law/standard at successful termination.

    While in some circumstances (like uncaught exceptions) this routine may not
    run (think users forgot to test and implement all potential errors), the
    intent is for implementers to use it when all actions have been taken
    before ending execution.

    The compilance extension, while at this point could not prevent an action,
    since now is able to know all the context, can decide log more information
    or even do additional checks or actions, like do not authorize local cache.

    Parameters
    ----------
    Tolerance: int
        Give a numeric hint about tolerance if the computed result is not 100%
        compliant. While compilance extensions may use this value for
        customized implementations, implementators should assume that 0 may
        break the program imediatelly (like raise an exception)
    Verbose: int, default=0
        Verbose is recommended to be used as an way to help debug errors.
        But some implementers of the compliance extension to literaly
        return True while doing other checks without warn the user.

    Returns
    -------
    bool
        True means 100% compliant on the context. False may return instead of
        exception based on Tolerance.
    """

    # TODO: implement plugin-like feature, while use this as facade
    # TODO: consider strerr for verbose; but this depends on how we would
    #       test https://docs.pytest.org/en/stable/capture.html
    return True


def get_compliance_extra_rules():
    print('TODO: this is an draft. Improve-me')


def verbose_event(context=None):
    """Method to call when a human enable verbose (MAY EXPOSE DATA INTERNALS)

    Routines like HConteiner()->describe() provide an interface do debug
    not just the program, but data itself. While this is useful when
    developing and or/debugging with example data, in production, with real
    data that are not even from your organization, someone may need to debug
    and see what is breaking.

    verbose_event() (or compliance extension) is one way do to it
    _less wrong_.

    Problem One: what generate this event could leaked some data:

        While an verbose_event is unlikely to allow who is debugging to
        save/export data (if need, other compliance functions could be made),
        it could expose computed results from compliance rules
        (like the reason to deny an action to the user on a more
        sophisticated interface).

        verbose_event() is likely to

    Problem Two: how you extend this function could also leak data:

        Since more often than not verbose_event() is likely to not only be
        used in good faith (or people just testing plugins for your
        compliance extension; and not just this, but on their local machines!)
        and that do exist more recommended ways to catch intentional behavior,
        if compliance extensions BY DEFAULT just log even data not just
        metadata to ask the data contributor what was the in the dataset, your
        solution to protect potential data leak will leak even more sensitive
        data.

    Strong suggestion [Emerson Rocha's opinion]:

        An good approach is (TODO: document better)

    Args:
        context (Any, optional): Extra information. Defaults to None.
    """

    # TODO: implement logger, maybe syslog (Emerson Rocha, 2021-02-26 23:25)

    print("verbose_event", file=sys.stderr)
