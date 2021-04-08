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

// const HDPbLispCorLibrarium = {

/**
 * Trivia:
 *   - 'mathēmaticam'
 *     - https://en.wiktionary.org/wiki/mathematica#Latin
 */
const MathematicamLibrarium = {
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
    },
    '-': function () {
        if (!arguments || arguments.length == 0) {
            // Error message from LISP-1.5-Programmers-Manual.pdf
            // TODO: we need to define error messages
            throw new SyntaxError('CONDITION NOT SATISFIED IN COMPILED FUNCTION');
        }
        if (arguments.length == 1) return arguments[0];
        let resultatum = 0;
        for (let i = 0; i < arguments.length; i++) {
            resultatum -= arguments[i];
        }
        return resultatum;
    }
}

// b:
//   ATOM:
//   CAR:
//   CDR:
//   COND:
//   CONS:
//   EQ:
//   LAMBDA:
//   PRINT:
//   QUOTE:
//   READ:

const LISPLibrarium = {
    'LISP->ATOM': function () {
        // Error message from LISP-1.5-Programmers-Manual.pdf
        // TODO: we need to define error messages
        throw new SyntaxError('FUNCTION OBJECT HAS NO DEFINITION- APPLY');
    },
    'LISP->CAR': function () {
        // Error message from LISP-1.5-Programmers-Manual.pdf
        // TODO: we need to define error messages
        throw new SyntaxError('FUNCTION OBJECT HAS NO DEFINITION- APPLY');
    },
    'LISP->CDR': function () {
        // Error message from LISP-1.5-Programmers-Manual.pdf
        // TODO: we need to define error messages
        throw new SyntaxError('FUNCTION OBJECT HAS NO DEFINITION- APPLY');
    },
    'LISP->COND': function () {
        // Error message from LISP-1.5-Programmers-Manual.pdf
        // TODO: we need to define error messages
        throw new SyntaxError('FUNCTION OBJECT HAS NO DEFINITION- APPLY');
    },
    'LISP->EQ': function () {
        // Error message from LISP-1.5-Programmers-Manual.pdf
        // TODO: we need to define error messages
        throw new SyntaxError('FUNCTION OBJECT HAS NO DEFINITION- APPLY');
    },
    'LISP->LAMBDA': function () {
        // Error message from LISP-1.5-Programmers-Manual.pdf
        // TODO: we need to define error messages
        throw new SyntaxError('FUNCTION OBJECT HAS NO DEFINITION- APPLY');
    },
    'LISP->QUOTE': function () {
        // Error message from LISP-1.5-Programmers-Manual.pdf
        // TODO: we need to define error messages
        throw new SyntaxError('FUNCTION OBJECT HAS NO DEFINITION- APPLY');
    },
}

// const HDPbLispCorLibrarium = { ...MathematicamLibrarium, ...LISPLibrarium }
const HDPbLispCorLibrarium = {
    '+': MathematicamLibrarium['+'],
    // Trivia: 'summam': https://en.wiktionary.org/wiki/summa#Latin
    'summam': MathematicamLibrarium['+'],
    'lat->summam': MathematicamLibrarium['+'],

    '-': MathematicamLibrarium['-'],
    // Trivia: 'subtractiōnem': https://en.wiktionary.org/wiki/subtractio#Latin
    'subtractionem': MathematicamLibrarium['-'],
    'lat->subtractionem': MathematicamLibrarium['-'],

    // TODO: find good names in Latin for Lisp bare dictionary
    'ATOM': LISPLibrarium['LISP->ATOM'],
    'CAR': LISPLibrarium['LISP->CAR'],
    'CDR': LISPLibrarium['LISP->CDR'],
    'COND': LISPLibrarium['LISP->COND'],
    'EQ': LISPLibrarium['LISP->EQ'],
    'LAMBDA': LISPLibrarium['LISP->LAMBDA'],
    'QUOTE': LISPLibrarium['LISP->QUOTE']
}

export { HDPbLispCorLibrarium, MathematicamLibrarium, LISPLibrarium }