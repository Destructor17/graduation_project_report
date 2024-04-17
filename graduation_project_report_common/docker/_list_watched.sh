cd $(dirname $0)/

find ../.. \
    -not \( -path ../../.git -prune \) \
    -not \( -path ../../_build -prune \) \
    -not \( -path ../../graduation_project_report_common/tmp -prune \) \
