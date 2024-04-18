cd $(dirname $0)/../..

set -ex

# export PATH="$(cd /usr/local/texlive/????/bin/*; pwd):$PATH"
make --directory=graduation_project_report_common/docker

rm -f _build/*.pdf
latexmk -pdf -halt-on-error -output-directory=_build -interaction=nonstopmode
