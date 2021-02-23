
# python3 -m pip install https://github.com/EticaAI/HXL-Data-Science-file-formats/archive/main.zip

# TODO: see https://stackoverflow.com/questions/5062793/is-it-possible-to-use-two-python-packages-with-the-same-name  #noqa
# TODO: see https://packaging.python.org/guides/packaging-namespace-packages/  #noqa
# TODO: see https://www.python.org/dev/peps/pep-0420/
# TODO: see https://pawamoy.github.io/posts/plugins-as-python-native-namespace-packages/
# TODO: see https://github.com/napari/napari/issues/139
# @see https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html

# ln -s /workspace/git/EticaAI/HXL-Data-Science-file-formats/hxlm /home/fititnt/.local/lib/python3.8/site-packages/hxlm

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# TODO: this configuration, while somewhat eventually would allow plugins with
#       higher priority, still save o disk on {path}/hxlm and not
#       {path}/hxlm_eticaai (so it could allow several extensions). This
#       eventually will be fixed when I manage to learn more about python
#       internals (fititnt, 2021-02-23 02:56 UTC)
setuptools.setup(
    # using username 'eticaai' to provide some namespace
    # we're not planning to release this on pip (at least not soon)
    # So users would need to install via github.
    # Anyway, tend to be a good idea allow user import different packages
    name="hxlm_eticaai",
    namespace_packages=["hxlm"],
    version="0.7.0",
    author="Emerson Rocha",
    author_email="rocha@ieee.org",
    description="Internal usage. Not production ready. Ignore it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EticaAI/HXL-Data-Science-file-formats",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Typing :: Typed",
        "Topic :: Utilities"
    ],
    # packages=setuptools.find_packages(),
    packages=setuptools.find_namespace_packages(),
    python_requires='>=3.7',
)