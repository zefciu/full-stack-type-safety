full-stack-typing.pdf: full-stack-typing.latex stack-simple.pdf weak.tex dynamic.tex inference.tex stricter.tex looser.tex duck.tex styles.tex weak-sql.tex strong-django.tex Makefile
	latex -output-format pdf full-stack-typing.latex

styles.tex: Makefile
	pygmentize -S manni -f latex > styles.tex

stack-simple.pdf: stack-simple.svg Makefile
	inkscape stack-simple.svg -A stack-simple.pdf --export-ignore-filters

weak.tex: weak.c Makefile
	pygmentize -o weak.tex weak.c

inference.tex: inference.go Makefile
	pygmentize -o inference.tex inference.go

dynamic.tex: dynamic.py Makefile
	pygmentize -o dynamic.tex dynamic.py

stricter.tex: stricter.hs Makefile
	pygmentize -o stricter.tex stricter.hs

looser.tex: looser.js Makefile
	pygmentize -o looser.tex looser.js

duck.tex: duck.go Makefile
	pygmentize -o duck.tex duck.go

weak-sql.tex: weak-sql.sql Makefile
	pygmentize -o weak-sql.tex weak-sql.sql

strong-django.tex: strong-django.py Makefile
	pygmentize -o strong-django.tex strong-django.py
