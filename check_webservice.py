#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Koldo Oteo - (koteo [at] sitereliabilityengineer.io)
# December 18th 2017
import sys, time
import argparse
import httplib
import xml.dom.minidom
 
### Parse arguments
parser = argparse.ArgumentParser(description='Example:  ./query_webservice.py -file /tmp/file.xml \
                                 -host hostname.domain -context /context -soapv v1.1')
parser.add_argument('-file', action='store', dest='xml',
                    help='xml File Name')
parser.add_argument('-host', action='store', dest='host',
                    help='Webservice host')
parser.add_argument('-context', action='store', dest='context',
                    help='Webservice context')
parser.add_argument('-soapv', action='store', dest='soapv',
                    help='Soap Version v1.1 or v1.2')
# Print Parser Help
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
param = parser.parse_args()
###
 
### FUNCTION TO Read xml File
def read_xml():
   with open(param.xml, 'r') as f:
      xmlmsg = f.read()
      return xmlmsg
 
###
 
### FUNCTION TO POST XML TO WEBSERVICE
def post_xml(xmlmsg):
   """HTTP XML Post request"""
   if param.soapv == "v1.2":
      headers = {"Content-type": "application/soap+xml","Content-Length": "%d" % len(xmlmsg), "charset": "utf-8", "SOAPAction": "", "User-Agent": "PythonSOAPClient"}
   elif param.soapv == "v1.1":
      headers = {"Content-type": "text/xml","Content-Length": "%d" % len(xmlmsg), "charset": "utf-8", "SOAPAction": "", "User-Agent": "PythonSOAPClient"}
   conn = httplib.HTTPSConnection(param.host)
   conn.request("POST", param.context, "", headers)
   # Send xml
   conn.send(xmlmsg)
   response = conn.getresponse()
   print "HTTP_CODE: %s  HEALTH: %s" % (response.status, response.reason)
   data = response.read()
   #resultxml = xml.dom.minidom.parseString(data)
   #print (resultxml.toprettyxml())
   conn.close()
 
###
# READ XML FILE
xmlmsg = read_xml()
 
# GET EXECUTION TOTAL TIME AND POST XML
start_time = time.time()
post_xml(xmlmsg)
print("Exec_Total_Time: %s ms" % int(round((time.time() - start_time) * 1000)))
 
 
###
