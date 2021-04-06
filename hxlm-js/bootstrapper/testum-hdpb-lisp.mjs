// console.log('bootstrapper/testum-hdpb-lisp.mjs (draft)')

// node hxlm-js/bootstrapper/testum-hdpb-lisp.mjs

import { HDPbLisp } from './hdpb-lisp.mjs'

console.log(HDPbLisp.just_testing_parser('( + 1 1 )'))
console.log(HDPbLisp.just_testing_parser('(+ 1 (- 3 1 ))'))
console.log(HDPbLisp.just_testing_parser('(+ 1 (- 3 1 ) (+ 1 1 ))'))

console.log(HDPbLisp.just_testing_parser2('( + 1 1 )'))
console.log(HDPbLisp.just_testing_parser2('(+ 1 (- 3 1 ))'))
console.log(HDPbLisp.just_testing_parser2('(+ 1 (- 3 1 ) (+ 1 1 ))'))