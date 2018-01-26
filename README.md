# Ansible role for LVM

Results:

* logical volume `/dev/firefly/local`
* lv uses pvs defined in `volumes`
* lv is mounted to `/mnt/local`
* `/home`,`/var`,`/tmp` are moved to `/mnt/local` and bind mounted back

# Vars

* create lvm using use all available devices, except one mounted to root folder path
```yaml
volumes: auto
```
* create lvm using use all available devices, listed in variable
```yaml
volumes: ['/dev/sda/', '/dev/sdb']
```

Please note `volumes` variable is required.

* intelligent partition scheme is enabled by default and can be disabled using
```yaml
lvm_bindings: 'True'
```
