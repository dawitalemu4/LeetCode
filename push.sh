problems=0
output=$"# Easy
"

for name in "./Easy"/*; do
    name=$(echo "$name" | sed 's/\.\/Easy\///')
    output+="$name

"
    problems=$((problems+1))
done

output+=$"
# Medium
"

for name in "./Medium"/*; do
    name=$(echo "$name" | sed 's/\.\/Medium\///')
    output+="$name

"
    problems=$((problems+1))
done

output+=$"
# Hard
"

for name in "./Hard"/*; do
    name=$(echo "$name" | sed 's/\.\/Hard\///')
    output+="$name

"
    problems=$((problems+1))
done

output+="
"$problems" problems solved"

echo "$output" > README.md

git add .

while getopts "m:" arg; do

    case $arg in
        m) message=$OPTARG;;
    esac

    git commit -m "$message"

    git push origin test

done
