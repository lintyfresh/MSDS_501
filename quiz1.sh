#nums=(1 2 14 21 36 9)
#threshold=5
#for numbers in ${nums[@]}
    #do
    #if [ $numbers -gt $threshold ]
    #then
        echo $numbers
    #fi
#done

git_repo=$1
folder_path=$2

if [ $# -ne 2 ]
then
    echo Please check the format.
    echo Example: "sh ./hw1.sh git_url folder_path"
    exit
fi

if [ -d $folder_path ]
then
    cd $folder_path
    git pull $git_repo
    if [ $? -eq 0 ]
    then
        echo Sucess: pulled from $git_repo to $folder_path
        ls -l
        exit
    else
        echo Failed to pull from $git_repo to $folder_path
        exit
    fi
else
    git clone $git_repo to $folder_path
    if [ $? -eq 0 ]
    then
        echo Sucess: cloned from $git_repo to $folder_path
        ls -l
        exit
    else
        echo Failed to clone from $git_repo to $folder_path
        exit
fi


