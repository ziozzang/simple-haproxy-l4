#!python3

import os

def get_osenv(name_str, default_val=''):
    res = default_val
    if name_str in os.environ:
        res = os.environ[name_str]
    return res

MAXCONN             = get_osenv('MAXCONN', '50000')
SERVER_PORT         = get_osenv('SERVER_PORT','8888')
STATUS_PORT         = get_osenv('STATUS_PORT', '8080')
CLIENT_TIMEOUT      = get_osenv('CLIENT_TIMEOUT', '60s')
SERVER_TIMEOUT      = get_osenv('SERVER_TIMEOUT', '30s')
SERVER_OPT          = get_osenv('SERVER_OPT', 'inter 3s fastinter 1s rise 3 fall 2')
# rise: add server after check n times passed / fail: remove server after check n times failed
# inter: general checking interval / fastinter: if failed status, checking interval
CONN_TRY_TIMEOUT    = get_osenv('CONN_TRY_TIMEOUT', '8s')
LB_POLICY           = get_osenv('LB_POLICY', 'source')
# source: IP based hash
# static-rr : weighted Round-Robin
# leastconn : least connection
# roundrobin: round robin

print(f'''
global
  maxconn {MAXCONN}
  log /dev/stdout  local0
  log /dev/stderr  local1 notice
  chroot /var/lib/haproxy
  stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
  stats timeout 30s
  user haproxy
  group haproxy
  daemon

defaults
  log  global
  mode  tcp
  #option  tcplog
  option  dontlognull
  timeout client    {CLIENT_TIMEOUT}
  timeout server    {SERVER_TIMEOUT}
  timeout connect   {CONN_TRY_TIMEOUT}

frontend haproxynode
    bind *:{SERVER_PORT}
    mode tcp
    default_backend backendnodes

frontend stats
    bind *:{STATUS_PORT}
    mode http
    stats enable
    stats uri /
    stats refresh 10s

backend backendnodes
    balance {LB_POLICY}''')


n = 0
target_server = []
if 'TARGET_SERVER' in os.environ:
    target_server = os.environ['TARGET_SERVER'].strip().split(',')
    for i in target_server:
        j = i.split(':',1)
        nm = f'{n}_{i}'
        print(f'    server {nm} {i} check {SERVER_OPT}')
        n += 1
