"""Common data shared between tests"""

# pylint: disable=missing-function-docstring
# pylint: disable=unused-variable


from dateutil import parser
from loadero_python.resources.assert_resource import AssertParams
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
    FileType,
    PaymentPlan,
    PaymentStatus,
    MemberRole,
    Language,
    TestDuration,
)
from loadero_python.resources.test import TestParams, Script
from loadero_python.resources.group import GroupParams
from loadero_python.resources.file import FileParams
from loadero_python.resources.project import (
    PlanLimitsParams,
    SubscriptionSettingsParams,
    SubscriptionParams,
    ProjectComputeUnitUsageParams,
    ProjectParams,
)
from loadero_python.resources.pagination import PaginationParams
from loadero_python.resources.resource import FilterKey, QueryParams

API_BASE = "http://mock.loadero.api/v2/"
ACCESS_TOKEN = "LOADERO_PROJECT_ACCESS_TOKEN"
PROJECT_ID = 538591
GROUP_ID = 34421
TEST_ID = 12734
FILE_ID = 923
PARTICIPANT_ID = 92559
ASSERT_ID = 29643
RUN_ID = 937561
RESULT_LOG_ID = 552648
RESULT_ID = 992341
RESULT_ASSERT_ID = 9876231
RUN_ASSERT_ID = 871342
METRIC_ID = 912388482
RESULT_MOS_ID = 99283476
RESULT_TIMECARD_ID = 88277471
RUN_PARTICIPANT_ID = 233992
PROFILE_ID = 87
ASSERT_PRECONDITION_ID = 9862123
SUBSCRIPTION_ID = 71984
AWS_INFO_ID = 9929311

SCRIPT = Script(content="pytest test script")
# Relative to repo root dir.
SCRIPT_FILE_PATH = "tests_unit/res/sample_test_script.py"
SCRIPT_FILE_DATA = """def test_on_loadero(driver: TestUIDriver):
    print("hello test")
"""


CREATED_TIME_STRING = "2022-04-01T13:54:25.689Z"
CREATED_TIME = parser.parse(CREATED_TIME_STRING)

UPDATED_TIME_STRING = "2024-02-03T15:42:54.689Z"
UPDATED_TIME = parser.parse(UPDATED_TIME_STRING)


LIMIT = 332
OFFSET = 931

PAGINATION_JSON = {
    "limit": LIMIT,
    "offset": OFFSET,
    "page": 991201,
    "total_pages": 9231,
    "total_items": 9283411,
}


def check_pagination_params(params: PaginationParams):
    assert params.limit == LIMIT
    assert params.offset == OFFSET
    assert params.page == 991201
    assert params.total_pages == 9231
    assert params.total_items == 9283411


FILTER_JSON = {
    "compute_unit": ["g6", "g1"],
    "name": "clever name",
    "selenium_result": ["pass"],
    "count_from": 431,
}


PAGED_RESPONSE_JSON = {
    "filter": FILTER_JSON,
    "pagination": PAGINATION_JSON,
    "results": [],
}


PARTICIPANT_JSON = {
    "id": PARTICIPANT_ID,
    "group_id": GROUP_ID,
    "test_id": TEST_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
    "profile_id": PROFILE_ID,
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
    assert params.participant_id == PARTICIPANT_ID
    assert params.group_id == GROUP_ID
    assert params.test_id == TEST_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
    assert params.count == 3
    assert not params.record_audio
    assert params.name == "pytest participant"
    assert params.compute_unit == ComputeUnit.CU_G4
    assert params.audio_feed == AudioFeed.AF_SILENCE
    assert params.browser == Browser.B_CHROMELATEST
    assert params.location == Location.L_EU_CENTRAL_1
    assert params.network == Network.N_4G
    assert params.video_feed == VideoFeed.VF_480P_15FPS


GROUP_JSON = {
    "count": 8,
    "created": CREATED_TIME_STRING,
    "id": GROUP_ID,
    "name": "pytest_group",
    "test_id": TEST_ID,
    "updated": UPDATED_TIME_STRING,
    "total_cu_count": 1234,
    "participant_count": 331,
}


def check_group_params(params: GroupParams):
    assert params.group_id == GROUP_ID
    assert params.created == CREATED_TIME
    assert params.name == "pytest_group"
    assert params.test_id == TEST_ID
    assert params.updated == UPDATED_TIME
    assert params.count == 8
    assert params.total_cu_count == 1234
    assert params.participant_count == 331


ASSERT_JSON = {
    "id": ASSERT_ID,
    "test_id": TEST_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
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
    assert params.assert_id == ASSERT_ID
    assert params.test_id == TEST_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
    assert params.expected == "892"
    assert params.operator is Operator.O_GT
    assert params.path is MetricPath.MACHINE_NETWORK_BITRATE_IN_AVG


test_json = {
    "id": TEST_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
    "increment_strategy": "linear",
    "mode": "load",
    "name": "pytest test",
    "participant_timeout": 13,
    "project_id": PROJECT_ID,
    "script_file_id": 65,
    "start_interval": 12,
    "group_count": 52,
    "participant_count": 9355,
}


def check_test_params(params: TestParams, with_script: bool = True):
    assert params.test_id == TEST_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
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


FILE_JSON = {
    "id": FILE_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
    "file_type": "test_script",
    "content": "pytest test script",
    "project_id": PROJECT_ID,
}


def check_file_params(params: FileParams):
    assert params.file_id == FILE_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
    assert params.file_type is FileType.FT_TEST_SCRIPT
    assert params.content == "pytest test script"


EXECUTION_STARTED_STRING = "2021-02-26T14:53:24.228Z"
EXECUTION_STARTED = parser.parse(EXECUTION_STARTED_STRING)

EXECUTION_FINISHED_STRING = "2023-06-26T19:38:25.268Z"
EXECUTION_FINISHED = parser.parse(EXECUTION_FINISHED_STRING)

PROCESSING_STARTED_STRING = "2025-07-29T19:31:29.468Z"
PROCESSING_STARTED = parser.parse(PROCESSING_STARTED_STRING)

PROCESSING_FINISHED_STRING = "2019-07-09T18:39:30.488Z"
PROCESSING_FINISHED = parser.parse(PROCESSING_FINISHED_STRING)

RUN_JSON = {
    "id": RUN_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
    "test_id": TEST_ID,
    "status": "done",
    "metric_status": "calculating",
    "mos_status": "available",
    "test_mode": "load",
    "increment_strategy": "linear",
    "processing_started": PROCESSING_STARTED_STRING,
    "processing_finished": PROCESSING_FINISHED_STRING,
    "execution_started": EXECUTION_STARTED_STRING,
    "execution_finished": EXECUTION_FINISHED_STRING,
    "script_file_id": FILE_ID,
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
    assert params.run_id == RUN_ID
    assert params.test_id == TEST_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
    assert params.status == RunStatus.RS_DONE
    assert params.metric_status == MetricStatus.MS_CALCULATING
    assert params.mos_status == MetricStatus.MS_AVAILABLE
    assert params.test_mode == TestMode.TM_LOAD
    assert params.increment_strategy == IncrementStrategy.IS_LINEAR
    assert params.processing_started == PROCESSING_STARTED
    assert params.processing_finished == PROCESSING_FINISHED
    assert params.execution_started == EXECUTION_STARTED
    assert params.execution_finished == EXECUTION_FINISHED
    assert params.script_file_id == FILE_ID
    assert params.test_name == "pytest test"
    assert params.start_interval == 98
    assert params.participant_timeout == 92
    assert params.launching_account_id == 12
    assert params.success_rate == 0.3
    assert params.total_cu_count == 3.3
    assert params.group_count == 5
    assert params.participant_count == 89
    assert params.mos_test is True


RESULT_LOG_JSON = {
    "id": RESULT_LOG_ID,
    "created": CREATED_TIME_STRING,
    "result_id": RESULT_ID,
    "webrtc": "webrtc_log.txt",
    "selenium": "selenium_log.txt",
    "browser": "browser_log.txt",
    "rru": "rru_log.txt",
    "allure_report": "allure_report_log.txt",
}


def check_result_log_params(params: ResultLogParams):
    assert params.result_log_id == RESULT_LOG_ID
    assert params.created == CREATED_TIME
    assert params.result_id == RESULT_ID
    assert params.webrtc == "webrtc_log.txt"
    assert params.selenium == "selenium_log.txt"
    assert params.browser == "browser_log.txt"
    assert params.rru == "rru_log.txt"
    assert params.allure_report == "allure_report_log.txt"


RESULT_ASSERT_JSON = {
    "path": "machine/cpu/available/total",
    "operator": "gt",
    "expected": "value",
    "id": RESULT_ASSERT_ID,
    "created": CREATED_TIME_STRING,
    "result_id": RESULT_ID,
    "run_assert_id": RUN_ASSERT_ID,
    "actual": "actual",
    "status": "fail",
    "message": "message",
}


def check_result_assert_params(params: ResultAssertParams):
    assert params.result_assert_id == RESULT_ASSERT_ID
    assert params.path == MetricPath.MACHINE_CPU_AVAILABLE_TOTAL
    assert params.operator == Operator.O_GT
    assert params.expected == "value"
    assert params.created == CREATED_TIME
    assert params.result_id == RESULT_ID
    assert params.actual == "actual"
    assert params.status == AssertStatus.AS_FAIL
    assert params.message == "message"


ARTIFACT_INFO_JSON = {
    "paths": [
        "artifact_path1",
        "artifact_path2",
    ],
    "error": "artifact error",
}

ARTIFACTS_INFO_JSON = {
    "audio": ARTIFACT_INFO_JSON,
    "downloads": {},
    "screenshots": ARTIFACT_INFO_JSON,
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


METRIC_JSON = {
    "id": METRIC_ID,
    "created": CREATED_TIME_STRING,
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
    assert params.metric_id == METRIC_ID
    assert params.created == CREATED_TIME
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


METRICS_JSON = {
    "machine": {
        "machine/cpu/available": METRIC_JSON,
        "machine/ram/percent": METRIC_JSON,
    },
    "webrtc": {
        "webrtc/audio/codec/in": METRIC_JSON,
        "webrtc/audio/rtt": METRIC_JSON,
    },
}


def check_metrics_params(params: MetricsParams):
    assert len(params.machine) == 2
    assert len(params.webrtc) == 2

    check_metric_params(params.machine[MetricBasePath.MACHINE_CPU_AVAILABLE])
    check_metric_params(params.machine[MetricBasePath.MACHINE_RAM_PERCENT])
    check_metric_params(params.webrtc[MetricBasePath.WEBRTC_AUDIO_CODEC_IN])
    check_metric_params(params.webrtc[MetricBasePath.WEBRTC_AUDIO_RTT])


START_TIME_STRING = "2018-03-02T11:34:28.689Z"
START_TIME = parser.parse(START_TIME_STRING)

END_TIME_STRING = "2020-08-01T18:12:24.689Z"
END_TIME = parser.parse(END_TIME_STRING)


RESULT_MOS_JSON = {
    "id": RESULT_MOS_ID,
    "created": CREATED_TIME_STRING,
    "result_id": RESULT_ID,
    "algorithm": "visqol",
    "score": 3.2,
    "start": START_TIME_STRING,
    "end": END_TIME_STRING,
}


def check_result_mos_params(params: ResultMOSParams):
    assert params.result_mos_id == RESULT_MOS_ID
    assert params.created == CREATED_TIME
    assert params.result_id == RESULT_ID
    assert params.algorithm == MosAlgorithm.MA_VISQOL
    assert params.score == 3.2
    assert params.start == START_TIME
    assert params.end == END_TIME


MEAN_OPINION_SCORES_JSON = {
    "visqol": [
        RESULT_MOS_JSON,
        RESULT_MOS_JSON,
    ],
}


def check_mean_opinion_scores_params(params: MeanOpinionScoresParams):
    assert len(params.visqol) == 2
    check_result_mos_params(params.visqol[0])
    check_result_mos_params(params.visqol[1])


RESULT_TIMECARD_JSON = {
    "id": RESULT_TIMECARD_ID,
    "created": CREATED_TIME_STRING,
    "result_id": RESULT_ID,
    "name": "timecard name",
    "start": 12314,
    "end": 4123,
}


def check_result_timecard_params(params: ResultTimecardParams):
    assert params.result_timecard_id == RESULT_TIMECARD_ID
    assert params.created == CREATED_TIME
    assert params.result_id == RESULT_ID
    assert params.name == "timecard name"
    assert params.start == 12314
    assert params.end == 4123


DATA_SYNC_JSON = {
    "result_timecards": [
        RESULT_TIMECARD_JSON,
        RESULT_TIMECARD_JSON,
    ]
}


def check_result_data_sync_params(params: DataSyncParams):
    assert len(params.result_timecards) == 2
    check_result_timecard_params(params.result_timecards[0])
    check_result_timecard_params(params.result_timecards[1])


RUN_PARTICIPANT_JSON = {
    "id": RUN_PARTICIPANT_ID,
    "updated": UPDATED_TIME_STRING,
    "created": CREATED_TIME_STRING,
    "run_id": RUN_ID,
    "group_name": "group name",
    "group_num": 23,
    "participant_name": "participant name",
    "participant_num": 123,
    "profile_id": PROFILE_ID,
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
    assert params.run_participant_id == RUN_PARTICIPANT_ID
    assert params.run_id == RUN_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
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


RESULT_JSON = {
    "id": RESULT_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
    "start": START_TIME_STRING,
    "end": END_TIME_STRING,
    "status": "timeout",
    "selenium_result": "aborted",
    "mos_status": "calculating",
    "participant_details": RUN_PARTICIPANT_JSON,
}


def check_result_params(params: ResultParams):
    assert params.result_id == RESULT_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
    assert params.start == START_TIME
    assert params.end == END_TIME
    assert params.status == ResultStatus.RS_TIMEOUT
    assert params.selenium_result == ResultStatus.RS_ABORTED
    assert params.mos_status == MetricStatus.MS_CALCULATING
    check_run_participant_params(params.participant_details)


EXTENDED_RESULT_JSON = RESULT_JSON.copy()
EXTENDED_RESULT_JSON.update(
    {
        "log_paths": RESULT_LOG_JSON,
        "asserts": [RESULT_ASSERT_JSON, RESULT_ASSERT_JSON],
        "artifacts": ARTIFACTS_INFO_JSON,
        "metrics": METRICS_JSON,
        "mos": MEAN_OPINION_SCORES_JSON,
        "data_sync": DATA_SYNC_JSON,
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

ASSERT_PRECONDITION_JSON = {
    "assert_id": ASSERT_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
    "expected": "10",
    "id": ASSERT_PRECONDITION_ID,
    "operator": "gt",
    "property": "group_num",
}

ASSERT_PRECONDITION_REQUEST_JSON = {
    "expected": "10",
    "operator": "gt",
    "property": "group_num",
}


def check_assert_precondition_params(params: AssertPreconditionParams):
    assert params.assert_precondition_id == ASSERT_PRECONDITION_ID
    assert params.assert_id == ASSERT_ID
    assert params.test_id == TEST_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
    assert params.expected == "10"
    assert params.operator == Operator.O_GT
    assert params.precondition_property == Property.P_GROUP_NUM


PLAN_LIMITS_JSON = {
    "plan_duration": "24h",
    "max_test_duration": "23h",
    "included_test_duration": "22h",
    "max_test_cu": 50,
    "max_monthly_cu": 500,
    "included_compute_units": 13,
    "mos_enabled": True,
    "locations": ["eu-central-1", "eu-west-1"],
    "compute_units": ["g1", "g6"],
    "browsers": ["chromeLatest", "firefoxLatest"],
    "api_access": True,
    "aws_access": False,
    "session_recording_access": True,
    "assert_preconditions_access": True,
}


def check_plan_limits_params(params: PlanLimitsParams):
    assert params.plan_duration == "24h"
    assert params.max_test_duration == "23h"
    assert params.included_test_duration == "22h"
    assert params.max_test_cu == 50
    assert params.max_monthly_cu == 500
    assert params.included_compute_units == 13
    assert params.mos_enabled is True
    assert params.locations == [Location.L_EU_CENTRAL_1, Location.L_EU_WEST_1]
    assert params.compute_units == [ComputeUnit.CU_G1, ComputeUnit.CU_G6]
    assert params.browsers == [Browser.B_CHROMELATEST, Browser.B_FIREFOXLATEST]
    assert params.api_access is True
    assert params.aws_access is False
    assert params.session_recording_access is True
    assert params.assert_preconditions_access is True


SUBSCRIPTION_SETTINGS_JSON = {
    "max_participant_cu": "g4",
    "max_test_duration": "8h",
    "max_monthly_cu": 321,
    "max_test_cu": 92931,
    "mos_enabled": False,
}


def check_subscription_settings_params(params: SubscriptionSettingsParams):
    assert params.max_participant_cu == ComputeUnit.CU_G4
    assert params.max_test_duration == TestDuration.TD_8H
    assert params.max_monthly_cu == 321
    assert params.max_test_cu == 92931
    assert params.mos_enabled is False


SUBSCRIPTION_ACTIVATION_DATE_STRING = "2011-09-02T11:34:28.689Z"
SUBSCRIPTION_ACTIVATION_DATE = parser.parse(SUBSCRIPTION_ACTIVATION_DATE_STRING)

SUBSCRIPTION_JSON = {
    "subscription_id": SUBSCRIPTION_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
    "payment_plan": "single_pro",
    "activation_date": SUBSCRIPTION_ACTIVATION_DATE_STRING,
    "payment_status": "processing",
    "billing_email": "bill@email.com",
    "settings": SUBSCRIPTION_SETTINGS_JSON,
}


def check_subscription_params(params: SubscriptionParams):
    assert params.subscription_id == SUBSCRIPTION_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
    assert params.payment_plan == PaymentPlan.PP_SINGLE_PRO
    assert params.activation_date == SUBSCRIPTION_ACTIVATION_DATE
    assert params.payment_status == PaymentStatus.PS_PROCESSING
    assert params.billing_email == "bill@email.com"

    check_subscription_settings_params(params.settings)


PROJECT_COMPUTE_UNIT_USAGE_JSON = {
    "included": 293,
    "used": 9233,
}


def check_project_compute_unit_usage_params(
    params: ProjectComputeUnitUsageParams,
):
    assert params.included == 293
    assert params.used == 9233


PROJECT_JSON = {
    "id": PROJECT_ID,
    "created": CREATED_TIME_STRING,
    "updated": UPDATED_TIME_STRING,
    "name": "pytest project",
    "trial_expired": True,
    "member_count": 5,
    "account_role": "administrator",
    "language": "python",
    "aws_info_id": AWS_INFO_ID,
    "subscription_id": SUBSCRIPTION_ID,
    "plan_limits": PLAN_LIMITS_JSON,
    "subscription": SUBSCRIPTION_JSON,
    "compute_unit_usage": PROJECT_COMPUTE_UNIT_USAGE_JSON,
}


def check_project_params(params: ProjectParams):
    assert params.project_id == PROJECT_ID
    assert params.created == CREATED_TIME
    assert params.updated == UPDATED_TIME
    assert params.name == "pytest project"
    assert params.trial_expired is True
    assert params.member_count == 5
    assert params.account_role == MemberRole.MR_ADMINISTRATOR
    assert params.language == Language.L_PYTHON
    assert params.aws_info_id == AWS_INFO_ID
    assert params.subscription_id == SUBSCRIPTION_ID

    check_plan_limits_params(params.plan_limits)
    check_subscription_params(params.subscription)
    check_project_compute_unit_usage_params(params.compute_unit_usage)


QUERY_PARAM_VALUES = [
    CREATED_TIME,
    ComputeUnit.CU_G4,
    [Language.L_PYTHON, MemberRole.MR_ADMINISTRATOR],
    1,
    "pytest project",
    True,
]


def build_query_params(keys: list[FilterKey]) -> QueryParams:
    qp = QueryParams()

    qp.limit(LIMIT)
    qp.offset(OFFSET)

    for i, key in enumerate(keys):
        qp.filter(key, QUERY_PARAM_VALUES[i % len(QUERY_PARAM_VALUES)])

    return qp
