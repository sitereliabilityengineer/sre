#!/bin/sh
# Koldo Oteo <koldo.oteo1@gmail.com>
# 

## VARS DEFINITION
# Define filename and location with hosts/ips and host group names
hfile=hosts_file.txt

##

# Display the available host groups names
# With grep we search for a string that starts with [ followed by a string (downcase or uppercase)
# With the tr we delete the characters [ / ]
echo -e "Available host groups:\n"
echo -e "############"
grep -e '\[[a-zA-Z]' $hfile | tr -d '[/]'
echo -e "############"

echo -e "\n"
# Input the name of the host group
echo -e "Please input host group name:"
read h_group

# Input the username you are going to use for ssh
echo -e "Please input the username you will use for ssh:"
read usr

# Here you have to input the command you want to execute remotely by ssh
echo -e "Please input the command you want to execute:"
read comm

clear
# with the  first sed we look for the first host group until we close the host group with [/h_group] 
# with the second sed we delete the first line and the last, because here we dont need the host group name
# with the for, we read line by line and we execute ssh with output
for i in $(sed -n -e '/\['$h_group'\]/,/\[\/'$h_group'\]/ p' hosts_file.txt | sed -e '1d;$d')
	do ssh  "$usr"@$i "$comm"
done
