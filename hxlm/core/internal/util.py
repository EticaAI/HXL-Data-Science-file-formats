"""hxlm.core.internal.util is (TODO: document)
"""

# from pkgutil import iter_modules
import pkgutil
import hxlm


def _get_submodules():
    """List plugins.
    TODO: not sure if is efficient or may have bugs. But is for debug so ok.
          (fititnt, 2021-02-24 02:25 UTC)

    See
    ---
    - https://stackoverflow.com/questions/48000761
      /list-submodules-of-a-python-module
    - https://docs.python.org/3/library/pkgutil.html

    """
    # import hxlm
    # print('hxlm modules (root)')
    # for submodule in iter_modules(hxlm.__path__):
    #     print(submodule.name)
    #     print(submodule)
    #     # print(submodule.__path__)

    # @see https://stackoverflow.com/questions/1707709
    #      /list-all-the-modules-that-are-part-of-a-python-package

    package = hxlm
    for importer, modname, ispkg in \
        pkgutil.walk_packages(path=package.__path__,
                              prefix=package.__name__+'.',
                              onerror=lambda x: None):
        print(modname)
