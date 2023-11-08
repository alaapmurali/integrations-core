# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from typing_extensions import Literal

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    channel: str = Field(..., min_length=1)
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    message_flows: Optional[bool] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    mq_password: Optional[str] = Field(None, min_length=1)
    mq_port: int
    mq_server: str = Field(..., min_length=1)
    mq_user: Optional[str] = Field(None, min_length=1)
    mqcd_version: Optional[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]] = None
    persist_connections: Optional[bool] = None
    queue_manager: str = Field(..., min_length=1)
    resource_statistics: Optional[bool] = None
    service: Optional[str] = None
    tags: Optional[tuple[str, ...]] = None
    tls_auth: Optional[bool] = None
    tls_certificate_label: Optional[str] = None
    tls_cipher_spec: Optional[str] = None
    tls_key_repository_location: Optional[str] = Field(None, min_length=1)

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
