var _pj;
function _pj_snippets(container) {
    function in_es6(left, right) {
        if (((right instanceof Array) || ((typeof right) === "string"))) {
            return (right.indexOf(left) > (- 1));
        } else {
            if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                return right.has(left);
            } else {
                return (left in right);
            }
        }
    }
    container["in_es6"] = in_es6;
    return container;
}
_pj = {};
_pj_snippets(_pj);
/*hxlm_minimam.lang
License: Public Domain*/
function factum_to_sexpr(factum) {
    /*Convert Factum object to S-expression string

    Args:
    factum ([Factum]): An Factum object

    Returns:
    [str]: An S-expression string
    */
    var desc, resultatum;
    if (_pj.in_es6("linguam", factum)) {
        desc = (((("(" + factum.linguam) + " \"") + factum.descriptionem) + "\")");
    } else {
        desc = (("\"" + factum.descriptionem) + "\"");
    }
    resultatum = "(vkg.attr.factum ";
    resultatum += (("(vkg.attr.descriptionem " + desc) + ")");
    if (_pj.in_es6("fontem", factum)) {
        resultatum += (("(vkg.attr.fontem \"" + factum.fontem.toString()) + "\")");
    }
    if (_pj.in_es6("datum", factum)) {
        resultatum += (("(vkg.attr.datum \"" + factum.datum.toString()) + "\")");
    }
    resultatum += ")";
    return resultatum;
}

//# sourceMappingURL=hxlm_minimam.js.map
