#/bin/bash

# Run the same steps lint_fromat github action localy. Make sure that before 
# running this script a venv for this repo has been created and activated.


function header() {
    echo "###############################################################################"
    echo "## $1"
    echo "###############################################################################"
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

function run_tests() {
    # $1 - coverage report type
    # $2 - test type or ommited
    # $3 - spesific test
    if [ $# -eq 1 ]; then # run all unit and integration tests
        header "unit tests"
        run_test $1 tests_unit
        header "integration tests"
        run_test $1 tests_integration .env
    elif [ "$2" == "u" ]; then
        if [ $# -eq 2 ]; then # run all unit tests
            header "unit tests"
            run_test $1 tests_unit
        else # run spesified unit test
            header "unit test"
            run_test $1 $3
        fi
    elif [ "$2" == "i" ]; then # run all integration tests
        run_test $1 tests_integration .env
    else 
        echo "Invalid argument"
    fi
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
    
    header "unit tests"
    run_test term tests_unit
    
    header "integration tests"
    run_test term tests_integration .env
elif [ "$1" == "l" ]; then
    lint
elif [ "$1" == "f" ]; then
    format
elif [ "$1" == "t" ]; then # test with report in terminal
    run_tests term $2 $3
elif [ "$1" == "c" ]; then # test with coverage reports
    run_tests xml $2 $3
elif [ "$1" == "oc" ]; then # open coverage report
    open htmlcov/index.html 
else
    echo "Invalid argument"
fi
