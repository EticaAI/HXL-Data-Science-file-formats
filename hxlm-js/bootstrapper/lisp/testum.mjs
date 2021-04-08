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
let example2 = '(+ 1 (- 3 1 ) (+ 1 1 ))'

// let example_str2 = '(🇧🇷 (⚕️ "hospital"))'
console.log('_____example1', example1)
console.log(HDPbLisp.just_testing_parser3(example1))
console.log('')
console.log('')
console.log('')
console.log('_____example2', example2)
console.log(HDPbLisp.just_testing_parser3(example2))
console.log('')
console.log('')
console.log('')
console.log('_____example2 ast_ltr', example2)
console.log(HDPbLisp.ast_ltr(example2))
console.log('_____example2 ast_rtl', example2)
console.log(HDPbLisp.ast_rtl(example2))
console.log('_____example2 ast', example2)
console.log(HDPbLisp.ast(example2))
console.log('evaluate')
console.log(HDPbLisp.evaluate(example2))
console.log('')


// console.log('example_str2', example_str2)
// console.log(HDPbLisp.just_testing_parser3(example_str2))