/**
 * Trivia:
 * - "testum"
 *   - https://en.wiktionary.org/wiki/testum#Latin
 *     - https://en.wiktionary.org/wiki/test#English
 */


// node hxlm-js/bootstrapper/testum.mjs

console.log('bootstrapper/testum.js')

// import { HDPbLisp }  from './hdpb-lisp.mjs'
import { HDPbMiniman, HDPbL10n ,HDPbLisp }  from './hdpb-minimam.mjs'
import { HDPbAux }  from './hdpb-aux.mjs'

console.log(HDPbMiniman)

// let HDP_DEBUG = true
let bootstrapping = HDPbMiniman.bootstrapping()
let ego = HDPbL10n.quis_sum()

// HDP Language _bootstrapping_ based on you (_ego_)
let hdp = new HDPbMiniman(bootstrapping, ego)

// Output the current version of this library
console.log("HDP Miniman version:", hdp.version)

// Output what we can automate for you
console.log("HDPbMiniman.EGO :", hdp.EGO)

// This return an quick overview
hdp.explanare().then(console.log).catch(console.error)

// Return the Localization Knowledge Graph, when ready
hdp.explanare('LKG').then(console.log).catch(console.error)

// Return the Vocabulary Knowledge Graph, when ready
hdp.explanare('VKG').then(console.log).catch(console.error)

console.log(HDPbMiniman.version)