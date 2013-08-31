#!/bin/sh

DIR=${0%buildrun.sh}

"${DIR}build.sh" "$1" "$2"

if [ "$?" -eq "0" ]
then
    "${DIR}run.sh" "$1" "$2"

fi
