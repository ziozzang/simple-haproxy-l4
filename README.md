# simple-haproxy-l4
Simple Haproxy container for TCP Load balancer (L4).

# Why make this?
to make LB-as-a-Service. (w/ Kubernetes??)

# Author
- Jioh L. Jung

# How to Use
- build container. and set environments for injection.

# Environments values

| Environ Value | Comment | Default Value |
| --- | --- | --- |
| MAXCONN | maximum connection | 50000 |
| SERVER_PORT | port to listen | 8888 |
| STATUS_PORT | status port (at /) | 8080 |
| CLIENT_TIMEOUT | timeout for client | 60s |
| SERVER_TIMEOUT | timeout for server(backend) | 30s |
| SERVER_OPT | Backend host connection option | inter 3s fastinter 1s rise 3 fail 2 |
| CONN_TRY_TIMNE_OUT | | 8s |
| LB_POLICY | load balancer type | source |
| TARGET_SERVER | target backend server | N/A |

- SERVER_OPT
  - inter: checking interval
  - fastinter: if failed status, checking interval
  - rise: after n times checking passed, add to service up
  - fail: after n times checking failed, remove from service
- TARGET_SERVER
  - target backend servers list. splited by ','
  - ex: google.com:443,naver.com:443


