#!/usr/bin/python
#
# Ansible module to manage arbitrary objects via API in fortigate devices
# (c) 2017, Will Wagner <willwagner602@gmail.com> and Eugene Opredelennov <eoprede@gmail.com>
# GNU General Public License v3.0+ (see COPYING or
# https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: fortios_api_snmp_sysinfo
extends_documentation_fragment: fortios_api_doc
version_added: "2.4"
short_description: Manages firewall SNMP Sysinfo parameters
description:
    - Manages firewall SNMP Sysinfo parameters
author:
    - Will Wagner (@willwagner602)
      Eugene Opredelennov (@eoprede)
notes:
    - Tested against Fortigate v5.4.5 VM
    - Can use all of the parameters supported by Fortigate API

options:
    sysinfo:
        description:
            - Set of SNMP Sysinfo parameters
        required: true
        type: list
        suboptions:
            status:
                description:
                    - SNMP Status
                required: false
                options: ['enable','disable']

'''
EXAMPLES = '''
---
name: set system snmp sysinfo
tags:
- snmp
fortios_api_snmp_sysinfo:
  conn_params:
    fortigate_username: admin
    fortigate_password: test
    fortigate_ip: 1.2.3.4
    port: 10080
    verify: false
    secure: false
    proxies:
        http: socks5://127.0.0.1:9000
  sysinfo:
  - status: enable

'''

RETURN = '''
proposed:
    description: k/v pairs of parameters passed into module
    returned: always
    type: dict
existing:
    description:
        - k/v pairs of existing configuration
    returned: always
    type: dict
end_state:
    description: k/v pairs of configuration after module execution
    returned: always
    type: dict
updates:
    description: command sent to the device
    returned: always
    type: list
changed:
    description: check to see if a change was made on the device
    returned: always
    type: boolean
'''

from ansible.module_utils.fortios_api import API

system_global_api_args = {
    'endpoint': ['cmdb', 'system.snmp', 'sysinfo'],
    'list_identifier': 'sysinfo',
    'object_identifier': '',
    'default_ignore_params': []}


def main():
    forti_api = API(system_global_api_args)
    forti_api.apply_configuration_to_endpoint()


if __name__ == "__main__":
    main()
