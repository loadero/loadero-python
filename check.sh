#/bin/bash

# Run the same steps lint_fromat github action localy. Make sure that before 
# running this script a venv for this repo has been created and activated.

pip install -r requirements.txt -q
pylint --rcfile=.pylintrc loadero_python tests/*.py
black --check --verbose --config pyproject.toml loadero_python tests
pytest tests -vv
