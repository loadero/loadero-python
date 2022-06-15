"""Describes generics and utility functions of Loadero resources."""

from __future__ import annotations
from typing import Callable
import json
from datetime import datetime


class Serializable:
    """Base class for serializable objects. Serializable objects can be
    converted to and from JSON using Python dictionary as a JSON representation.
    """

    def to_dict(self) -> dict[str, any]:
        """Returns a dictionary representation of the object."""
        raise NotImplementedError

    def to_dict_full(self) -> dict[str, any]:
        """Returns a dictionary representation of the object that contains all
        of the objects attributes."""
        raise NotImplementedError

    def from_dict(self, json_dict: dict[str, any]) -> Serializable:
        """Returns an instance of the object from a dictionary."""
        raise NotImplementedError


class ParamsSerializer(Serializable):
    """
    ParamsSerializer implements Serializable for Loadero resource params.
    """

    # pylint: disable=dangerous-default-value
    def __init__(
        self,
        attribute_map: dict[str, str] = {},
        custom_deserializers: dict[str, any] = {},
        body_attributes: list[str] = [],
        required_body_attributes: list[str] = [],
    ):
        """Initializes the resource params serializer.

        Args:
            attribute_map (dict[str, str], optional): Mapping of JSON field
                names to attribute names in object. Defaults to {}.
            custom_deserializers (dict[str, any], optional): Mapping of JSON
                field names to functions with signature (json_dict) -> (object)
                that convert the specified JSON value in a custom manner.
                Defaults to {}.
            body_attributes (list[str], optional): List of JSON field names
                that are going to be serialized if present. Defaults to [].
            required_body_attributes (list[str], optional): List of JSON field
                names that will fail serialization if missing. Defaults to [].
        """

        super().__init__()

        self.__attribute_map = attribute_map
        self.__custom_deserializers = custom_deserializers
        self.__body_attributes = body_attributes
        self.__required_body_attributes = required_body_attributes

        self.__reverse_attribute_map = {}
        for k, v in self.__attribute_map.items():
            self.__reverse_attribute_map[v] = k

    def to_dict(self) -> dict[str, any]:
        """Converts the resource params object to a dictionary JSON
        representation that contains only the body attributes.

        Raises:
            ValueError: If one or more required attributes is missing.

        Returns:
            dict[str, any]: The resource params object as a dictionary.
        """
        json_dict = {}

        for (
            python_attribute_name,
            python_attribute_value,
        ) in self.__dict__.items():
            if python_attribute_name not in self.__reverse_attribute_map:
                continue  # skip unknown attributes

            json_attribute_name = self.__reverse_attribute_map[
                python_attribute_name
            ]

            if json_attribute_name not in self.__body_attributes:
                continue  # skip non-body attributes

            if python_attribute_value is None:
                if json_attribute_name in self.__required_body_attributes:
                    raise ValueError(
                        f"Missing required attribute '{json_attribute_name}'"
                    )

                continue

            json_dict[json_attribute_name] = self.__get_attribute_dict(
                python_attribute_value
            )

        return json_dict

    def __get_attribute_dict(self, attribute, full=False):
        """Recursively converts the attribute to a dictionary that only
        contains the body attributes."""

        if isinstance(attribute, Serializable):
            if full:
                return attribute.to_dict_full()

            return attribute.to_dict()

        if isinstance(attribute, list):
            return [self.__get_attribute_dict(item, full) for item in attribute]

        if isinstance(attribute, datetime):
            return str(attribute)

        if isinstance(attribute, dict):
            return {
                self.__get_attribute_dict(k, full): self.__get_attribute_dict(
                    v, full
                )
                for k, v in attribute.items()
            }

        return attribute

    def to_dict_full(self) -> dict[str, any]:
        """
        Returns a dictionary representation of the object that contains all
        of the objects attributes.


        Returns:
            dict[str, any]: dictionary representation of the object.
        """

        json_dict = {}

        for (
            python_attribute_name,
            python_attribute_value,
        ) in self.__dict__.items():
            if python_attribute_name not in self.__reverse_attribute_map:
                continue  # skip unknown attributes

            json_attribute_name = self.__reverse_attribute_map[
                python_attribute_name
            ]

            if python_attribute_value is None:
                continue

            json_dict[json_attribute_name] = self.__get_attribute_dict(
                python_attribute_value, full=True
            )

        return json_dict

    def from_dict(self, json_dict: dict[str, any]) -> ParamsSerializer:
        """Sets the attributes of the resource params object from a JSON
        representation.

        Args:
            json_dict (dict[str, any]): JSON parsed as dictionary
                representation of the resource.

        Returns:
            ParamsSerializer: The resource params object.
        """

        for json_attribute_name, json_attribute_value in json_dict.items():
            if json_attribute_name not in self.__attribute_map:
                continue  # skip unknown attributes

            python_attribute_name = self.__attribute_map[json_attribute_name]

            if json_attribute_name in self.__custom_deserializers:
                self.__dict__[
                    python_attribute_name
                ] = self.__custom_deserializers[json_attribute_name](
                    json_attribute_value
                )
            else:
                self.__dict__[python_attribute_name] = json_attribute_value

        return self


def from_dict_as_list(
    resource_params_class: type,
) -> Callable[[dict[str, any]], list[LoaderoResourceParams]]:
    """Returns a function that deserializes a dictionary to a list of new
    instances of the resource params class

    Args:
        resource_params_class (type): Loadero resource params class.

    Returns:
        function: Function that deserializes a json dictionary to a list of new
            LoaderoResourceParams objects.
    """

    def func(json_value: dict[str, any]) -> list[LoaderoResourceParams]:
        resources = []

        for jv in json_value:
            r = resource_params_class()
            resources.append(r.from_dict(jv))

        return resources

    return func


def from_dict_as_new(
    resource_params_class: type,
) -> Callable[[dict[str, any]], LoaderoResourceParams]:
    """Returns a function that deserializes a dictionary to a new instance of
    the resource params class.

    Args:
        resource_params_class (type): Loadero resource params class.

    Returns:
        function: Function that deserializes a json dictionary to a new
            LoaderoResourceParams object.
    """

    def func(json_value: dict[str, any]) -> LoaderoResourceParams:
        r = resource_params_class()
        r.from_dict(json_value)

        return r

    return func


class LoaderoResourceParams(ParamsSerializer):
    """Base class for Loadero resource params."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return json.dumps(self.to_dict_full(), indent=4)


class LoaderoResource:
    """Base class for Loadero resources."""


class DuplicateResourceBodyParams(LoaderoResourceParams):
    """Duplicate resource body params."""

    def __init__(self, name: str or None = None):
        super().__init__(
            attribute_map={
                "name": "name",
            },
            body_attributes=[
                "name",
            ],
        )

        self.name = name


def convert_params_list(
    resource_class: type, params: list[LoaderoResource]
) -> list:
    """
    Converts a list of resource params to a list of resource objects.
    User of this function is responsible for matching the type of params and
    resource, otherwise the function will produce invalid resource instances.

    Args:
        resource_class (type): Class name of the target resource object type.
        params (list[LoaderoResource]): List of resource params.

    Returns:
        List[LoaderoResource]: List of resource objects.
    """

    resources = []
    for p in params:
        resources.append(resource_class(params=p))

    return resources
