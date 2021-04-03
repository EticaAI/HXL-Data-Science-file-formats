// console.log('bootstrapper/hdp-minimam.mjs')


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

/**
 * @example <caption>Minimal usage with javascript</caption>
 * <!doctype html>
 * <html>
 * <body>
 * <script>
 *   const HXLM_LKG="../hxlm/ontologia/json/core.lkg.json"
 *   const HXLM_VKG="../hxlm/ontologia/json/core.vkg.json"
 * </script>
 * <script src="./bootstrapper/hdp-minimam.mjs"></script>
 * <script>
 * HDPMiniman.explanare()
 * </script>
 * </body>
 * </html>
 */
class HDPMiniman {
    FONTEM_LKG = null
    FONTEM_VKG = null
    ONTOLOGIA_LKG = null
    ONTOLOGIA_VKG = null
    // constructor(ONTOLOGIA_LKG, ONTOLOGIA_VKG) {
    constructor(res) {
        // console.log(res)

        if (HDP_DEBUG) {
            console.log('HDPMiniman: HDP_DEBUG == true')
        }

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
        //       or rely on additional checks outside HDPMiniman
        let resultatum = new Object({
            securum: null,
            insecurum: null, // insecurum: true,
            factum: '(qdp->ENG "Not tested")',
        })
        HDP_DEBUG && console.log('_securum', resultatum)
        return resultatum
    }

    /**
     * Initium Localization Knowledge Graph 
     *
     * Trivia:
     * - https://en.wiktionary.org/wiki/initium
     */
    _initium_lkg() {
        let this_ = this
        fetch(self.FONTEM_LKG).then(async function (response) {
            var contentType = response.headers.get("content-type");
            if (contentType && contentType.indexOf("application/json") !== -1) {
                const json = await response.json()
                const sec = this_._securum(json, 'LKG')
                if (!sec.insecurum) {
                    self.ONTOLOGIA_LKG = json
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
    _initium_vkg() {
        let this_ = this
        fetch(self.FONTEM_VKG).then(async function (response) {
            var contentType = response.headers.get("content-type");
            if (contentType && contentType.indexOf("application/json") !== -1) {
                const json = await response.json()
                const sec = this_._securum(json, 'VKG')
                if (!sec.insecurum) {
                    self.ONTOLOGIA_VKG = json
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
    explanare(index) {
        let resultatum = new Object()
        // let vkg_ = this._get_lkg()
        // console.log('vkg_', vkg_)
        resultatum.FONTEM_LKG = self.FONTEM_LKG
        resultatum.FONTEM_VKG = self.FONTEM_VKG
        // resultatum.ONTOLOGIA_LKG = vkg_

        resultatum.ONTOLOGIA_LKG = self.ONTOLOGIA_LKG || this._get_lkg()

        // if (!self.ONTOLOGIA_LKG) {
        //     resultatum.ONTOLOGIA_LKG = this._get_lkg()
        // } else {

        // }

        resultatum.ONTOLOGIA_LKG = self.ONTOLOGIA_LKG
        resultatum.ONTOLOGIA_VKG = self.ONTOLOGIA_VKG
        // resultatum.push('FONTEM_ONTOLOGIA_VKG', self.FONTEM_ONTOLOGIA_VKG)
        if (index) {
            return resultatum[index]
        }
        return resultatum
    }
}
// let hdp = new HDPMiniman()

// hdp.explanare();

