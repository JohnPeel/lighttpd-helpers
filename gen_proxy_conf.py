#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-o', '--host')
group.add_argument('-s', '--subdir')
parser.add_argument('-i', '--ip', required=True)
parser.add_argument('-p', '--port', required=True, type=int)
parser.add_argument('-l', '--ssl', action='store_true')
parser.set_defaults(ssl=False)

url_template = '''
$HTTP["url"] =~ "^/%s(/.*)?$" {
  proxy.server = (
    "" => (
      (
        "host" => "%s",
        "port" => %d
      )
    )
  )
}
'''.strip()

host_template_ssl = '''
$HTTP["host"] == "%s" {
  include_shell "/usr/bin/gen_ssl_section.py -o %s"

  proxy.server = (
    "" => (
      "%s" => (
        "host" => "%s",
        "port" => %d
      )
    )
  )
}
'''.strip()

host_template = '''
$HTTP["host"] == "%s" {
  proxy.server = (
    "" => (
      "%s" => (
        "host" => "%s",
        "port" => %d
      )
    )
  )
}
'''.strip()

if (__name__ == '__main__'):
    args = parser.parse_args()
    if args.host:
        if args.ssl:
    	    print(host_template_ssl % (args.host, args.host, args.host, args.ip, args.port))
        else:
            print(host_template % (args.host, args.host, args.ip, args.port))
    if args.subdir:
        print(url_template % (args.subdir, args.ip, args.port))
