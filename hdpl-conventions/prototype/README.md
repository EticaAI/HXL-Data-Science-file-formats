# HDPLisp prototype (early draft)


TODO:
- https://beautifulracket.com/stacker/source-listing.html
- https://docs.racket-lang.org/reference/reader.html#%28mod-path._s-exp%29

## Internal nodes
- <https://docs.racket-lang.org/pkg/index.html>
- <https://docs.racket-lang.org/guide/module-basics.html>
- <https://stackoverflow.com/questions/39428903/raco-pkg-install-subfolder-of-git-repo>


```bash
cd hdpl-conventions/prototype/

## Create raw project
raco pkg new hdpl

## Install/Reinstall from local path
raco pkg install --link ./hdpl/

## See docs
raco docs hdpl

## remove the package
raco pkg remove hdpl

```
