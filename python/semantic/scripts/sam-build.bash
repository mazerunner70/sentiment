#!/bin/bash

function build_lambda {
    local SAM_DIR=$1
    local LAMBDA_NAME=$2
    local CLEAR_DIRECTORY=$3
    local OTHER_COPY_SOURCE_DIR=$4

    printf "Building lambda: ${LAMBDA_NAME}\n"
    local BUILD_APP_DIR=${SAM_DIR}/build-${LAMBDA_NAME}
    printf "Build dir: ${BUILD_APP_DIR}\n"

    if [[ ${CLEAR_DIRECTORY} == "1" ]]; then
        printf "clearing build directory\n"
        rm -r ${BUILD_APP_DIR}
    fi

    if [[ ! -f ${BUILD_APP_DIR}/requirements-built.txt ]]; then
        # Bring in python deps
        pip3.6 install -r ${LAMBDA_NAME}-requirements.txt -t ${BUILD_APP_DIR}/
        touch ${BUILD_APP_DIR}/requirements-built.txt
    fi

    #copy .env file
    cp ../.env ${BUILD_APP_DIR}/.env

    #add lambda handler
    cp ${LAMBDA_NAME}-main.py ${BUILD_APP_DIR}/${LAMBDA_NAME}-main.py
    cp -R ../${LAMBDA_NAME} ${BUILD_APP_DIR}
    if [ ! -d "${BUILD_APP_DIR}/${OTHER_COPY_SOURCE_DIR}" ]; then
        cp -R ../${OTHER_COPY_SOURCE_DIR} ${BUILD_APP_DIR}/${OTHER_COPY_SOURCE_DIR}
    fi

}

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

# ensure script can be run from anywhere, so long as its location
# does not change relative to the sam-app
function getWorkArea {
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
    printf "This script located at ${SCRIPT_DIR}\n"

    # Location and change dir to the SAM workarea
    RELATIVE_DIR="../sam-app"
    SAM_APP_DIR="$( cd ${SCRIPT_DIR}/${RELATIVE_DIR} >/dev/null && pwd )"
    if [ ! -d "$SAM_APP_DIR" ]; then
        printf "Error - ${SAM_APP_DIR} should be a valid dir!\n"
        exit 3
    fi
    printf "dir: ${SAM_APP_DIR}"
}

getWorkArea

printf "SAM app directory at ${SAM_APP_DIR}\n"
pushd ${SAM_APP_DIR}

build_lambda ${SAM_APP_DIR} 'semantic' ${clearDirectory} 'nltk-data'
build_lambda ${SAM_APP_DIR} 'access' ${clearDirectory} ''
build_lambda ${SAM_APP_DIR} 'comprehend' ${clearDirectory} ''


popd
