from pkgutil import iter_modules


def _get_plugins():
    """List plugins.
    TODO: not sure if is efficient or may have bugs. But is for debug so ok.
          (fititnt, 2021-02-24 02:25 UTC)

    See
    ---
    - https://stackoverflow.com/questions/48000761
      /list-submodules-of-a-python-module
    - https://docs.python.org/3/library/pkgutil.html

    """
    import hxlm
    for submodule in iter_modules(hxlm.__path__):
        print(submodule.name)
