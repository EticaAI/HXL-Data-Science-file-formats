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
function parse_blocks(sxpr) {

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
}

export { HDPbLisp }