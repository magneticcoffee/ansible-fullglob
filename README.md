# Ansible fullglob plugins

`fileglob` just globs files (hence the name) and all the magic dwimming in the ansible source makes it hard to just glob for dirs in paths (e.g. `conf/users/*/foo.conf`).

These plugins provide a simple glob mechanism relative to the playbook: `with_fullglob` and ` | fullglob`.
