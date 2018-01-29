# Ansible role for disk partitioning

Install:

`ansible-galaxy install RebelMouseTeam.partitioning,1.0.0`

Usage:

```yaml
#cloud-config
output: {all: '| tee -a /var/log/cloud-init-output.log'}
write_files:
  - path: /root/requirements.yml
    content: |
      - src: RebelMouseTeam.partitioning,1.0.0
  - path: /root/bootstrap.yml
    content: |
      - hosts: localhost
        connection: local
        gather_facts: yes
        become: yes
        roles:
          - RebelMouseTeam.partitioning
runcmd:
  - sleep 90
  - ansible-galaxy install -p /etc/ansible/roles -r /root/requirements.yml
  - HOME=/root ansible-playbook /root/bootstrap.yml
  ```

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
