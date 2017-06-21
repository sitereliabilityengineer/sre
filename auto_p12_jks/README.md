# auto_p12_jks.py: Tool for automating the creation of .p12 files
1) You need to create a .zip with a private key .key file into the zip. 
2) .crt file with the certificate
3) A params.txt file with 3 lines:
    In the first line you put the password of the privatekey and p12 
    In the second an alias for the privatekey
    In the third line, you put the mail where is going to be sent the .p12 file.

You wil also need to configure some vars:

    autop12_dir is the directory where you are going to upload the .zip files. 
    smtp_host is the host of the smtp server, 
    smtp_port with the smtp port. 
    There's also mail_from where you put the e-mail address of the sender.
