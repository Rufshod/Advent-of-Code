#!/bin/bash

# error message if no argument was passed when running the script
if [ -z "$1" ]; then
    echo "Please provide the year you are doing as an argument."
    exit 1
fi

# store passed argument as foldername
foldername="$1"

echo "Year selected: ${foldername}"
echo "Creating files in [${foldername}] folder..."

# create target folder and subfolder if they don't exist
mkdir -p "$foldername"
mkdir -p "$foldername/data"

# loop through day 1-25 and create a .py file for code and .txt file for puzzle input
for ((day=3; day<=25; day++))
do
    # create exercise files:
    if [ $day -lt 10 ]; then
        filename="0${day}" # prepend 0 to single digit days
    else
        filename="$day"
    fi

    # name of .py and .txt file to be created
    code_file="${foldername}/${filename}.py"
    data_file="${filename}.txt"

    # boilerplate code to put in .py file
    boilerplate_code="# day ${filename}

# setup
with open('data/${filename}.txt', 'r') as file:
    data = file.read() # TODO format data here

# part 1

"
    # create .py file with boilerplate code, and empty .txt file
    echo "$boilerplate_code" > "$code_file"
    touch "${foldername}/data/${data_file}"

done

echo "Setup finished"
