# hxlm.locale

> This is an early draft (Emerson Rocha, 2021-03-18 20:05 UTC)

See:

- <https://github.com/EticaAI/HXL-Data-Science-file-formats/issues/15#issuecomment-802217559>
  - https://docs.python.org/3/library/gettext.html
  - https://docs.python.org/3/library/gettext.html#internationalizing-your-programs-and-modules
  - https://www.gnu.org/software/gettext/manual/gettext.html
  - https://phrase.com/blog/posts/translate-python-gnu-gettext/
  - https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/
  - Maybe?
    - https://wiki.maemo.org/Internationalize_a_Python_application


About locale:

- https://phrase.com/blog/posts/beginners-guide-to-locale-in-python/


## Example commands to generate .po files

```bash
# root directory

xgettext hxlm/core/bin/hdpcli.py --output=hxlm/locale/hdp.pot --language=Python --package-name='hxlm' --package-version="0.8.3" --default-domain=hdp  --add-comments --no-location

xgettext hxlm/core/bin/hdpcli.py --output=hxlm/locale/pt/LC_MESSAGES/hdp.po --language=Python --package-name='hxlm' --package-version="0.8.3" --default-domain=hdp  --add-comments --no-location --join-existing

# xgettext hxlm/core/bin/hdpcli.py --output-dir=hxlm/locale/ --language=Python --package-name='hxlm' --package-version="0.8.3" --default-domain=hdp --no-location
```

<!--

- https://lokalise.com/blog/beginners-guide-to-python-i18n/
- https://stackoverflow.com/questions/4150053/python-tkinter-using-tkinter-for-rtl-right-to-left-languages-like-arabic-hebr
-->