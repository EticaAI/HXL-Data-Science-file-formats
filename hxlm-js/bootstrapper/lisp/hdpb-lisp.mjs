// console.log('bootstrapper/hdplisp.mjs (draft)')

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


function normalize_input(sxpr) {
    sxpr = sxpr.replace('[', '(').replace('{', '(');
    sxpr = sxpr.replace(']', ')').replace('}', ')');
    sxpr = sxpr.replace('( ', '(').replace(' )', ')')
    return sxpr
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

// https://stackoverflow.com/questions/36527642/difference-between-codepointat-and-charcodeat

function parse(sxpr) {
    let idx = 0
    let point = sxpr.codePointAt(idx)
    let level = 0
    let col = 0
    let ast = []
    let ast_bloc = []
    let token = ''
    let pointstr_last = ''
    while (point) {
        let pointstr = String.fromCodePoint(point)
        // let pointstr_last = String.fromCodePoint(sxpr.codePointAt(idx))
        idx += 1
        if (pointstr === '(') {
            level += 1
        }
        if (pointstr === ')') {
            ast.push(ast_bloc)
            ast_bloc = []
            level -= 1
        }
        // TODO: deal with strings and symbols with spaces
        if (pointstr === ' ') {
            col += 1
            // let pointstr_last = String.fromCodePoint(sxpr.codePointAt(idx))
            ast_bloc.push(pointstr_last.replace('(', '').replace(')', ''))
            pointstr_last = ''
            // continue
        }

        pointstr_last += pointstr.replace(' ', '')
        console.log(level, col, pointstr, ast_bloc, ast)
        point = sxpr.codePointAt(idx)
    }

}

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

    /**
     * @deprecated to be removed
     */
    static just_testing_parser(sxpr) {
        let sxpr_norm = normalize_input(sxpr)
        return sxpr_norm.split(' ')
    }

    /**
     * @deprecated to be removed
     */
    static just_testing_parser2(sxpr) {
        let sxpr_norm = normalize_input(sxpr)
        parse(sxpr_norm)
        return sxpr_norm.split(' ')
    }

    /**
     * @deprecated to be removed
     */
    static just_testing_parser3(sxpr) {
        // console.log('just_testing_parser3', sxpr)
        let sxpr_norm = normalize_input(sxpr)
        let sxpr_tokens = tokenize_input(sxpr_norm)
        // console.log('sxpr_tokens', sxpr_tokens)
        let parsed = parse_recursive_ltr(sxpr_tokens)
        // console.log('parsed', parsed)
        return parsed
    }
}

export { HDPbLisp }