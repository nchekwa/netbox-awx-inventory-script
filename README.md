# Create inventory in Ansble Tower (AWX) based on default netbox ansbile script

1) Put script ie. in /opt/scripts/pb.netbox_inventory.yml 

2) In AWX section scripts:
```yaml
plugin: netbox
api_endpoint: http://192.168.254.90
validate_certs: False
config_context: True
token: 678bcbfccbbcb6a59069438b89b5d0f9e4a3081a
group_by:
  - device_roles
query_filters:
  - tag: ansible
compose:
  ansible_network_os: platform.slug

```