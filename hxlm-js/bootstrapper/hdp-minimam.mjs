console.log('bootstrapper/hdp-minimam.mjs')


// TODO: learn modern javascript, without transpile all the things. To read:
//       - https://blog.rocketseat.com.br/as-melhores-features-do-es6-es7-e-es8/
//       - https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API/Using_Fetch
//       - https://stackoverflow.com/questions/41715994/how-to-document-ecma6-classes-with-jsdoc
//       - https://jsdoc.app/
//       - https://jsdoc.app/howto-es2015-classes.html
//       - https://google.github.io/styleguide/jsguide.html
//       (Emerson Rocha, 2021-04-03 12:57 UTC)

// class App {
//     static log() {
//         console.log('Hey');
//     }
// }

// App.log();

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
    // constructor(ONTOLOGIA_LKG, ONTOLOGIA_VKG) {
    constructor(res) {
        if (res && res.LKG) {
            self.FONTEM_LKG = res.LKG
        }
        if (res && res.VKG) {
            self.FONTEM_VKG = res.VKG
        }
    }

    /**
     * Trivia
     * - "explanare":
     *   - explano: https://en.wiktionary.org/wiki/explano#Latin
     *   - explanare: https://en.wiktionary.org/wiki/explanare#Latin
     */
    static explanare() {
        let resultatum = new Object()
        resultatum.FONTEM_LKG =  self.FONTEM_LKG
        resultatum.FONTEM_VKG =  self.FONTEM_VKG
        // resultatum.push('FONTEM_ONTOLOGIA_VKG', self.FONTEM_ONTOLOGIA_VKG)
        return resultatum
    }
}
// let hdp = HDPMiniman()

// hdp.explanare();

