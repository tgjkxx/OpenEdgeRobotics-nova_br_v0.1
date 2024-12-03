# Copyright 2013 NEC Corporation.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

add_tenant_access = {
    'type': 'object',
    'properties': {
        'addTenantAccess': {
            'type': 'object',
            'properties': {
                'tenant': {
                    # defined from project_id in instance_type_projects table
                    'type': 'string', 'minLength': 1, 'maxLength': 255,
                },
            },
            'required': ['tenant'],
            'additionalProperties': False,
        },
    },
    'required': ['addTenantAccess'],
    'additionalProperties': False,
}


remove_tenant_access = {
    'type': 'object',
    'properties': {
        'removeTenantAccess': {
            'type': 'object',
            'properties': {
                'tenant': {
                    # defined from project_id in instance_type_projects table
                    'type': 'string', 'minLength': 1, 'maxLength': 255,
                },
            },
            'required': ['tenant'],
            'additionalProperties': False,
        },
    },
    'required': ['removeTenantAccess'],
    'additionalProperties': False,
}

# TODO(stephenfin): Remove additionalProperties in a future API version
index_query = {
    'type': 'object',
    'properties': {},
    'additionalProperties': True,
}
