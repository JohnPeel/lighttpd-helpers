#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--host', required=True)

ssl_template = '''
$SERVER["socket"] == ":443" {
  ssl.engine    = "enable"
  ssl.pemfile   = "/etc/letsencrypt/live/%s/ssl.pem"
  ssl.ca-file   = "/etc/letsencrypt/live/%s/chain.pem"
  
  ssl.use-sslv2 = "disable"
  ssl.use-sslv3 = "disable"
  ssl.use-compression = "disable"

  ssl.honor-cipher-order = "enable"
  ssl.disable-client-renegotiation = "enable"
  ssl.dh-file = "/etc/lighttpd/dhparams.pem"
  ssl.ec-curve = "secp384r1"

  ssl.cipher-list = "ECDH+AESGCM:DH+AESGCM:RSA+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AES:RSA+3DES:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!PSK:!RC4"
  setenv.add-response-header = (
    "Strict-Transport-Security" => "max-age=63072000",
    "X-Frame-Options" => "SAMEORIGIN", # DENY",
    "X-Content-Type-Options" => "nosniff"
  )
}
'''.strip()

if (__name__ == '__main__'):
    args = parser.parse_args()
    print(ssl_template % (args.host, args.host))
