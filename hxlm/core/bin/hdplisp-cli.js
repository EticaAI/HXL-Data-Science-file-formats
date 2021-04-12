#!/usr/bin/env node
//==============================================================================
//
//         FILE:  hdplisp-cli.js
//
//        USAGE:  hxl2example hxlated-data.hxl my-exported-file.example
//                cat hxlated-data.hxl | hxl2example > my-exported-file.example
//                //Via web, in two different terminals, do it
//                    hug -f bin/hxl2example
//                    ngrok http 8000
//
//  DESCRIPTION:  hxl2example is an example script to create other scripts with
//                some bare minimum command line interface that could work.
//                With exception of external libraries, the hxl2example is
//                meant to be somewhat self-contained one-file executable ready
//                to just be added to the path.
//
//                Hug API can be used to create an ad-hoc web interface to your
//                script. This can be both useful if you are using an software
//                that accepts an URL as data source and you don't want to use
//                this script to save a file locally.
//
//      OPTIONS:  ---
//
// REQUIREMENTS:  - python3
//                    - libhxl (@see https://pypi.org/project/libhxl/)
//                    - hug (https://github.com/hugapi/hug/)
//                    - your-extra-python-lib-here
//                - your-non-python-dependency-here
//         BUGS:  ---
//        NOTES:  ---
//       AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
//      COMPANY:  EticaAI
//      LICENSE:  Public Domain / BSD Zero Clause License
//                SPDX-License-Identifier: Unlicense OR 0BSD
//      VERSION:  v1.0
//      CREATED:  2021-04-10 18:49 UTC
//     REVISION:  ---
//==============================================================================

// Maybe for short term, we do this? https://github.com/dj51d/setuptools-node

// ./hxlm/core/bin/hdplisp-cli.js

console.log('Hello hxlm/core/bin/hdplisp-cli.js!')