import os
import sys

# python bs to make loadero import work
sys.path.append(os.path.dirname(__file__) + "/..")


from jinja2 import Environment, FileSystemLoader, select_autoescape
from loadero_python.api_client import APIClient


def metric_path_member_name(value: str) -> str:
    return value.replace("/", "_").upper()


APIClient(
    51,
    "e39462286ebc351cefd4e0dfd55c735f24c5446a441e0957",
    "https://api.stage.loadero.com/v2/",
)


env = Environment(
    loader=FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    autoescape=select_autoescape(),
)

metric_paths = []
for mp in APIClient().get("statics/metric_path/"):
    metric_paths.append(
        {
            "name": metric_path_member_name(mp),
            "value": mp,
        }
    )

metric_paths.sort(key=lambda x: x["name"])

with open(
    os.path.split(os.path.split(__file__)[0])[0]
    + "/loadero_python/resources/metric_path.py",
    "w",
) as f:
    f.write(
        env.get_template("metric_path.j2").render(metric_paths=metric_paths)
    )
