# Ansible role for disk partitioning

This role results in:

* logical volume `/dev/firefly/local`
* lv uses pvs defined in `lvm_disks`
* lv is mounted to `/mnt/local`
* `/home`,`/var`,`/tmp` are moved to `/mnt/local` and bind mounted back

Note:

* in `auto` mode role uses all disks except one mounted to the root
* role does handle adding more disks to lvm, but not removing them from it
* role fails if any disk listed in lvm_disks is mounted out of lvm

# Vars
* create lvm using use all available devices, except one mounted to root folder path
```yaml
lvm_disks: auto
```
* create lvm using use all available devices, listed in variable
```yaml
lvm_disks: ['/dev/sda/', '/dev/sdb']
```
* intelligent partition scheme is enabled by default and can be disabled using
```yaml
partitioning: 'True'
```
