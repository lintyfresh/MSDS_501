url=$1
folder=$2
if [ $# -ne 2 ]
then
    echo Please check the format.
    echo Example: "sh ./hw1.sh git_url folder_path"
    exit
fi

if [ -d "$folder" ]
then
cd "$folder"
git pull $url
    if [ $? -eq 0 ]
    then
        echo Success: Pulled from $url to $folder
        ls -la
    else
        echo Failed to pull from $url to $folder
        exit
    fi

else
    git clone $url $folder
    if [ $? -eq 0 ]
    then
        echo Success: Cloned from $url to $folder
        ls -la
    else    
        echo Failed to clone from $url to $folder
        exit
    fi
fi


