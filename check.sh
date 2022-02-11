#/bin/bash

# Run the same steps lint_fromat github action localy. Make sure that before 
# running this script a venv for this repo has been created and activated.

pip3 install -r requirements.txt 
pylint --rcfile=.pylintrc loadero-python
black --check --verbose --config pyproject.toml loadero-python
