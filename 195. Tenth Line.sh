# Read from the file file.txt and output the tenth line to stdout.

# solution 1: pipeline

#!/bin/bash
tail -n+10 file.txt|head -1

# tail -n 10 file.txt shows the last 10 lines
# tail -n+10 file.txt shows from the 10th line to the end
# If your file has 15 lines, this command outputs lines 10, 11, 12, 13, 14, and 15

# pipe: This takes the output from the tail command and feeds it directly into the next command as input.

# head -n 1 (or head -1): takes whatever it receives and prints only the very first line




# Solution 2: stream editor

#!/bin/bash
sed -n 10p file.txt

# By default, sed prints every line it processes
# sed -n 10p
# Line 1-9: sed reads them, sees they aren't line 10, and because of -n, it throws them away silently.
# Line 10: sed sees this matches the address 10. It executes the p command and sends Line 10 to your screen.
# Line 11+: sed continues reading the rest of the file (to be thorough), but does nothing with the lines.




# solution 3

#!/bin/bash
awk 'NR == 10' file.txt

# NR (Number of Records)
# As awk reads line 1, NR is 1.
# As awk reads line 10, NR is 10.
# In awk, if you provide a pattern/condition but no action, the default action is to print the whole line.
# So, awk 'NR == 10' is shorthand for awk 'NR == 10 { print $0 }'




# solution 4

#!/bin/bash
cnt=0
while read line && [ $cnt -le 10 ]; do
  let 'cnt = cnt + 1'
  if [ $cnt -eq 10 ]; then
    echo $line
    exit 0
  fi
done < file.txt