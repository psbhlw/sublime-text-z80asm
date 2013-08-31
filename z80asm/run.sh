#!/bin/sh
# ----------------------------------------------------------------------------
# This script runs the emulator. At first it's search for emul.sh in the
# project folder. If it's found - call it, otherwise it will search for
# .sna/.spg/.trd/.scl/.tap and call EMUL with it.
# Current directory at entry to this script is asm-file's directory.
# There are two input parameters:
#   1. filename (without path),
#   2. project file path.
# ----------------------------------------------------------------------------

EMUL=unreal

# Get file name without extension
NAME=${1%.*}

# Run external script from project folder if exists
if [ -f "$2/emul.sh" ]
then
    cd "$2"
    emul.sh "$1" "$2"

# Check if .sna file exists
elif [ -f "$NAME.sna" ]
then
    "$EMUL" "$NAME.sna"

# Check if .spg file exists
elif [ -f "$NAME.spg" ]
then
    "$EMUL" "$NAME.spg"

# Check if .trd file exists
elif [ -f "$NAME.trd" ]
then
    "$EMUL" "$NAME.trd"

# Check if .scl file exists
elif [ -f "$NAME.scl" ]
then
    "$EMUL" "$NAME.scl"

# Check if .tap file exists
elif [ -f "$NAME.tap" ]
then
    "$EMUL" "$NAME.tap"

else
    echo No image file found!

fi
