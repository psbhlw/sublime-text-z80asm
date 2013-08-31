#!/bin/sh
# ----------------------------------------------------------------------------
# This script builds the source. At first it's search for build.sh in the
# project folder. If it's found - call it, otherwise run ASM against asm-file.
# Current directory at entry to this script is asm-file's directory.
# There are two input parameters:
#   1. filename (without path),
#   2. project file path.
# ----------------------------------------------------------------------------

ASM=sjasmplus

# Run external script from project folder if exists
if [ -f "$2/build.sh" ]
then
    cd "$2"
    build.sh "$1" "$2"

elif [ -f "$1" ]
then
    # Simple compile
    "$ASM" "$1"

    # Compile with listings, symbols, exports
    # "$ASM" --lst="${1%.*}.lst" --sym="${1%.*}.sym" --exp="${1%.*}.exp" "$1"

    # Remove .out file
    if [ "$?" -eq "0"]
    then
        rm "${1%.*}.out"
        exit 0
    fi

else
    echo "Source file not found!"
    exit 1
fi
