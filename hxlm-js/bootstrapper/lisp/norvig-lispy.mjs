/**
 * 
 * This file contains some bare minimum port of S-expressions to run on
 * JavaScript and directly is based on Peter Norvig work Lispy
 * (not yet Lispy2) to allow boostrap early work on hdpb-lisp (HDPLisp).
 * This is likely to be rewriten on future (if not because of license, by
 * functionality) but at the moment it's easier do do something.
 *
 * See:
 *  - '(How to Write a (Lisp) Interpreter (in Python))'
 *     - http://norvig.com/lispy.html
 *  - '(An ((Even Better) Lisp) Interpreter (in Python))'
 *     - http://norvig.com/lispy2.html
 *
 * License of this file
 *   Peter Norvig does not have a clear license, neither most of dozens of
 *   (mostly) incomplete ports of his work to other languages.
 *   For sake of license with something, as this date of 2021-04-07
 *   Emerson Rocha will label it as 'Public Domain dedication',
 *   list names of people who contribute per function. If someone do have
 *   complaints on future, just contact-me and (if need), the entire file
 *   either will be removed. Note that the hxlm-js is public domain dedication
 *   
 *
 * @license Unlicense
 * SPDX-License-Identifier: Unlicense
 */


const _HDP_DEBUG = typeof (HDP_DEBUG) !== 'undefined' && HDP_DEBUG || false
// const _HDP_DEBUG = typeof (HDP_DEBUG) !== 'undefined' && HDP_DEBUG || true

/**
 * Initial version based on a ported version from http://norvig.com/lispy.html
 */
function parse_recursive_ltr(tokens, deep) {
    let deep_ = (deep && (deep + 1) || 1)
    let prefix_ = "> ".repeat(deep_)


    _HDP_DEBUG && console.log("\n" + prefix_ + 'parse_recursive_ltr', deep, tokens)
    // console.log('tokens', tokens, typeof tokens, tokens.length)
    // console.log('++++'.length)
    // if (!tokens || tokens.length === 0) {
    // if (!tokens) {
    if (!tokens || tokens.length === 0) {
        let type_ = typeof tokens
        let value_ = String(tokens)
        throw new Error("EOF ? typeof [" + type_ + '] raw [' + value_ + ']')
    }

    // let deep_ = (deep && (deep + 1) || 1)

    let token = tokens.shift()
    _HDP_DEBUG && console.log(prefix_ + '... token', token)
    // console.log('>>> token', token, deep_)

    if (token === '(') {
        _HDP_DEBUG && console.log(prefix_ + '... start')
        let L = []
        // console.log('>. ',  tokens[0])
        while (tokens[0] !== ')') {
            L.push(parse_recursive_ltr(tokens, deep_))
            _HDP_DEBUG && console.log('... while ... tokens', tokens)
            // console.log('tokens.shift', tokens.shift())
            _HDP_DEBUG && console.log(prefix_ + '... looping, L now: ', L, ', tokens:', tokens)
            // if (typeof tokens.shift() === 'undefined') {
            //     _HDP_DEBUG && console.log(prefix_ + '... break')
            //     break
            // }
        }
        _HDP_DEBUG && console.log('... end while ... tokens', tokens)
        tokens.shift()  // pop ), if any
        return L
    } else if (token === ')') {
        throw new Error(") ?")
    } else {
        return atom(token)
    }
}

function atom(token) {
    // _HDP_DEBUG && console.log('atom', token)
    if (Number.isNaN(token) || (token === '+') || (token === '-')) {
        // return String.toString(token)
        _HDP_DEBUG && console.log('atom => not numeric, symbol', token)
        return token
    } else {
        _HDP_DEBUG && console.log('atom => numeric', token)
        return Number(token)
        // if (Number.i(token)) {
        //     return String.toString(token)
        // }
    }
    // if (Number.isInteger(token)) {
    //     parseInt(token)
    // }
}

function tokenize_input(sxpr) {
    // TODO: deal with strings in spaces
    sxpr = sxpr.replace(/\[/g, '(').replace(/\{/g, '('); // {} are aliases to ()
    sxpr = sxpr.replace(/\]/g, ')').replace(/\}/g, ')'); // [] are aliases to ()
    sxpr = sxpr.replace(/\(/g, ' ( ').replace(/\)/g, ' ) ')
    // console.log('oioioi antes, ', sxpr)
    sxpr = sxpr.split(' ')

    // console.log('oioioi, ', sxpr)

    // First and last items of array will be empty string ''. Clean here
    // TODO: test more this
    let cleaned = sxpr.filter((v) => v != '')
    // console.log('sxpr', sxpr)
    // console.log('cleaned', cleaned)
    // return sxpr
    return cleaned
}

// export { atom, parse_recursive_ltr }
export { parse_recursive_ltr }