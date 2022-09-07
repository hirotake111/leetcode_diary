#!/bin/zsh

PARENT=leetcode

if [ -z "$1" ]
then
    cat <<- EOF

=== usege ===
$0 <directory_name>
-> creates a new directory with a file "solution.py"
=============
EOF
    exit 1
fi

NEW_DIR=$PARENT/$1

if [ -d $NEW_DIR ] 
then
    cat << EOF

directory $NEWDIR already exists - skipped.
EOF
    exit 0
fi


mkdir $NEW_DIR
cd $NEW_DIR
touch solution.py
echo "done!"
