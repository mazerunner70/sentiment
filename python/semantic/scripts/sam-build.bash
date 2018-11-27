#!/bin/bash

#instructions from 


while getopts ":c" opt; do
    case ${opt} in
      c )
        clearDirectory=1
        ;;
      \? )
        echo "Usage: $0 [-c]"
        ;;
    esac
done

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
echo "This script located at ${SCRIPT_DIR}"

RELATIVE_DIR="../sam-app"
SAM_APP_DIR="$( cd ${SCRIPT_DIR}/${RELATIVE_DIR} >/dev/null && pwd )"
if [ ! -d "$SAM_APP_DIR" ]; then
    printf "Error - ${SAM_APP_DIR} should be a valid dir!\n"
    exit 3
fi

printf "SAM app directory at ${SAM_APP_DIR}\n"

pushd ${SAM_APP_DIR}
if [[ "${clearDirectory}" -eq "1" ]]; then
    printf "clearing SAM directory\n"
    rm -r ${SAM_APP_DIR}/build
fi
pip3.6 install -r requirements.txt -t build

cp app.py build/app.py
cp -R ../semantic build
if [ ! -d "$SAM_APP_DIR/build/taggers" ]; then
    cp -R ../nltk_data/* build
fi

popd
