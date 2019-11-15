# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ExtensionsV1beta1DeploymentStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'available_replicas': 'int',
        'collision_count': 'int',
        'conditions': 'list[ExtensionsV1beta1DeploymentCondition]',
        'observed_generation': 'int',
        'ready_replicas': 'int',
        'replicas': 'int',
        'unavailable_replicas': 'int',
        'updated_replicas': 'int'
    }

    attribute_map = {
        'available_replicas': 'availableReplicas',
        'collision_count': 'collisionCount',
        'conditions': 'conditions',
        'observed_generation': 'observedGeneration',
        'ready_replicas': 'readyReplicas',
        'replicas': 'replicas',
        'unavailable_replicas': 'unavailableReplicas',
        'updated_replicas': 'updatedReplicas'
    }

    def __init__(self, available_replicas=None, collision_count=None, conditions=None, observed_generation=None, ready_replicas=None, replicas=None, unavailable_replicas=None, updated_replicas=None):  # noqa: E501
        """ExtensionsV1beta1DeploymentStatus - a model defined in OpenAPI"""  # noqa: E501

        self._available_replicas = None
        self._collision_count = None
        self._conditions = None
        self._observed_generation = None
        self._ready_replicas = None
        self._replicas = None
        self._unavailable_replicas = None
        self._updated_replicas = None
        self.discriminator = None

        if available_replicas is not None:
            self.available_replicas = available_replicas
        if collision_count is not None:
            self.collision_count = collision_count
        if conditions is not None:
            self.conditions = conditions
        if observed_generation is not None:
            self.observed_generation = observed_generation
        if ready_replicas is not None:
            self.ready_replicas = ready_replicas
        if replicas is not None:
            self.replicas = replicas
        if unavailable_replicas is not None:
            self.unavailable_replicas = unavailable_replicas
        if updated_replicas is not None:
            self.updated_replicas = updated_replicas

    @property
    def available_replicas(self):
        """Gets the available_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501

        Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.  # noqa: E501

        :return: The available_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._available_replicas

    @available_replicas.setter
    def available_replicas(self, available_replicas):
        """Sets the available_replicas of this ExtensionsV1beta1DeploymentStatus.

        Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.  # noqa: E501

        :param available_replicas: The available_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :type: int
        """

        self._available_replicas = available_replicas

    @property
    def collision_count(self):
        """Gets the collision_count of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501

        Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.  # noqa: E501

        :return: The collision_count of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._collision_count

    @collision_count.setter
    def collision_count(self, collision_count):
        """Sets the collision_count of this ExtensionsV1beta1DeploymentStatus.

        Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.  # noqa: E501

        :param collision_count: The collision_count of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :type: int
        """

        self._collision_count = collision_count

    @property
    def conditions(self):
        """Gets the conditions of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501

        Represents the latest available observations of a deployment's current state.  # noqa: E501

        :return: The conditions of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :rtype: list[ExtensionsV1beta1DeploymentCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ExtensionsV1beta1DeploymentStatus.

        Represents the latest available observations of a deployment's current state.  # noqa: E501

        :param conditions: The conditions of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :type: list[ExtensionsV1beta1DeploymentCondition]
        """

        self._conditions = conditions

    @property
    def observed_generation(self):
        """Gets the observed_generation of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501

        The generation observed by the deployment controller.  # noqa: E501

        :return: The observed_generation of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this ExtensionsV1beta1DeploymentStatus.

        The generation observed by the deployment controller.  # noqa: E501

        :param observed_generation: The observed_generation of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def ready_replicas(self):
        """Gets the ready_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501

        Total number of ready pods targeted by this deployment.  # noqa: E501

        :return: The ready_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """Sets the ready_replicas of this ExtensionsV1beta1DeploymentStatus.

        Total number of ready pods targeted by this deployment.  # noqa: E501

        :param ready_replicas: The ready_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :type: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self):
        """Gets the replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501

        Total number of non-terminated pods targeted by this deployment (their labels match the selector).  # noqa: E501

        :return: The replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this ExtensionsV1beta1DeploymentStatus.

        Total number of non-terminated pods targeted by this deployment (their labels match the selector).  # noqa: E501

        :param replicas: The replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def unavailable_replicas(self):
        """Gets the unavailable_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501

        Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.  # noqa: E501

        :return: The unavailable_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._unavailable_replicas

    @unavailable_replicas.setter
    def unavailable_replicas(self, unavailable_replicas):
        """Sets the unavailable_replicas of this ExtensionsV1beta1DeploymentStatus.

        Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.  # noqa: E501

        :param unavailable_replicas: The unavailable_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :type: int
        """

        self._unavailable_replicas = unavailable_replicas

    @property
    def updated_replicas(self):
        """Gets the updated_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501

        Total number of non-terminated pods targeted by this deployment that have the desired template spec.  # noqa: E501

        :return: The updated_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._updated_replicas

    @updated_replicas.setter
    def updated_replicas(self, updated_replicas):
        """Sets the updated_replicas of this ExtensionsV1beta1DeploymentStatus.

        Total number of non-terminated pods targeted by this deployment that have the desired template spec.  # noqa: E501

        :param updated_replicas: The updated_replicas of this ExtensionsV1beta1DeploymentStatus.  # noqa: E501
        :type: int
        """

        self._updated_replicas = updated_replicas

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtensionsV1beta1DeploymentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
