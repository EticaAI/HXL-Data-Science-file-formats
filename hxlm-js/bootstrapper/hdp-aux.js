console.log('hdp-aux.js')

// TODO: https://wesbos.com/template-strings-html


class HDPAux {

    _DEBUG = false
    _console_html_wrapper = '.hdp-console-items'

    constructor(res) {
        if (typeof HDP_DEBUG !== 'undefined') {
            self._DEBUG = HDP_DEBUG
        }
    }

    _console_html_template(res_str, lang) {
        let lang_ = lang || 'lang-json';
        let tpl = `<div class="hdp-console-item">
        <pre><code class="${lang_}>
    ${res_str}
        </code>
      </pre>
    </div>`
        return tpl
    }

    static dump_to_html(res, selector) {
        console.log(document.querySelector(selector).innerHTML)
        let out = document.querySelector(selector)
        out.innerHTML = JSON.stringify(res, null, 2)
        // out.innerHTML = JSON.stringify(res, space = 2)
        // https://highlightjs.org/usage/
        if (hljs && hljs.highlightAll) {
            hljs.highlightAll()
        }
    }

    console_html(res) {
        let wrapper_qss = this._console_html_wrapper
        let wrapper_el = document.querySelector(wrapper_qss)
        let output = this._console_html_template(
            JSON.stringify(res, null, 2)
        )
        console.log('')
        // console.log('testeste', out, this._console_html_template())
        if (wrapper_el) {
            wrapper_el.appendChild(output)
        } else {
            console.error('HDPAux.console_html [' +
                wrapper_qss + '] not found');
            console.log('HDPAux.console_html fallback', res);
        }
        // this_._DEBUG && console.log('console_html out', out)
    }
}