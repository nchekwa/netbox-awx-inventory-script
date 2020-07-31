#!/usr/bin/env python
import json
import os

p = os.popen("/usr/bin/ansible-inventory --list -i /opt/scripts/netbox_inventory.yml")
data = json.loads(p.read())

output_data = data
for device in data['_meta']['hostvars']:
    if data['_meta']['hostvars'][device]['config_context'][0]:
        output_data['_meta']['hostvars'][device].update(data['_meta']['hostvars'][device]['config_context'][0])
    del output_data['_meta']['hostvars'][device]['config_context']

print(json.dumps(output_data, sort_keys=True, indent=2))
