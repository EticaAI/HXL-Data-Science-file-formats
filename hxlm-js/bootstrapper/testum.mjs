/**
 * Trivia:
 * - "testum"
 *   - https://en.wiktionary.org/wiki/testum#Latin
 *     - https://en.wiktionary.org/wiki/test#English
 */


// node hxlm-js/bootstrapper/testum.js

console.log('bootstrapper/testum.js')

import { HDPAux }  from './hdp-aux.mjs'
import { HDPLisp }  from './hdplisp.mjs'
import { HDPMiniman }  from './hdp-minimam.mjs'

console.log(HDPMiniman)

// let HDP_DEBUG = true
let bootstrapping = HDPMiniman.bootstrapping()
let ego = HDPAux.quis_sum()

// HDP Language _bootstrapping_ based on you (_ego_)
let hdp = new HDPMiniman(bootstrapping, ego)

// Output the current version of this library
console.log("HDP Miniman version:", hdp.version)

// Output what we can automate for you
console.log("HDPMiniman.EGO :", hdp.EGO)

// This return an quick overview
hdp.explanare().then(console.log).catch(console.error)

// Return the Localization Knowledge Graph, when ready
hdp.explanare('LKG').then(console.log).catch(console.error)

// Return the Vocabulary Knowledge Graph, when ready
hdp.explanare('VKG').then(console.log).catch(console.error)

console.log(HDPMiniman.version)