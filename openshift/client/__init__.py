# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.admissionregistration_v1beta1_service_reference import AdmissionregistrationV1beta1ServiceReference
from .models.apiregistration_v1beta1_service_reference import ApiregistrationV1beta1ServiceReference
from .models.v1_aggregation_rule import V1AggregationRule
from .models.v1_allowed_flex_volume import V1AllowedFlexVolume
from .models.v1_applied_cluster_resource_quota import V1AppliedClusterResourceQuota
from .models.v1_applied_cluster_resource_quota_list import V1AppliedClusterResourceQuotaList
from .models.v1_binary_build_source import V1BinaryBuildSource
from .models.v1_bitbucket_web_hook_cause import V1BitbucketWebHookCause
from .models.v1_broker_template_instance import V1BrokerTemplateInstance
from .models.v1_broker_template_instance_list import V1BrokerTemplateInstanceList
from .models.v1_broker_template_instance_spec import V1BrokerTemplateInstanceSpec
from .models.v1_build import V1Build
from .models.v1_build_config import V1BuildConfig
from .models.v1_build_config_list import V1BuildConfigList
from .models.v1_build_config_spec import V1BuildConfigSpec
from .models.v1_build_config_status import V1BuildConfigStatus
from .models.v1_build_list import V1BuildList
from .models.v1_build_log import V1BuildLog
from .models.v1_build_output import V1BuildOutput
from .models.v1_build_post_commit_spec import V1BuildPostCommitSpec
from .models.v1_build_request import V1BuildRequest
from .models.v1_build_source import V1BuildSource
from .models.v1_build_spec import V1BuildSpec
from .models.v1_build_status import V1BuildStatus
from .models.v1_build_status_output import V1BuildStatusOutput
from .models.v1_build_status_output_to import V1BuildStatusOutputTo
from .models.v1_build_strategy import V1BuildStrategy
from .models.v1_build_trigger_cause import V1BuildTriggerCause
from .models.v1_build_trigger_policy import V1BuildTriggerPolicy
from .models.v1_csi_persistent_volume_source import V1CSIPersistentVolumeSource
from .models.v1_cluster_network import V1ClusterNetwork
from .models.v1_cluster_network_entry import V1ClusterNetworkEntry
from .models.v1_cluster_network_list import V1ClusterNetworkList
from .models.v1_cluster_resource_quota import V1ClusterResourceQuota
from .models.v1_cluster_resource_quota_list import V1ClusterResourceQuotaList
from .models.v1_cluster_resource_quota_selector import V1ClusterResourceQuotaSelector
from .models.v1_cluster_resource_quota_spec import V1ClusterResourceQuotaSpec
from .models.v1_cluster_resource_quota_status import V1ClusterResourceQuotaStatus
from .models.v1_cluster_role_scope_restriction import V1ClusterRoleScopeRestriction
from .models.v1_controller_revision import V1ControllerRevision
from .models.v1_controller_revision_list import V1ControllerRevisionList
from .models.v1_custom_build_strategy import V1CustomBuildStrategy
from .models.v1_custom_deployment_strategy_params import V1CustomDeploymentStrategyParams
from .models.v1_daemon_set import V1DaemonSet
from .models.v1_daemon_set_condition import V1DaemonSetCondition
from .models.v1_daemon_set_list import V1DaemonSetList
from .models.v1_daemon_set_spec import V1DaemonSetSpec
from .models.v1_daemon_set_status import V1DaemonSetStatus
from .models.v1_daemon_set_update_strategy import V1DaemonSetUpdateStrategy
from .models.v1_deployment import V1Deployment
from .models.v1_deployment_cause import V1DeploymentCause
from .models.v1_deployment_cause_image_trigger import V1DeploymentCauseImageTrigger
from .models.v1_deployment_condition import V1DeploymentCondition
from .models.v1_deployment_config import V1DeploymentConfig
from .models.v1_deployment_config_list import V1DeploymentConfigList
from .models.v1_deployment_config_rollback import V1DeploymentConfigRollback
from .models.v1_deployment_config_rollback_spec import V1DeploymentConfigRollbackSpec
from .models.v1_deployment_config_spec import V1DeploymentConfigSpec
from .models.v1_deployment_config_status import V1DeploymentConfigStatus
from .models.v1_deployment_details import V1DeploymentDetails
from .models.v1_deployment_list import V1DeploymentList
from .models.v1_deployment_log import V1DeploymentLog
from .models.v1_deployment_request import V1DeploymentRequest
from .models.v1_deployment_spec import V1DeploymentSpec
from .models.v1_deployment_status import V1DeploymentStatus
from .models.v1_deployment_strategy import V1DeploymentStrategy
from .models.v1_deployment_trigger_image_change_params import V1DeploymentTriggerImageChangeParams
from .models.v1_deployment_trigger_policy import V1DeploymentTriggerPolicy
from .models.v1_docker_build_strategy import V1DockerBuildStrategy
from .models.v1_docker_strategy_options import V1DockerStrategyOptions
from .models.v1_egress_network_policy import V1EgressNetworkPolicy
from .models.v1_egress_network_policy_list import V1EgressNetworkPolicyList
from .models.v1_egress_network_policy_peer import V1EgressNetworkPolicyPeer
from .models.v1_egress_network_policy_rule import V1EgressNetworkPolicyRule
from .models.v1_egress_network_policy_spec import V1EgressNetworkPolicySpec
from .models.v1_event_series import V1EventSeries
from .models.v1_exec_new_pod_hook import V1ExecNewPodHook
from .models.v1_fs_group_strategy_options import V1FSGroupStrategyOptions
from .models.v1_generic_web_hook_cause import V1GenericWebHookCause
from .models.v1_git_build_source import V1GitBuildSource
from .models.v1_git_hub_web_hook_cause import V1GitHubWebHookCause
from .models.v1_git_lab_web_hook_cause import V1GitLabWebHookCause
from .models.v1_git_source_revision import V1GitSourceRevision
from .models.v1_group import V1Group
from .models.v1_group_list import V1GroupList
from .models.v1_group_restriction import V1GroupRestriction
from .models.v1_host_subnet import V1HostSubnet
from .models.v1_host_subnet_list import V1HostSubnetList
from .models.v1_id_range import V1IDRange
from .models.v1_iscsi_persistent_volume_source import V1ISCSIPersistentVolumeSource
from .models.v1_identity import V1Identity
from .models.v1_identity_list import V1IdentityList
from .models.v1_image import V1Image
from .models.v1_image_change_cause import V1ImageChangeCause
from .models.v1_image_change_trigger import V1ImageChangeTrigger
from .models.v1_image_import_spec import V1ImageImportSpec
from .models.v1_image_import_status import V1ImageImportStatus
from .models.v1_image_label import V1ImageLabel
from .models.v1_image_layer import V1ImageLayer
from .models.v1_image_list import V1ImageList
from .models.v1_image_lookup_policy import V1ImageLookupPolicy
from .models.v1_image_signature import V1ImageSignature
from .models.v1_image_source import V1ImageSource
from .models.v1_image_source_path import V1ImageSourcePath
from .models.v1_image_stream import V1ImageStream
from .models.v1_image_stream_image import V1ImageStreamImage
from .models.v1_image_stream_import import V1ImageStreamImport
from .models.v1_image_stream_import_spec import V1ImageStreamImportSpec
from .models.v1_image_stream_import_status import V1ImageStreamImportStatus
from .models.v1_image_stream_list import V1ImageStreamList
from .models.v1_image_stream_mapping import V1ImageStreamMapping
from .models.v1_image_stream_spec import V1ImageStreamSpec
from .models.v1_image_stream_status import V1ImageStreamStatus
from .models.v1_image_stream_tag import V1ImageStreamTag
from .models.v1_image_stream_tag_list import V1ImageStreamTagList
from .models.v1_jenkins_pipeline_build_strategy import V1JenkinsPipelineBuildStrategy
from .models.v1_lifecycle_hook import V1LifecycleHook
from .models.v1_local_resource_access_review import V1LocalResourceAccessReview
from .models.v1_named_tag_event_list import V1NamedTagEventList
from .models.v1_net_namespace import V1NetNamespace
from .models.v1_net_namespace_list import V1NetNamespaceList
from .models.v1_o_auth_access_token import V1OAuthAccessToken
from .models.v1_o_auth_access_token_list import V1OAuthAccessTokenList
from .models.v1_o_auth_authorize_token import V1OAuthAuthorizeToken
from .models.v1_o_auth_authorize_token_list import V1OAuthAuthorizeTokenList
from .models.v1_o_auth_client import V1OAuthClient
from .models.v1_o_auth_client_authorization import V1OAuthClientAuthorization
from .models.v1_o_auth_client_authorization_list import V1OAuthClientAuthorizationList
from .models.v1_o_auth_client_list import V1OAuthClientList
from .models.v1_parameter import V1Parameter
from .models.v1_pod_dns_config import V1PodDNSConfig
from .models.v1_pod_dns_config_option import V1PodDNSConfigOption
from .models.v1_pod_security_policy_review import V1PodSecurityPolicyReview
from .models.v1_pod_security_policy_review_spec import V1PodSecurityPolicyReviewSpec
from .models.v1_pod_security_policy_review_status import V1PodSecurityPolicyReviewStatus
from .models.v1_pod_security_policy_self_subject_review import V1PodSecurityPolicySelfSubjectReview
from .models.v1_pod_security_policy_self_subject_review_spec import V1PodSecurityPolicySelfSubjectReviewSpec
from .models.v1_pod_security_policy_subject_review import V1PodSecurityPolicySubjectReview
from .models.v1_pod_security_policy_subject_review_spec import V1PodSecurityPolicySubjectReviewSpec
from .models.v1_pod_security_policy_subject_review_status import V1PodSecurityPolicySubjectReviewStatus
from .models.v1_project import V1Project
from .models.v1_project_list import V1ProjectList
from .models.v1_project_request import V1ProjectRequest
from .models.v1_project_spec import V1ProjectSpec
from .models.v1_project_status import V1ProjectStatus
from .models.v1_rbd_persistent_volume_source import V1RBDPersistentVolumeSource
from .models.v1_recreate_deployment_strategy_params import V1RecreateDeploymentStrategyParams
from .models.v1_replica_set import V1ReplicaSet
from .models.v1_replica_set_condition import V1ReplicaSetCondition
from .models.v1_replica_set_list import V1ReplicaSetList
from .models.v1_replica_set_spec import V1ReplicaSetSpec
from .models.v1_replica_set_status import V1ReplicaSetStatus
from .models.v1_repository_import_spec import V1RepositoryImportSpec
from .models.v1_repository_import_status import V1RepositoryImportStatus
from .models.v1_resource_access_review import V1ResourceAccessReview
from .models.v1_resource_quota_status_by_namespace import V1ResourceQuotaStatusByNamespace
from .models.v1_role_binding_restriction import V1RoleBindingRestriction
from .models.v1_role_binding_restriction_list import V1RoleBindingRestrictionList
from .models.v1_role_binding_restriction_spec import V1RoleBindingRestrictionSpec
from .models.v1_rolling_deployment_strategy_params import V1RollingDeploymentStrategyParams
from .models.v1_rolling_update_daemon_set import V1RollingUpdateDaemonSet
from .models.v1_rolling_update_deployment import V1RollingUpdateDeployment
from .models.v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy
from .models.v1_route import V1Route
from .models.v1_route_ingress import V1RouteIngress
from .models.v1_route_ingress_condition import V1RouteIngressCondition
from .models.v1_route_list import V1RouteList
from .models.v1_route_port import V1RoutePort
from .models.v1_route_spec import V1RouteSpec
from .models.v1_route_status import V1RouteStatus
from .models.v1_route_target_reference import V1RouteTargetReference
from .models.v1_run_as_user_strategy_options import V1RunAsUserStrategyOptions
from .models.v1_se_linux_context_strategy_options import V1SELinuxContextStrategyOptions
from .models.v1_scope_restriction import V1ScopeRestriction
from .models.v1_secret_build_source import V1SecretBuildSource
from .models.v1_secret_local_reference import V1SecretLocalReference
from .models.v1_secret_spec import V1SecretSpec
from .models.v1_security_context_constraints import V1SecurityContextConstraints
from .models.v1_security_context_constraints_list import V1SecurityContextConstraintsList
from .models.v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR
from .models.v1_service_account_pod_security_policy_review_status import V1ServiceAccountPodSecurityPolicyReviewStatus
from .models.v1_service_account_reference import V1ServiceAccountReference
from .models.v1_service_account_restriction import V1ServiceAccountRestriction
from .models.v1_signature_condition import V1SignatureCondition
from .models.v1_signature_issuer import V1SignatureIssuer
from .models.v1_signature_subject import V1SignatureSubject
from .models.v1_source_build_strategy import V1SourceBuildStrategy
from .models.v1_source_control_user import V1SourceControlUser
from .models.v1_source_revision import V1SourceRevision
from .models.v1_source_strategy_options import V1SourceStrategyOptions
from .models.v1_stage_info import V1StageInfo
from .models.v1_stateful_set import V1StatefulSet
from .models.v1_stateful_set_condition import V1StatefulSetCondition
from .models.v1_stateful_set_list import V1StatefulSetList
from .models.v1_stateful_set_spec import V1StatefulSetSpec
from .models.v1_stateful_set_status import V1StatefulSetStatus
from .models.v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy
from .models.v1_step_info import V1StepInfo
from .models.v1_subject_rules_review import V1SubjectRulesReview
from .models.v1_subject_rules_review_spec import V1SubjectRulesReviewSpec
from .models.v1_supplemental_groups_strategy_options import V1SupplementalGroupsStrategyOptions
from .models.v1_tls_config import V1TLSConfig
from .models.v1_tag_event import V1TagEvent
from .models.v1_tag_event_condition import V1TagEventCondition
from .models.v1_tag_image_hook import V1TagImageHook
from .models.v1_tag_import_policy import V1TagImportPolicy
from .models.v1_tag_reference import V1TagReference
from .models.v1_tag_reference_policy import V1TagReferencePolicy
from .models.v1_template import V1Template
from .models.v1_template_instance import V1TemplateInstance
from .models.v1_template_instance_condition import V1TemplateInstanceCondition
from .models.v1_template_instance_list import V1TemplateInstanceList
from .models.v1_template_instance_object import V1TemplateInstanceObject
from .models.v1_template_instance_requester import V1TemplateInstanceRequester
from .models.v1_template_instance_spec import V1TemplateInstanceSpec
from .models.v1_template_instance_status import V1TemplateInstanceStatus
from .models.v1_template_list import V1TemplateList
from .models.v1_user import V1User
from .models.v1_user_identity_mapping import V1UserIdentityMapping
from .models.v1_user_list import V1UserList
from .models.v1_user_restriction import V1UserRestriction
from .models.v1_volume_device import V1VolumeDevice
from .models.v1_web_hook_trigger import V1WebHookTrigger
from .models.v1beta1_aggregation_rule import V1beta1AggregationRule
from .models.v1beta1_allowed_flex_volume import V1beta1AllowedFlexVolume
from .models.v1beta1_daemon_set_condition import V1beta1DaemonSetCondition
from .models.v1beta1_event import V1beta1Event
from .models.v1beta1_event_list import V1beta1EventList
from .models.v1beta1_event_series import V1beta1EventSeries
from .models.v1beta1_ingress_tls import V1beta1IngressTLS
from .models.v1beta1_mutating_webhook_configuration import V1beta1MutatingWebhookConfiguration
from .models.v1beta1_mutating_webhook_configuration_list import V1beta1MutatingWebhookConfigurationList
from .models.v1beta1_rule_with_operations import V1beta1RuleWithOperations
from .models.v1beta1_stateful_set_condition import V1beta1StatefulSetCondition
from .models.v1beta1_validating_webhook_configuration import V1beta1ValidatingWebhookConfiguration
from .models.v1beta1_validating_webhook_configuration_list import V1beta1ValidatingWebhookConfigurationList
from .models.v1beta1_webhook import V1beta1Webhook
from .models.v1beta1_webhook_client_config import V1beta1WebhookClientConfig
from .models.v1beta2_daemon_set_condition import V1beta2DaemonSetCondition
from .models.v1beta2_stateful_set_condition import V1beta2StatefulSetCondition

# import apis into sdk package
from .apis.admissionregistration_v1beta1_api import AdmissionregistrationV1beta1Api
from .apis.apps_openshift_io_api import AppsOpenshiftIoApi
from .apis.apps_openshift_io_v1_api import AppsOpenshiftIoV1Api
from .apis.apps_v1_api import AppsV1Api
from .apis.authorization_openshift_io_api import AuthorizationOpenshiftIoApi
from .apis.authorization_openshift_io_v1_api import AuthorizationOpenshiftIoV1Api
from .apis.build_openshift_io_api import BuildOpenshiftIoApi
from .apis.build_openshift_io_v1_api import BuildOpenshiftIoV1Api
from .apis.events_api import EventsApi
from .apis.events_v1beta1_api import EventsV1beta1Api
from .apis.image_openshift_io_api import ImageOpenshiftIoApi
from .apis.image_openshift_io_v1_api import ImageOpenshiftIoV1Api
from .apis.network_openshift_io_api import NetworkOpenshiftIoApi
from .apis.network_openshift_io_v1_api import NetworkOpenshiftIoV1Api
from .apis.oapi_api import OapiApi
from .apis.oauth_openshift_io_api import OauthOpenshiftIoApi
from .apis.oauth_openshift_io_v1_api import OauthOpenshiftIoV1Api
from .apis.project_openshift_io_api import ProjectOpenshiftIoApi
from .apis.project_openshift_io_v1_api import ProjectOpenshiftIoV1Api
from .apis.quota_openshift_io_api import QuotaOpenshiftIoApi
from .apis.quota_openshift_io_v1_api import QuotaOpenshiftIoV1Api
from .apis.route_openshift_io_api import RouteOpenshiftIoApi
from .apis.route_openshift_io_v1_api import RouteOpenshiftIoV1Api
from .apis.security_openshift_io_api import SecurityOpenshiftIoApi
from .apis.security_openshift_io_v1_api import SecurityOpenshiftIoV1Api
from .apis.template_openshift_io_api import TemplateOpenshiftIoApi
from .apis.template_openshift_io_v1_api import TemplateOpenshiftIoV1Api
from .apis.template_openshift_io_api import TemplateOpenshiftIoApi
from .apis.user_openshift_io_api import UserOpenshiftIoApi
from .apis.user_openshift_io_v1_api import UserOpenshiftIoV1Api

# import ApiClient
from .api_client import ApiClient

from kubernetes.client.configuration import Configuration
from kubernetes.client.configuration import Configuration