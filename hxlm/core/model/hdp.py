"""hxlm.core.model.hdp contains HDP class

This is used by the HDP Declarative Programming Command Line Interface


Copyleft 🄯 2021, Emerson Rocha (Etica.AI) <rocha@ieee.org>
License: Public Domain / BSD Zero Clause License
SPDX-License-Identifier: Unlicense OR 0BSD
"""


class HDP:
    """Class used by HDP Declarative Programming Command Line Interface
    """

    def __init__(self, hdp_entry_point: str = None,
                 yml_string: str = None,
                 json_string: str = None
                 ):
        """
        Constructs all the necessary attributes for the HDPCLI object.
        """

        if hdp_entry_point:
            self._prepare_from_entry_point(hdp_entry_point)
        if json_string:
            self._prepare_from_json_string(json_string)
        if yml_string:
            self._prepare_from_entry_point(yml_string)

    def _prepare_from_entry_point(self, hdp_entry_point):
        pass

    def _prepare_from_json_string(self, json_string):
        pass

    def _prepare_from_yml_string(self, hdp_yml_string):
        pass
