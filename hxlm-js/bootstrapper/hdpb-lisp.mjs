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
    sxpr = sxpr.replace('[', '(').replace('{', '('); // {} are aliases to ()
    sxpr = sxpr.replace(']', ')').replace('}', ')'); // [] are aliases to ()
    sxpr = sxpr.replace('(', ' ( ').replace(')', ' ) ')
    sxpr = sxpr.split(' ')

    // First and last items of array will be empty string ''. Clean here
    // TODO: test more this
    let cleaned = sxpr.filter((v) => v != '')
    // console.log('sxpr', sxpr)
    // console.log('cleaned', cleaned)
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

// const _HDP_DEBUG = typeof(HDP_DEBUG) !== 'undefined' && HDP_DEBUG || false
const _HDP_DEBUG = typeof(HDP_DEBUG) !== 'undefined' && HDP_DEBUG || true

/**
 * Initial version based on a ported version from http://norvig.com/lispy.html
 */
function parse_recursive_ltr(sxpr_token, deep) {
    let deep_ = (deep && (deep + 1) || 1)


    _HDP_DEBUG && console.log("\n", '> > parse_recursive_ltr', sxpr_token, deep)
    // console.log('sxpr_token', sxpr_token, typeof sxpr_token, sxpr_token.length)
    // console.log('++++'.length)
    // if (!sxpr_token || sxpr_token.length === 0) {
    if (!sxpr_token) {
        let type_ = typeof sxpr_token
        let value_ = String(sxpr_token)
        throw new Error("EOF ? typeof [" + type_ + '] raw [' + value_ + ']')
    }

    // let deep_ = (deep && (deep + 1) || 1)

    let token = sxpr_token.shift()
    // console.log('>>> token', token, deep_)

    if (token === '(') {
        _HDP_DEBUG && console.log('    ... start')
        let partial = []
        // console.log('>. ',  sxpr_token[0])
        while (sxpr_token[0] !== ')') {
            partial.push(parse_recursive_ltr(sxpr_token, deep_))
            // console.log('sxpr_token.shift', sxpr_token.shift())
            if (typeof sxpr_token.shift() === 'undefined') {
                break
            }
        }
        sxpr_token.shift()  // pop ), if any
        return partial
    } else if (token === ')') {
        throw new Error(") ?")
    } else {
        return atom(token)
    }
}

function atom(token) {
    _HDP_DEBUG && console.log('atom', token)
    if (Number.isNaN(token) || (token === '+') || (token === '-')) {
        // return String.toString(token)
        _HDP_DEBUG && console.log('      ... not numeric, symbol')
        return token
    } else {
        _HDP_DEBUG && console.log('      ... numeric')
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


    static ast(sxpr) {

    }


    static just_testing_parser(sxpr) {
        let sxpr_norm = normalize_input(sxpr)
        return sxpr_norm.split(' ')
    }
    static just_testing_parser2(sxpr) {
        let sxpr_norm = normalize_input(sxpr)
        parse(sxpr_norm)
        return sxpr_norm.split(' ')
    }
    static just_testing_parser3(sxpr) {
        console.log('> just_testing_parser3', sxpr)
        let sxpr_norm = normalize_input(sxpr)
        let sxpr_tokens = tokenize_input(sxpr_norm)
        console.log('sxpr_tokens', sxpr_tokens)
        let parsed = parse_recursive_ltr(sxpr_tokens)
        console.log('parsed', parsed)
        return parsed
    }
}

export { HDPbLisp }