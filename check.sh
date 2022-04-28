#/bin/bash

# Run the same steps lint_fromat github action localy. Make sure that before 
# running this script a venv for this repo has been created and activated.




if [ "$1" == "t" ]
then 
    pytest -vv --cov=loadero_python --cov-report term tests
else
    pip install -r requirements.txt -q
    pylint --rcfile=.pylintrc loadero_python tests/*.py
    black --diff --check --config pyproject.toml loadero_python tests
    # pytest -vv --cov=loadero_python --cov-report term tests
    pytest --cov=loadero_python --cov-report term tests
fi
