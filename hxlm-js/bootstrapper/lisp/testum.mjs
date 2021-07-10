// console.log('bootstrapper/lisp/testum.mjs (draft)')

// node hxlm-js/bootstrapper/lisp/testum.mjs

import { HDPbLisp } from './hdpb-lisp.mjs'

// let example_nil = '()'
// console.log('example_nil', example_nil)
// console.log(HDPbLisp.just_testing_parser2(example_nil))
// console.log('')
// console.log('')
// let example1 = '(+ 1 2 3 4 5 6 7 8 9)'
// console.log('example1', example1)
// console.log(HDPbLisp.just_testing_parser2(example1))
// console.log('')
// console.log('')
// let example2 = '(+ 1 (- 3 1 ) (+ 1 1 ))'
// console.log('example2', example2)
// console.log(HDPbLisp.just_testing_parser2(example2))


// // https://stackoverflow.com/questions/21397316/split-javascript-string-into-array-of-codepoints-taking-into-account-surrogat

// let example_str1 = '(⚕️ "hospital")'
// console.log('example_str1', example_str1)
// console.log(HDPbLisp.just_testing_parser2(example_str1))
// console.log('')
// let example_str2 = '(🇧🇷 (⚕️ "hospital"))'
// console.log('example_str2', example_str2)
// console.log(HDPbLisp.just_testing_parser2(example_str2))

// console.log('')
// console.log('')
// console.log('just_testing_parser3')

// console.log('')
// console.log('')
// console.log('')

let example1 = '(+ 1 2 3 4 5 6 7 8 9)'
let example1_lat = '(summam 1 2 3 4 5 6 7 8 9)'
let example2 = '(+ 1 (- 3 1 ) (+ 1 1 ))'

console.log('_____example1 ast', example1)
console.log(HDPbLisp.ast(example1))
console.log('_____example1 evaluate', example1)
console.log(HDPbLisp.evaluate(example1))

console.log('_____example1_lat ast', example1_lat)
console.log(HDPbLisp.ast(example1_lat))
console.log('_____example1_lat evaluate', example1_lat)
console.log(HDPbLisp.evaluate(example1_lat))
console.log('')
console.log('')
// console.log('_____example2 ast_ltr', example2)
// console.log(HDPbLisp.ast_ltr(example2))
// console.log('_____example2 ast_rtl', example2)
// console.log(HDPbLisp.ast_rtl(example2))
console.log('_____example2 ast', example2)
console.log(HDPbLisp.ast(example2))
console.log('evaluate')
console.log(HDPbLisp.evaluate(example2))
console.log('')

console.log('_____', '(identicum? ' + example2 + ' ' + example2 + ')')
console.log(HDPbLisp.evaluate('(identicum? ' + example2 + ' ' + example2 + ')'))
console.log('_____', '(identicum? ' + example1 + ' ' + example2 + ')')
console.log(HDPbLisp.evaluate('(identicum? ' + example1 + ' ' + example2 + ')'))
console.log('')
console.log('_____', '(non-identicum? ' + example1 + ' ' + example2 + ')')
console.log(HDPbLisp.evaluate('(non-identicum? ' + example1 + ' ' + example2 + ')'))
console.log('')

// console.log('')
// HDPbLisp.REPL()
// console.log(HDPbLisp.ast(example1_lat))
// console.log('example_str2', example_str2)
// console.log(HDPbLisp.just_testing_parser3(example_str2))