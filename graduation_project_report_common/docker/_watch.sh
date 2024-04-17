cd $(dirname $0)/..

while true; do

inotifywait -qq -e modify,create,delete -r .. || exit 2
sh docker/_build.sh || true

done