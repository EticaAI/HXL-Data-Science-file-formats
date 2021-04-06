// console.log('bootstrapper/testum-hdpb-lisp.mjs (draft)')

// node hxlm-js/bootstrapper/testum-hdpb-lisp.mjs

import { HDPbLisp } from './hdpb-lisp.mjs'

// console.log(HDPbLisp.just_testing_parser('( + 1 1 )'))
// console.log(HDPbLisp.just_testing_parser('(+ 1 (- 3 1 ))'))
// console.log(HDPbLisp.just_testing_parser('(+ 1 (- 3 1 ) (+ 1 1 ))'))

// console.log(HDPbLisp.just_testing_parser2('( + 1 1 )'))
// console.log(HDPbLisp.just_testing_parser2('(+ 1 (- 3 1 ))'))

let example_nil = '()'
console.log('example_nil', example_nil)
console.log(HDPbLisp.just_testing_parser2(example_nil))
console.log('')
console.log('')
let example1 = '( + 1 1 )'
console.log('example1', example1)
console.log(HDPbLisp.just_testing_parser2(example1))
console.log('')
console.log('')
let example2 = '(+ 1 (- 3 1 ) (+ 1 1 ))'
console.log('example2', example2)
console.log(HDPbLisp.just_testing_parser2(example2))