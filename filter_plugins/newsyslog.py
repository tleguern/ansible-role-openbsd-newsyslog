from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError

def newsyslog(line):
  name = line['name']
  owner = line['owner']
  group = line['group']
  mode = line['mode']
  count = line['count']
  size = line['size'] if 'size' in line else '*'
  when = line['when'] if 'when' in line else '*'
  flags = line['flags'] if 'flags' in line else 'Z'
  monitor = line['monitor'] if 'monitor' in line else None
  pidfile = line['pidfile'] if 'pidfile' in line else None
  signal = line['signal'] if 'signal' in line else None
  command = line['command'] if 'command' in line else None

  output = "{} {}:{} {:<4} {:<5} {:<4} {:<5} {}".format(name, owner, group, mode, count, size, when, flags)
  if monitor:
    output += f" {monitor}"
  if pidfile:
    output += f" {pidfile}"
  if signal:
    output += f" {signal}"
  if command:
    output += f' "{command}"'
  
  return output

class FilterModule(object):
    ''' Newsyslog filter '''

    def filters(self):
        return {
            'newsyslog': newsyslog
        }
