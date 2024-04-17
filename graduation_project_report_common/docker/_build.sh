set -ex
cd $(dirname $0)/..

/usr/local/texlive/????/bin/*/xelatex -halt-on-error -output-directory=build main.tex 