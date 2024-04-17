cd $(dirname $0)/../..

set -ex

# export PATH="$(cd /usr/local/texlive/????/bin/*; pwd):$PATH"
rm -f build/main.pdf
make --directory=graduation_project_report_common/docker

latexmk -pdf -halt-on-error -output-directory=_build -interaction=nonstopmode graduation_project_report_common/main.tex
