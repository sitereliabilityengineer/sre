# auto_p12_jks.py: Tool for automating the creation of .p12 files

At this moment, the script only works with unauthenticated smtp´s. In the future will also create a .jks

## Steps:

1) You need to create a .zip with a private key .key file into the zip. 
2) .crt file with the certificate
3) A params.txt file with 3 lines:
    In the first Line you have to put the password of the pem file with the private key.
    In the second Line you have to put the password of the privatekey and p12.
    In the third Line, an alias for the privatekey.
    In the fourth Line, you have to put the mail where is going to be sent the .p12 file.

You wil also need to configure some vars:

    autop12_dir is the directory where you are going to upload the .zip files. 
    smtp_host is the host of the smtp server, 
    smtp_port with the smtp port. 
    mail_from where you put the e-mail address of the sender.
