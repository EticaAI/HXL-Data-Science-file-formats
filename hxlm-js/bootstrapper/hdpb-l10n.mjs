// console.log('bootstrapper/hdp-l10n.mjs (draft)')

/**
 * HDPbL10n
 *
 * Trivia:
 *   - i18n with lowercase "i"
 *   - L10n with UPPERCASE "L"
 */
class HDPbL10n {

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
        // TODO: navigator.languages does not work when running with NodeJS.
        //       we should at least make it not break hard
        //       (Emerson Rocha, 2021-04-06 00:05 UTC)

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

export { HDPbL10n }
