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

else
    NEW_DIR=$PARENT/$1
    mkdir $NEW_DIR
    cd $NEW_DIR
    touch solution.py
    echo "done!"
fi
