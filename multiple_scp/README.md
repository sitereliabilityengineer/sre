# multiple_scp

/*** For quicker execution, the best option is to configure ssh passwordless (but you always need to take care of the ssh keys). You could do it with ssh-keygen and ssh-copy-id ***/

Script to copy files to multiple servers.


Script named: multiple_scp.sh
	* This scripts require arguments from the cli.
	* First arg: -f the file with the host groups
	* Second arg:-s to show the host group names (requires -f )
	* Third arg: -n to define the host group name (requires -f)
	* Fourth arg:-u username to use with ssh (requires -f -n)
	* Fifth arg: -o Origin directory or file to copy to destination  (requires -f -n -u)
	* Sixth arg: -d destination directory (requires -f -n -u -o)
