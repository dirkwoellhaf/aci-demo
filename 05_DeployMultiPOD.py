#!/usr/bin/env python
'''
 This is a quick and dirty collection of script-snippets!

 NO OFFICIAL SUPPORT!!!
'''
import getpass
import requests
import time
import sys
import json
#import array

import aci_demo

#-------------------------------------------------------------------------------
# Functions
def UnsupportedInput():
    print "Unsupported Input! Check the verified scalability guide for more details."

def DefinePOD(mp_pods):
    mp_pod=1

    mp_json = '{}'

    mp_data = json.loads(mp_json)
    mp_data["pods"] = mp_pods

    while mp_pod <=mp_pods:
        mp_pod_spine = 1

        print "\nDetails for POD "+str(mp_pod)
        mp_pod_spines = raw_input('\nNode-ID of Spines in POD '+str(mp_pod)+' [201,202, etc.]: ')
        mp_data["pod-"+str(mp_pod)+"-spines"]=str(mp_pod_spines)

        mp_pod_spines = mp_pod_spines.split(",")

        for mp_pod_spine in mp_pod_spines:
            mp_pod_spine_ports = raw_input('\nPorts on Spine-'+str(mp_pod_spine)+' [eth1/1,eth1/2, etc.]: ')
            mp_data["pod-"+str(mp_pod)+"-spine-"+str(mp_pod_spine)+"-ports"]=str(mp_pod_spine_ports)
            mp_pod_spine_ports = mp_pod_spine_ports.split(",")

            for mp_pod_spine_port in mp_pod_spine_ports:
                mp_pod_spine_port_address = raw_input('\nIP-Address for '+str(mp_pod_spine_port)+' [X.X:X.X/Y]: ')
                mp_data["pod-"+str(mp_pod)+"-spine-"+str(mp_pod_spine)+"-port-"+str(mp_pod_spine_port)]=str(mp_pod_spine_port_address)

        mp_pod += 1

    print json.dumps(mp_data, indent=4)
    if raw_input('MultiPOD Data correct? [Y/N]: ').upper() == "Y":
        return mp_data
    else:
        exit

def DeployMultiPOD(mp_data):
    #print mp_data["pods"]
    pod=1
    while pod <= mp_data["pods"]:
        print "POD-"+str(pod)+" - Spines: "+ mp_data["pod-"+str(pod)+"-spines"]
        pod += 1




#-------------------------------------------------------------------------------
# Main

mp_supported_pods = 6

if __name__ == '__main__':
    print ""
    if raw_input('\nDeploy ACI MultiPOD? [Y/N]: ').upper() == "Y":
        mp_pods = int(raw_input('\nNumer of PODs? [2-'+str(mp_supported_pods)+']: '))

        if mp_pods <= mp_supported_pods:
            mp_data = DefinePOD(mp_pods)
            DeployMultiPOD(mp_data)

        else:
            UnsupportedInput()
