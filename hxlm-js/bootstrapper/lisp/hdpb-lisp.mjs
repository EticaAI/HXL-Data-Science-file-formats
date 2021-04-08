/**
 * @see https://github.com/informatimago/lisp-1-5/blob/master/LISP-1.5-Programmers-Manual.pdf
 * @see http://www.softwarepreservation.org/projects/LISP/lisp15_family
 */


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


import { parse_recursive_ltr, evaluate } from './norvig-lispy.mjs'
import { tokenize_input, normalize_input } from './util.mjs'

const _HDP_DEBUG = typeof (HDP_DEBUG) !== 'undefined' && HDP_DEBUG || false
// const _HDP_DEBUG = typeof (HDP_DEBUG) !== 'undefined' && HDP_DEBUG || true

/**
 * Placeholder
 */
class HDPbLisp {
    version = "0.8.5"


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

    static evaluate(sxpr, optionem){
        let parsed = this.ast(sxpr, optionem)
        let resultatum = evaluate(parsed)
        return resultatum
    }

    // /**
    //  * @deprecated to be removed
    //  */
    // static just_testing_parser(sxpr) {
    //     let sxpr_norm = normalize_input(sxpr)
    //     return sxpr_norm.split(' ')
    // }

    // /**
    //  * @deprecated to be removed
    //  */
    // static just_testing_parser2(sxpr) {
    //     let sxpr_norm = normalize_input(sxpr)
    //     parse(sxpr_norm)
    //     return sxpr_norm.split(' ')
    // }

    // /**
    //  * @deprecated to be removed
    //  */
    // static just_testing_parser3(sxpr) {
    //     // console.log('just_testing_parser3', sxpr)
    //     let sxpr_norm = normalize_input(sxpr)
    //     let sxpr_tokens = tokenize_input(sxpr_norm)
    //     // console.log('sxpr_tokens', sxpr_tokens)
    //     let parsed = parse_recursive_ltr(sxpr_tokens)
    //     // console.log('parsed', parsed)
    //     return parsed
    // }
}

export { HDPbLisp }