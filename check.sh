#/bin/bash

# Run the same steps lint_fromat github action localy. Make sure that before 
# running this script a venv for this repo has been created and activated.


failed=0


function header() {
    echo "\033[0;36m"
    echo "###############################################################################"
    echo "## $1"
    echo "###############################################################################"
    echo "\033[0m"
}

function run_test() {
    if [ $# -eq 2 ]; then 
        pytest --cov=loadero_python --cov-report $1 -vv $2
    elif [ $# -eq 3 ]; then # run with env
        cmd="pytest --cov=loadero_python --cov-report $1 -vv $2"
        env -$(cat $3) sh -c "$cmd"
    else
        echo "Invalid number of arguments"
    fi
}

function integration_tests() {
    header "running integration tests"
    env -$(cat .env) sh -c "pytest --cov=loadero_python --cov-report term -vv tests/integration" || failed=1
}

function unit_tests() {
    header "running unit tests"
    pytest --cov=loadero_python --cov-report term -vv tests/unit || failed=1
}

function unit_tests_with_report() {
    header "running unit tests with report"
    pytest --cov=loadero_python --cov-report term -vv tests/unit > pytest-coverage.txt
    if [ $? != 0 ]; then
        failed=1
    fi
}

function lint() {
    header "running lint"
    pylint -j 4 --rcfile=.pylintrc loadero_python tests || failed=1
}

function format() {
    header "running format"
    black --diff --check --config pyproject.toml loadero_python tests || failed=1
}


if [ $# -eq 0 ]; then
    lint
    
    format
    
    unit_tests
    
    integration_tests

elif [ "$1" == "lint" ] || [ "$1" == "l" ]; then
    lint

elif [ "$1" == "format" ] || [ "$1" == "f" ]; then
    format

elif [ "$1" == "test" ] || [ "$1" == "t" ]; then # test with report in terminal

    if [ $# -eq 1 ]; then # no additional arguments spesified, run all tests (unit and integration)
        unit_tests

        integration_tests

    elif [ "$2" == "unit" ] || [ "$2" == "u" ]; then
        unit_tests

    elif [ "$2" == "integration" ] || [ "$2" == "i" ]; then
        integration_tests

    elif [ "$2" == "report" ] || [ "$2" == "r" ]; then
        unit_tests_with_report

    else 
        echo "Invalid argument"
    fi

elif [ "$1" == "b" ]; then # build
    header "building source distribution"
    python -m build --sdist
    header "building wheel"
    python -m build --wheel

elif [ "$1" == "u" ]; then # upload
    twine check dist/*
    twine upload --repository pypi dist/*
    rm dist/*

else
    echo "Invalid argument"
fi


if [ $failed -eq 1 ]; then
    header "checks failed"
    exit 1
fi
