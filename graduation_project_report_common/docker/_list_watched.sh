cd $(dirname $0)/

find ../.. \
    -not \( -path ../../.git -prune \) \
    -not \( -path ../../build -prune \) \
    -not \( -path ../../graduation_project_report_common/tmp -prune \) \
