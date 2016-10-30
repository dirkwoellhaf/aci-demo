#!/usr/bin/env python

import json

json_data= '''
{
	"pods": 2,
    "pod": ""
}'''

json_data[1].append({"f":var3, "g":var4, "h":var5})
data = json.loads(json_data)

print "ORG DATA:" + str(data["pods"])


#data["pod-1"] = "world"
#data["pod-1-spines"] = "201,202"
#data["pod-1-spine-201-ports"] = "eth1/1,eth2/2"
#data["pod-1-spine-201-eth1/1-address"] = "1.1.1.1/30"
#data["pod-1-spine-201-eth2/2-address"] = "1.1.2.1/30"




print json.dumps(data)
