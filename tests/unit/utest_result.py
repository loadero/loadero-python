"""Result returned tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member


import json
import re
from urllib.parse import urlparse, parse_qs
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.result import (
    ResultAPI,
    ResultFilterKey,
    ResultLogParams,
    ResultAssertParams,
    ArtifactInfoParams,
    ArtifactsInfoParams,
    MetricParams,
    MetricsParams,
    ResultMOSParams,
    MeanOpinionScoresParams,
    ResultTimecardParams,
    DataSyncParams,
    ResultParams,
    Result,
)
from loadero_python.resources.metric_path import MetricPath, MetricBasePath
from loadero_python.resources.classificator import (
    MosAlgorithm,
    Operator,
    AssertStatus,
    ResultStatus,
    MetricStatus,
)
from loadero_python.resources.run_participant import RunParticipantParams
from . import common


class UTestResultLogParams:
    @staticmethod
    def utest_result_log_id():
        rl = ResultLogParams()
        rl.__dict__["_result_log_id"] = common.RESULT_LOG_ID
        assert rl.result_log_id == common.RESULT_LOG_ID

    @staticmethod
    def utest_created():
        rl = ResultLogParams()
        rl.__dict__["_created"] = common.CREATED_TIME
        assert rl.created == common.CREATED_TIME

    @staticmethod
    def utest_result_id():
        rl = ResultLogParams()
        rl.__dict__["_result_id"] = common.RESULT_ID
        assert rl.result_id == common.RESULT_ID

    @staticmethod
    def utest_webrtc():
        rl = ResultLogParams()
        rl.__dict__["_webrtc"] = "webrtc_log.txt"
        assert rl.webrtc == "webrtc_log.txt"

    @staticmethod
    def utest_selenium():
        rl = ResultLogParams()
        rl.__dict__["_selenium"] = "selenium_log.txt"
        assert rl.selenium == "selenium_log.txt"

    @staticmethod
    def utest_browser():
        rl = ResultLogParams()
        rl.__dict__["_browser"] = "browser_log.txt"
        assert rl.browser == "browser_log.txt"

    @staticmethod
    def utest_rru():
        rl = ResultLogParams()
        rl.__dict__["_rru"] = "rru_log.txt"
        assert rl.rru == "rru_log.txt"

    @staticmethod
    def utest_allure_report():
        rl = ResultLogParams()
        rl.__dict__["_allure_report"] = "allure_report_log.txt"
        assert rl.allure_report == "allure_report_log.txt"

    @staticmethod
    def utest_str():
        rl = ResultLogParams()
        rl.from_dict(common.RESULT_LOG_JSON)

        assert (
            str(rl)
            == """{
    "id": 552648,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "result_id": 992341,
    "webrtc": "webrtc_log.txt",
    "selenium": "selenium_log.txt",
    "browser": "browser_log.txt",
    "rru": "rru_log.txt",
    "allure_report": "allure_report_log.txt"
}"""
        )


class UTestResultAssert:
    @staticmethod
    def utest_result_assert_id():
        ra = ResultAssertParams()
        ra.__dict__["_result_assert_id"] = common.RESULT_ASSERT_ID
        assert ra.result_assert_id == common.RESULT_ASSERT_ID

    @staticmethod
    def utest_created():
        ra = ResultAssertParams()
        ra.__dict__["_created"] = common.CREATED_TIME
        assert ra.created == common.CREATED_TIME

    @staticmethod
    def utest_path():
        ra = ResultAssertParams()
        ra.__dict__["_path"] = MetricPath.MACHINE_CPU_AVAILABLE_TOTAL
        assert ra.path == MetricPath.MACHINE_CPU_AVAILABLE_TOTAL

    @staticmethod
    def utest_operator():
        ra = ResultAssertParams()
        ra.__dict__["_operator"] = Operator.O_GT
        assert ra.operator == Operator.O_GT

    @staticmethod
    def utest_expected():
        ra = ResultAssertParams()
        ra.__dict__["_expected"] = "value"
        assert ra.expected == "value"

    @staticmethod
    def utest_result_id():
        ra = ResultAssertParams()
        ra.__dict__["_result_id"] = common.RESULT_ID
        assert ra.result_id == common.RESULT_ID

    @staticmethod
    def utest_run_assert_id():
        ra = ResultAssertParams()
        ra.__dict__["_run_assert_id"] = common.RUN_ASSERT_ID
        assert ra.run_assert_id == common.RUN_ASSERT_ID

    @staticmethod
    def utest_message():
        ra = ResultAssertParams()
        ra.__dict__["_message"] = "message"
        assert ra.message == "message"

    @staticmethod
    def utest_actual():
        ra = ResultAssertParams()
        ra.__dict__["_actual"] = "actual"
        assert ra.actual == "actual"

    @staticmethod
    def utest_status():
        ra = ResultAssertParams()
        ra.__dict__["_status"] = AssertStatus.AS_FAIL
        assert ra.status == AssertStatus.AS_FAIL

    @staticmethod
    def utest_str():
        ra = ResultAssertParams()
        ra.from_dict(common.RESULT_ASSERT_JSON)

        assert (
            str(ra)
            == """{
    "id": 9876231,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "path": "machine/cpu/available/total",
    "operator": "gt",
    "expected": "value",
    "result_id": 992341,
    "run_assert_id": 871342,
    "message": "message",
    "actual": "actual",
    "status": "fail"
}"""
        )


class UTestArtifactInfoParams:
    @staticmethod
    def utest_error():
        ai = ArtifactInfoParams()
        ai.__dict__["_error"] = "error"
        assert ai.error == "error"

    @staticmethod
    def utest_paths():
        ai = ArtifactInfoParams()
        ai.__dict__["_paths"] = ["path1", "path2"]
        assert ai.paths == ["path1", "path2"]

    @staticmethod
    def utest_str():
        ai = ArtifactInfoParams()
        ai.from_dict(common.ARTIFACT_INFO_JSON)

        assert (
            str(ai)
            == """{
    "error": "artifact error",
    "paths": [
        "artifact_path1",
        "artifact_path2"
    ]
}"""
        )


class UTestArtifactsInfoParams:
    @staticmethod
    def utest_audio():
        a = ArtifactInfoParams()
        a.from_dict(common.ARTIFACT_INFO_JSON)

        ai = ArtifactsInfoParams()
        ai.__dict__["_audio"] = a
        assert ai.audio == a

    @staticmethod
    def utest_dowloads():
        a = ArtifactInfoParams()
        a.from_dict(common.ARTIFACT_INFO_JSON)

        ai = ArtifactsInfoParams()
        ai.__dict__["_downloads"] = a
        assert ai.downloads == a

    @staticmethod
    def utest_screenshots():
        a = ArtifactInfoParams()
        a.from_dict(common.ARTIFACT_INFO_JSON)

        ai = ArtifactsInfoParams()
        ai.__dict__["_screenshots"] = a
        assert ai.screenshots == a

    @staticmethod
    def utest_video():
        a = ArtifactInfoParams()
        a.from_dict(common.ARTIFACT_INFO_JSON)

        ai = ArtifactsInfoParams()
        ai.__dict__["_video"] = a
        assert ai.video == a

    @staticmethod
    def utest_str():
        ai = ArtifactsInfoParams()
        ai.from_dict(common.ARTIFACTS_INFO_JSON)

        assert (
            str(ai)
            == """{
    "audio": {
        "error": "artifact error",
        "paths": [
            "artifact_path1",
            "artifact_path2"
        ]
    },
    "downloads": {},
    "screenshots": {
        "error": "artifact error",
        "paths": [
            "artifact_path1",
            "artifact_path2"
        ]
    },
    "video": {}
}"""
        )


class UTestMetricParams:
    @staticmethod
    def utest_metric_id():
        m = MetricParams()
        m.__dict__["_metric_id"] = common.METRIC_ID
        assert m.metric_id == common.METRIC_ID

    @staticmethod
    def utest_created():
        m = MetricParams()
        m.__dict__["_created"] = common.CREATED_TIME
        assert m.created == common.CREATED_TIME

    @staticmethod
    def utest_data_count():
        m = MetricParams()
        m.__dict__["_data_count"] = 5
        assert m.data_count == 5

    @staticmethod
    def utest_metric_path():
        m = MetricParams()
        m.__dict__["_metric_path"] = MetricBasePath.MACHINE_CPU_USED
        assert m.metric_path == MetricBasePath.MACHINE_CPU_USED

    @staticmethod
    def utest_value():
        m = MetricParams()
        m.__dict__["_value"] = "value"
        assert m.value == "value"

    @staticmethod
    def utest_total():
        m = MetricParams()
        m.__dict__["_total"] = 9.8
        assert m.total == 9.8

    @staticmethod
    def utest_minimum():
        m = MetricParams()
        m.__dict__["_minimum"] = 9.8
        assert m.minimum == 9.8

    @staticmethod
    def utest_maximum():
        m = MetricParams()
        m.__dict__["_maximum"] = 9.8
        assert m.maximum == 9.8

    @staticmethod
    def utest_average():
        m = MetricParams()
        m.__dict__["_average"] = 9.8
        assert m.average == 9.8

    @staticmethod
    def utest_stddev():
        m = MetricParams()
        m.__dict__["_stddev"] = 9.8
        assert m.stddev == 9.8

    @staticmethod
    def utest_rstddev():
        m = MetricParams()
        m.__dict__["_rstddev"] = 9.8
        assert m.rstddev == 9.8

    @staticmethod
    def utest_perc_1st():
        m = MetricParams()
        m.__dict__["_perc_1st"] = 9.8
        assert m.perc_1st == 9.8

    @staticmethod
    def utest_perc_5th():
        m = MetricParams()
        m.__dict__["_perc_5th"] = 9.8
        assert m.perc_5th == 9.8

    @staticmethod
    def utest_perc_25th():
        m = MetricParams()
        m.__dict__["_perc_25th"] = 9.8
        assert m.perc_25th == 9.8

    @staticmethod
    def utest_perc_50th():
        m = MetricParams()
        m.__dict__["_perc_50th"] = 9.8
        assert m.perc_50th == 9.8

    @staticmethod
    def utest_perc_75th():
        m = MetricParams()
        m.__dict__["_perc_75th"] = 9.8
        assert m.perc_75th == 9.8

    @staticmethod
    def utest_prec_95th():
        m = MetricParams()
        m.__dict__["_perc_95th"] = 9.8
        assert m.perc_95th == 9.8

    @staticmethod
    def utest_perc_99th():
        m = MetricParams()
        m.__dict__["_perc_99th"] = 9.8
        assert m.perc_99th == 9.8

    @staticmethod
    def utest_str():
        m = MetricParams()
        m.from_dict(common.METRIC_JSON)

        assert (
            str(m)
            == """{
    "id": 912388482,
    "created": "2022-04-01 13:54:25.689000+00:00",
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
    "perc_99th": 75
}"""
        )


class UTestMetricsParams:
    @staticmethod
    def utest_machine():
        m = MetricsParams()
        d = {
            MetricBasePath.MACHINE_CPU_USED: MetricParams(),
        }
        m.__dict__["_machine"] = d
        assert m.machine == d

    @staticmethod
    def utest_webrtc():
        m = MetricsParams()
        d = {
            MetricBasePath.WEBRTC_AUDIO_CODEC_IN: MetricParams(),
        }
        m.__dict__["_webrtc"] = d
        assert m.webrtc == d

    @staticmethod
    def utest_str():
        m = MetricsParams()
        m.from_dict(common.METRICS_JSON)

        assert (
            str(m)
            == """{
    "machine": {
        "machine/cpu/available": {
            "id": 912388482,
            "created": "2022-04-01 13:54:25.689000+00:00",
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
            "perc_99th": 75
        },
        "machine/ram/percent": {
            "id": 912388482,
            "created": "2022-04-01 13:54:25.689000+00:00",
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
            "perc_99th": 75
        }
    },
    "webrtc": {
        "webrtc/audio/codec/in": {
            "id": 912388482,
            "created": "2022-04-01 13:54:25.689000+00:00",
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
            "perc_99th": 75
        },
        "webrtc/audio/rtt": {
            "id": 912388482,
            "created": "2022-04-01 13:54:25.689000+00:00",
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
            "perc_99th": 75
        }
    }
}"""
        )

    @staticmethod
    def utest_to_dict():
        m = MetricsParams()
        m.from_dict(common.METRICS_JSON)

        assert not m.to_dict()


class UTestResultMOSParams:
    @staticmethod
    def utest_result_mos_id():
        m = ResultMOSParams()
        m.__dict__["_result_mos_id"] = common.RESULT_MOS_ID
        assert m.result_mos_id == common.RESULT_MOS_ID

    @staticmethod
    def utest_created():
        m = ResultMOSParams()
        m.__dict__["_created"] = common.CREATED_TIME
        assert m.created == common.CREATED_TIME

    @staticmethod
    def utest_result_id():
        m = ResultMOSParams()
        m.__dict__["_result_id"] = common.RESULT_ID
        assert m.result_id == common.RESULT_ID

    @staticmethod
    def utest_algorithm():
        m = ResultMOSParams()
        m.__dict__["_algorithm"] = MosAlgorithm.MA_VISQOL
        assert m.algorithm == MosAlgorithm.MA_VISQOL

    @staticmethod
    def utest_score():
        m = ResultMOSParams()
        m.__dict__["_score"] = 4.123
        assert m.score == 4.123

    @staticmethod
    def utest_start():
        m = ResultMOSParams()
        m.__dict__["_start"] = common.START_TIME
        assert m.start == common.START_TIME

    @staticmethod
    def utest_end():
        m = ResultMOSParams()
        m.__dict__["_end"] = common.END_TIME
        assert m.end == common.END_TIME

    @staticmethod
    def utest_str():
        m = ResultMOSParams()
        m.from_dict(common.RESULT_MOS_JSON)

        assert (
            str(m)
            == """{
    "id": 99283476,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "result_id": 992341,
    "algorithm": "visqol",
    "score": 3.2,
    "start": "2018-03-02 11:34:28.689000+00:00",
    "end": "2020-08-01 18:12:24.689000+00:00"
}"""
        )


class UTestMeanOpinionScoresParams:
    @staticmethod
    def utest_visqol():
        m = MeanOpinionScoresParams()
        l = [ResultMOSParams(), ResultMOSParams()]
        m.__dict__["_visqol"] = l
        assert m.visqol == l

    @staticmethod
    def utest_str():
        m = MeanOpinionScoresParams()
        m.from_dict(common.MEAN_OPINION_SCORES_JSON)

        assert (
            str(m)
            == """{
    "visqol": [
        {
            "id": 99283476,
            "created": "2022-04-01 13:54:25.689000+00:00",
            "result_id": 992341,
            "algorithm": "visqol",
            "score": 3.2,
            "start": "2018-03-02 11:34:28.689000+00:00",
            "end": "2020-08-01 18:12:24.689000+00:00"
        },
        {
            "id": 99283476,
            "created": "2022-04-01 13:54:25.689000+00:00",
            "result_id": 992341,
            "algorithm": "visqol",
            "score": 3.2,
            "start": "2018-03-02 11:34:28.689000+00:00",
            "end": "2020-08-01 18:12:24.689000+00:00"
        }
    ]
}"""
        )

    @staticmethod
    def utest_to_dict():
        m = MeanOpinionScoresParams()
        m.from_dict(common.MEAN_OPINION_SCORES_JSON)

        assert not m.to_dict()


class UTestResultTimecardParams:
    @staticmethod
    def utest_result_timecard_id():
        m = ResultTimecardParams()
        m.__dict__["_result_timecard_id"] = common.RESULT_TIMECARD_ID
        assert m.result_timecard_id == common.RESULT_TIMECARD_ID

    @staticmethod
    def utest_created():
        m = ResultTimecardParams()
        m.__dict__["_created"] = common.CREATED_TIME
        assert m.created == common.CREATED_TIME

    @staticmethod
    def utest_result_id():
        m = ResultTimecardParams()
        m.__dict__["_result_id"] = common.RESULT_ID
        assert m.result_id == common.RESULT_ID

    @staticmethod
    def utest_test_name():
        m = ResultTimecardParams()
        m.__dict__["_name"] = "tc name"
        assert m.name == "tc name"

    @staticmethod
    def utest_start():
        m = ResultTimecardParams()
        m.__dict__["_start"] = 123
        assert m.start == 123

    @staticmethod
    def utest_end():
        m = ResultTimecardParams()
        m.__dict__["_end"] = 123
        assert m.end == 123

    @staticmethod
    def utest_str():
        m = ResultTimecardParams()
        m.from_dict(common.RESULT_TIMECARD_JSON)

        assert (
            str(m)
            == """{
    "id": 88277471,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "result_id": 992341,
    "name": "timecard name",
    "start": 12314,
    "end": 4123
}"""
        )


class UTestDataSyncParams:
    @staticmethod
    def utest_result_timecards():
        m = DataSyncParams()
        l = [ResultTimecardParams(), ResultTimecardParams()]
        m.__dict__["_result_timecards"] = l
        assert m.result_timecards == l

    @staticmethod
    def utest_str():
        m = DataSyncParams()
        m.from_dict(common.DATA_SYNC_JSON)

        assert (
            str(m)
            == """{
    "result_timecards": [
        {
            "id": 88277471,
            "created": "2022-04-01 13:54:25.689000+00:00",
            "result_id": 992341,
            "name": "timecard name",
            "start": 12314,
            "end": 4123
        },
        {
            "id": 88277471,
            "created": "2022-04-01 13:54:25.689000+00:00",
            "result_id": 992341,
            "name": "timecard name",
            "start": 12314,
            "end": 4123
        }
    ]
}"""
        )

    @staticmethod
    def utest_to_dict():
        m = DataSyncParams()
        m.from_dict(common.DATA_SYNC_JSON)

        assert not m.to_dict()


class UTestResultParams:
    @staticmethod
    def utest_created():
        m = ResultParams()
        m.__dict__["_created"] = common.CREATED_TIME
        assert m.created == common.CREATED_TIME

    @staticmethod
    def utest_updated():
        m = ResultParams()
        m.__dict__["_updated"] = common.UPDATED_TIME
        assert m.updated == common.UPDATED_TIME

    @staticmethod
    def utest_start():
        m = ResultParams()
        m.__dict__["_start"] = common.START_TIME
        assert m.start == common.START_TIME

    @staticmethod
    def utest_end():
        m = ResultParams()
        m.__dict__["_end"] = common.END_TIME
        assert m.end == common.END_TIME

    @staticmethod
    def utest_status():
        m = ResultParams()
        m.__dict__["_status"] = ResultStatus.RS_FAIL
        assert m.status == ResultStatus.RS_FAIL

    @staticmethod
    def utest_selenium_result():
        m = ResultParams()
        m.__dict__["_selenium_result"] = ResultStatus.RS_ABORTED
        assert m.selenium_result == ResultStatus.RS_ABORTED

    @staticmethod
    def utest_mos_status():
        m = ResultParams()
        m.__dict__["_mos_status"] = MetricStatus.MS_CALCULATING
        assert m.mos_status == MetricStatus.MS_CALCULATING

    @staticmethod
    def utest_participant_details():
        m = ResultParams()
        rpp = RunParticipantParams()
        m.__dict__["_participant_details"] = rpp
        assert m.participant_details == rpp

    @staticmethod
    def utest_log_paths():
        m = ResultParams()
        rlp = ResultLogParams()
        m.__dict__["_log_paths"] = rlp
        assert m.log_paths == rlp

    @staticmethod
    def utest_asserts():
        m = ResultParams()
        rap = ResultAssertParams()
        m.__dict__["_asserts"] = rap
        assert m.asserts == rap

    @staticmethod
    def utest_artifacts():
        m = ResultParams()
        aip = ArtifactsInfoParams()
        m.__dict__["_artifacts"] = aip
        assert m.artifacts == aip

    @staticmethod
    def utest_metrics():
        m = ResultParams()
        mp = MetricsParams()
        m.__dict__["_metrics"] = mp
        assert m.metrics == mp

    @staticmethod
    def utest_mos():
        m = ResultParams()
        mosp = MeanOpinionScoresParams()
        m.__dict__["_mos"] = mosp
        assert m.mos == mosp

    @staticmethod
    def utest_data_sync():
        m = ResultParams()
        rap = DataSyncParams()
        m.__dict__["_data_sync"] = rap
        assert m.data_sync == rap

    @staticmethod
    def utest_str():
        m = ResultParams()
        m.from_dict(common.EXTENDED_RESULT_JSON)

        print(m)

        assert (
            str(m)
            == """{
    "id": 992341,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00",
    "start": "2018-03-02 11:34:28.689000+00:00",
    "end": "2020-08-01 18:12:24.689000+00:00",
    "status": "timeout",
    "selenium_result": "aborted",
    "mos_status": "calculating",
    "participant_details": {
        "id": 233992,
        "run_id": 937561,
        "created": "2022-04-01 13:54:25.689000+00:00",
        "updated": "2024-02-03 15:42:54.689000+00:00",
        "participant_num": 123,
        "participant_name": "participant name",
        "group_num": 23,
        "group_name": "group name",
        "compute_unit": "g4",
        "audio_feed": "silence",
        "browser": "chromeLatest",
        "location": "eu-central-1",
        "network": "4g",
        "video_feed": "480p-15fps",
        "record_audio": true
    },
    "log_paths": {
        "id": 552648,
        "created": "2022-04-01 13:54:25.689000+00:00",
        "result_id": 992341,
        "webrtc": "webrtc_log.txt",
        "selenium": "selenium_log.txt",
        "browser": "browser_log.txt",
        "rru": "rru_log.txt",
        "allure_report": "allure_report_log.txt"
    },
    "asserts": [
        {
            "id": 9876231,
            "created": "2022-04-01 13:54:25.689000+00:00",
            "path": "machine/cpu/available/total",
            "operator": "gt",
            "expected": "value",
            "result_id": 992341,
            "run_assert_id": 871342,
            "message": "message",
            "actual": "actual",
            "status": "fail"
        },
        {
            "id": 9876231,
            "created": "2022-04-01 13:54:25.689000+00:00",
            "path": "machine/cpu/available/total",
            "operator": "gt",
            "expected": "value",
            "result_id": 992341,
            "run_assert_id": 871342,
            "message": "message",
            "actual": "actual",
            "status": "fail"
        }
    ],
    "artifacts": {
        "audio": {
            "error": "artifact error",
            "paths": [
                "artifact_path1",
                "artifact_path2"
            ]
        },
        "downloads": {},
        "screenshots": {
            "error": "artifact error",
            "paths": [
                "artifact_path1",
                "artifact_path2"
            ]
        },
        "video": {}
    },
    "metrics": {
        "machine": {
            "machine/cpu/available": {
                "id": 912388482,
                "created": "2022-04-01 13:54:25.689000+00:00",
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
                "perc_99th": 75
            },
            "machine/ram/percent": {
                "id": 912388482,
                "created": "2022-04-01 13:54:25.689000+00:00",
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
                "perc_99th": 75
            }
        },
        "webrtc": {
            "webrtc/audio/codec/in": {
                "id": 912388482,
                "created": "2022-04-01 13:54:25.689000+00:00",
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
                "perc_99th": 75
            },
            "webrtc/audio/rtt": {
                "id": 912388482,
                "created": "2022-04-01 13:54:25.689000+00:00",
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
                "perc_99th": 75
            }
        }
    },
    "mos": {
        "visqol": [
            {
                "id": 99283476,
                "created": "2022-04-01 13:54:25.689000+00:00",
                "result_id": 992341,
                "algorithm": "visqol",
                "score": 3.2,
                "start": "2018-03-02 11:34:28.689000+00:00",
                "end": "2020-08-01 18:12:24.689000+00:00"
            },
            {
                "id": 99283476,
                "created": "2022-04-01 13:54:25.689000+00:00",
                "result_id": 992341,
                "algorithm": "visqol",
                "score": 3.2,
                "start": "2018-03-02 11:34:28.689000+00:00",
                "end": "2020-08-01 18:12:24.689000+00:00"
            }
        ]
    },
    "data_sync": {
        "result_timecards": [
            {
                "id": 88277471,
                "created": "2022-04-01 13:54:25.689000+00:00",
                "result_id": 992341,
                "name": "timecard name",
                "start": 12314,
                "end": 4123
            },
            {
                "id": 88277471,
                "created": "2022-04-01 13:54:25.689000+00:00",
                "result_id": 992341,
                "name": "timecard name",
                "start": 12314,
                "end": 4123
            }
        ]
    }
}"""
        )


@pytest.fixture
def mock():
    httpretty.enable(allow_net_connect=False, verbose=True)
    httpretty.reset()

    APIClient(common.PROJECT_ID, common.ACCESS_TOKEN, common.API_BASE, False)

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/results/\d*/$"
        ),
        body=json.dumps(common.EXTENDED_RESULT_JSON),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all
    pg = common.PAGED_RESPONSE_JSON.copy()
    pg["results"] = [common.RESULT_JSON, common.RESULT_JSON]

    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/results/$"
        ),
        body=json.dumps(pg),
        forcing_headers={"Content-Type": "application/json"},
    )

    yield

    httpretty.disable()


@pytest.mark.usefixtures("mock")
class UTestResult:
    @staticmethod
    def utest_init_empty():
        r = Result()
        assert r.params is not None
        assert r.params.run_id is None
        assert r.params.result_id is None

    @staticmethod
    def utest_init_with_params():
        r = Result(run_id=5, params=ResultParams(4))
        assert r.params is not None
        assert r.params.run_id == 5
        assert r.params.result_id == 4

    @staticmethod
    def utest_init_with_ids():
        r = Result(run_id=5, result_id=4)
        assert r.params is not None
        assert r.params.run_id == 5
        assert r.params.result_id == 4

    @staticmethod
    def utest_read():
        common.check_result_params(
            Result(run_id=common.RUN_ID, result_id=common.RESULT_ID)
            .read()
            .params
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_invalid_run_id():
        r = Result(result_id=common.RESULT_ID)
        with pytest.raises(Exception):
            r.read()

    @staticmethod
    def utest_read_invalid_result_id():
        r = Result(run_id=common.RUN_ID)
        with pytest.raises(Exception):
            r.read()


@pytest.mark.usefixtures("mock")
class UTestResultAPI:
    @staticmethod
    def utest_read():
        common.check_extended_result_params(
            ResultAPI.read(
                ResultParams(run_id=common.RUN_ID, result_id=common.RESULT_ID)
            )
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all():
        resp = ResultAPI.read_all(common.RUN_ID)

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_result_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_read_all_with_query_params():
        resp = ResultAPI.read_all(
            common.RUN_ID, common.build_query_params(list(ResultFilterKey))
        )

        common.check_pagination_params(resp.pagination)
        assert resp.filter == common.FILTER_JSON

        assert len(resp.results) == 2

        for ret in resp.results:
            common.check_result_params(ret)

        assert (
            len(parse_qs(urlparse(httpretty.last_request().url).query))
            == len(ResultFilterKey) + 2
        )
        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    @staticmethod
    def utest_request_mos():
        with pytest.raises(Exception):
            ResultAPI.request_mos(common.RUN_ID, common.RESULT_ID)

    @staticmethod
    def utest_route():
        assert (
            ResultAPI.route(common.RUN_ID)
            == "projects/538591/runs/937561/results/"
        )

        assert (
            ResultAPI.route(common.RUN_ID, common.RESULT_ID)
            == "projects/538591/runs/937561/"
            "results/992341/"
        )
