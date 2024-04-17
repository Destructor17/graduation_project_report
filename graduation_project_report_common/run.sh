cd $(dirname $0)/docker

docker-compose up --build || exit 1
docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh
