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


raco pkg update --link ./hdpl/

## See docs
raco docs hdpl

## remove the package
raco pkg remove hdpl

```

### Prepare deploy

```bash
# prepare to deploy

raco setup --check-pkg-deps --unused-pkg-deps hdpl
```

### Create shareable executable from library
> See also:
> - https://stackoverflow.com/questions/62972086/racket-scheme-compile-to-single-binary-no-dependencies-ffi-and-static-linking
> - https://docs.racket-lang.org/raco/exe-dist.html
> - https://docs.racket-lang.org/pkg/implementation.html
> - https://alex-hhh.github.io/2019/09/racket-binary-packages.html


```bash
cd hdpl-conventions/prototype/hdpl/
raco exe -o hdpl-cli main.rkt
raco distribute dist/ hdpl-cli
# tree dist/
# dist/
# ├── bin
# │   └── hdpl-cli
# └── lib
#     └── plt
#         └── racketcs-8.0
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/hdpl-conventions/prototype/hdpl$ ls -lha dist/bin/hdpl-cli 
# -rwxr-xr-x 1 fititnt fititnt 1,9M abr 15 16:11 dist/bin/hdpl-cli
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/hdpl-conventions/prototype/hdpl$ ls -lha dist/lib/plt/racketcs-8.0 
# -rwxr-xr-x 1 fititnt fititnt 44M fev 22 16:00 dist/lib/plt/racketcs-8.0
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/hdpl-conventions/prototype/hdpl$ ./dist/bin/hdpl-cli 
# hello world

### TODO: this is partial atempt using root directory instead of subfolder

# # raco distribute /workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/hdpl-cli/

# # cd root directory, like cd /workspace/git/EticaAI/HXL-Data-Science-file-formats/
# raco exe -o hdpl-conventions/prototype/hdpl/hdpl-cli hdpl-conventions/prototype/hdpl/main.rkt
# raco distribute -v hdpl-conventions/prototype/hdpl/hdpl-cli temp/hdpl-cli/


### Quick test, delete later ___________________________________________________
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/hello-racket$ cat hello.rkt 
# #lang racket
# (writeln "hello")
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/hello-racket$ raco exe hello.rkt 
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/hello-racket$ ls -lha
# total 12M
# drwxrwxr-x 2 fititnt fititnt 4,0K abr 15 16:18 .
# drwxrwxr-x 8 fititnt fititnt 4,0K abr 15 16:17 ..
# -rwxr-xr-x 1 fititnt fititnt  12M abr 15 16:18 hello
# -rw-rw-r-- 1 fititnt fititnt   30 abr 15 16:17 hello.rkt

# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/hello-racket$ raco distribute -v dist/ hello
#  [output to "dist/"]
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/hello-racket$ tree
# .
# ├── dist
# │   ├── bin
# │   │   └── hello
# │   └── lib
# │       └── plt
# │           └── racketcs-8.0
# ├── hello
# └── hello.rkt

# 4 directories, 4 files
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/hello-racket$ ls -lha dist/bin/hello 
# -rwxr-xr-x 1 fititnt fititnt 12M abr 15 16:19 dist/bin/hello
# fititnt@bravo:/workspace/git/EticaAI/HXL-Data-Science-file-formats/temp/hello-racket$ ls -lha dist/lib/plt/racketcs-8.0 
# -rwxr-xr-x 1 fititnt fititnt 44M fev 22 16:00 dist/lib/plt/racketcs-8.0


```