cd $(dirname $0)/docker

. ../_common.sh

docker-compose up --build || exit 1


while true
do
    docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh
    sh _list_watched.sh | inotifywait -e modify,create,delete,move --fromfile -
done
