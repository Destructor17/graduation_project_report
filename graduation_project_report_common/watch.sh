cd $(dirname $0)/docker

docker-compose up --build || exit 1


while true
do
    docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh
    inotifywait -e modify,create,delete,move -r ../.. @build @graduation_project_report_common/tmp
done
