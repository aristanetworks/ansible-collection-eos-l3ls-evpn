<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

Requirements to use this example:

- Follow the [installation guide](../../docs/installation/collection-installation.md) for AVD
- Run the following playbook to copy the AVD **examples** to your current working directory, for example `ansible-avd-examples`:

```shell
ansible-playbook arista.avd.install_examples
```

This will show the following:

```shell
 ~/ansible-avd-examples# ansible-playbook arista.avd.install_examples

PLAY [Install Examples]**********************************************************************************************

TASK [Copy all examples to ~/ansible-avd-examples]*******************************************************************
changed: [localhost]

PLAY RECAP
*********************************************************************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

!!! info
    If the content of any file is ***modified*** and the playbook is rerun, the file ***will not*** be overwritten. However, if any file in the example is ***deleted*** and the playbook is rerun, Ansible will re-create the file.

After the playbook has run successfully, the directory structure of the example should look like below, the contents of which will be covered in later sections:
