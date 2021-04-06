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

/**
 * Initial version based on a ported version from http://norvig.com/lispy.html
 */
function parse_recursive_ltr(sxpr_token) {
    if (!sxpr_token || sxpr_token.lenght == 0) {
        throw "EOF ?"
    }

    let token = sxpr_token.pop()

    if (token === '(') {
        parts = []
        while (sxpr_token[0] !== ')') {
            parts.push(parse_recursive_ltr())
        }
        sxpr_token.pop()
        return parts
    } else if (token === ')') {
        throw ") ?"
    } else {
        return atom(sxpr_token)
    }
}

function atom(token) {
    if (Number.isNaN(token)) {
        return String.toString(token)
    } else {
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
        let sxpr_norm = normalize_input(sxpr)
        let sxpr_tokens = tokenize_input(sxpr_norm)
        console.log('sxpr_tokens', sxpr_tokens)
        let parsed = parse_recursive_ltr(sxpr_tokens)
        console.log('parsed', parsed)
        return parsed
    }
}

export { HDPbLisp }