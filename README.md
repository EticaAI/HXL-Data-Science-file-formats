# Data Science files exported from HXL (The Humanitarian Exchange Language)
**[public draft][Proof of concept] Common file formats used for Data Science
exported from HXL (The Humanitarian Exchange Language)**

---

<!-- TOC depthFrom:2 -->

- [The HXL-Data-Science-file-formats main focus](#the-hxl-data-science-file-formats-main-focus)
    - [`HXL2` Command line tools](#hxl2-command-line-tools)
    - [Vocabulary/Taxonomies](#vocabularytaxonomies)
- [Additional Guides](#additional-guides)
    - [Command line tools overview](#command-line-tools-overview)
    - [Alternatives to preview spreadsheets with over 1.000.000 rows](#alternatives-to-preview-spreadsheets-with-over-1000000-rows)

<!-- /TOC -->

---

## The HXL-Data-Science-file-formats main focus

### `HXL2` Command line tools
- See folder [bin/](bin/)
- See discussions at
  - <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues>
  - <https://github.com/HXL-CPLP/forum/issues/52>

At the moment, beyond the [`hxl2example`](bin/hxl2example), this project does
not have usable command line tools to automate work.

### Vocabulary/Taxonomies
- <https://docs.google.com/spreadsheets/d/1vFkBSharAEg5g5K2u_iDLCBvpWWPqpzC1hcL6QpFNZY/edit#gid=1297379331>

This HXL Spreadsheet have live information about this proof of concept.

## Additional Guides

### Command line tools overview
- [guides/command-line-tools-overview.sh](guides/command-line-tools-overview.sh)

Here there is an an quick overview of different command line tools that
worth at least mention, in special if are dealing with raw  formats already not
HXLated.

### Alternatives to preview spreadsheets with over 1.000.000 rows
- [guides/preview-huge-ammount-of-data.md](guides/preview-huge-ammount-of-data.md)

90% of the time 1.000.000 rows is likely to be enough even if you are dealing
with data science projects. So it means that there is no need to use command
line tools or use more complex solutions, like import to an database or pay for
enterprise solutions.

This guide if when you need to go over these limits without change too much your
tools.

# License

[![Public Domain Dedication](img/public-domain.png)](UNLICENSE)

The [EticaAI](https://github.com/EticaAI) has dedicated the work to the
[public domain](UNLICENSE) by waiving all of their rights to the work worldwide
under copyright law, including all related and neighboring rights, to the extent
allowed by law. You can copy, modify, distribute and perform the work, even for
commercial purposes, all without asking permission.
