import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_lvm(host):
    assert host.file('/mnt/local/').is_directory


def test_home_owner(host):
    assert host.file('/home/ubuntu').user == 'ubuntu'
    assert host.file('/mnt/local/home/ubuntu').user == 'ubuntu'


def test_swapfile(host):
    assert host.file('/mnt/local/swapfile').is_file
