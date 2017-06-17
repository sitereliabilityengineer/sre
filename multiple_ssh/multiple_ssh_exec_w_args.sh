#!/bin/sh
# Koldo Oteo <koldo.oteo1@gmail.com>
#

### FUNCTIONS

#
usage()
{
cat <<EOF

Usage:   $0 [OPTION]

Example: $0 -f hosts_file.txt -s (it displays the host groups)
	 $0 -f hosts_file.txt -n host_group -u USER -c command (runs command on the host group)

        Options:
                -h,     Print help.
                -f,     File with host groups.
		-s,	Show host groups names.
                -n,     Host group name.
                -u,     User you use to login via ssh.
                -c,     Command to run in remote server.

EOF
exit 0
}

#
show_hgroups()
{
echo -e "Available host groups:\n"
echo -e "##########"
grep -e '\[[a-zA-Z]' $f | tr -d '[/]'
echo -e "##########"
echo -e "\n"
}

#
exec_comm()
{
for i in $(sed -n -e '/\['$n'\]/,/\[\/'$n'\]/ p' "$f" | sed -e '1d;$d')
        do ssh  "$u"@$i "$c"
done
}

###

while getopts ":hf:sn:u:c:" opts; do
    case "${opts}" in
        h)
	    usage 
            ;;
        f)
            f=${OPTARG}
            ;;
        s)
	    s=1
            ;;
        n)
            n=${OPTARG}
            ;;
        u)
            u=${OPTARG}
            ;;
        c)
            c=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done

#
[[ -z "$1" ]] && usage

if

[ -n "$f" ] && [ -n "$c" ]  && [ -n "$u" ] && [ -n "$c" ]
then
	exec_comm
fi

if [ -n "$f" ] && [ -n "$s" ]
then
	show_hgroups
fi
