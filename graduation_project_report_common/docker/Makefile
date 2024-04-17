all: ../config/env.diplom.sty ../../_build/EXISTS

../config/env.diplom.sty: cfggen.py ../../config.json
	mkdir -p ../config
	python3 cfggen.py || rm -f ../config/env.diplom.sty

../../_build/EXISTS:
	mkdir -p ../../_build
	touch ../../_build/EXISTS
