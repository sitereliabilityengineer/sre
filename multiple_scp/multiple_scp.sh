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
	 $0 -f hosts_file.txt -n host_group -u USER -o files_to_copy -d /destination_directory

        Options:
                -h,     Print help.
                -f,     File with host groups.
		-s,	Show host groups names.
                -n,     Host group name.
                -u,     User you use for scp.
                -o,     Origin files to copy.
		-d,	Destination directory.

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
        do scp -pr "$o" "$u"@$i:"$d"
done
}

###

while getopts ":hf:sn:u:o:d:" opts; do
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
        o)
            o=${OPTARG}
            ;;
	d)
	    d=${OPTARG}
	    ;;
        *)
            usage
            ;;
    esac
done

#
[[ -z "$1" ]] && usage

if

[ -n "$f" ] && [ -n "$n" ]  && [ -n "$u" ] && [ -n "$o" ] && [ -n "$d" ]
then
	exec_comm
fi

if [ -n "$f" ] && [ -n "$s" ]
then
	show_hgroups
fi
