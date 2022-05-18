"""Describes generics and utility functions of Loadero resources."""


from tabulate import tabulate


class LoaderoResource:
    """Base class for Loadero resources."""


# TODO:
# from / to json logic is likely to change in the future. Participants need
# the ability to not specify group id, Tests do not need to clear the script
# attribute - this would remove a call to the api. For now serialization should
# stay as is, until more reqired features become apparent.
# TODO: Add support for optional body attributes.
def to_json(
    resource: dict[str, any],
    attribute_map: dict[str, str],
    body_attributes: list[str],
) -> dict[str, any]:
    """Converts Loadero resources to JSON dictionaries.

    Args:
        resource (dict[str, any]): Loadero resources __dict__.
        attribute_map (dict[str, str]): Loadero resources attribute map.
        body_attributes (list[str]): Loadero resources body attributes.

    Raises:
        Exception: If resource field required by body attributes is not defined.

    Returns:
        dict[str, any]: Loadero resources JSON representation as a dictionary.
    """
    json_value = {}

    for k, v in resource.items():
        if k not in attribute_map:
            continue

        if attribute_map[k] not in body_attributes:
            continue

        if v is None:
            raise Exception(
                f"{attribute_map[k]} is a required "
                "attribute and cannot be None"
            )

        if isinstance(v, LoaderoResource):
            json_value[attribute_map[k]] = v.to_json()
        else:
            json_value[attribute_map[k]] = v

    return json_value


def from_json(
    resource: dict[str, any],
    json_value: dict[str, any],
    attribute_map: dict[str, str],
    custom_deserializers: dict[str, any] or None = None,
) -> None:
    """Converts JSON dictionary to Loadero resource.

    Args:
        resource (dict[str, any]): Loadero resources __dict__.
        json_value (dict[str, any]): JSON representation as a dictionary.
        attribute_map (dict[str, str]): Loadero resources attribute map.
        custom_deserializers (dict[str, any]): Loadero resources custom
            deserializers. Defaults to None.
    """

    for k, v in resource.items():
        if k not in attribute_map:
            continue

        resource[k] = None

    reverse_attribute_map = {}

    for k, v in attribute_map.items():
        reverse_attribute_map[v] = k

    for k, v in json_value.items():
        if k not in reverse_attribute_map:
            # Loadero API returned some field that is not needed.
            continue

        if custom_deserializers is not None and k in custom_deserializers:
            resource[reverse_attribute_map[k]] = custom_deserializers[k](v)
        else:
            resource[reverse_attribute_map[k]] = v


def to_string(resource: dict[str, any], attribute_map: dict[str, str]) -> str:
    """Parses Loadero resource into human readable string representation.

    Args:
        resource (dict[str, any]): Loadero resources __dict__.
        attribute_map (dict[str, str]): Loadero resources attribute map.

    Returns:
        str: Human readable string representation of Loadero resource.
    """

    table = []
    for k, v in resource.items():
        if k not in attribute_map:
            continue

        if v is None:
            v = ""

        table.append([attribute_map[k], str(v)])

    table.sort()

    return tabulate(table, tablefmt="github")
