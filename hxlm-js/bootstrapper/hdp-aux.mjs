/**
 * @license      Public Domain
 * @author       Emerson Rocha <rocha(at)ieee.org>
 * @description  HDPAux is not actually part of the HDP conventions, but
 *               contains some code to help with interface.
 * @created      2021
 *
 * This work is done with love and special attention to details for the
 * international community that does not have in English its mother language.
 * Part of the JavaScript scripts are based on
 * <https://github.com/fititnt/ais-ethics-tags> / <https://tags.etica.ai/>
 **/

// TODO: look at https://en.wikipedia.org/wiki/Semantic_bootstrapping


class HDPAux {

    _DEBUG = false

    static _console_QS = '.hdp-console-items'

    constructor(res) {
        if (typeof HDP_DEBUG !== 'undefined') {
            self._DEBUG = HDP_DEBUG
        }
    }

    static _console_html_template(res_str, lang, namen, visibile) {
        let iid = "hciid-" + Date.now()
        console.log('hdpauxtpl', lang, namen, visibile)

        let codeclass = 'collapse'

        if (visibile) {
            codeclass = ''
        }

        let tpl = `
    <div class="hdp-console-item">
        <p>
            <button type="button" class="btn btn-sm btn-info" data-toggle="collapse" data-target="#${iid}">
                Display/Hide
            </button> ${namen}
        </p>
        <pre class="${codeclass}" id="${iid}"><code class="${lang}">${res_str}</code></pre>
    </div>`
        return tpl
    }

    /**
     * HDPAux helper to print help code on screen
     *
     * @param {Object} res       Thing to output
     * @param {String} lang      An programming language class (see highlightjs.org)
     * @param {String} namen     An friendly name to add to header
     * @param {Bool}   visibile  Initial visibilty of code (trivia: Latin visibilis)
     */
    static console_html(res, lang, namen, visibile) {
        // console.log('console_html started', res)
        // console.log('console_html', self._console_html_wrapper, self._console_html_template())
        // let wrapper_qss = HDPAux._hdp_console_items_selector
        let wrapper_el = document.querySelector(HDPAux._console_QS)
        // console.log('console_html wrapper_el', wrapper_el)
        let lang_ = lang || 'lang-json';
        let namen_ = namen || 'log-' + (new Date().toISOString())
        let output = HDPAux._console_html_template(
            JSON.stringify(res, null, 2),
            lang_,
            namen_,
            visibile
        )
        // console.log('console_html', wrapper_el, output)
        // console.log('testeste', out, this._console_html_template())
        if (wrapper_el) {
            wrapper_el.innerHTML = output + wrapper_el.innerHTML
            // wrapper_el.appendChild(output)
            // https://highlightjs.org/usage/
            if (hljs && hljs.highlightAll) {
                hljs.highlightAll()
            }
        } else {
            console.error('HDPAux.console_html [' +
                HDPAux._console_QS + '] not found');
            console.log('HDPAux.console_html fallback', res);
        }
        // this_._DEBUG && console.log('console_html out', out)
    }

    /**
     * Who I am
     *
     * Trivia:
     *   - 'Quis sum?' is 'who I am' in Latin
     *   - 'mea linguam' is 'my (natural) language' in Latin
     *   - 'mea linguam fontem' is 'my source (natural) language' in Latin
     *   - 'mea linguam et alli' needs revision. (its an array)
     *   - Code:
     *     - Based on the English version ais-ethics-tags.js (https://tags.etica.ai)
     * @returns {Object}
     */
    static quis_sum() {
        let resultatum = {};
        resultatum.meaLinguam = navigator.language || navigator.userLanguage;
        resultatum.meaLinguamEtAliiFontem = navigator.languages || [resultatum.meaLinguam];
        resultatum.meaLinguamEtAlii = [];
        resultatum.meaLinguamEtAliiFontem.forEach(function (lang) {
            let wdLang = lang.split('-');
            if (resultatum.meaLinguamEtAlii.indexOf(wdLang[0]) === -1) {
                resultatum.meaLinguamEtAlii.push(wdLang[0]);
            }
        })
        return resultatum
    }
}

export default HDPAux