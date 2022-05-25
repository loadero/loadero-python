"""Common data shared between tests"""

from dateutil import parser
from loadero_python.resources.script import Script


api_base = "http://mock.loadero.api/v2/"
access_token = "LOADERO_PROJECT_ACCESS_TOKEN"
project_id = 538591
group_id = 34421
test_id = 12734
file_id = 923
participant_id = 92559
file_id = 294325
assert_id = 29643


script = Script(content="pytest test script")


created_time = parser.parse("2022-04-01T13:54:25.689Z")
updated_time = parser.parse("2024-02-03T15:42:54.689Z")


paged_response = {
    "filter": {},
    "pagination": {"limit": 0, "offset": 0, "page": 0, "total_pages": 0},
    "results": [],
}


participant_json = {
    "id": participant_id,
    "group_id": group_id,
    "test_id": test_id,
    "created": "2022-04-01T13:54:25.689Z",
    "updated": "2024-02-03T15:42:54.689Z",
    "profile_id": 87,
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
    "created": "2022-04-01T13:54:25.689Z",
    "id": group_id,
    "name": "pytest_group",
    "test_id": test_id,
    "updated": "2024-02-03T15:42:54.689Z",
}


assert_json = {
    "id": assert_id,
    "test_id": test_id,
    "created": "2022-04-01T13:54:25.689Z",
    "updated": "2024-02-03T15:42:54.689Z",
    "expected": "892",
    "operator": "gt",
    "path": "machine/network/bitrate/in/avg",
}


test_json = {
    "id": test_id,
    "created": "2022-04-01T13:54:25.689Z",
    "updated": "2024-02-03T15:42:54.689Z",
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
    "created": "2022-04-01T13:54:25.689Z",
    "file_type": "test_script",
    "id": file_id,
    "project_id": project_id,
    "updated": "2024-02-03T15:42:54.689Z",
}
