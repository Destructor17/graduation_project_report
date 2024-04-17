all: ../../config/env.diplom.sty ../../build/.gitignore

../../config/env.diplom.sty: cfggen.py ../../config.json
	mkdir -p ../../config
	echo "*\n!.gitignore" > ../../config/.gitignore
	python3 cfggen.py || rm -f ../../config/env.diplom.sty

../../build/.gitignore:
	mkdir -p ../../build
	echo "*\n!.gitignore" > ../../build/.gitignore
