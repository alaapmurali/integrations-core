# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>


def shared_skip_proxy():
    return False


def shared_timeout():
    return 10


def instance_allow_redirects():
    return True


def instance_auth_type():
    return 'basic'


def instance_blacklist_project_names():
    return []


def instance_collect_hypervisor_load():
    return True


def instance_collect_hypervisor_metrics():
    return True


def instance_collect_network_metrics():
    return True


def instance_collect_project_metrics():
    return True


def instance_collect_server_diagnostic_metrics():
    return True


def instance_collect_server_flavor_metrics():
    return True


def instance_disable_generic_tags():
    return False


def instance_domain_id():
    return 'default'


def instance_empty_default_hostname():
    return False


def instance_endpoint_interface():
    return 'public'


def instance_exclude_network_ids():
    return []


def instance_exclude_server_ids():
    return []


def instance_kerberos_auth():
    return 'disabled'


def instance_kerberos_delegate():
    return False


def instance_kerberos_force_initiate():
    return False


def instance_log_requests():
    return False


def instance_min_collection_interval():
    return 15


def instance_paginated_limit():
    return 1000


def instance_persist_connections():
    return False


def instance_request_size():
    return 16


def instance_skip_proxy():
    return False


def instance_timeout():
    return 10


def instance_tls_ignore_warning():
    return False


def instance_tls_use_host_header():
    return False


def instance_tls_verify():
    return True


def instance_use_agent_proxy():
    return True


def instance_use_legacy_auth_encoding():
    return True


def instance_use_legacy_check_version():
    return False


def instance_use_shortname():
    return False


def instance_whitelist_project_names():
    return []
