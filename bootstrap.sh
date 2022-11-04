#!/bin/bash
HAPROXY_CFG='/usr/local/etc/haproxy/haproxy.cfg'

cd /
echo "Generate haproxy configuration..."
python3 haproxy_config_gen.py > ${HAPROXY_CFG}
echo "Checking haproxy configuration..."
haproxy -c -f ${HAPROXY_CFG}
RET="$?"

if [ "$RET" == "0" ]; then
	echo "Start HAProxy..."
	haproxy -f ${HAPROXY_CFG}
	echo "Started"
	sleep inf
else
	echo "Haproxy failed to start (exit code: ${RET})"
	exit ${RET}
fi

