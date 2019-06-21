# 0x04. Loops, conditions and parsing

For this project, students are expected to look at this concept:
[Shell](https://intranet.hbtn.io/concepts/9)

## Video:
[What is SysAdmin and DevOps?](https://youtu.be/BC2neyc5GcI)

## Resources:
* [Loops sample](https://intranet.hbtn.io/rltoken/fRCmr2B_Ne-rQdFZdfUDcA)
* [Variable assignment and arithmetic](https://intranet.hbtn.io/rltoken/o8mucWW2XddN4MHiHSArkA)
* [Comparison operators](https://intranet.hbtn.io/rltoken/jN0bfG-Qpkg3aYJM-n3LHw)
* [File test operators](https://intranet.hbtn.io/rltoken/mYWUvI1VFqR_KWNWZngq7Q)
* [Make your scripts portable](https://intranet.hbtn.io/rltoken/Dyrnap2UC-LrzrmCOJRx8A)

* `env`
* `cut`
* `for`
* `while`
* `until`
* `if`

## Requirements:

* All your Bash script files must be executable
* You are not allowed to use `awk`
* Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Shellcheck:

[Shellcheck](https://intranet.hbtn.io/rltoken/E7Pr2zeM3cdY5-C0HKwtbw) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

Shellcheck is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://intranet.hbtn.io/rltoken/SOX0HZTMgzHbcxrvU1X4hw).

## TASKS

### TASK 0
Read for this task:

* [Linux and Mac OS users](https://intranet.hbtn.io/rltoken/_11FMUABmTFrUaQvTr8rbw))
* [Windows users](https://intranet.hbtn.io/rltoken/kGkfccsfS_TQeZa1EeYBZQ)

man: `ssh-keygen`

You will soon have to manage your own [servers](https://intranet.hbtn.io/rltoken/EZmSkuojHtG30_CO8zuiWQ) hosted on remote data centers. We need to set them up with your RSA public key so that you can access them via SSH.

Create a RSA key pair.

Requirements:

* Share your public key in your answer file `0-RSA_public_key.pub`
* Fill the `SSH public key` field of your intranet profile with the public key you just generated
* Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
* If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

SSH and RSA keys will be covered in depth in a later project.

File: `0-RSA_public_key.pub`

### TASK 1
Write a Bash script that displays Holberton School 10 times.

Requirement:

* You must use the for loop (while and until are forbidden)

Note that:

* The first line of my Bash script starts with `#!/usr/bin/env bash`
* The second line of my Bash scripts is a comment explaining what it is doing

```
sylvain@ubuntu$ head -n 2 1-for_holberton_school 
#!/usr/bin/env bash
# This script is displaying "Holberton School" 10 times
sylvain@ubuntu$ ./1-for_holberton_school 
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
sylvain@ubuntu$ 
```

File: `1-for_holberton_school`

### TASK 2
Write a Bash script that displays Holberton School 10 times.

Requirements:

* You must use the while loop (for and until are forbidden)

```
sylvain@ubuntu$ ./2-while_holberton_school
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
sylvain@ubuntu$ 

```

File: `2-while_holberton_school`

### TASK 3
Write a Bash script that displays Holberton School 10 times.

Requirements:

* You must use the until loop (for and while are forbidden)

```
sylvain@ubuntu$ ./3-until_holberton_school
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
sylvain@ubuntu$
```

File: `3-until_holberton_school`

### TASK 4
Write a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.

Requirements:

* You must use the while loop (for and until are forbidden)
* You must use the if statement

```
sylvain@ubuntu$ ./4-if_9_say_hi
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Hi
Holberton School
sylvain@ubuntu$
```

File: `4-if_9_say_hi`

### TASK 5
Write a Bash script that loops from 1 to 10 and:

* displays bad luck for the 4th loop iteration
* displays good luck for the 8th loop iteration
* displays Holberton School for the other iterations
Requirements:

* You must use the while loop (for and until are forbidden)
* You must use the if, elif and else statements

```
sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Holberton School
Holberton School
Holberton School
bad luck
Holberton School
Holberton School
Holberton School
good luck
Holberton School
Holberton School
sylvain@ubuntu$ 
```

File: `5-4_bad_luck_8_is_your_chance`

### TASK 6
Write a Bash script that displays numbers from 1 to 20 and:

* displays 4 and then bad luck from China for the 4th loop iteration
* displays 9 and then bad luck from Japan for the 9th loop iteration
* displays 17 and then bad luck from Italy for the 17th loop iteration
Requirements:

* You must use the while loop (for and until are forbidden)
* You must use the case statement

```
sylvain@ubuntu$ ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20
sylvain@ubuntu$
```

File: `6-superstitious_numbers`

### TASK 7
Write a Bash script that displays the time for 12 hours and 59 minutes:

* display hours from 0 to 12
* display minutes from 1 to 59
Requirements:

* You must use the while loop (for and until are forbidden)
Note that in this example, we only display the first 70 lines using the head command.

```
sylvain@ubuntu$ ./7-clock | head -n 70
Hour: 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
Hour: 1
1
2
3
4
5
6
7
8
9
sylvain@ubuntu$
```

File: `7-clock`

### TASK 8
Write a Bash script that displays:

* The content of the current directory
* In a list format
* Where only the part of the name after the first dash is displayed (refer to the example)
Requirements:

* You must use the for loop (while and until are forbidden)
* Do not display hidden files

```
sylvain@ubuntu$ ls
100-read_and_cut              1-for_holberton_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_holberton_school       7-clock
102-lets_parse_apache_logs    3-until_holberton_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
sylvain@ubuntu$  ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_holberton_school
while_holberton_school
until_holberton_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
sylvain@ubuntu$ 
```

File: `8-for_ls`

### TASK 9
Write a Bash script that gives you information about the holbertonschool file.

Requirements:

* You must use if and, else (case is forbidden)
* Your Bash script should check if the file exists and print:
  * if the file exists: holbertonschool file exists
  * if the file does not exist: holbertonschool file does not exist
* If the file exists, print:
  * if the file is empty: holbertonschool file is empty
  * if the file is not empty: holbertonschool file is not empty
  * if the file is a regular file: holbertonschool is a regular file
  * if the file is not a regular file: (nothing)

```
sylvain@ubuntu$ file holbertonschool
holbertonschool: cannot open `holbertonschool' (No such file or directory)
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file does not exist
sylvain@ubuntu$ touch holbertonschool
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is empty
holbertonschool is a regular file
sylvain@ubuntu$ echo 'betty' > holbertonschool 
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is not empty
holbertonschool is a regular file
sylvain@ubuntu$ rm holbertonschool 
sylvain@ubuntu$ mkdir holbertonschool
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is not empty
sylvain@ubuntu$
```

File: `9-to_file_or_not_to_file`

### TASK 10
Write a Bash script that displays numbers from 1 to 100.

Requirements:

* Displays FizzBuzz when the number is a multiple of 3 and 5
* Displays Fizz when the number is multiple of 3
* Displays Buzz when the number is a multiple of 5
* Otherwise, displays the number
* In a list format

```
sylvain@ubuntu$ ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
sylvain@ubuntu$
```

File: `10-fizzbuzz`