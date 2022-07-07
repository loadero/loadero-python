"""Common data shared between tests"""

# pylint: disable=missing-function-docstring

from dateutil import parser
from loadero_python.resources.assert_resource import AssertParams
from loadero_python.resources.script import Script
from loadero_python.resources.assert_precondition import (
    AssertPreconditionParams,
)
from loadero_python.resources.metric_path import MetricPath, MetricBasePath

from loadero_python.resources.participant import ParticipantParams
from loadero_python.resources.run import RunParams
from loadero_python.resources.result import (
    ResultAssertParams,
    ResultParams,
    ResultLogParams,
    MetricParams,
    MetricsParams,
    ArtifactsInfoParams,
    ResultMOSParams,
    MeanOpinionScoresParams,
    ResultTimecardParams,
    DataSyncParams,
)
from loadero_python.resources.run_participant import RunParticipantParams
from loadero_python.resources.classificator import (
    MosAlgorithm,
    RunStatus,
    MetricStatus,
    TestMode,
    IncrementStrategy,
    ResultStatus,
    ComputeUnit,
    AudioFeed,
    Browser,
    Location,
    Network,
    VideoFeed,
    Property,
    Operator,
    AssertStatus,
)
from loadero_python.resources.test import TestParams
from loadero_python.resources.group import GroupParams

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


def check_participant_params(params: ParticipantParams):
    assert params.participant_id == participant_id
    assert params.group_id == group_id
    assert params.test_id == test_id
    assert params.created == created_time
    assert params.updated == updated_time
    assert params.count == 3
    assert not params.record_audio
    assert params.name == "pytest participant"
    assert params.compute_unit == ComputeUnit.CU_G4
    assert params.audio_feed == AudioFeed.AF_SILENCE
    assert params.browser == Browser.B_CHROMELATEST
    assert params.location == Location.L_EU_CENTRAL_1
    assert params.network == Network.N_4G
    assert params.video_feed == VideoFeed.VF_480P_15FPS


group_json = {
    "count": 8,
    "created": created_time_string,
    "id": group_id,
    "name": "pytest_group",
    "test_id": test_id,
    "updated": updated_time_string,
}

# assert


def check_group_params(params: GroupParams):
    assert params.group_id == group_id
    assert params.created == created_time
    assert params.name == "pytest_group"
    assert params.test_id == test_id
    assert params.updated == updated_time
    assert params.count == 8


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


def check_test_params(params: TestParams, with_script: bool = True):
    assert params.test_id == test_id
    assert params.created == created_time
    assert params.updated == updated_time
    assert params.name == "pytest test"
    assert params.start_interval == 12
    assert params.participant_timeout == 13
    assert params.mode is TestMode.TM_LOAD
    assert params.increment_strategy is IncrementStrategy.IS_LINEAR
    assert params.group_count == 52
    assert params.participant_count == 9355
    assert params.deleted is None

    if with_script:
        assert params.script.content == "pytest test script"


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
    "status": "done",
    "metric_status": "calculating",
    "mos_status": "available",
    "test_mode": "load",
    "increment_strategy": "linear",
    "processing_started": processing_started_string,
    "processing_finished": processing_finished_string,
    "execution_started": execution_started_string,
    "execution_finished": execution_finished_string,
    "script_file_id": file_id,
    "test_name": "pytest test",
    "start_interval": 98,
    "participant_timeout": 92,
    "launching_account_id": 12,
    "success_rate": 0.3,
    "total_cu_count": 3.3,
    "group_count": 5,
    "participant_count": 89,
    "mos_test": True,
}


def check_run_params(params: RunParams):
    assert params.run_id == run_id
    assert params.test_id == test_id
    assert params.created == created_time
    assert params.updated == updated_time
    assert params.status == RunStatus.RS_DONE
    assert params.metric_status == MetricStatus.MS_CALCULATING
    assert params.mos_status == MetricStatus.MS_AVAILABLE
    assert params.test_mode == TestMode.TM_LOAD
    assert params.increment_strategy == IncrementStrategy.IS_LINEAR
    assert params.processing_started == processing_started
    assert params.processing_finished == processing_finished
    assert params.execution_started == execution_started
    assert params.execution_finished == execution_finished
    assert params.script_file_id == file_id
    assert params.test_name == "pytest test"
    assert params.start_interval == 98
    assert params.participant_timeout == 92
    assert params.launching_account_id == 12
    assert params.success_rate == 0.3
    assert params.total_cu_count == 3.3
    assert params.group_count == 5
    assert params.participant_count == 89
    assert params.mos_test is True


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


def check_result_log_params(params: ResultLogParams):
    assert params.result_log_id == result_log_id
    assert params.created == created_time
    assert params.result_id == result_id
    assert params.webrtc == "webrtc_log.txt"
    assert params.selenium == "selenium_log.txt"
    assert params.browser == "browser_log.txt"
    assert params.rru == "rru_log.txt"
    assert params.allure_report == "allure_report_log.txt"


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


def check_result_assert_params(params: ResultAssertParams):
    assert params.result_assert_id == result_assert_id
    assert params.path == MetricPath.MACHINE_CPU_AVAILABLE_TOTAL
    assert params.operator == Operator.O_GT
    assert params.expected == "value"
    assert params.created == created_time
    assert params.result_id == result_id
    assert params.actual == "actual"
    assert params.status == AssertStatus.AS_FAIL
    assert params.message == "message"


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


def check_artifacts_info_params(params: ArtifactsInfoParams):
    assert params.audio.paths == [
        "artifact_path1",
        "artifact_path2",
    ]
    assert params.audio.error == "artifact error"
    assert params.downloads.paths is None
    assert params.screenshots.paths == [
        "artifact_path1",
        "artifact_path2",
    ]
    assert params.screenshots.error == "artifact error"
    assert params.video.paths is None


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


def check_metric_params(params: MetricParams):
    assert params.metric_id == metric_id
    assert params.created == created_time
    assert params.data_count == 102
    assert params.metric_path == MetricBasePath.MACHINE_CPU_AVAILABLE
    assert params.value == "value"
    assert params.total == 82.1
    assert params.minimum == 10
    assert params.maximum == 5.3
    assert params.average == 23
    assert params.stddev == 25
    assert params.rstddev == 7
    assert params.perc_1st == 0.1
    assert params.perc_5th == 0.2
    assert params.perc_25th == 92.5
    assert params.perc_50th == 1.1
    assert params.perc_75th == 35
    assert params.perc_95th == 64
    assert params.perc_99th == 75


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


def check_metrics_params(params: MetricsParams):
    assert len(params.machine) == 2
    assert len(params.webrtc) == 2

    check_metric_params(params.machine[MetricBasePath.MACHINE_CPU_AVAILABLE])
    check_metric_params(params.machine[MetricBasePath.MACHINE_RAM_PERCENT])
    check_metric_params(params.webrtc[MetricBasePath.WEBRTC_AUDIO_CODEC_IN])
    check_metric_params(params.webrtc[MetricBasePath.WEBRTC_AUDIO_RTT])


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


def check_result_mos_params(params: ResultMOSParams):
    assert params.result_mos_id == result_mos_id
    assert params.created == created_time
    assert params.result_id == result_id
    assert params.algorithm == MosAlgorithm.MA_VISQOL
    assert params.score == 3.2
    assert params.start == start_time
    assert params.end == end_time


mean_opinion_scores_json = {
    "visqol": [
        result_mos_json,
        result_mos_json,
    ],
}


def check_mean_opinion_scores_params(params: MeanOpinionScoresParams):
    assert len(params.visqol) == 2
    check_result_mos_params(params.visqol[0])
    check_result_mos_params(params.visqol[1])


result_timecard_json = {
    "id": result_timecard_id,
    "created": created_time_string,
    "result_id": result_id,
    "name": "timecard name",
    "start": 12314,
    "end": 4123,
}


def check_result_timecard_params(params: ResultTimecardParams):
    assert params.result_timecard_id == result_timecard_id
    assert params.created == created_time
    assert params.result_id == result_id
    assert params.name == "timecard name"
    assert params.start == 12314
    assert params.end == 4123


data_sync_json = {
    "result_timecards": [
        result_timecard_json,
        result_timecard_json,
    ]
}


def check_result_data_sync_params(params: DataSyncParams):
    assert len(params.result_timecards) == 2
    check_result_timecard_params(params.result_timecards[0])
    check_result_timecard_params(params.result_timecards[1])


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


def check_run_participant_params(params: RunParticipantParams):
    assert params.run_participant_id == run_participant_id
    assert params.run_id == run_id
    assert params.created == created_time
    assert params.updated == updated_time
    assert params.participant_num == 123
    assert params.participant_name == "participant name"
    assert params.group_num == 23
    assert params.group_name == "group name"
    assert params.compute_unit == ComputeUnit.CU_G4
    assert params.audio_feed == AudioFeed.AF_SILENCE
    assert params.browser == Browser.B_CHROMELATEST
    assert params.location == Location.L_EU_CENTRAL_1
    assert params.network == Network.N_4G
    assert params.video_feed == VideoFeed.VF_480P_15FPS


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
}


def check_result_params(params: ResultParams):
    assert params.result_id == result_id
    assert params.created == created_time
    assert params.updated == updated_time
    assert params.start == start_time
    assert params.end == end_time
    assert params.status == ResultStatus.RS_TIMEOUT
    assert params.selenium_result == ResultStatus.RS_ABORTED
    assert params.mos_status == MetricStatus.MS_CALCULATING
    check_run_participant_params(params.participant_details)


extended_result_json = result_json.copy()
extended_result_json.update(
    {
        "log_paths": result_log_json,
        "asserts": [result_assert_json, result_assert_json],
        "artifacts": artifacts_info_json,
        "metrics": metrics_json,
        "mos": mean_opinion_scores_json,
        "data_sync": data_sync_json,
    }
)


def check_extended_result_params(params: ResultParams):
    check_result_params(params)

    check_result_log_params(params.log_paths)

    assert len(params.asserts) == 2
    for ret in params.asserts:
        check_result_assert_params(ret)

    check_artifacts_info_params(params.artifacts)

    check_metrics_params(params.metrics)

    check_mean_opinion_scores_params(params.mos)

    check_result_data_sync_params(params.data_sync)


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
    assert params.precondition_property == Property.P_GROUP_NUM
