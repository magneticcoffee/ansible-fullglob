# Ansible fullglob plugins

Simple workaround for the globbing behavior described in [ansible/ansible#17136](https://github.com/ansible/ansible/issues/17136)

`fileglob` just globs files (hence the name) and all the magic dwimming in the ansible source makes it hard to just glob for dirs in paths (e.g. `conf/users/*/foo.conf`).

These plugins provide a simple glob mechanism relative to the playbook: `with_fullglob` and ` | fullglob`.
