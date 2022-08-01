#/bin/bash

# Run the same steps lint_fromat github action localy. Make sure that before 
# running this script a venv for this repo has been created and activated.


function header() {
    echo "###############################################################################"
    echo "## $1"
    echo "###############################################################################"
}

function unit_test() {
    header "running unit tests"
    pytest --cov=loadero_python --cov-report term -vv tests_unit
}

function intgration_test() {
    header "running integration tests"
    env -$(cat .env) sh -c "pytest --cov=loadero_python --cov-report term -vv tests_integration"
}

function lint() {
    header "running lint"
    pylint -j 4 --rcfile=.pylintrc loadero_python tests_unit tests_integration
}

function format() {
    header "running format"
    black --diff --check --config pyproject.toml loadero_python tests_unit tests_integration
}

if [ $# -eq 0 ]; then
    lint
    format
    unit_test
    intgration_test
elif [ "$1" == "l" ]; then
    lint
elif [ "$1" == "f" ]; then
    format
elif [ "$1" == "t" ]; then
    if [ $# -eq 1 ]; then
        unit_test
        intgration_test
    elif [ "$2" == "u" ]; then
        unit_test
    elif [ "$2" == "i" ]; then
        intgration_test
    else 
        echo "Invalid argument"
    fi
else
    echo "Invalid argument"
fi
