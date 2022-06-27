"""Result returned tests"""


# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member

import json
import re
import pytest
import httpretty
from loadero_python.api_client import APIClient
from loadero_python.resources.result import (
    ResultAPI,
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
    def utest_result_log_id(self):
        rl = ResultLogParams()
        rl.__dict__["_result_log_id"] = common.result_log_id
        assert rl.result_log_id == common.result_log_id

    def utest_created(self):
        rl = ResultLogParams()
        rl.__dict__["_created"] = common.created_time
        assert rl.created == common.created_time

    def utest_result_id(self):
        rl = ResultLogParams()
        rl.__dict__["_result_id"] = common.result_id
        assert rl.result_id == common.result_id

    def utest_webrtc(self):
        rl = ResultLogParams()
        rl.__dict__["_webrtc"] = "webrtc_log.txt"
        assert rl.webrtc == "webrtc_log.txt"

    def utest_selenium(self):
        rl = ResultLogParams()
        rl.__dict__["_selenium"] = "selenium_log.txt"
        assert rl.selenium == "selenium_log.txt"

    def utest_browser(self):
        rl = ResultLogParams()
        rl.__dict__["_browser"] = "browser_log.txt"
        assert rl.browser == "browser_log.txt"

    def utest_rru(self):
        rl = ResultLogParams()
        rl.__dict__["_rru"] = "rru_log.txt"
        assert rl.rru == "rru_log.txt"

    def utest_allure_report(self):
        rl = ResultLogParams()
        rl.__dict__["_allure_report"] = "allure_report_log.txt"
        assert rl.allure_report == "allure_report_log.txt"

    def utest_str(self):
        rl = ResultLogParams()
        rl.from_dict(common.result_log_json)

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
    def utest_result_assert_id(self):
        ra = ResultAssertParams()
        ra.__dict__["_result_assert_id"] = common.result_assert_id
        assert ra.result_assert_id == common.result_assert_id

    def utest_created(self):
        ra = ResultAssertParams()
        ra.__dict__["_created"] = common.created_time
        assert ra.created == common.created_time

    def utest_path(self):
        ra = ResultAssertParams()
        ra.__dict__["_path"] = MetricPath.MACHINE_CPU_AVAILABLE_TOTAL
        assert ra.path == MetricPath.MACHINE_CPU_AVAILABLE_TOTAL

    def utest_operator(self):
        ra = ResultAssertParams()
        ra.__dict__["_operator"] = Operator.O_GT
        assert ra.operator == Operator.O_GT

    def utest_expected(self):
        ra = ResultAssertParams()
        ra.__dict__["_expected"] = "value"
        assert ra.expected == "value"

    def utest_result_id(self):
        ra = ResultAssertParams()
        ra.__dict__["_result_id"] = common.result_id
        assert ra.result_id == common.result_id

    def utest_run_assert_id(self):
        ra = ResultAssertParams()
        ra.__dict__["_run_assert_id"] = common.run_assert_id
        assert ra.run_assert_id == common.run_assert_id

    def utest_message(self):
        ra = ResultAssertParams()
        ra.__dict__["_message"] = "message"
        assert ra.message == "message"

    def utest_actual(self):
        ra = ResultAssertParams()
        ra.__dict__["_actual"] = "actual"
        assert ra.actual == "actual"

    def utest_status(self):
        ra = ResultAssertParams()
        ra.__dict__["_status"] = AssertStatus.AS_FAIL
        assert ra.status == AssertStatus.AS_FAIL

    def utest_str(self):
        ra = ResultAssertParams()
        ra.from_dict(common.result_assert_json)

        assert (
            str(ra)
            == """{
    "path": "machine/cpu/available/total",
    "operator": "gt",
    "expected": "value",
    "id": 9876231,
    "created": "2022-04-01 13:54:25.689000+00:00",
    "result_id": 992341,
    "run_assert_id": 871342,
    "actual": "actual",
    "status": "fail",
    "message": "message"
}"""
        )


class UTestArtifactInfoParams:
    def utest_error(self):
        ai = ArtifactInfoParams()
        ai.__dict__["_error"] = "error"
        assert ai.error == "error"

    def utest_paths(self):
        ai = ArtifactInfoParams()
        ai.__dict__["_paths"] = ["path1", "path2"]
        assert ai.paths == ["path1", "path2"]

    def utest_str(self):
        ai = ArtifactInfoParams()
        ai.from_dict(common.artifact_info_json)

        assert (
            str(ai)
            == """{
    "paths": [
        "artifact_path1",
        "artifact_path2"
    ],
    "error": "artifact error"
}"""
        )


class UTestArtifactsInfoParams:
    def utest_audio(self):
        a = ArtifactInfoParams()
        a.from_dict(common.artifact_info_json)

        ai = ArtifactsInfoParams()
        ai.__dict__["_audio"] = a
        assert ai.audio == a

    def utest_dowloads(self):
        a = ArtifactInfoParams()
        a.from_dict(common.artifact_info_json)

        ai = ArtifactsInfoParams()
        ai.__dict__["_downloads"] = a
        assert ai.downloads == a

    def utest_screenshots(self):
        a = ArtifactInfoParams()
        a.from_dict(common.artifact_info_json)

        ai = ArtifactsInfoParams()
        ai.__dict__["_screenshots"] = a
        assert ai.screenshots == a

    def utest_video(self):
        a = ArtifactInfoParams()
        a.from_dict(common.artifact_info_json)

        ai = ArtifactsInfoParams()
        ai.__dict__["_video"] = a
        assert ai.video == a

    def utest_str(self):
        ai = ArtifactsInfoParams()
        ai.from_dict(common.artifacts_info_json)

        assert (
            str(ai)
            == """{
    "audio": {
        "paths": [
            "artifact_path1",
            "artifact_path2"
        ],
        "error": "artifact error"
    },
    "downloads": {},
    "screenshots": {
        "paths": [
            "artifact_path1",
            "artifact_path2"
        ],
        "error": "artifact error"
    },
    "video": {}
}"""
        )


class UTestMetricParams:
    def utest_metric_id(self):
        m = MetricParams()
        m.__dict__["_metric_id"] = common.metric_id
        assert m.metric_id == common.metric_id

    def utest_created(self):
        m = MetricParams()
        m.__dict__["_created"] = common.created_time
        assert m.created == common.created_time

    def utest_data_count(self):
        m = MetricParams()
        m.__dict__["_data_count"] = 5
        assert m.data_count == 5

    def utest_metric_path(self):
        m = MetricParams()
        m.__dict__["_metric_path"] = MetricBasePath.MACHINE_CPU_USED
        assert m.metric_path == MetricBasePath.MACHINE_CPU_USED

    def utest_value(self):
        m = MetricParams()
        m.__dict__["_value"] = "value"
        assert m.value == "value"

    def utest_total(self):
        m = MetricParams()
        m.__dict__["_total"] = 9.8
        assert m.total == 9.8

    def utest_minimum(self):
        m = MetricParams()
        m.__dict__["_minimum"] = 9.8
        assert m.minimum == 9.8

    def utest_maximum(self):
        m = MetricParams()
        m.__dict__["_maximum"] = 9.8
        assert m.maximum == 9.8

    def utest_average(self):
        m = MetricParams()
        m.__dict__["_average"] = 9.8
        assert m.average == 9.8

    def utest_stddev(self):
        m = MetricParams()
        m.__dict__["_stddev"] = 9.8
        assert m.stddev == 9.8

    def utest_rstddev(self):
        m = MetricParams()
        m.__dict__["_rstddev"] = 9.8
        assert m.rstddev == 9.8

    def utest_perc_1st(self):
        m = MetricParams()
        m.__dict__["_perc_1st"] = 9.8
        assert m.perc_1st == 9.8

    def utest_perc_5th(self):
        m = MetricParams()
        m.__dict__["_perc_5th"] = 9.8
        assert m.perc_5th == 9.8

    def utest_perc_25th(self):
        m = MetricParams()
        m.__dict__["_perc_25th"] = 9.8
        assert m.perc_25th == 9.8

    def utest_perc_50th(self):
        m = MetricParams()
        m.__dict__["_perc_50th"] = 9.8
        assert m.perc_50th == 9.8

    def utest_perc_75th(self):
        m = MetricParams()
        m.__dict__["_perc_75th"] = 9.8
        assert m.perc_75th == 9.8

    def utest_prec_95th(self):
        m = MetricParams()
        m.__dict__["_perc_95th"] = 9.8
        assert m.perc_95th == 9.8

    def utest_perc_99th(self):
        m = MetricParams()
        m.__dict__["_perc_99th"] = 9.8
        assert m.perc_99th == 9.8

    def utest_str(self):
        m = MetricParams()
        m.from_dict(common.metric_json)

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
    def utest_machine(self):
        m = MetricsParams()
        d = {
            MetricBasePath.MACHINE_CPU_USED: MetricParams(),
        }
        m.__dict__["_machine"] = d
        assert m.machine == d

    def utest_webrtc(self):
        m = MetricsParams()
        d = {
            MetricBasePath.WEBRTC_AUDIO_CODEC_IN: MetricParams(),
        }
        m.__dict__["_webrtc"] = d
        assert m.webrtc == d

    def utest_str(self):
        m = MetricsParams()
        m.from_dict(common.metrics_json)

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

    def utest_to_dict(self):
        m = MetricsParams()
        m.from_dict(common.metrics_json)

        assert not m.to_dict()


class UTestResultMOSParams:
    def utest_result_mos_id(self):
        m = ResultMOSParams()
        m.__dict__["_result_mos_id"] = common.result_mos_id
        assert m.result_mos_id == common.result_mos_id

    def utest_created(self):
        m = ResultMOSParams()
        m.__dict__["_created"] = common.created_time
        assert m.created == common.created_time

    def utest_result_id(self):
        m = ResultMOSParams()
        m.__dict__["_result_id"] = common.result_id
        assert m.result_id == common.result_id

    def utest_algorithm(self):
        m = ResultMOSParams()
        m.__dict__["_algorithm"] = MosAlgorithm.MA_VISQOL
        assert m.algorithm == MosAlgorithm.MA_VISQOL

    def utest_score(self):
        m = ResultMOSParams()
        m.__dict__["_score"] = 4.123
        assert m.score == 4.123

    def utest_start(self):
        m = ResultMOSParams()
        m.__dict__["_start"] = common.start_time
        assert m.start == common.start_time

    def utest_end(self):
        m = ResultMOSParams()
        m.__dict__["_end"] = common.end_time
        assert m.end == common.end_time

    def utest_str(self):
        m = ResultMOSParams()
        m.from_dict(common.result_mos_json)

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
    def utest_visqol(self):
        m = MeanOpinionScoresParams()
        l = [ResultMOSParams(), ResultMOSParams()]
        m.__dict__["_visqol"] = l
        assert m.visqol == l

    def utest_str(self):
        m = MeanOpinionScoresParams()
        m.from_dict(common.mean_opinion_scores_json)

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

    def utest_to_dict(self):
        m = MeanOpinionScoresParams()
        m.from_dict(common.mean_opinion_scores_json)

        assert not m.to_dict()


class UTestResultTimecardParams:
    def utest_result_timecard_id(self):
        m = ResultTimecardParams()
        m.__dict__["_result_timecard_id"] = common.result_timecard_id
        assert m.result_timecard_id == common.result_timecard_id

    def utest_created(self):
        m = ResultTimecardParams()
        m.__dict__["_created"] = common.created_time
        assert m.created == common.created_time

    def utest_result_id(self):
        m = ResultTimecardParams()
        m.__dict__["_result_id"] = common.result_id
        assert m.result_id == common.result_id

    def utest_test_name(self):
        m = ResultTimecardParams()
        m.__dict__["_name"] = "tc name"
        assert m.name == "tc name"

    def utest_start(self):
        m = ResultTimecardParams()
        m.__dict__["_start"] = 123
        assert m.start == 123

    def utest_end(self):
        m = ResultTimecardParams()
        m.__dict__["_end"] = 123
        assert m.end == 123

    def utest_str(self):
        m = ResultTimecardParams()
        m.from_dict(common.result_timecard_json)

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
    def utest_result_timecards(self):
        m = DataSyncParams()
        l = [ResultTimecardParams(), ResultTimecardParams()]
        m.__dict__["_result_timecards"] = l
        assert m.result_timecards == l

    def utest_str(self):
        m = DataSyncParams()
        m.from_dict(common.data_sync_json)

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

    def utest_to_dict(self):
        m = DataSyncParams()
        m.from_dict(common.data_sync_json)

        assert not m.to_dict()


class UTestResultParams:
    def utest_created(self):
        m = ResultParams()
        m.__dict__["_created"] = common.created_time
        assert m.created == common.created_time

    def utest_updated(self):
        m = ResultParams()
        m.__dict__["_updated"] = common.updated_time
        assert m.updated == common.updated_time

    def utest_start(self):
        m = ResultParams()
        m.__dict__["_start"] = common.start_time
        assert m.start == common.start_time

    def utest_end(self):
        m = ResultParams()
        m.__dict__["_end"] = common.end_time
        assert m.end == common.end_time

    def utest_status(self):
        m = ResultParams()
        m.__dict__["_status"] = ResultStatus.RS_FAIL
        assert m.status == ResultStatus.RS_FAIL

    def utest_selenium_result(self):
        m = ResultParams()
        m.__dict__["_selenium_result"] = ResultStatus.RS_ABORTED
        assert m.selenium_result == ResultStatus.RS_ABORTED

    def utest_mos_status(self):
        m = ResultParams()
        m.__dict__["_mos_status"] = MetricStatus.MS_CALCULATING
        assert m.mos_status == MetricStatus.MS_CALCULATING

    def utest_participant_details(self):
        m = ResultParams()
        rpp = RunParticipantParams()
        m.__dict__["_participant_details"] = rpp
        assert m.participant_details == rpp

    def utest_log_paths(self):
        m = ResultParams()
        rlp = ResultLogParams()
        m.__dict__["_log_paths"] = rlp
        assert m.log_paths == rlp

    def utest_asserts(self):
        m = ResultParams()
        rap = ResultAssertParams()
        m.__dict__["_asserts"] = rap
        assert m.asserts == rap

    def utest_artifacts(self):
        m = ResultParams()
        aip = ArtifactsInfoParams()
        m.__dict__["_artifacts"] = aip
        assert m.artifacts == aip

    def utest_metrics(self):
        m = ResultParams()
        mp = MetricsParams()
        m.__dict__["_metrics"] = mp
        assert m.metrics == mp

    def utest_mos(self):
        m = ResultParams()
        mosp = MeanOpinionScoresParams()
        m.__dict__["_mos"] = mosp
        assert m.mos == mosp

    def utest_data_sync(self):
        m = ResultParams()
        rap = DataSyncParams()
        m.__dict__["_data_sync"] = rap
        assert m.data_sync == rap

    def utest_str(self):
        m = ResultParams()
        m.from_dict(common.extended_result_json)

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
        "updated": "2024-02-03 15:42:54.689000+00:00",
        "created": "2022-04-01 13:54:25.689000+00:00",
        "run_id": 937561,
        "group_name": "group name",
        "group_num": 23,
        "participant_name": "participant name",
        "participant_num": 123,
        "record_audio": true,
        "compute_unit": "g4",
        "audio_feed": "silence",
        "browser": "chromeLatest",
        "location": "eu-central-1",
        "network": "4g",
        "video_feed": "480p-15fps"
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
            "path": "machine/cpu/available/total",
            "operator": "gt",
            "expected": "value",
            "id": 9876231,
            "created": "2022-04-01 13:54:25.689000+00:00",
            "result_id": 992341,
            "run_assert_id": 871342,
            "actual": "actual",
            "status": "fail",
            "message": "message"
        },
        {
            "path": "machine/cpu/available/total",
            "operator": "gt",
            "expected": "value",
            "id": 9876231,
            "created": "2022-04-01 13:54:25.689000+00:00",
            "result_id": 992341,
            "run_assert_id": 871342,
            "actual": "actual",
            "status": "fail",
            "message": "message"
        }
    ],
    "artifacts": {
        "audio": {
            "paths": [
                "artifact_path1",
                "artifact_path2"
            ],
            "error": "artifact error"
        },
        "downloads": {},
        "screenshots": {
            "paths": [
                "artifact_path1",
                "artifact_path2"
            ],
            "error": "artifact error"
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

    APIClient(common.project_id, common.access_token, common.api_base)

    # read
    httpretty.register_uri(
        httpretty.GET,
        re.compile(
            r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/results/\d*/$"
        ),
        body=json.dumps(common.extended_result_json),
        forcing_headers={"Content-Type": "application/json"},
    )

    # read all
    pg = common.paged_response.copy()
    pg["results"] = [common.result_json, common.result_json]

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
    def utest_init_empty(self):
        r = Result()
        assert r.params is not None
        assert r.run_id is None
        assert r.params.result_id is None

    def utest_init_with_params(self):
        r = Result(run_id=5, params=ResultParams(4))
        assert r.params is not None
        assert r.run_id == 5
        assert r.params.result_id == 4

    def utest_init_with_ids(self):
        r = Result(run_id=5, result_id=4)
        assert r.params is not None
        assert r.run_id == 5
        assert r.params.result_id == 4

    def utest_read(self):
        common.check_result_params(
            Result(run_id=common.run_id, result_id=common.result_id)
            .read()
            .params
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_invalid_run_id(self):
        r = Result(result_id=common.result_id)
        with pytest.raises(Exception):
            r.read()

    def utest_read_invalid_result_id(self):
        r = Result(run_id=common.run_id)
        with pytest.raises(Exception):
            r.read()


@pytest.mark.usefixtures("mock")
class UTestResultAPI:
    def utest_read(self):
        common.check_extended_result_params(
            ResultAPI.read(common.run_id, common.result_id)
        )

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_all(self):
        resp = ResultAPI.read_all(common.run_id)

        for ret in resp:
            common.check_result_params(ret)

        assert httpretty.last_request().method == httpretty.GET
        assert not httpretty.last_request().parsed_body

    def utest_read_all_null_results(self):
        rpg = common.paged_response.copy()
        rpg["results"] = None

        httpretty.register_uri(
            httpretty.GET,
            re.compile(
                r"^http://mock\.loadero\.api/v2/projects/\d*/runs/\d*/results/$"
            ),
            body=json.dumps(rpg),
            forcing_headers={"Content-Type": "application/json"},
        )

        assert not ResultAPI.read_all(common.run_id)

    def utest_request_mos(self):
        ResultAPI.request_mos(common.run_id, common.result_id)

    def utest_route(self):
        assert (
            ResultAPI.route(common.run_id)
            == "http://mock.loadero.api/v2/projects/538591/runs/937561/results/"
        )

        assert (
            ResultAPI.route(common.run_id, common.result_id)
            == "http://mock.loadero.api/v2/projects/538591/runs/937561/"
            "results/992341/"
        )
