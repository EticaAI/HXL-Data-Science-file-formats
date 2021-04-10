/**
 * @file    hxlm-js/bootstrapper/lisp/util.mjs
 * @license Unlicense
 * SPDX-License-Identifier: Unlicense
 */


const _HDP_DEBUG = typeof (HDP_DEBUG) !== 'undefined' && HDP_DEBUG || false
// const _HDP_DEBUG = typeof (HDP_DEBUG) !== 'undefined' && HDP_DEBUG || true

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

    // sxpr = sxpr.replace("'(", "QUOTE(")

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

export {tokenize_input, normalize_input}