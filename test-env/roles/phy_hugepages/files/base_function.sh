#!/usr/bin/env bash

proxyCommand='nc -x child-prc.intel.com:1080 %h %p'
installzip="if [ -f /etc/redhat-release ];then sudo yum install -y zip unzip; else sudo apt-get install -y zip unzip; fi"

function checkArgEmpty() {                                                                                                                      
	if [ ! -n "$1" ]; then 
		echo "IS NULL" 
	else 
		echo "NOT NULL" 
	fi                                                                                                                                        
}

function installZip() {
	if [ -f /etc/redhat-release ]; then
		sudo yum install -y zip unzip
	else
		sudo apt-get install -y zip unzip
	fi
}

function getAllFilesInDirectory() {
	for file in $(ls -a $1); do
		if [ -d $1"/"$file ]; then
			if [[ $file != '.' && $file != '..' ]]; then
				getAllFilesInDirectory $1"/"$file
			fi
		else
			echo $1"/"$file
		fi
	done
}

#eval $installzip
function printLine() {
	if [ ! $1 ]; then
		outword='='
	else
		outword=$1
	fi
	shellwidth=$(stty size | awk '{print $2}')
	yes $outword | sed $shellwidth'q' | tr -d '\n'
}

function containsStr() {
	if [[ $1 =~ $2 ]]; then
		return 0
	else
		return 1
	fi
}

function echoColor() {
	case $1 in
	green)
		echo -e "\033[32;40m$2\033[0m"
		;;
	red)
		echo -e "\033[31;40m$2\033[0m"
		;;
	*)
		echo "Example: echo_color red string"
		;;
	esac
}

function rootAuth() {
	if [ $UID -ne 0 ]; then
		echoColor red "Non root user. Please run as root."
		exit 1
	else
		echoColor green "Root user"
	fi
}

function systemType() {
	if [ -f /etc/redhat-release ]; then
		echo "CentOS"
	elif [ -f /etc/lsb-release ]; then
		echo "Ubuntu"
	else
		echo "Unknown"
		exit 1
	fi
}

function switchDirectoryExecScript() {
	# $1: script absolute path $2 cmd args
	cd $(dirname $1)
	suffixFlag=$(echo $(basename $1) | awk -F "." '{print $2}')
	echo $suffixFlag
	if [ $suffixFlag == "py" ]; then
		if [ ! -n "$2" ]; then
			pipenv run ./$(basename $1)
		else
			python3 ./$(basename $1) $2
		fi
	else
		./$(basename $1) "$2"
		echo $(pwd)
		cd -
	fi
}


function waitHostRestart() {
	echo "Waiting for restart......"
	sleep 12
	while true; do
		if ping -c 1 $1 >/dev/null; then
			echo "$1 OK."
			echo done!
			break
		else
			echo "$1 NO! "
			echo "Waiting for restart......"
			sleep 10s
		fi
	done
}

function progreSh() {
	LR='\033[1;31m'
	LG='\033[1;32m'
	LY='\033[1;33m'
	LC='\033[1;36m'
	LW='\033[1;37m'
	NC='\033[0m'
	if [ "${1}" = "0" ]; then TME=$(date +"%s"); fi
	SEC=$(printf "%04d\n" $(($(date +"%s") - ${TME})))
	SEC="$SEC sec"
	PRC=$(printf "%.0f" ${1})
	SHW=$(printf "%3d\n" ${PRC})
	LNE=$(printf "%.0f" $((${PRC} / 2)))
	LRR=$(printf "%.0f" $((${PRC} / 2 - 12)))
	if [ ${LRR} -le 0 ]; then LRR=0; fi
	LYY=$(printf "%.0f" $((${PRC} / 2 - 24)))
	if [ ${LYY} -le 0 ]; then LYY=0; fi
	LCC=$(printf "%.0f" $((${PRC} / 2 - 36)))
	if [ ${LCC} -le 0 ]; then LCC=0; fi
	LGG=$(printf "%.0f" $((${PRC} / 2 - 48)))
	if [ ${LGG} -le 0 ]; then LGG=0; fi
	LRR_=""
	LYY_=""
	LCC_=""
	LGG_=""
	for ((i = 1; i <= 13; i++)); do
		DOTS=""
		for ((ii = ${i}; ii < 13; ii++)); do DOTS="${DOTS}."; done
		if [ ${i} -le ${LNE} ]; then LRR_="${LRR_}#"; else LRR_="${LRR_}."; fi
		echo -ne "  ${LW}${SEC}  ${LR}${LRR_}${DOTS}${LY}............${LC}............${LG}............ ${SHW}%${NC}\r"
		if [ ${LNE} -ge 1 ]; then sleep .05; fi
	done
	for ((i = 14; i <= 25; i++)); do
		DOTS=""
		for ((ii = ${i}; ii < 25; ii++)); do DOTS="${DOTS}."; done
		if [ ${i} -le ${LNE} ]; then LYY_="${LYY_}#"; else LYY_="${LYY_}."; fi
		echo -ne "  ${LW}${SEC}  ${LR}${LRR_}${LY}${LYY_}${DOTS}${LC}............${LG}............ ${SHW}%${NC}\r"
		if [ ${LNE} -ge 14 ]; then sleep .05; fi
	done
	for ((i = 26; i <= 37; i++)); do
		DOTS=""
		for ((ii = ${i}; ii < 37; ii++)); do DOTS="${DOTS}."; done
		if [ ${i} -le ${LNE} ]; then LCC_="${LCC_}#"; else LCC_="${LCC_}."; fi
		echo -ne "  ${LW}${SEC}  ${LR}${LRR_}${LY}${LYY_}${LC}${LCC_}${DOTS}${LG}............ ${SHW}%${NC}\r"
		if [ ${LNE} -ge 26 ]; then sleep .05; fi
	done
	for ((i = 38; i <= 49; i++)); do
		DOTS=""
		for ((ii = ${i}; ii < 49; ii++)); do DOTS="${DOTS}."; done
		if [ ${i} -le ${LNE} ]; then LGG_="${LGG_}#"; else LGG_="${LGG_}."; fi
		echo -ne "  ${LW}${SEC}  ${LR}${LRR_}${LY}${LYY_}${LC}${LCC_}${LG}${LGG_}${DOTS} ${SHW}%${NC}\r"
		if [ ${LNE} -ge 38 ]; then sleep .05; fi
	done
}

<<'EOF'
printf "\n\n"
echo "this is a test for progress bar~"
#wget https://releases.ubuntu.com/20.04/ubuntu-20.04.3-live-server-amd64.iso &
for((index=0;index<=100;index++))
do
	progreSh $index
done
echo "this is a test for progress bar~"
printf "\n\n"
#
EOF
