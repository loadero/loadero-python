# Loadero-Python

Python client for Loadero API.

Loadero-Python provides a easy to use programatic access to Loadero API.

Allows to manage Loadero tests, participants, asserts, runs and other resources,
start and stop tests, extract test run results.

Can be used to run Loadero tests as a part of CI/CD.

Loadero performance and load testing service is available via Loadero's
[site](https://loadero.com/) and REST API.

## Installation

Loadero-Python is available on [PyPI](https://pypi.org/project/loadero-python/)
and can be installed by running

```bash
pip install loadero-python
```

## Usage

### API access

Before using Loadero-Python client an API access token needs to be acquired.
Currently this can be done by contacting
[support](mailto:support@loadero.com?subject=I%20want%20to%20request%20project%20access%20token%20for%20API).

**Note** Access tokens are project specific and cannot be used across multiple
projects. Make sure to specify the project ID in the request for access token.

### Initalisation

After acquiring the access token Loadero-Python needs to be initialized with it.
Loadero-Python uses a singleton object `APIClient` from
`loadero_python.api_client` module to perform all requests to the API. Since
`APIClient` is a singleton it needs to be initialized once like so

```py
from loadero_python.api_client import APIClient

APIClient(
    project_id=1234,
    access_token="your_access_token",
)
```

Further examples will not include `APIClient` initalisation. It is assumed that
the client has been initialize at an earlier step.

### Creating a test

With an initialized `APIClient` Loadero-Python can now manage resources in teh
project. Since all resources have a similar structure this showcase will cover
only the core functionalit starting with creating a test. Test attributes can be
specified directly as arguments in params initalisation or with builder methods.

```py
from loadero_python.resources.test import Test, TestParams, Script
from loadero_python.resources.classificator import TestMode, IncrementStrategy

test1 = Test(
    params=TestParams(
        name="my first loadero python test",
        start_interval=1,
        participant_timeout=10 * 60, # ten minutes
        mode=TestMode.TM_LOAD,
        increment_strategy=IncrementStrategy.IS_LINEAR,
        script=Script(content='print("hello test script")'),
    )
).create()

test2 = Test(
    params=TestParams()
    .with_name("my second loadero python test")
    .with_start_interval(1)
    .with_participant_timeout(10 * 60) # ten minutes
    .with_mode(TestMode.TM_PERFORMANCE)
    .with_increment_strategy(IncrementStrategy.IS_RANDOM)
    .with_script(Script(content='print("hello test script")'))
).create()
```

`TestMode` and `IncrementStrategy` are two of many classificator constant
enumerations.

Resource create and update operations have required and optional attributes. If
an required attribute is missing the API call will fail. Loadero-Python checks
if all of the required attributes have been populated before making the API call
and raises an exception if one or more required attributes are missing.

For test resource the required attributes are:

- `name`
- `start_interval`
- `participant_timeout`
- `mode`
- `increment_strategy`

After the create operation completes the `test1` and `test2` objects will have a
few more of its attributes populated. To view any resources attributes it can be
simply printed.

```py
print(test1)
```

Similar output can be expected

```
{
    "id": 12734,
    "name": "pytest test",
    "start_interval": 12,
    "participant_timeout": 13,
    "mode": "load",
    "increment_strategy": "linear",
    "created": "2022-04-01 13:54:25.689000+00:00",
    "updated": "2024-02-03 15:42:54.689000+00:00",
    "script_file_id": 65,
    "group_count": 52,
    "participant_count": 9355
}
```

## Structure

Loadero-Python library structure is similar to Loadero API's. Main structural
components are:

- API client
- resources and operations with them

### API client

Contained within `loadero_python.api_client` module is the `APIClient` singleton
object. It needs to be initialized once with project ID and access token. All
requests to Loadero API are done with `APIClient` object. It adds the required
headers to make valid API requests. Additionally `APIClient` rate limits all
requests to be compliant with Loadero API's access limits. Rate limiting can be
opted out on initalisation.

### Resources and Operations

Loadero-Python separates resources and their operations by modules

- assert precondition - `loadero_python.resources.assert_precondition`
- assert - `loadero_python.resources.assert_resource`
- classificator - `loadero_python.resources.classificator`
- file - `loadero_python.resources.file`
- group - `loadero_python.resources.group`
- metric path - `loadero_python.resources.metric_path`
- participant - `loadero_python.resources.participant`
- project - `loadero_python.resources.project`
- result - `loadero_python.resources.result`
- run participant - `loadero_python.resources.run_participant`
- run - `loadero_python.resources.run`
- test - `loadero_python.resources.test`

All resources except classificators and metric paths are split into tree parts

- `ResourceParams` - class that holds a single resource instances data.
  (`TestParams`, `RunParams`, ...)

- `ResourceAPI` - class that implements all available API operations for a
  specific resource. (`TestAPI`, `RunAPI`) Resource API's can be very different
  depending on the resource. For example `TestAPI` implements create, read,
  update and delete operations, but `ResultAPI` only read (that is because
  result is a read-only resource and has no create, update or delete operations
  in Loadero API).

- `Resource` - class that combines previously described `ResourceParams` and
  `ResourceAPI` classes to provide easy access to resources data and simple to
  use interface that operates with the resources data. (`Test`, `Run`, ...)

https://pypi.org/project/loadero-python/

https://wiki.loadero.com/loadero-usage/api/
