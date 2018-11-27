#!/bin/bash

sam local generate-event s3 put --bucket SemanticWils --key test1.csv | sam local invoke --debug CreateThumbnail
