"""script to generate loadero statistics"""

# pylint: disable=wrong-import-position
# pylint: disable=import-error
# pylint: disable=missing-function-docstring


import os
import sys

# python bs to make loadero import work
sys.path.append(os.path.dirname(__file__) + "/..")


import argparse
from jinja2 import Environment, FileSystemLoader, select_autoescape
from loadero_python.api_client import APIClient


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--token",
        type=str,
        help="project token",
        required=True,
    )

    parser.add_argument(
        "--pid",
        type=int,
        help="project token",
        required=True,
    )

    parser.add_argument(
        "--api",
        type=str,
        help="api url",
        required=True,
    )

    return parser.parse_args()


def classificator_member_name(c_type: str, value: str) -> str:
    if value[0] == "-":
        value = "neg_" + value[1:]

    value = "".join(map(lambda x: x[0], c_type.split("_"))) + "_" + value

    value = value.replace("-", "_")
    value = value.replace(".", "_")

    return value.upper()


def metric_path_member_name(value: str) -> str:
    return value.replace("/", "_").upper()


def metric_base_path_value(value: str) -> str:
    return "/".join(value.split("/")[:-1])


def classificator_class_name(value: str) -> str:
    return value.title().replace("_", "")


def generate_classificators(env: Environment):
    classificators = []

    for t, cs in APIClient().get("statics/").items():
        if t == "browser":
            continue

        c = {}

        c["type"] = t
        c["class_name"] = classificator_class_name(t)

        members = []

        for m in cs:
            members.append(
                {
                    "name": classificator_member_name(t, m["value"]),
                    "value": m["value"],
                }
            )

        members.sort(key=lambda x: x["name"])

        c["members"] = members

        classificators.append(c)

    classificators.sort(key=lambda x: x["class_name"])

    with open(
        os.path.split(os.path.split(__file__)[0])[0]
        + "/loadero_python/resources/classificator.py",
        "w",
    ) as f:
        f.write(
            env.get_template("classificator.j2").render(
                classificators=classificators
            )
        )


def generate_metric_paths(env: Environment):
    metric_paths = []
    metric_base_path_values = set()
    for mp in APIClient().get("statics/metric_path/"):
        metric_paths.append(
            {
                "name": metric_path_member_name(mp),
                "value": mp,
            }
        )

        non_aggregated = [
            "webrtc/audio/connections/in",
            "webrtc/audio/connections/out",
            "webrtc/video/connections/in",
            "webrtc/video/connections/out",
            "webrtc/audio/codec/in",
            "webrtc/audio/codec/out",
            "webrtc/video/codec/in",
            "webrtc/video/codec/out",
        ]

        if mp in non_aggregated:
            metric_base_path_values.add(mp)
        else:
            metric_base_path_values.add(metric_base_path_value(mp))

    metric_base_paths = []
    for mbp in metric_base_path_values:
        metric_base_paths.append(
            {
                "name": metric_path_member_name(mbp),
                "value": mbp,
            }
        )

    metric_base_paths.sort(key=lambda x: x["name"])

    metric_paths.sort(key=lambda x: x["name"])

    with open(
        os.path.split(os.path.split(__file__)[0])[0]
        + "/loadero_python/resources/metric_path.py",
        "w",
    ) as f:
        f.write(
            env.get_template("metric_path.j2").render(
                metric_paths=metric_paths, metric_base_paths=metric_base_paths
            )
        )


if __name__ == "__main__":
    args = parse_args()

    APIClient(args.pid, args.token, args.api)

    env = Environment(
        loader=FileSystemLoader(os.path.dirname(__file__) + "/templates"),
        autoescape=select_autoescape(),
    )

    generate_classificators(env)

    generate_metric_paths(env)

    print("generated classificator and metric pats constants")
