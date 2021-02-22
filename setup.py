import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# python -m pip install -e

setuptools.setup(
    # using username 'eticaai' to provide some namespace
    # we're not planning to release this on pip (at least not soon)
    # So users would need to install via github.
    # Anyway, tend to be a good idea allow user import different packages
    name="hxlm_eticaai",
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
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)