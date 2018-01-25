# Ansible role for LVM

# Vars

* create lvm using use all available devices, except one mounted to root folder path
```yaml
volumes: auto
```
* create lvm using use all available devices, listed in variable
```yaml
volumes: ['/dev/sda/', '/dev/sdb']
```
