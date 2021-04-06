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
        return sxpr_norm.split(' ')
    }
}

export { HDPbLisp }