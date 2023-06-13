#!/bin/bash

# pwd 
# hostname


# Required_HugePage=$1
# Required_Size=$2

# HugePages_Total=$(grep HugePages_Total /proc/meminfo | awk '{print $2}')
# Hugepagesize=$(grep Hugepagesize /proc/meminfo | awk '{print $2}')
# HugePages_Free=$(grep HugePages_Free /proc/meminfo | awk '{print $2}')


# touch a.txt
# echo $HugePages_Total $Hugepagesize $HugePages_Free 

# echo $Required_HugePage $Required_Size

# touch b.txt




# case $1 in
#     --search) 
#         echo 
#     --find) 
#         $PYTHON_CMD -find $* 2>&1 | tee $LOG_NAME;
#         exit $? ;;
#     --set) 
#         warning ;
#         CONF_PATH=$2; shift;
#         ( $PYTHON_CMD -set $CONF_PATH $* 2>&1; echo $? > status ) | tee $LOG_NAME; 
#         if [ `cat status` $EQ 0 ];  then 
#             if [ $BACKEND $EQ 'xmlcli' ]; then
#                 reboot
#             else 
#                 /bin/bash syscfg_run.sh
#                 if [ $? $EQ 0 ];  then 
#                     rm -f syscfg_run.sh
#                     reboot
#                 fi
#             fi
#         fi ;
#         exit $? ;;
# esac


# a=()
# a+=(100)
# a+=(1)
# echo $a
# echo ${a[@]}



my_array=(A B "C" D)

echo $my_array $my_array[1] ${my_array[1]} ${my_array[@]} ${my_array}