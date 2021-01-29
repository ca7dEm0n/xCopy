###
 # @Author: cA7dEm0n
 # @Blog: http://www.a-cat.cn
 # @Since: 2020-05-22 23:39:03
 # @Motto: 欲目千里，更上一层
### 
SCRIPT_DIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd)
source ${SCRIPT_DIR}/.env

declare -r  SGR_RESET="\033[0m"
declare -r  SGR_FAINT="\033[2m"
declare -r  SGR_RED="\033[31m"
declare -r  SGR_CYAN="\033[36m"
declare -r  SGR_GREEN="\033[42m"

echoRed () {
    : print red color
    printf "${SGR_RED}%s${SGR_RESET}\n" "$*"
}

echoGreen() {
    : print green color
    printf "${SGR_GREEN}%s${SGR_RESET}\n" "$*"
}

processPS() {
    local proc=$1
    local args=$2
    ps -ef |ggrep -v grep|grep ${arg} "${proc}"
}

xCopyPS() {
    local arg=$1
    processPS "xCopy.py" ${arg}
}

start() {
    xCopyPS -q && echo "xCopy is Running Status ..." && exit 0
    nohup ${XCOPY_PYTHON} ${SCRIPT_DIR}/xCopy.py > ${SCRIPT_DIR}/run.log 2>&1 &
    status
}

log() {
    tail -F ${SCRIPT_DIR}/xcopy.log
}

status() {
   xCopyPS -q && { printf "xCopy Running Status:\t"; echoGreen "[OK]"; } || { printf "xCopy Running Status:\t"; echoRed "[Fail]"; }
}

stop() {
    xCopyPS -q && echo "Stop xCopy Now.." || { echo "xCopy is not running."; exit 0; }
    kill $(ps -ef|grep  'xCopy.py'|grep -v "grep" |awk '{print $2}') 
    status
}

restart() {
    stop
    sleep 0.5
    start
}

$*