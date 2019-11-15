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


class V1beta1CSIDriverSpec(object):
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
        'attach_required': 'bool',
        'pod_info_on_mount': 'bool'
    }

    attribute_map = {
        'attach_required': 'attachRequired',
        'pod_info_on_mount': 'podInfoOnMount'
    }

    def __init__(self, attach_required=None, pod_info_on_mount=None):  # noqa: E501
        """V1beta1CSIDriverSpec - a model defined in OpenAPI"""  # noqa: E501

        self._attach_required = None
        self._pod_info_on_mount = None
        self.discriminator = None

        if attach_required is not None:
            self.attach_required = attach_required
        if pod_info_on_mount is not None:
            self.pod_info_on_mount = pod_info_on_mount

    @property
    def attach_required(self):
        """Gets the attach_required of this V1beta1CSIDriverSpec.  # noqa: E501

        attachRequired indicates this CSI volume driver requires an attach operation (because it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach controller should call the attach volume interface which checks the volumeattachment status and waits until the volume is attached before proceeding to mounting. The CSI external-attacher coordinates with CSI volume driver and updates the volumeattachment status when the attach operation is complete. If the CSIDriverRegistry feature gate is enabled and the value is specified to false, the attach operation will be skipped. Otherwise the attach operation will be called.  # noqa: E501

        :return: The attach_required of this V1beta1CSIDriverSpec.  # noqa: E501
        :rtype: bool
        """
        return self._attach_required

    @attach_required.setter
    def attach_required(self, attach_required):
        """Sets the attach_required of this V1beta1CSIDriverSpec.

        attachRequired indicates this CSI volume driver requires an attach operation (because it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach controller should call the attach volume interface which checks the volumeattachment status and waits until the volume is attached before proceeding to mounting. The CSI external-attacher coordinates with CSI volume driver and updates the volumeattachment status when the attach operation is complete. If the CSIDriverRegistry feature gate is enabled and the value is specified to false, the attach operation will be skipped. Otherwise the attach operation will be called.  # noqa: E501

        :param attach_required: The attach_required of this V1beta1CSIDriverSpec.  # noqa: E501
        :type: bool
        """

        self._attach_required = attach_required

    @property
    def pod_info_on_mount(self):
        """Gets the pod_info_on_mount of this V1beta1CSIDriverSpec.  # noqa: E501

        If set to true, podInfoOnMount indicates this CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations. If set to false, pod information will not be passed on mount. Default is false. The CSI driver specifies podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and validating the information passed in as VolumeContext. The following VolumeConext will be passed if podInfoOnMount is set to true. This list might grow, but the prefix will be used. \"csi.storage.k8s.io/pod.name\": pod.Name \"csi.storage.k8s.io/pod.namespace\": pod.Namespace \"csi.storage.k8s.io/pod.uid\": string(pod.UID)  # noqa: E501

        :return: The pod_info_on_mount of this V1beta1CSIDriverSpec.  # noqa: E501
        :rtype: bool
        """
        return self._pod_info_on_mount

    @pod_info_on_mount.setter
    def pod_info_on_mount(self, pod_info_on_mount):
        """Sets the pod_info_on_mount of this V1beta1CSIDriverSpec.

        If set to true, podInfoOnMount indicates this CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations. If set to false, pod information will not be passed on mount. Default is false. The CSI driver specifies podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and validating the information passed in as VolumeContext. The following VolumeConext will be passed if podInfoOnMount is set to true. This list might grow, but the prefix will be used. \"csi.storage.k8s.io/pod.name\": pod.Name \"csi.storage.k8s.io/pod.namespace\": pod.Namespace \"csi.storage.k8s.io/pod.uid\": string(pod.UID)  # noqa: E501

        :param pod_info_on_mount: The pod_info_on_mount of this V1beta1CSIDriverSpec.  # noqa: E501
        :type: bool
        """

        self._pod_info_on_mount = pod_info_on_mount

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
        if not isinstance(other, V1beta1CSIDriverSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
