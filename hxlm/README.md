# About hxlm-eticaai

> TODO: update this description from `hxlm-eticaai` to `hdp-toolchain`
> (Emerson Rocha, 2021-04-01 17:09 UTC)

hxlm-eticaai is an working draft. Some internal notes:

- `hxlm.core`: on a ideal scenario, would be a place with both functions that
  are either useful for basic functionality for other data classes and
  functions.
    - if have to be take political decisions (think anything like use `yes`
      for boolean truthy and `no` for boolean false; good example are
      country/territory names)
- `hxlm.??_` (where "??" is an ISO_3166-1 alpha-2):
    - What is "??"? See https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    - "??_" works as an prefix. Users are encoraged to use user-assigned codes
      like AA, QM to QZ, XA to XZ, and ZZ.
- `hxlm.xz_eticaai`: is an namespace by Etica.AI.
- `hxlm.xl_por`: xl_por (preffix XL) is an example of drafted plugins for
  portuguese language. Local customizations could fork `xl_por` to `xk_por`

## About prefixes
### Etica.AI guidelines (optional)

- Published code, both on places like GitHub or Python Package Index (PyPI)
  should not automatically be trusted.
    - This often actually does not means developers acting in bad faith, but
      human error.
    - Depending of your
      [threat model](https://en.wikipedia.org/wiki/Threat_model) please ask
      someone to review code and maybe even copy an paste an private copy.
- Etica.AI is likely to publish early drafts (or working drafts) prefixed with
  `XA` when the code is based on public documentation on how the organization
  would behave.
  - `XA` prefixes should not be considered "official". If you work with such
    organization please ask if you can use EticaAI code or if they already
    have private forks
  - Individuals with valid credentials can ask Etica.AI to remove code, even
    `XA` prefixed.
- If you work within the namespace-related organization:
  - Use the country prefix, not an user asigned-prefix (if you organization
    is not transnational). If you are not yet authorized to make decisions,
    just make comments in the source code.
  - If the organization is transnational, consider atleast `XA`
- Do not publish prefix with `AA` (but you can use for internal use)
  - Eventually prefixes with `AA` may be coded to have even higher priority
    over any other except core.
  - The `ZZ` also is likely to have lower priority.


## Usage

Not well documented yet. See `hxlm-tests.py`.

---
<!--

This folder have an very early draft used by
[/bin/hxlquickmeta](../hxlquickmeta).

The idea is eventually abstract more what was bootstraped on
EticaAI-Data_HXL-Data-Science-file-formats
<https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1066910203>
simmilar to what libraries like Pandas and Numpy do it.

- TODO: Look at other abstractions beyond numpy

> https://numpy.org/doc/stable/user/basics.rec.html
> Users looking to manipulate tabular data, such as stored in csv files, may
find other pydata projects more suitable, such as xarray, pandas, or DataArray.
These provide a high-level interface for tabular data analysis and are better
optimized for that use. For instance, the C-struct-like memory layout of
structured arrays in numpy can lead to poor cache behavior in comparison.


>> https://github.com/pydata/xarray

> Xarray introduces labels in the form of dimensions, coordinates and attributes
on top of raw NumPy-like arrays, which allows for a more intuitive, more
concise, and less error-prone developer experience. The package includes a
large and growing library of domain-agnostic functions for advanced analytics
and visualization with these data structures.

>> Xarray was inspired by and borrows heavily from pandas, the popular data 
analysis package focused on labelled tabular data. It is particularly tailored
to working with netCDF files, which were the source of xarray's data model,
and integrates tightly with dask for parallel computing.

- https://medium.com/pangeo/thoughts-on-the-state-of-xarray-within-the-broader-scientific-python-ecosystem-5cee3c59cd2b

> benchmark https://github.com/pydata/xarray/issues/2799


>> netCDF

- https://www.unidata.ucar.edu/software/netcdf/examples/files.html


>> xarrays
> What is your approach to metadata?
> http://xarray.pydata.org/en/stable/faq.html#approach-to-metadata
> We are firm believers in the power of labeled data! In addition to dimensions and coordinates, xarray supports arbitrary metadata in the form of global (Dataset) and variable specific (DataArray) attributes (attrs).
> 
> Automatic interpretation of labels is powerful but also reduces flexibility. With xarray, we draw a firm line between labels that the library understands (dims and coords) and labels for users and user code (attrs). For example, we do not automatically interpret and enforce units or CF conventions. (An exception is serialization to and from netCDF files.)
> 
> An implication of this choice is that we do not propagate attrs through most operations unless explicitly flagged (some methods have a keep_attrs option, and there is a global flag for setting this to be always True or False). Similarly, xarray does not check for conflicts between attrs when combining arrays and datasets, unless explicitly requested with the option compat='identical'. The guiding principle is that metadata should not be allowed to get in the way.

-->