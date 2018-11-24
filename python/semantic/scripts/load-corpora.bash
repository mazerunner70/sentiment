#!/bin/bash


SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
echo "This script located at ${SCRIPT_DIR}"
RELATIVE_DIR="../nltk_data"
NLTK_DATA_DIR="$( cd ${SCRIPT_DIR}/${RELATIVE_DIR} >/dev/null && pwd )"
if [ ! -d "$NLTK_DATA_DIR" ]; then
    printf "Error - ${NLTK_DATA_DIR} should be a valid dir!\n"
    exit 3
fi

printf "NLTK data directory at ${NLTK_DATA_DIR}\n"

if [ -d "$NLTK_DATA_DIR/corpora" ]; then
    printf "copora already downloaded\n"
    printf "Reload if required by deleting dir at "
    printf "$NLTK_DATA_DIR/corpora\n"
else
    export NLTK_DATA=$NLTK_DATA_DIR
    python3.6 -m textblob.download_corpora
fi

if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    export NLTK_DATA=$NLTK_DATA_DIR
else
    printf "This script is not source'd so cannot change env vars\n"
    printf "Please run the command below to allow the corpora to be used\n"
    printf "export NLTK_DATA=$NLTK_DATA_DIR\n"
fi
printf "Please restart VSCode after setting the env var.\n"
