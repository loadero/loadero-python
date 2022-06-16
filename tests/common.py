"""Common data shared between tests"""

# pylint: disable=missing-function-docstring

from dateutil import parser
from loadero_python.resources.assert_resource import AssertParams
from loadero_python.resources.script import Script
from loadero_python.resources.assert_precondition import (
    AssertPreconditionParams,
)
from loadero_python.resources.classificator import Property, Operator
from loadero_python.resources.metric_path import MetricPath


api_base = "http://mock.loadero.api/v2/"
access_token = "LOADERO_PROJECT_ACCESS_TOKEN"
project_id = 538591
group_id = 34421
test_id = 12734
file_id = 923
participant_id = 92559
file_id = 294325
assert_id = 29643
run_id = 937561
result_log_id = 552648
result_id = 992341
result_assert_id = 9876231
run_assert_id = 871342
metric_id = 912388482
result_mos_id = 99283476
result_timecard_id = 88277471
run_participant_id = 233992
profile_id = 87
assert_precondition_id = 9862123


script = Script(content="pytest test script")


created_time_string = "2022-04-01T13:54:25.689Z"
created_time = parser.parse(created_time_string)

updated_time_string = "2024-02-03T15:42:54.689Z"
updated_time = parser.parse(updated_time_string)


paged_response = {
    "filter": {},
    "pagination": {"limit": 0, "offset": 0, "page": 0, "total_pages": 0},
    "results": [],
}


participant_json = {
    "id": participant_id,
    "group_id": group_id,
    "test_id": test_id,
    "created": created_time_string,
    "updated": updated_time_string,
    "profile_id": profile_id,
    "count": 3,
    "record_audio": False,
    "name": "pytest participant",
    "compute_unit": "g4",
    "audio_feed": "silence",
    "browser": "chromeLatest",
    "location": "eu-central-1",
    "media_type": "custom",
    "network": "4g",
    "video_feed": "480p-15fps",
}


group_json = {
    "count": 8,
    "created": created_time_string,
    "id": group_id,
    "name": "pytest_group",
    "test_id": test_id,
    "updated": updated_time_string,
}

# assert

assert_json = {
    "id": assert_id,
    "test_id": test_id,
    "created": created_time_string,
    "updated": updated_time_string,
    "expected": "892",
    "operator": "gt",
    "path": "machine/network/bitrate/in/avg",
}

assert_request_json = {
    "expected": "892",
    "operator": "gt",
    "path": "machine/network/bitrate/in/avg",
}


def check_assert_params(params: AssertParams):
    assert params.assert_id == assert_id
    assert params.test_id == test_id
    assert params.created == created_time
    assert params.updated == updated_time
    assert params.expected == "892"
    assert params.operator is Operator.O_GT
    assert params.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG


test_json = {
    "id": test_id,
    "created": created_time_string,
    "updated": updated_time_string,
    "increment_strategy": "linear",
    "mode": "load",
    "name": "pytest test",
    "participant_timeout": 13,
    "project_id": project_id,
    "script_file_id": 65,
    "start_interval": 12,
    "group_count": 52,
    "participant_count": 9355,
}


file_json = {
    "content": "pytest test script",
    "created": created_time_string,
    "file_type": "test_script",
    "id": file_id,
    "project_id": project_id,
    "updated": updated_time_string,
}

execution_started_string = "2021-02-26T14:53:24.228Z"
execution_started = parser.parse(execution_started_string)

execution_finished_string = "2023-06-26T19:38:25.268Z"
execution_finished = parser.parse(execution_finished_string)

processing_started_string = "2025-07-29T19:31:29.468Z"
processing_started = parser.parse(processing_started_string)

processing_finished_string = "2019-07-09T18:39:30.488Z"
processing_finished = parser.parse(processing_finished_string)

run_json = {
    "id": run_id,
    "created": created_time_string,
    "updated": updated_time_string,
    "test_id": test_id,
    "status": "running",
    "metric_status": "calculating",
    "mos_status": "available",
    "test_mode": "load",
    "increment_strategy": "linear",
    "processing_started": processing_started_string,
    "processing_finished": processing_finished_string,
    "execution_started": execution_started_string,
    "execution_finished": execution_finished_string,
    "script_file_id": file_id,
    "test_name": "py test test",
    "start_interval": 98,
    "participant_timeout": 92,
    "launching_account_id": 12,
    "success_rate": 0.3,
    "total_cu_count": 3.3,
    "group_count": 5,
    "participant_count": 89,
    "mos_test": True,
}

result_log_json = {
    "id": result_log_id,
    "created": created_time_string,
    "result_id": result_id,
    "webrtc": "webrtc_log.txt",
    "selenium": "selenium_log.txt",
    "browser": "browser_log.txt",
    "rru": "rru_log.txt",
    "allure_report": "allure_report_log.txt",
}


result_assert_json = {
    "path": "machine/cpu/available/total",
    "operator": "gt",
    "expected": "value",
    "id": result_assert_id,
    "created": created_time_string,
    "result_id": result_id,
    "run_assert_id": run_assert_id,
    "actual": "actual",
    "status": "fail",
    "message": "message",
}

artifact_info_json = {
    "paths": [
        "artifact_path1",
        "artifact_path2",
    ],
    "error": "artifact error",
}

artifacts_info_json = {
    "audio": artifact_info_json,
    "downloads": {},
    "screenshots": artifact_info_json,
    "video": {},
}

metric_json = {
    "id": metric_id,
    "created": created_time_string,
    "data_count": 102,
    "metric_path": "machine/cpu/available",
    "value": "value",
    "total": 82.1,
    "minimum": 10,
    "maximum": 5.3,
    "average": 23,
    "stddev": 25,
    "rstddev": 7,
    "perc_1st": 0.1,
    "perc_5th": 0.2,
    "perc_25th": 92.5,
    "perc_50th": 1.1,
    "perc_75th": 35,
    "perc_95th": 64,
    "perc_99th": 75,
}


metrics_json = {
    "machine": {
        "machine/cpu/available": metric_json,
        "machine/ram/percent": metric_json,
    },
    "webrtc": {
        "webrtc/audio/codec/in": metric_json,
        "webrtc/audio/rtt": metric_json,
    },
}

start_time_string = "2018-03-02T11:34:28.689Z"
start_time = parser.parse(start_time_string)

end_time_string = "2020-08-01T18:12:24.689Z"
end_time = parser.parse(end_time_string)


result_mos_json = {
    "id": result_mos_id,
    "created": created_time_string,
    "result_id": result_id,
    "algorithm": "visqol",
    "score": 3.2,
    "start": start_time_string,
    "end": end_time_string,
}


mean_opinion_scores_json = {
    "visqol": [
        result_mos_json,
        result_mos_json,
    ],
}

result_timecard_json = {
    "id": result_timecard_id,
    "created": created_time_string,
    "result_id": result_id,
    "name": "timecard name",
    "start": 12314,
    "end": 4123,
}

data_sync_json = {
    "result_timecards": [
        result_timecard_json,
        result_timecard_json,
    ]
}

run_participant_json = {
    "id": run_participant_id,
    "updated": updated_time_string,
    "created": created_time_string,
    "run_id": run_id,
    "group_name": "group name",
    "group_num": 23,
    "participant_name": "participant name",
    "participant_num": 123,
    "profile_id": profile_id,
    "record_audio": True,
    "compute_unit": "g4",
    "audio_feed": "silence",
    "browser": "chromeLatest",
    "location": "eu-central-1",
    "media_type": "custom",
    "network": "4g",
    "video_feed": "480p-15fps",
}

result_json = {
    "id": result_id,
    "created": created_time_string,
    "updated": updated_time_string,
    "start": start_time_string,
    "end": end_time_string,
    "status": "timeout",
    "selenium_result": "aborted",
    "mos_status": "calculating",
    "participant_details": run_participant_json,
    "log_paths": result_log_json,
    "asserts": [result_assert_json, result_assert_json],
    "artifacts": artifacts_info_json,
    "metrics": metrics_json,
    "mos": mean_opinion_scores_json,
    "data_sync": data_sync_json,
}

# assert precondition

assert_precondition_json = {
    "assert_id": assert_id,
    "created": created_time_string,
    "updated": updated_time_string,
    "expected": "10",
    "id": assert_precondition_id,
    "operator": "gt",
    "property": "group_num",
}

assert_precondition_request_json = {
    "expected": "10",
    "operator": "gt",
    "property": "group_num",
}


def check_assert_precondition_params(params: AssertPreconditionParams):
    assert params.assert_precondition_id == assert_precondition_id
    assert params.assert_id == assert_id
    assert params.test_id == test_id
    assert params.created == created_time
    assert params.updated == updated_time
    assert params.expected == "10"
    assert params.operator == Operator.O_GT
    assert params.procondition_property == Property.P_GROUP_NUM
