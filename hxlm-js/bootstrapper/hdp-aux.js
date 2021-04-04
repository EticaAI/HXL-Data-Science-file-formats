console.log('hdp-aux.js')

// TODO: https://wesbos.com/template-strings-html


class HDPAux {

    _DEBUG = false
    static _console_QS = '.hdp-console-items'

    constructor(res) {
        if (typeof HDP_DEBUG !== 'undefined') {
            self._DEBUG = HDP_DEBUG
        }
    }

    static _console_html_template(res_str, lang) {
        let lang_ = lang || 'lang-json';
        let iid = "hciid-" + Date.now()
        // console.log('lang_', lang_, res_str, iid)
        let tpl = `<div class="hdp-console-item" id="${iid}>
        <pre>aaa<code class="${lang_}>
    ${res_str}
        </code>
      </pre>
    </div>`
        return tpl
    }

    // static dump_to_html(res, selector) {
    //     // console.log('dump_to_html', document.querySelector(selector).innerHTML)
    //     let out = document.querySelector(selector)
    //     out.innerHTML = JSON.stringify(res, null, 2)
    //     // out.innerHTML = JSON.stringify(res, space = 2)
    //     // https://highlightjs.org/usage/
    //     if (hljs && hljs.highlightAll) {
    //         hljs.highlightAll()
    //     }
    // }

    static console_html(res) {
        // console.log('console_html started', res)
        // console.log('console_html', self._console_html_wrapper, self._console_html_template())
        // let wrapper_qss = HDPAux._hdp_console_items_selector
        let wrapper_el = document.querySelector(HDPAux._console_QS)
        // console.log('console_html wrapper_el', wrapper_el)
        let output = HDPAux._console_html_template(
            JSON.stringify(res, null, 2)
        )
        // console.log('console_html', wrapper_el, output)
        // console.log('testeste', out, this._console_html_template())
        if (wrapper_el) {
            wrapper_el.innerHTML = wrapper_el.innerHTML + output
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
}