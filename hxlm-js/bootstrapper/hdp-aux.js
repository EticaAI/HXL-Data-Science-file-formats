// console.log('hdp-aux.js')

class HDPAux {
    static dump_to_html(res, selector) {
        console.log(document.querySelector(selector).innerHTML)
        let out = document.querySelector(selector)
        out.innerHTML = JSON.stringify(res, null, 2)
        // out.innerHTML = JSON.stringify(res, space = 2)
        // https://highlightjs.org/usage/
        if (hljs && hljs.highlightAll){
            hljs.highlightAll()
        }
    }
  }