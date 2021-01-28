# ansible-role-openbsd-newsyslog

[![builds.sr.ht status](https://builds.sr.ht/~tleguern/ansible-role-openbsd-newsyslog.svg)](https://builds.sr.ht/~tleguern/ansible-role-openbsd-newsyslog?)

Ansible role for OpenBSD's newsyslog, an equivalent to logrotate.

Automatic testing is provided using molecule's delegated driver and https://builds.sr.ht.

## Requirements

None.

## Role Variables

| Variable | Description |
|----------|-------------|
| `newsyslog_config` | newsyslog configuration in plain text |
| `newsyslog_extra_rules` | Additional rules to append to the default configuration |

Variables `newsyslog_config` and `newsyslog_extra_rules` are mutually incompatible.

### `newsyslog_extra_rules`

This variable is as YAML representation of lines in newsyslog.conf as a list of hashes.

| Key     | Default value |
|---------|---------------|
|   name  |     mandatory | 
|   owner |     mandatory |
|   group |     mandatory |
|    mode |     mandatory |
|   count |     mandatory |
|    size |           `*` |
|    when |           `*` |
|   flags |           `Z` |
| monitor |      optional |
| pidfile |      optional |
|  signal |      optional |
| command |      optional |

Example:

```yaml
newsyslog_extra_rules:
  - name: /var/log/mysql.log
    owner: root
    group: wheel
    mode: 600
    count: 5
```

## Dependencies

None.

## Example Playbooks

Overwriting existing newsyslog.conf:

```yml
- hosts: syslog
  vars:
    newsyslog_config: |
      /var/cron/log root:wheel 600 7 300 * Z
      /var/www/logs/www.example.com.access.log root:daemon 644 4 * * Z "pkill -USR1 -u root -U root -x httpd"
  roles:
    - role: aversiste.newsyslog
```

Appending lines to a default configuration:

```yml
- hosts: matomo
  vars:
    newsyslog_extra_rules:
      - name: /var/www/logs/www.example.com.access.log
        owner: root
        group: daemon
        mode: 644
        count: 4
        command: "pkill -USR1 -u root -U root -x httpd"
  roles:
  - role: aversiste.newsyslog
```

## License

ISC

## Contributing

Either send [send GitHub pull requests](https://github.com/Aversiste/ansible-role-openbsd-newsyslog) or [send patches on SourceHut](https://lists.sr.ht/~tleguern/misc).

## Author Information

Written by Tristan Le Guern.
