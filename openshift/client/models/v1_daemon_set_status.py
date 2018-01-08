# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1DaemonSetStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'collision_count': 'int',
        'conditions': 'list[V1DaemonSetCondition]',
        'current_number_scheduled': 'int',
        'desired_number_scheduled': 'int',
        'number_available': 'int',
        'number_misscheduled': 'int',
        'number_ready': 'int',
        'number_unavailable': 'int',
        'observed_generation': 'int',
        'updated_number_scheduled': 'int'
    }

    attribute_map = {
        'collision_count': 'collisionCount',
        'conditions': 'conditions',
        'current_number_scheduled': 'currentNumberScheduled',
        'desired_number_scheduled': 'desiredNumberScheduled',
        'number_available': 'numberAvailable',
        'number_misscheduled': 'numberMisscheduled',
        'number_ready': 'numberReady',
        'number_unavailable': 'numberUnavailable',
        'observed_generation': 'observedGeneration',
        'updated_number_scheduled': 'updatedNumberScheduled'
    }

    def __init__(self, collision_count=None, conditions=None, current_number_scheduled=None, desired_number_scheduled=None, number_available=None, number_misscheduled=None, number_ready=None, number_unavailable=None, observed_generation=None, updated_number_scheduled=None):
        """
        V1DaemonSetStatus - a model defined in Swagger
        """

        self._collision_count = None
        self._conditions = None
        self._current_number_scheduled = None
        self._desired_number_scheduled = None
        self._number_available = None
        self._number_misscheduled = None
        self._number_ready = None
        self._number_unavailable = None
        self._observed_generation = None
        self._updated_number_scheduled = None
        self.discriminator = None

        if collision_count is not None:
          self.collision_count = collision_count
        if conditions is not None:
          self.conditions = conditions
        self.current_number_scheduled = current_number_scheduled
        self.desired_number_scheduled = desired_number_scheduled
        if number_available is not None:
          self.number_available = number_available
        self.number_misscheduled = number_misscheduled
        self.number_ready = number_ready
        if number_unavailable is not None:
          self.number_unavailable = number_unavailable
        if observed_generation is not None:
          self.observed_generation = observed_generation
        if updated_number_scheduled is not None:
          self.updated_number_scheduled = updated_number_scheduled

    @property
    def collision_count(self):
        """
        Gets the collision_count of this V1DaemonSetStatus.
        Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.

        :return: The collision_count of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._collision_count

    @collision_count.setter
    def collision_count(self, collision_count):
        """
        Sets the collision_count of this V1DaemonSetStatus.
        Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.

        :param collision_count: The collision_count of this V1DaemonSetStatus.
        :type: int
        """

        self._collision_count = collision_count

    @property
    def conditions(self):
        """
        Gets the conditions of this V1DaemonSetStatus.
        Represents the latest available observations of a DaemonSet's current state.

        :return: The conditions of this V1DaemonSetStatus.
        :rtype: list[V1DaemonSetCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1DaemonSetStatus.
        Represents the latest available observations of a DaemonSet's current state.

        :param conditions: The conditions of this V1DaemonSetStatus.
        :type: list[V1DaemonSetCondition]
        """

        self._conditions = conditions

    @property
    def current_number_scheduled(self):
        """
        Gets the current_number_scheduled of this V1DaemonSetStatus.
        The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

        :return: The current_number_scheduled of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._current_number_scheduled

    @current_number_scheduled.setter
    def current_number_scheduled(self, current_number_scheduled):
        """
        Sets the current_number_scheduled of this V1DaemonSetStatus.
        The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

        :param current_number_scheduled: The current_number_scheduled of this V1DaemonSetStatus.
        :type: int
        """
        if current_number_scheduled is None:
            raise ValueError("Invalid value for `current_number_scheduled`, must not be `None`")

        self._current_number_scheduled = current_number_scheduled

    @property
    def desired_number_scheduled(self):
        """
        Gets the desired_number_scheduled of this V1DaemonSetStatus.
        The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

        :return: The desired_number_scheduled of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._desired_number_scheduled

    @desired_number_scheduled.setter
    def desired_number_scheduled(self, desired_number_scheduled):
        """
        Sets the desired_number_scheduled of this V1DaemonSetStatus.
        The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

        :param desired_number_scheduled: The desired_number_scheduled of this V1DaemonSetStatus.
        :type: int
        """
        if desired_number_scheduled is None:
            raise ValueError("Invalid value for `desired_number_scheduled`, must not be `None`")

        self._desired_number_scheduled = desired_number_scheduled

    @property
    def number_available(self):
        """
        Gets the number_available of this V1DaemonSetStatus.
        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)

        :return: The number_available of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._number_available

    @number_available.setter
    def number_available(self, number_available):
        """
        Sets the number_available of this V1DaemonSetStatus.
        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)

        :param number_available: The number_available of this V1DaemonSetStatus.
        :type: int
        """

        self._number_available = number_available

    @property
    def number_misscheduled(self):
        """
        Gets the number_misscheduled of this V1DaemonSetStatus.
        The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

        :return: The number_misscheduled of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._number_misscheduled

    @number_misscheduled.setter
    def number_misscheduled(self, number_misscheduled):
        """
        Sets the number_misscheduled of this V1DaemonSetStatus.
        The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

        :param number_misscheduled: The number_misscheduled of this V1DaemonSetStatus.
        :type: int
        """
        if number_misscheduled is None:
            raise ValueError("Invalid value for `number_misscheduled`, must not be `None`")

        self._number_misscheduled = number_misscheduled

    @property
    def number_ready(self):
        """
        Gets the number_ready of this V1DaemonSetStatus.
        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.

        :return: The number_ready of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._number_ready

    @number_ready.setter
    def number_ready(self, number_ready):
        """
        Sets the number_ready of this V1DaemonSetStatus.
        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.

        :param number_ready: The number_ready of this V1DaemonSetStatus.
        :type: int
        """
        if number_ready is None:
            raise ValueError("Invalid value for `number_ready`, must not be `None`")

        self._number_ready = number_ready

    @property
    def number_unavailable(self):
        """
        Gets the number_unavailable of this V1DaemonSetStatus.
        The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)

        :return: The number_unavailable of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._number_unavailable

    @number_unavailable.setter
    def number_unavailable(self, number_unavailable):
        """
        Sets the number_unavailable of this V1DaemonSetStatus.
        The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)

        :param number_unavailable: The number_unavailable of this V1DaemonSetStatus.
        :type: int
        """

        self._number_unavailable = number_unavailable

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1DaemonSetStatus.
        The most recent generation observed by the daemon set controller.

        :return: The observed_generation of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1DaemonSetStatus.
        The most recent generation observed by the daemon set controller.

        :param observed_generation: The observed_generation of this V1DaemonSetStatus.
        :type: int
        """

        self._observed_generation = observed_generation

    @property
    def updated_number_scheduled(self):
        """
        Gets the updated_number_scheduled of this V1DaemonSetStatus.
        The total number of nodes that are running updated daemon pod

        :return: The updated_number_scheduled of this V1DaemonSetStatus.
        :rtype: int
        """
        return self._updated_number_scheduled

    @updated_number_scheduled.setter
    def updated_number_scheduled(self, updated_number_scheduled):
        """
        Sets the updated_number_scheduled of this V1DaemonSetStatus.
        The total number of nodes that are running updated daemon pod

        :param updated_number_scheduled: The updated_number_scheduled of this V1DaemonSetStatus.
        :type: int
        """

        self._updated_number_scheduled = updated_number_scheduled

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1DaemonSetStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
