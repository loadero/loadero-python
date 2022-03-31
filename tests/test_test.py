"""Test resource tests"""


from datetime import datetime
from loadero_python.resources import test, script


time_now = datetime.now()


class TestTestParams:
    """Test parameters tests"""

    def test_created(self):
        t = test.TestParams()
        t.__dict__["_created"] = time_now
        assert t.created == time_now

    def test_updated(self):
        t = test.TestParams()
        t.__dict__["_updated"] = time_now
        assert t.updated == time_now

    def test_script_file_id(self):
        t = test.TestParams()
        t.__dict__["_script_file_id"] = 5
        assert t.script_file_id == 5

    def test_group_count(self):
        t = test.TestParams()
        t.__dict__["_group_count"] = 5
        assert t.group_count == 5

    def test_participant_count(self):
        t = test.TestParams()
        t.__dict__["_participant_count"] = 5
        assert t.participant_count == 5

    def test_deleted(self):
        t = test.TestParams()
        t.__dict__["_deleted"] = True

        assert t.deleted is True

    def test_project_id(self):
        t = test.TestParams()
        t.__dict__["_project_id"] = 5
        assert t.project_id == 5

    def test_builder_id(self):
        t = test.TestParams()
        t.with_id(5)
        assert t.test_id == 5

    def test_builder_name(self):
        t = test.TestParams()
        t.with_name("test")
        assert t.name == "test"

    def test_builder_start_interval(self):
        t = test.TestParams()
        t.with_start_interval(5)
        assert t.start_interval == 5

    def test_builder_participant_timeout(self):
        t = test.TestParams()
        t.with_participant_timeout(5)
        assert t.participant_timeout == 5

    def test_builder_mode(self):
        t = test.TestParams()
        t.with_mode("load")
        assert t.mode == "load"

    def test_builder_increment_strategy(self):
        t = test.TestParams()
        t.with_increment_strategy("linear")
        assert t.increment_strategy == "linear"

    def test_builder_mos_test(self):
        t = test.TestParams()
        t.with_mos_test(True)
        assert t.mos_test is True

    def test_builder_script(self):
        t = test.TestParams()
        t.with_script(script.Script(content="hello"))
        assert t.script.script == "hello"


def test_test_params():
    tp = test.TestParams(start_interval=4)
    assert tp.start_interval == 4

    tp.with_name("webrtc test")
    assert tp.name == "webrtc test"


# def test_test():
#     api = APIClient()
#     tp = test.TestParams(start_interval=4)

#     t = test.Test(params=tp)

#     t.read()
