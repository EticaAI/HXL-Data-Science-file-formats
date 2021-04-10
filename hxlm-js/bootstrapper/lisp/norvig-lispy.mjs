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
 *  - GitHub search by 'lispy' and JavaScript code
 *     - https://github.com/search?l=JavaScript&q=lispy
 *     - Some results
 *       - https://github.com/burtonjb/LispyJS
 *       - https://github.com/kawakami-o3/yaLispy/blob/master/JavaScript/lisp.js
 *       - https://github.com/njlr/mathematical
 *       - https://github.com/breeze4/lispyjs/tree/master/src
 *       - https://github.com/Shimin-Zhang/JS-Lispy
 *       - https://github.com/z5h/zb-lisp
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

import { HDPbLispCorLibrarium } from './cor-librarium.mjs'
const CorLibrarium = HDPbLispCorLibrarium

// Trivia: cōnsuētūdinem, https://en.wiktionary.org/wiki/consuetudo#Latin
const ConsuetudinemLibrarium = Object({

})


function atom(token) {
    // _HDP_DEBUG && console.log('atomzzz', token, Number.isNaN(token))

    if (!isNaN(token)) {
        return Number(token)
    } else {
        return token
    }

    // if (Number.isNaN(token) || (token === '+') || (token === '-')) {
    //     // return String.toString(token)
    //     _HDP_DEBUG && console.log('atom => not numeric, symbol', token)
    //     return token
    // } else {
    //     _HDP_DEBUG && console.log('atom => numeric', token)
    //     return Number(token)
    // }
}

/**
 * http://norvig.com/lispy.html
 */
function evaluate(ast_sxpr, env, constructum) {
    _HDP_DEBUG && console.log('evaluate args', typeof ast_sxpr, ast_sxpr, constructum)

    let env_ = env || { ...CorLibrarium, ...ConsuetudinemLibrarium };
    _HDP_DEBUG && console.log('evaluate env_', env_)

    let constructum_ = constructum || Object({
        'LISP->define': 'define',
        'LISP->if': 'if',
        'LISP->quote': 'QUOTE'
    });
    _HDP_DEBUG && console.log('evaluate builtin_', constructum_)

    if (typeof ast_sxpr === 'number') {
        return ast_sxpr
    }

    if (typeof ast_sxpr === 'string') {
        if (typeof env['symbolum'] !== 'undefined') {
            if (typeof env_[ast_sxpr][ast_sxpr] !== 'undefined') {
                return env_[ast_sxpr][ast_sxpr]
            }
        }
        return env_[ast_sxpr]
    }

    // TODO: this may be a pointer, not a raw string. Fix it
    // if (typeof ast_sxpr === 'string') {
    //     return ast_sxpr
    // }

    if (Array.isArray(ast_sxpr)) {
        // let resultatum = ast_sxpr.map(function(item) {
        //     return evaluate(item, )
        // })

        if (ast_sxpr[0] === constructum_['LISP->define']) {

            console.log('define ast_sxpr', ast_sxpr, ast_sxpr[2])

            // const resultatum = evaluate(ast_sxpr[2], env_)
            const resultatum = ast_sxpr[2]
            env_[ast_sxpr[1]] = resultatum

            // _HDP_DEBUG && console.log('define ' , ast_sxpr[1] , resultatum)
            console.log('DEBUG: define ' , ast_sxpr[1] , ast_sxpr[2], resultatum)

            // For now alwats when defining we will show the messages
            console.log(constructum_['LISP->define'] + ' ' + ast_sxpr[1] , resultatum)
            return resultatum
            // elif x[0] == 'define':           # definition
            //     (_, symbol, exp) = x
            //     env[symbol] = eval(exp, env)

            // throw new EvalError(constructum_['LISP->define'] + ' not implemented... yet');
        }
        if (ast_sxpr[0] === constructum_['LISP->if']) {
            throw new EvalError(constructum_['LISP->if'] + ' not implemented... yet');
        }
        if (ast_sxpr[0] === constructum_['LISP->quote']) {
            return ast_sxpr[1]
            // throw new EvalError(constructum_['LISP->quote'] + ' not implemented... yet');
        }

        // The typical drill

        let resultatum = ast_sxpr.map(function (item) {
            return evaluate(item, env_)
        })
        _HDP_DEBUG && console.log('resultatum', typeof resultatum, resultatum, ast_sxpr)

        let actum = resultatum.shift()
        _HDP_DEBUG && console.log('actum', typeof actum, actum)
        let evaluated = actum.apply(null, resultatum);
        _HDP_DEBUG && console.log('evaluated', evaluated)
        return evaluated
    }

    // if (typeof ast_sxpr === 'string') {
    //     _HDP_DEBUG && console.log('evaluate ast_sxpr === string', ast_sxpr, env_[ast_sxpr], env_)
    //     return env_[ast_sxpr]
    // } else {
    //     _HDP_DEBUG && console.log('nop')
    // }


    // "Evaluate an expression in an environment."
    // if isinstance(x, Symbol):        # variable reference
    //     return env[x]
    // elif isinstance(x, Number):      # constant number
    //     return x
    // elif x[0] == 'if':               # conditional
    //     (_, test, conseq, alt) = x
    //     exp = (conseq if eval(test, env) else alt)
    //     return eval(exp, env)
    // elif x[0] == 'define':           # definition
    //     (_, symbol, exp) = x
    //     env[symbol] = eval(exp, env)
    // else:                            # procedure call
    //     proc = eval(x[0], env)
    //     args = [eval(arg, env) for arg in x[1:]]
    //     return proc(*args)
}

function standard_env() {
    // def standard_env() -> Env:
    // "An environment with some Scheme standard procedures."
    // env = Env()
    // env.update(vars(math)) # sin, cos, sqrt, pi, ...
    // env.update({
    //     '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv,
    //     '>': op.gt, '<': op.lt, '>=': op.ge, '<=': op.le, '=': op.eq,
    //     'abs': abs,
    //     'append': op.add,
    //     'apply': lambda proc, args: proc(* args),
    //     'begin': lambda * x: x[-1],
    //     'car': lambda x: x[0],
    //     'cdr': lambda x: x[1:],
    //     'cons': lambda x, y: [x] + y,
    //     'eq?': op.is_,
    //     'expt': pow,
    //     'equal?': op.eq,
    //     'length': len,
    //     'list': lambda * x: List(x),
    //     'list?': lambda x: isinstance(x, List),
    //     'map': map,
    //     'max': max,
    //     'min': min,
    //     'not': op.not_,
    //     'null?': lambda x: x == [],
    //     'number?': lambda x: isinstance(x, Number),
    //     'print': print,
    //     'procedure?': callable,
    //     'round': round,
    //     'symbol?': lambda x: isinstance(x, Symbol),
    // })
    // return env
}



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

// export { atom, parse_recursive_ltr }
export { parse_recursive_ltr, evaluate }