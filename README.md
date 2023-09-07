# Loadero-Python

Python client for managing [Loadero](https://loadero.com) tests.

Loadero-Python provides easy-to-use programmatic access to Loadero API. Allows
to manage tests, participants, asserts, runs and other Loadero resources, start
and stop tests and extract test run results. Example usage might be running
Loadero tests as a part of CI/CD.

## Table of Contents

<!-- generate with https://luciopaiva.com/markdown-toc/ -->

- [Installation](#installation)
- [Usage](#usage)
  - [API Access](#api-access)
  - [Initialization](#initialization)
  - [Working with Existing Resources](#working-with-existing-resources)
  - [Creating a Test](#creating-a-test)
  - [Running a Test](#running-a-test)
    - [Polling](#polling)
    - [Stopping Test Execution](#stopping-test-execution)
  - [Getting Results](#getting-results)
    - [Participant Results](#participant-results)
      - [Log Retrieval](#log-retrieval)
      - [Extracting Failed Asserts](#extracting-failed-asserts)
      - [Checking metrics](#checking-metrics)
  - [Filtering and Pagination](#filtering-and-pagination)
    - [Filtering](#filtering)
    - [Pagination](#pagination)
- [Structure](#structure)
  - [API client](#api-client)
  - [Resources](#resources)
  - [Resource Params](#resource-params)
  - [Constants](#constants)
  - [Resource API](#resource-api)
- [Contributing](#contributing)

## Installation

Loadero-Python is available on [PyPI](https://pypi.org/project/loadero-python/)
and can be installed by running

```bash
pip install loadero-python
```

## Usage

### API Access

Before using the Loadero-Python client an API access token needs to be acquired.
This can be done in the projects settings page in Loadero web-app.
More information about the API can be found in the
[Loadero wiki](https://wiki.loadero.com/docs/loadero-usage/api/direct-api-access)

**Note** Access tokens are project specific and cannot be used across multiple
projects. Make sure to specify the project ID in the request for an access
token.

### Initialization

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

Further examples will not include `APIClient` initialization. It is assumed that
the client has been initialized at an earlier step.

### Working with Existing Resources

Loadero resources have a tree-like structure hence there can be child and parent
resources.

```
project
   |
   |----tests----groups-----participants
   |      |
   |      |------asserts----assert_preconditions
   |
   |----files
   |
   |----runs-----results
```

Every parent resource can read all of its child resources.

`Project` class from `loadero_python.resources.project` module provides an entry
point to access all resources.

`Project` class can be imported with

```py
from loadero_python.resources.project import Project
```

All tests in a project can be read with

```py
tests, pagination, filters = Project().tests()
```

Notice, that project ID was not specified in this example, this is because the
`APIClient` has already been initialized with the project ID and corresponding
access token.

- `tests` is a list of `Test` objects from `loadero_python.resources.test`
  module
- `pagination` is a `PaginationParams` object from
  `loadero_python.resources.pagination` module.
- `filters` is a python dictionary of applied filters.

A more detailed explanation of `pagination` and `filters` return values is
available in the [Filtering and Pagination](#filtering-and-pagination) section.

### Creating a Test

With an initialized `APIClient` Loadero-Python can now manage resources in the
project. Test is a resource one of many in Loadero-Python. More information
about all the resources that Loadero-Python provides can be found in the
[Structure](#structure) section. This usage guide cannot demonstrate all of
Loadero-Python's functionality hence will cover only common use case scenarios
starting with creating a test.

Test resource is contained within the `loadero_python.resources.test` module.
From it `Test`, `TestParams`, and `Script` classes need to be imported.

```py
from loadero_python.resources.test import Test, TestParams, Script
```

Additionally, `TestMode` and `IncrementStrategy` classificator constant
enumerations need to be imported from `loadero_python.resources.classificator`.
They will be used for test attribute definitions.

```py
from loadero_python.resources.classificator import TestMode, IncrementStrategy
```

Test attributes can be specified in two ways. Directly as arguments in params
initialization.

```py
test = Test(
    params=TestParams(
        name="my first loadero python test",
        start_interval=1,
        participant_timeout=10 * 60, # ten minutes
        mode=TestMode.TM_LOAD,
        increment_strategy=IncrementStrategy.IS_LINEAR,
        script=Script(content='print("hello test script")'),
    )
).create()
```

or with builder methods.

```py
test = Test(
    params=TestParams()
    .with_name("my second loadero python test")
    .with_start_interval(1)
    .with_participant_timeout(10 * 60) # ten minutes
    .with_mode(TestMode.TM_PERFORMANCE)
    .with_increment_strategy(IncrementStrategy.IS_RANDOM)
    .with_script(Script(content='print("hello test script")'))
).create()
```

Resource create and update operations have required and optional attributes. If
a required attribute is missing the API call will fail. Loadero-Python checks if
all of the required attributes have been populated before making the API call
and raises an exception if one or more required attributes are missing.

For test resources, the required attributes are:

- `name`
- `start_interval`
- `participant_timeout`
- `mode`
- `increment_strategy`

After the create operation completes the `test` object will have a few more of
its attributes populated. Any resource attributes can be simply printed.

```py
print(test)
```

This will output a JSON object representation of the resource.

```json
{
  "id": 1234,
  "name": "my first loadero python test",
  "start_interval": 1,
  "participant_timeout": 600,
  "mode": "load",
  "increment_strategy": "linear",
  "script": "print(\"hello test script\")",
  "created": "2022-08-25 15:33:04+00:00",
  "updated": "2022-08-25 15:33:04+00:00",
  "script_file_id": 12345
}
```

Different output formats can be achieved by using `to_dict` and `to_dict_full`
resource params methods. Both methods return a python dictionary representation
of the resource. `to_dict` will return only the required attributes and optional
attributes if present. `to_dict_full` will return all attributes present.
**Note** `to_dict` will raise an exception if one or more required attribute is
missing.

```py
import yaml

print(yaml.dump(test.params.to_dict_full()))
```

```yaml
created: "2022-08-25 15:33:04+00:00"
id: 1234
increment_strategy: linear
mode: load
name: my first loadero python test
participant_timeout: 600
script: print("hello test script")
script_file_id: 12345
start_interval: 1
updated: "2022-08-25 15:33:04+00:00"
```

### Running a Test

To run a test the only required attribute is test ID.

For the `test` object from previous examples, the `test_id` attribute has been
populated by create operation, so it can simply be run by calling the `launch`
method.

```py
run = test.launch()
```

If a test ID is known it can be run directly.

```py
run = Test(test_id=1234).launch()
```

All tests in a project can be run with

```py
for test in Project().tests()[0]:
    test.launch()
```

#### Polling

After a test has been launched, waiting for the test to finish can be achieved
with the `poll` method.

```py
run.poll()
```

By default, the `poll` method will make an API call to check if the test
execution has finished every 15 seconds and will wait up to 12 hours. This
functionality can be customized with the `interval` and `timeout` arguments.

```py
# will poll every 5 seconds and will wait up to 10 minutes.
run.poll(interval=5.0, timeout=10 * 60.0)
```

If test execution does not finish within the specified timeout, the `poll`
method will raise an exception.

#### Stopping Test Execution

If test execution needs to be prematurely stopped, it can be done with the
`stop` method.

```py
run.stop()
```

**Note** `stop` only sends an API request that starts a Loadero procedure of
stopping the test. This process is NOT immediate. Even though the `stop` API
request completes relatively quickly, the test can remain running for a while
longer.

**Note** If another process is polling the test execution, it will automatically
stop if the test is stopped.

### Getting Results

After the test run finishes execution, the `run` object already contains many
useful attributes that may be used in result analysis. The attributes are stored
on the `run.params` field. `run.params` is an `RunParams` object from
`loadero_python.resources.run` module.

```py
print(run.params.success_rate)
```

#### Participant Results

`run` object describes a result overview of the whole test. To get a more
detailed result information about each test participant's results needs to be
read.

```py
results, _, _ = run.Results()
result = results[0]
```

The ignored return values are pagination and filters. They are not relevant for
result retrieval, hence they are omitted. A more detailed explanation of these
values is available in the [Filtering and Pagination](#filtering-and-pagination)
section.

`results` is a list of `Result` objects from `loadero_python.resources.result`
module. A single result corresponds to a single participant in the test.

`Result` just like a regular resource object has a `params` field of type
`ResultParams` that contains its attributes. The result resource has the largest
amount of attributes, so this showcase will cover only common use cases.

##### Log Retrieval

```py
import requests

resp = requests.get(result.params.log_paths.selenium)
if not resp:
    print("failed to download selenium log")
    exit(1)

with open(f"selenium_log_of_result_{result.params.result_id}", "w") as f:
    f.write(resp.text)
```

`result.params.log_paths.selenium` is an URL to an Selenium log. It first needs
to be downloaded using the HTTP library `requests`. Then it can be written to a
file.

##### Extracting Failed Asserts

Before extracting failed asserts. `AssertStatus` classificator constant
enumeration needs to be imported.

```py
from loadero_python.resources.classificator import AssertStatus
```

```py
failed_asserts = []

for result_assert in result.params.asserts:
    if result_assert.status == AssertStatus.AS_FAIL
        failed_asserts.append(result_assert)
```

##### Checking metrics

Loadero tests collect various different metrics from CPU, RAM, and network usage
to video and audio quality indicators. Loadero organizes these metrics with
metric base paths - a path-like string that uniquely identifies metric data. For
example, CPU usage metric data is described by the metric base path
`machine/cpu/used`.

After test execution finishes Loadero processes the collected metric data by
applying aggregator functions.

- total
- minimum
- maximum
- average
- standard deviation
- relative standard deviation
- 1st percentile
- 5th percentile
- 25th percentile
- 50th percentile
- 75th percentile
- 95th percentile
- 99th percentile

The result is a single float value identified by a metric path. For example, the
maximal CPU usage is described by the metric path - `machine/cpu/used/max`

In Loadero-Python metric base paths - `MetricBasePath` and metric paths -
`MetricPath` are constant enumerations of all the available metric and metric
base paths. Contained within the `loadero_python.resources.metric_path` module.

To access a specific metric `MetricBasePath` enumeration needs to be imported.

```py
from loadero_python.resources.metric_path import MetricBasePath
```

Then a specific metric can be checked like this

```py
if result.params.metrics is None or result.metrics.machine is None:
    print("result has no machine metrics")
    exit(1)

if MetricBasePath.MACHINE_CPU_AVAILABLE not in result.params.metrics.machine:
    print("result has no machine cpu available metric")
    exit(1)

if (
    result.params.metrics.machine[MetricBasePath.MACHINE_CPU_AVAILABLE].average
    < 10.0
):
    print("test is well configured. efficient usage of CPU resources")
```

The `not None` checks are required because some or all metrics for a result can
be missing. For example, non-WebRTC tests will not have any `webrtc` metrics.

### Filtering and Pagination

Read-all operations have the option to limit the number of resources returned,
offset a limited read-all operation by some amount of resources and filter out
undesired resources.

This is done by passing a query params argument when performing a read-all
operation.

`QueryParams` class is contained in `loadero_python.resources.resource` module
and can be imported with

```py
from loadero_python.resources.resource import QueryParams
```

#### Filtering

Filters are resource-specific and are defined in each resource module. For
example, test resource filters are defined in the `TestFilterKey` constant
enumeration in the `loadero_python.resources.test` module.

`TestFilterKey` can be imported with

```py
from loadero_python.resources.test import TestFilterKey
```

Now test read all operations can be filtered like this

```py
tests, _, filters = Project().tests(
    query_params=QueryParams().filter(
        TestFilterKey.PARTICIPANT_TIMEOUT_TO, 10 * 60 # ten minutes
    )
)
```

The ignored value is pagination. It can be ignored because pagination will
contain useful page information when limit and offset query_params have been
applied.

This will return tests whose participant timeout attribute is smaller than ten
minutes.

`filters` is a python dictionary with the applied filters.

#### Pagination

When performing a read-all operation that will return many resources it is good
practice to limit the number of resources returned and perform multiple smaller
reads. This can be achieved by limiting and offsetting the number of resources
returned.

```py
tests, pagination, _ = Project().tests(
    query_params=QueryParams().limit(20).offset(10)
)
```

This time the ignored value is filters. It can be ignored because no filters
were applied.

Let's assume that the project has 28 tests numbered from 1 to 28, then this
read-all operation would return tests with numbers from 11 to 28. This happens
because the returned resources were offset by 10 and the next resource after the
10th is the 11th. Only 18 resources were returned because the remaining
resources after offset were smaller than the defined limit - 20.

`pagination` is an instance `PaginationParams` class from
`loadero_python.resources.resource` module. It contains information about the
applied limit and offset, plus additional information describing how many
resources remain to be read.

## Structure

The Loadero-Python library structure is similar to the Loadero API structure.
The main structural components are:

- API client
- resources and operations with them

### API client

Contained within `loadero_python.api_client` module is the `APIClient` singleton
object. It needs to be initialized once with the project ID and access token.
All requests to Loadero API are done with the `APIClient` object. It adds the
required headers to make valid API requests. Additionally, the `APIClient` rate
limits all requests to be compliant with Loadero API's access limits. Rate
limiting can be opted out on initialization.

```py
APIClient(
    project_id=1234,
    access_token="your_access_token",
    rate_limit=False,
)
```

### Resources

Each resource has a separate module.

| Resource class       | Module                                         |
| -------------------- | ---------------------------------------------- |
| `AssertPrecondition` | `loadero_python.resources.assert_precondition` |
| `Assert`             | `loadero_python.resources.assert_resource`     |
| `File`               | `loadero_python.resources.file`                |
| `Group`              | `loadero_python.resources.group`               |
| `Participant`        | `loadero_python.resources.participant`         |
| `Project`            | `loadero_python.resources.project`             |
| `Result`             | `loadero_python.resources.result`              |
| `RunParticipant`     | `loadero_python.resources.run_participant`     |
| `Run`                | `loadero_python.resources.run`                 |
| `Test`               | `loadero_python.resources.test`                |

All resource classes have a similar structure:

- Resource classes have an attribute `params` that is used to store the data of
  a single instance of the resource. Read more about resource params
  [here](#resource-params).
- most resources implement common CRUD manipulation methods - `create`, `read`,
  `update`, `delete`, `duplicate`. Some resources do not have these methods
  because they are impossible or not available via API access. For example,
  `Project` resource has only `read` method because API access prohibits updates
  to this resource.
- resources that can have child resources have methods for reading all the child
  resources.
  ```py
  # reads all groups in test
  groups, _, _ = Test(test_id=123).groups()
  ```

### Resource Params

Every resource has a resource params class that stores the data of a single
resource instance.

Resource params class for each resource is available in the resources module.

| Resource params class      | Module                                         |
| -------------------------- | ---------------------------------------------- |
| `AssertPreconditionParams` | `loadero_python.resources.assert_precondition` |
| `AssertParams`             | `loadero_python.resources.assert_resource`     |
| `FileParams`               | `loadero_python.resources.file`                |
| `GroupParams`              | `loadero_python.resources.group`               |
| `ParticipantParams`        | `loadero_python.resources.participant`         |
| `ProjectParams`            | `loadero_python.resources.project`             |
| `ResultParams`             | `loadero_python.resources.result`              |
| `RunParticipantParams`     | `loadero_python.resources.run_participant`     |
| `RunParams`                | `loadero_python.resources.run`                 |
| `TestParams`               | `loadero_python.resources.test`                |

Resource params classes provide access to the resource attributes.

```py
# read a test and print its name
print(Test(test_id=123).read().params.name)
```

### Constants

Loadero-Python has two modules for constants.

- `loadero_python.resources.classificator` for classificator constant
  enumerations.
- `loadero_python.resources.metric_path` for metric path and metric base path
  constant enumerations.

### Resource API

Every resource has its own API class also available in the resources module.

| Resource class          | Module                                         |
| ----------------------- | ---------------------------------------------- |
| `AssertPreconditionAPI` | `loadero_python.resources.assert_precondition` |
| `AssertAPI`             | `loadero_python.resources.assert_resource`     |
| `FileAPI`               | `loadero_python.resources.file`                |
| `GroupAPI`              | `loadero_python.resources.group`               |
| `ParticipantAPI`        | `loadero_python.resources.participant`         |
| `ProjectAPI`            | `loadero_python.resources.project`             |
| `ResultAPI`             | `loadero_python.resources.result`              |
| `RunParticipantAPI`     | `loadero_python.resources.run_participant`     |
| `RunAPI`                | `loadero_python.resources.run`                 |
| `TestAPI`               | `loadero_python.resources.test`                |

Resource API class implements all the available API operations of that resource.
Resource API classes are internally used by all resources, but the class on its
own is not very useful.

## Contributing

Found a bug? - Feel free to open an
[issue](https://github.com/loadero/loadero-python/issues/new/choose).

Would like to request a feature? - Open an issue describing the request and the
reason for it or contact Loadero [support](mailto:support@loadero.com).

Want to contribute? - Open
[issues](https://github.com/loadero/loadero-python/issues) is a good place where
to find stuff that needs to be worked on.
