#!/bin/bash

# HOST_INFO=host.info
# for IP in $(awk '/^[^#]/{print $1}' $HOST_INFO); do
# 	#取出用户名和端口
#     USER=$(awk -v ip=$IP 'ip==$1{print $2}' $HOST_INFO)
#     PORT=$(awk -v ip=$IP 'ip==$1{print $3}' $HOST_INFO)
# 	#创建临时文件，保存信息
#     TMP_FILE=/tmp/disk.tmp
# 	#通过公钥登录获取主机磁盘信息
#     ssh -p $PORT $USER@$IP 'df -h' > $TMP_FILE
# 	#分析磁盘占用空间
#     USE_RATE_LIST=$(awk 'BEGIN{OFS="="}/^\/dev/{print $NF,int($5)}' $TMP_FILE)
# 	#循环磁盘列表，进行判断
#     for USE_RATE in $USE_RATE_LIST; do
# 		#取出等号（=）右边的值 挂载点名称
#         PART_NAME=${USE_RATE%=*}  
# 		#取出等号（=）左边的值  磁盘利用率
#         USE_RATE=${USE_RATE#*=}
# 		#进行判断
#         if [ $USE_RATE -ge 80 ]; then
#             echo "Warning: $PART_NAME Partition usage $USE_RATE%!"
#             echo "服务器$IP的磁盘空间占用过高，请及时处理" | mail -s "空间不足警告" 你的qq@qq.com
# 		else
# 			echo "服务器$IP的$PART_NAME目录空间良好"
#         fi
#     done
# done


# HOST_INFO=host.info
# for IP in $(awk '/^[^#]/{print $1}' $HOST_INFO); do

#     USER=$(awk -v ip=$IP 'ip==$1{print $2}' $HOST_INFO)
#     PORT=$(awk -v ip=$IP 'ip==$1{print $3}' $HOST_INFO)
#     # PORT=$(awk '{print $3}' $HOST_INFO)
#     echo "${IP}" $USER $PORT
# done


# LOG_DIR=$(pwd)
# LOG_FILE_LIST="inventory.ini"
# mkdir b.txt
# for LOG_FILE in $LOG_FILE_LIST; do
#     echo $LOG_FILE
#     mv $LOG_DIR/$LOG_FILE $LOG_DIR/b.txt
# done


# DATE=$(date +%d/%b/%Y:%H:%M)
# LOG_FILE=/usr/local/nginx/logs/demo2.access.log
# ABNORMAL_IP=$(tail -n5000 $LOG_FILE |grep $DATE |awk '{a[$1]++}END{for(i in a)if(a[i]>10)print i}')
# for IP in $ABNORMAL_IP; do
#     if [ $(iptables -vnL |grep -c "$IP") -eq 0 ]; then
#         iptables -I INPUT -s $IP -j DROP
#         echo "$(date +'%F_%T') $IP" >> /tmp/drop_ip.log
#     fi
# done
# echo
# echo -e "\tMenu\n"
# echo -e "1. Install Nginx" &&echo -e "2. Installdfsa PdfsHP"
# echo -e "3. Install MySQL"
# echo -e "4. Deploy LNMP"
# echo -e "9. Quit"




# #!/bin/bash

# for arg in elem1 elem2 ... elemN
# do
#     ./cat.sh --search $arg | tee -a search.log
# done

# !/bin/sh
# BIOS_VERSION=`sudo dmidecode -t bios|grep Version`
# # xmlcli for server only platform EGS onwards will support.
# BACKEND=xmlcli
# lscpu | grep -q amx
# if [ $? != 0 ]; then
#     BACKEND=syscfg
#     if [[ "$BIOS_VERSION" =~ "CRB" ]]; then
#         BACKEND=xmlcli
#     fi
#     if [[ $BACKEND = "syscfdfg" ]]; then
#         # ./syscfg /s ${SYSTEM_NAME}.ini /b  
#         echo 100afd
#     fi
# fi

# if ! command -v conda >/dev/null 2>&1; then                  
#         echo "start install miniconda......"               
#         echo 100
# fi   

PS3="Choose the package manager: "   #select选项提示符
select ITEM in bower npm gem pip     #select循环，已编号和字符串的形式标出
do
echo -n "Enter the package name: " && read PACKAGE  #不换行输入想要安装的包
case ${ITEM} in                      ##
  bower) bower install ${PACKAGE} ;; 
  npm) npm install ${PACKAGE} ;;
  gem) gem install ${PACKAGE} ;;
  pip) pip install ${PACKAGE} ;;
esac
break # 避免无限循环
done