I usually need to check webservices. I check the http code and the time it takes to give me back the result of the soap query. It works only with ssl.

To execute the code:

python ./query_webservice.py -file /tmp/file.xml -host ws.example.com -context /context/ws -soapv v1.1

You will need to have a valid file.xml and specify the soap version

The output result:

HTTP_CODE: 200 HEALTH: OK
Exec_Total_Time: 35 ms
