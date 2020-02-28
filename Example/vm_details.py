import argparse
import atexit
from pyVim.connect import SmartConnect, Disconnect
import humanize
import ssl
import logging
import time
import datetime
import json

MBFACTOR = float(1 << 20)

printVM = False
printDatastore = True
printHost = True


# LOG_FILENAME = 'example.log'
# logging.basicConfig(filename=LOG_FILENAME,
#                     filemode='a',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG)

log_file = dict()
log_file["DATA"] = {}

def GetArgs():

    parser = argparse.ArgumentParser(
        description='Process args for retrieving all the Virtual Machines')
    parser.add_argument('-s', '--host', required=True, action='store',
                        help='Remote host to connect to')
    parser.add_argument('-o', '--port', type=int, default=443, action='store',
                        help='Port to connect on')
    parser.add_argument('-u', '--user', required=True, action='store',
                        help='User name to use when connecting to host')
    parser.add_argument('-p', '--password', required=False, action='store',
                        help='Password to use when connecting to host')
    args = parser.parse_args()
    return args


def printHostInformation(host):
    try:
        summary = host.summary
        stats = summary.quickStats
        hardware = host.hardware
        cpuUsage = stats.overallCpuUsage
        memoryCapacity = hardware.memorySize
        memoryCapacityInMB = hardware.memorySize/MBFACTOR
        memoryUsage = stats.overallMemoryUsage
        freeMemoryPercentage = 100 - (
            (float(memoryUsage) / memoryCapacityInMB) * 100
        )
        print("--------------------------------------------------")
        print("Host name: ", host.name)
        # dump(host)
        print("Host CPU usage: ", cpuUsage)
        print("Host memory capacity: ", humanize.naturalsize(memoryCapacity,
                                                             binary=True))
        print("Host memory usage: ", memoryUsage / 1024, "GiB")
        print("Free memory percentage: " + str(freeMemoryPercentage) + "%")
        print("--------------------------------------------------")

        #logging.info("CPU usage for the host {0} is: {1}".format(host.name, cpuUsage))

        log_file["DATA"]["ESXI_host"] = host.name
        log_file["DATA"]["CPU _usage"] = cpuUsage
        log_file["created"] = datetime.datetime.utcnow().isoformat()
        with open("test.logs", 'a') as logfile:
            json.dump(log_file, logfile)
            logfile.write("\n")
        time.sleep(30)

    except Exception as error:
        print("Unable to access information for host: ", host.name)
        print(error)
        pass


def printComputeResourceInformation(computeResource):
    try:
        hostList = computeResource.host
        print("Compute resource name: ", computeResource.name)
        print("##################################################")
        for host in hostList:
            printHostInformation(host)
    except Exception as error:
        print("Unable to access information for compute resource: ",
              computeResource.name)
        print(error)
        pass


def main():
    args = GetArgs()
    try:
        si = SmartConnect(host=args.host, user=args.user,
                          pwd=args.password, port=int(args.port),
                          sslContext=ssl._create_unverified_context())
        # si = SmartConnect(host="172.30.9.56", port=443, user="administrator@vsphere.local",
        #                   pwd="Calsoft@123", sslContext=ssl._create_unverified_context())
        print("Connected")
        #time.sleep(60)
    except Exception as e:
        print(e)
    atexit.register(Disconnect, si)
    content = si.RetrieveContent()

    for datacenter in content.rootFolder.childEntity:
        print("Datacenter Name: " + datacenter.name)
        if printHost:
            if hasattr(datacenter.hostFolder, 'childEntity'):
                hostFolder = datacenter.hostFolder
                computeResourceList = hostFolder.childEntity
                for computeResource in computeResourceList:
                    printComputeResourceInformation(computeResource)
    return 0


while True:
    if __name__ == "__main__":
        main()