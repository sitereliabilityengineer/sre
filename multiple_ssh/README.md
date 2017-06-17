# multiple_ssh

/*** For quicker execution, the best option is to configure ssh passwordless (but you always need to take care of the ssh keys). You could do it with ssh-keygen and ssh-copy-id ***/

Here we have two scripts to execute remote commands on multiple servers.

Script named as: multiple_ssh_exec.sh
	* When executed, it displays a menu.
	* In the first lines it gives the host groups names.
	* You will need to input as first option a host group name.
	* On the second option you will need to input a Username.
	* Third option: input a command to execute on remote host.


Script named: multiple_ssh_exec_w_args.sh
	* This scripts require arguments from the cli.
	* First arg: -f the file with the host groups
	* Second arg:-s to show the host group names (requires -f )
	* Third arg: -n to define the host group name (requires -f)
	* Fourth arg:-u username to use with ssh (requires -f -n)
	* Fifth arg: -c command to use on remote host (requires -f -n -u)
