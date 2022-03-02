"""Script resource tests"""

from loadero_python.resources.script import Script

# Relative to repo root dir.
sample_test_script_py_path = "tests/res/sample_test_script.py"
sample_test_script_py_data = """def test_on_loadero(driver: TestUIDriver):
    print("hello test")
"""


def test_script_from_file():
    s1 = Script(script_file=sample_test_script_py_path)

    assert s1.script == sample_test_script_py_data

    s2 = Script()
    s2.from_file(sample_test_script_py_path)

    assert s2.script == sample_test_script_py_data


def test_script_from_data():
    s1 = Script(content=sample_test_script_py_data)

    assert s1.script == sample_test_script_py_data

    s2 = Script()
    s2.from_data(sample_test_script_py_data)

    assert s2.script == sample_test_script_py_data
