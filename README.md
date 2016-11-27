# Ansible fullglob plugins

`fileglob` just globs files (hence the name) and all the magic dwimming in the ansible source makes it hard to just glob for files.

These plugins provide a simple glob mechanism relative to the playbook: `with_fullglob` and ` | fullglob`.
