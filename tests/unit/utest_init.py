"""Loadero Python package structure tests. If imports work fine."""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=import-outside-toplevel


def contains(got: list[str], want: list[str]) -> bool:
    for w in want:
        if w not in got:
            print(f"{w} not in {got}")
            print(f"all wanted: {want}")
            return False

    return True


class UTestResources:
    @staticmethod
    def utest_resources():
        import loadero_python.resources as r

        assert contains(
            dir(r),
            [
                "assert_precondition",
                "assert_resource",
                "classificator",
                "file",
                "group",
                "metric_path",
                "pagination",
                "participant",
                "project",
                "resource",
                "result",
                "run",
                "run_participant",
                "test",
            ],
        )

    @staticmethod
    def utest_classificator():
        import loadero_python.resources.classificator as c

        assert contains(
            dir(c),
            [
                "Artifact",
                "AssertStatus",
                "AudioFeed",
                "AwsStatus",
                "Browser",
                "ComputeUnit",
                "Enum",
                "FileType",
                "IncrementStrategy",
                "Language",
                "Location",
                "MediaType",
                "MemberRole",
                "MetricKey",
                "MetricStatus",
                "MosAlgorithm",
                "Network",
                "NodeStatus",
                "Operator",
                "PaymentPlan",
                "PaymentStatus",
                "Property",
                "ResultStatus",
                "RunStatus",
                "Serializable",
                "TestDuration",
                "TestMode",
                "VersionedBrowser",
                "VideoFeed",
            ],
        )
