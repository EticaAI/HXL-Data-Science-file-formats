/**
 * @file    hxlm-js/bootstrapper/lisp/cor-librarium.mjs
 * @license Unlicense
 * SPDX-License-Identifier: Unlicense
 *
 * Trivia:
 *   - "cor"
 *     - https://en.wiktionary.org/wiki/cor#Latin
 *   - "librārium"
 *     - https://en.wiktionary.org/wiki/librarium#Latin
 */

HDPbLispCorLibrarium = {
    '+': function () {
        if (!arguments || arguments.length == 0) {
            // Error message from LISP-1.5-Programmers-Manual.pdf
            // TODO: we need to define error messages
            throw new SyntaxError('CONDITION NOT SATISFIED IN COMPILED FUNCTION');
        }
        if (arguments.length == 1) return arguments[0];
        let resultatum = 0;
        for (let i = 0; i < arguments.length; i++) {
            resultatum += arguments[i];
        }
        return resultatum;
    }
}