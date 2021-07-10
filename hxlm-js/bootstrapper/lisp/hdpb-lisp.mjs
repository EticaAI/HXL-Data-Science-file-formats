/**
 * @see https://github.com/informatimago/lisp-1-5/blob/master/LISP-1.5-Programmers-Manual.pdf
 * @see http://www.softwarepreservation.org/projects/LISP/lisp15_family
 */


// LISP-1 or LISP-2 ? http://ergoemacs.org/emacs/lisp1_vs_lisp2.html
// console.log('bootstrapper/lisp/hdplisp.mjs (draft)')

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
//   L:


import { parse_recursive_ltr, evaluate } from './norvig-lispy.mjs'
import { tokenize_input, normalize_input } from './util.mjs'

import { HDPbLispCorLibrarium } from './cor-librarium.mjs'
// const CorLibrarium = HDPbLispCorLibrarium

// // Trivia: cōnsuētūdinem, https://en.wiktionary.org/wiki/consuetudo#Latin
// const ConsuetudinemLibrarium = Object({

// })

const _HDP_DEBUG = typeof (HDP_DEBUG) !== 'undefined' && HDP_DEBUG || false
// const _HDP_DEBUG = typeof (HDP_DEBUG) !== 'undefined' && HDP_DEBUG || true


// https://stackoverflow.com/questions/34550890/how-to-detect-if-script-is-running-in-browser-or-in-node-js/48536927
// https://github.com/flexdinesh/browser-or-node
// https://github.com/jsdom/jsdom
const isBrowser = typeof window !== 'undefined' && typeof window.document !== 'undefined';
// const isNode = !isBrowser

// import { createRequire } from 'module';
// const require = createRequire(import.meta.url);

// if (!isBrowser) {
//     import { createRequire } from 'module';
//     const require = createRequire(import.meta.url);
//     const NodeREPL = require('repl');
// }


class HDPbLisp {
    version = "0.9.0"


    /**
     * HDPLisp Abstract syntax three with RTL format
     *
     * Trivia:
     *  - https://en.wikipedia.org/wiki/Right-to-left
     *  - https://en.wikipedia.org/wiki/Left-to-right
     *     - as 2021-04-06, this does not _even_ have dedicated Wikipedia page
     *
     * @param   {String}   sxpr      Input string
     * @param   {Object}   optionem  Object with booleans to explicit define
     *                               the source input
     *                               {
     *                                  lrt: false,
     *                                  rlt: true
     *                               }
     *                               ltr: Left-to-right? (like Lingua Latina?)
     *                               rtl: Right-to-left? (like Imperial Aramaic?)
     * @returns {Array}
     */
    static ast(sxpr, optionem) {
        // As a way of paying tribute to Arabic numbers, if a user does not
        // specify which AST he wants, we will provide the RTL.
        // As of today (2021-04-06) there is also an interest that hashing
        // algorithms also use RTL as a reference.
        // (Emerson Rocha, 2021-04-06 18:37 UTC)
        return this.ast_rtl(sxpr, optionem)
    }

    /**
     * HDPLisp Abstract syntax three with LTR format
     *
     * @param   {String}   sxpr      Input string
     * @param   {Object}   optionem  Object with booleans to explicit define
     *                               the source input
     *                               {
     *                                  lrt: false,
     *                                  rlt: true
     *                               }
     *                               ltr: Left-to-right? (like Lingua Latina?)
     *                               rtl: Right-to-left? (like Imperial Aramaic?)
     * @returns {Array}
     */
    static ast_ltr(sxpr, optionem) {
        let res = tokenize_input(sxpr)
        // TODO: implement optionem. In special if the initial token is not
        //       already on the text directin the user wants
        let resultatum = parse_recursive_ltr(res)
        return resultatum
    }

    /**
     * HDPLisp Abstract syntax three with RTL format
     *
     * Trivia:
     *  - https://en.wikipedia.org/wiki/Right-to-left
     *  - https://en.wikipedia.org/wiki/Left-to-right
     *     - as 2021-04-06, this does not _even_ have dedicated Wikipedia page
     *
     * @param   {String}   sxpr      Input string
     * @param   {Object}   optionem  Object with booleans to explicit define
     *                               the source input
     *                               {
     *                                  lrt: false,
     *                                  rlt: true
     *                               }
     *                               ltr: Left-to-right? (like Lingua Latina?)
     *                               rtl: Right-to-left? (like Imperial Aramaic?)
     * @returns {Array}
     */
    static ast_rtl(sxpr, optionem) {

        // TODO: ast_rtl
        return this.ast_ltr(sxpr, optionem)
    }

    static evaluate(sxpr, optionem) {
        let parsed = this.ast(sxpr, optionem)
        let resultatum = evaluate(parsed)
        return resultatum
    }

    /**
     * https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
     * https://davidwells.io/snippets/forcing-async-functions-to-sync-in-node
     */
    static REPL() {
        if (!isBrowser) {
            // https://nodejs.org/api/repl.html
            // Unsafe, and also break when looking via brower
            // @see https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/18#issuecomment-816866000
            const msg = 'message';
            require('repl').start('HDPLisp> ')
        }
    }
}


/**
 * @example
 *   const LispVM1 = new HDLbLispMachinamSimulatum()
 *   LispVM1.evaluate('(+ 1 2 )')
 */
class HDLbLispMachinamSimulatum {

    // Trivia: librārium, https://en.wiktionary.org/wiki/librarium#Latin
    librarium = null
    // @example
    // librarium = {
    //    '+': function(a, b) {return "..."}, 
    //    '-': function(a, b) {return "..."},
    //    symbolum: {
    //        'sym1': "my value",
    //        'sym3': "my value"
    //}
    //

    // Trivia: cōnstrūctum, https://en.wiktionary.org/wiki/constructus#Latin
    constructum = Object({
        'LISP->define': 'define',
        'LISP->if': 'if',
        'LISP->quote': 'quote'
    });

    constructor(optionem) {


        if (typeof optionem !== 'undefined' && optionem.librarium) {

            // TODO: while we do not document that this is a safe method to
            //       do deep copy without changing the upper level, we should
            //       at least when initializing a new VM, do a copy of entire
            //       first level
            //
            // TODO: do a deep copy for optionem.librarium.symbolum
            this.librarium = Object.assign({}, optionem.librarium)
            // this.librarium = optionem.librarium
        } else {
            this.librarium = this.corLibrarium()
        }
        // // Trivia: cōnsuētūdinem, https://en.wiktionary.org/wiki/consuetudo#Latin
        // const ConsuetudinemLibrarium = Object({

        // })
    }

    corLibrarium() {

        let resultum = HDPbLispCorLibrarium
        resultum['symbolum'] = Object()
        // https://en.wiktionary.org/wiki/symbolum#Latin

        return HDPbLispCorLibrarium
    }

    evaluate(sxpr) {
        // const Object({

        // })
        HDPbLisp.evaluate(sxpr)
        const ast_sxpr = HDPbLisp.ast(sxpr)
        // import { evaluate } from './norvig-lispy.mjs'
        const resultatum = evaluate(ast_sxpr, this.librarium, this.constructum)

        return resultatum
    }
}

export { HDPbLisp, HDLbLispMachinamSimulatum }