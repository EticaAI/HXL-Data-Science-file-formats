// console.log('bootstrapper/hdp-minimam.mjs')

// TODO: extract some parts created on this another project here
//       - https://github.com/fititnt/ais-ethics-tags/blob/master/assets
//         /js/ais-ethics-tags.js

// TODO: learn modern javascript, without transpile all the things. To read:
//       - https://blog.rocketseat.com.br/as-melhores-features-do-es6-es7-e-es8/
//       - https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API/Using_Fetch
//       - https://stackoverflow.com/questions/41715994/how-to-document-ecma6-classes-with-jsdoc
//       - https://jsdoc.app/
//       - https://jsdoc.app/howto-es2015-classes.html
//       - https://google.github.io/styleguide/jsguide.html
//       (Emerson Rocha, 2021-04-03 12:57 UTC)

// TODO: More stuff to do a quick look
//       - https://tools.ietf.org/html/rfc7517
//       - https://www.w3.org/TR/WebCryptoAPI/#dfn-JsonWebKey
//       - https://www.w3.org/TR/WebCryptoAPI/#SubtleCrypto-method-verify
//       - https://www.w3.org/TR/WebCryptoAPI/#algorithm-overview

// TODO: crypto stuff:
//       - https://github.com/openpgpjs/openpgpjs#security-recommendations
//       - https://github.com/openpgpjs/openpgpjs/wiki/Cure53-security-audit

// let HDP_DEBUG = true

// import { HDPAux } from './hdp-aux.mjs'
// import { HDPi18n } from './hdp-i18n.mjs'
import { HDPbL10n } from './hdpb-l10n.mjs'
import { HDPbLisp } from './lisp/hdpb-lisp.mjs'

class HDPbMiniman {
    version = "0.8.7"
    _DEBUG = false

    /**
     * @typedef  {Object} EGO Current user context
     * @example  {'meaLinguam': 'pt', meaLinguamEtAlii: ['pt'], meaLinguamEtAliiFontem: ['pt_BR']}
     */
    EGO = null

    /**
     * @typedef  {String}  FONTEM_LKG  Path to JSON LKG
     */
    FONTEM_LKG = null

    /**
     * @typedef  {String}  FONTEM_VKG  Path to JSON VKG
     */
    FONTEM_VKG = null

    /**
     * @typedef  {Object}  ONTOLOGIA_LKG  Parsed result of FONTEM_LKG
     */
    ONTOLOGIA_LKG = null

    /**
     * @typedef  {Object}  ONTOLOGIA_VKG  Parsed result of FONTEM_VKG
     */
    ONTOLOGIA_VKG = null

    /**
     * 
     * @param res {Object}  {'LKG': "/path/lkg.json", 'VKG': "/path/vkg.json"}
     * @param ego {Object}  Current user context
     */
    constructor(res, ego) {
        // console.log(res)

        if (typeof HDP_DEBUG !== 'undefined') {
            self._DEBUG = HDP_DEBUG
            console.log('HDPbMiniman HDP_DEBUG !== undefined', HDP_DEBUG)
        }

        this.EGO = ego

        // console.log('this.EGO', ego, this.EGO)

        if (res && res.LKG) {
            self.FONTEM_LKG = res.LKG
            this._initium_lkg()
        }
        if (res && res.VKG) {
            self.FONTEM_VKG = res.VKG
            this._initium_vkg()
        }
    }

    /**
     * Sēcūrum?
     *
     * Trivia:
     * - "sēcūrum"
     *   - https://en.wiktionary.org/wiki/securus
     * @param res 
     */
    _securum(res, modus) {
        // TODO: this function is an placeholder for a FULL integrity check
        //       (think of validate GPG et al) as build in functionality.
        //       Without this, is recomended for the user both trust HTTPS
        //       or rely on additional checks outside HDPbMiniman
        let resultatum = new Object({
            securum: null,
            insecurum: null, // insecurum: true,
            factum: '(qdp->ENG "Complex tests not implemented yet")',
        })
        self._DEBUG && console.log('_securum', resultatum)
        return resultatum
    }

    /**
     * Initium Localization Knowledge Graph 
     *
     * Trivia:
     * - https://en.wiktionary.org/wiki/initium
     */
    async _initium_lkg() {
        let topself = self
        let topthis = this
        // console.log('_initium_lkg', self.FONTEM_LKG, topself.FONTEM_LKG)
        return fetch(self.FONTEM_LKG).then(async function (response) {
            var contentType = response.headers.get("content-type");
            if (contentType && contentType.indexOf("application/json") !== -1) {
                const json = await response.json()
                const sec = topthis._securum(json, 'LKG')
                if (!sec.insecurum) {
                    // Remove either topself or topthis from here
                    topself.ONTOLOGIA_LKG = json
                    topthis.ONTOLOGIA_LKG = json
                    // console.log(self.ONTOLOGIA_LKG)
                    return json
                } else {
                    console.log('_initium_lkg ¬ securum', sec,
                        self.FONTEM_LKG, json)
                    alert('¬ securum', JSON.stringify([sec]))
                    return false
                }
            } else {
                console.log("Problem with res.VKG");
                return false
            }
        });
    }

    /**
     * Initium Vocabulary Knowledge Graph 
     *
     * Trivia:
     * - https://en.wiktionary.org/wiki/initium
     */
    async _initium_vkg() {
        let topself = self
        let topthis = this
        return fetch(self.FONTEM_VKG).then(async function (response) {
            var contentType = response.headers.get("content-type");
            if (contentType && contentType.indexOf("application/json") !== -1) {
                const json = await response.json()
                const sec = topthis._securum(json, 'VKG')
                if (!sec.insecurum) {
                    // Remove either topself or topthis from here
                    topself.ONTOLOGIA_VKG = json
                    topthis.ONTOLOGIA_VKG = json
                    // console.log(self.ONTOLOGIA_VKG)
                    return json
                } else {
                    console.log('_initium_vkg ¬ securum', sec,
                        json, self.FONTEM_VKG)
                    alert('¬ securum', JSON.stringify([sec]))
                    return false
                }
            } else {
                console.log("Error res.VKG");
                return false
            }
        });
    }

    /**
     * Bootstrapping linguam
     *
     * Trivia
     * - "bootstrapping":
     *   - linguistics: https://en.wikipedia.org/wiki/Bootstrapping_(linguistics)
     * - "linguam"
     *   - https://en.wiktionary.org/wiki/lingua#Latin
     */
    static bootstrapping() {
        let resultatum = new Object({
            LKG: "../hxlm/ontologia/json/core.lkg.json",
            VKG: "../hxlm/ontologia/json/core.vkg.json"
        })
        // resultatum.FONTEM_LKG = self.FONTEM_LKG
        // resultatum.FONTEM_VKG = self.FONTEM_VKG
        // resultatum.push('FONTEM_ONTOLOGIA_VKG', self.FONTEM_ONTOLOGIA_VKG)
        return resultatum
    }

    // async _fetch(url, checksum) {
    // async _fetch(url, checksum) {
    async _get(url, checksum) {
        return await fetch(url);
        // const response = await fetch(url);
        // // waits until the request completes...
        // console.log(response);
        // fetch(url).then(function (response) {
        //     let contentType = response.headers.get("content-type");
        //     if (contentType && contentType.indexOf("application/json") !== -1) {
        //         return response.json().then(function (json) {
        //             // process your JSON further
        //             console.log(json)
        //         });
        //     } else {
        //         console.log("Oops, we haven't got JSON!");
        //     }
        // });
    }

    async _get_lkg() {
        if (self.ONTOLOGIA_LKG) {
            return self.ONTOLOGIA_LKG
        } else {
            return this._initium_lkg()
        }
    }
    async _get_vkg() {
        if (self.ONTOLOGIA_VKG) {
            return self.ONTOLOGIA_VKG
        } else {
            return this._initium_vkg()
        }
    }

    /**
     * Linguam recōnstrūctiōnem
     * 
     * @TODO check if hashes match, preferable with user confirmation if is not
     *       running on localhost
     *
     * Trivia:
     * - "linguam"
     *   - https://en.wiktionary.org/wiki/lingua#Latin
     * - "cōnstrūctiōnem"
     *   - https://en.wiktionary.org/wiki/constructio#Latin
     */
    linguam_constructionem() {
        // self._get(self.FONTEM_LKG)
        // self._get(self.FONTEM_VKG)
        // console.log(await self._fetch(self.FONTEM_LKG))
        // console.log(await self._fetch(self.FONTEM_VKG))
    }
    /**
     * Explanare HDP
     *
     * Trivia
     * - "explanare":
     *   - explano: https://en.wiktionary.org/wiki/explano#Latin
     *   - explanare: https://en.wiktionary.org/wiki/explanare#Latin
     * - "index"
     *   - https://en.wiktionary.org/wiki/index#Latin
     */
    async explanare(index) {
        let topself = self
        let topthis = this
        // console.log('explanare, self._DEBUG', self._DEBUG)
        if (self._DEBUG) {
            console.log('explanare', {
                'FONTEM_LKG': topself.FONTEM_LKG,
                'FONTEM_VKG': topself.FONTEM_VKG,
                'ONTOLOGIA_LKG': topself.ONTOLOGIA_LKG,
                //'ONTOLOGIA_LKG2': topthis.ONTOLOGIA_LKG,
                'ONTOLOGIA_VKG': topself.ONTOLOGIA_VKG,
                //'ONTOLOGIA_VKG2': topthis.ONTOLOGIA_VKG
            })
        }

        // console.log()

        // Without options, we will return quick/sumrized information
        if (!index) {
            let resultatum = new Object()
            resultatum.FONTEM_LKG = topself.FONTEM_LKG
            resultatum.FONTEM_VKG = topself.FONTEM_VKG
            resultatum.LKG = topself.ONTOLOGIA_LKG || 'explanare("LKG") ...'
            resultatum.VKG = topself.ONTOLOGIA_VKG || 'explanare("VKG") ...'
            // resultatum.VKG = 'explanare("VKG") ...'
            // return resultatum
            return new Promise(function (resolve, reject) {
                resolve(resultatum)
                // reject('teste teste reject')
                // setTimeout(function(){
                //   resolve(['comedy', 'drama', 'action'])
                // }, 2000);
            });
        }
        if (index == 'LKG') {
            return this._initium_lkg()
            // return this._get_lkg()
        }
        if (index == 'VKG') {
            return this._initium_vkg()
            // return this._get_vkg()
        }

        // Unknow index
        throw ("index [" + index + "] ⊄ HDPbMiniman explanare()")


        // // resultatum.ONTOLOGIA_LKG = vkg_

        // resultatum.ONTOLOGIA_LKG = self.ONTOLOGIA_LKG || this._get_lkg()
        // resultatum.ONTOLOGIA_VKG = self.ONTOLOGIA_VKG || this._get_vkg()

        // if (index) {
        //     return resultatum[index]
        // }
        // return resultatum
    }

    /**
     * (draft) HDPLisp virtual machine
     *
     * Trivia:
     * - 'māchinam':
     *   - https://en.wiktionary.org/wiki/machina#Latin
     * - 'simulātum':
     *   - https://en.wiktionary.org/wiki/simulatus#Latin
     */
    async machinam_simulatum() {
        // Error message from LISP-1.5-Programmers-Manual.pdf
        // TODO: we need to define error messages
        throw new Error('FUNCTION OBJECT HAS NO DEFINITION- APPLY');
    }
}
// let hdp = new HDPbMiniman()

// hdp.explanare();

// export { HDPbMiniman, HDPAux, HDPbLisp }
export { HDPbMiniman, HDPbL10n, HDPbLisp }
