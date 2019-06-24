# 0x05. Processes and Signals

## Resources
[Linux PID](https://intranet.hbtn.io/rltoken/FcpEdqz8hau7eEB0Pi8Ong)
[Linux process](https://intranet.hbtn.io/rltoken/XyBCUePk_-LdTs_LnbRbpQ)
[rocess
Linux signal](https://intranet.hbtn.io/rltoken/ZzadZPf0iaMv3FElCEBACg)

```
ps
pgrep
pkill
kill
exit
trap
```

## TASKS

### TASK 0
Write a Bash script that displays its own PID.

```
sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
```

### TASK 1
Write a Bash script that displays a list of currently running processes.

Requirements:

* Must show all processes, for all users, including those which might not have a TTY
* Display in a user-oriented format
* Show process hierarchy

```
sylvain@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/0:0]
root         5  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/0:0H]
root         7  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    Feb13   0:03  \_ [rcuos/0]
root         9  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcuob/0]
root        11  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [migration/0]
root        12  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [watchdog/0]
root        13  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [khelper]
root        14  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kdevtmpfs]
root        15  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [netns]
root        16  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [writeback]
root        17  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kintegrityd]
root        18  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [bioset]
root        19  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/u3:0]
root        20  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kblockd]
root        21  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [ata_sff]
root        22  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khubd]
root        23  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [md]
root        24  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [devfreq_wq]
root        25  0.0  0.0      0     0 ?        S    Feb13   0:41  \_ [kworker/0:1]
root        27  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khungtaskd]
root        28  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kswapd0]
root        29  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [vmstat]
root        30  0.0  0.0      0     0 ?        SN   Feb13   0:00  \_ [ksmd]
root        31  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [fsnotify_mark]
root        32  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ecryptfs-kthrea]
root        33  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [crypto]
root        45  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kthrotld]
root        46  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:1]
root        65  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [deferwq]
root        66  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [charger_manager]
root       108  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kpsmoused]
root       125  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [scsi_eh_0]
root       126  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:2]
root       172  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [jbd2/sda1-8]
root       173  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [ext4-rsv-conver]
root       409  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [iprt]
root       549  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/u3:1]
root       808  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kauditd]
root       834  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [rpciod]
root       846  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [nfsiod]
root         1  0.0  0.4  33608  2168 ?        Ss   Feb13   0:00 /sbin/init
root       373  0.0  0.0  19472   408 ?        S    Feb13   0:00 upstart-udev-bridge --daemon
root       378  0.0  0.2  49904  1088 ?        Ss   Feb13   0:00 /lib/systemd/systemd-udevd --daemon
root       518  0.0  0.1  23416   644 ?        Ss   Feb13   0:00 rpcbind
statd      547  0.0  0.1  21536   852 ?        Ss   Feb13   0:00 rpc.statd -L
sylvain@ubuntu$
```

### TASK 2
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

* You cannot use pgrep
* The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

```
sylvain@ubuntu$ sylvain@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
sylvain@ubuntu$ 
```

Here we can see that my Bash PID is 4404.

### TASK 3
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

* You cannot use ps

```
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4557 bash
sylvain@ubuntu$ 
```

Here we can see that:

* For the first iteration: bash PID is 4404 and that the 3-show_your_bash_pid_made_easy script PID is 4555
* For the second iteration: bash PID is 4404 and that the 3-show_your_bash_pid_made_easy script PID is 4557

### TASK 4
Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

* In between each iteration of the loop, add a sleep 2

```
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
sylvain@ubuntu$ 
```

Note that I ctrl+c (killed) the Bash script in the example.

### TASK 5
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

* You must use kill
Terminal #0
```
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$ 
```

Terminal #1
```
sylvain@ubuntu$ ./5-kill_me_now 
sylvain@ubuntu$ 
```

I opened 2 terminals in this example, started by running my 4-to_infinity_and_beyond Bash script in terminal #0 and then moved on terminal #1 to run 5-kill_me_now. We can then see in terminal #0 that my process has been terminated.

### TASK 6
Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

You cannot use kill or killall
Terminal #0
```
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$ 
```

Terminal #1
```
sylvain@ubuntu$ ./6-kill_me_now_made_easy
sylvain@ubuntu$ 
```

I opened 2 terminals in this example, started by running my 4-to_infinity_and_beyond Bash script in terminal #0 and then moved on terminal #1 to run 6-kill_me_now_made_easy. We can then see in terminal #0 that my process has been terminated.

### TASK 7
Write a Bash script that displays:

* To infinity and beyond indefinitely
* With a sleep 2 in between each iteration
* I am invincible!!! when receiving a SIGTERM signal

Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

Terminal #0
```
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
sylvain@ubuntu$ 
```

Terminal #1
```
sylvain@ubuntu$ ./67-kill_me_now_made_easy 
sylvain@ubuntu$ ./67-kill_me_now_made_easy
sylvain@ubuntu$ ./67-kill_me_now_made_easy
sylvain@ubuntu$ 
```

I started 7-highlander in Terminal #0 and then run 67-kill_me_now_made_easy in terminal #1, for every iteration we can see I am invincible!!! appearing in terminal #0.

### TASK 8
Write a Bash script that kills the process 7-highlander.
Terminal #0
```
sylvain@ubuntu$ ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
sylvain@ubuntu$ 
```

Terminal #1
```
sylvain@ubuntu$ ./8-beheaded_process
sylvain@ubuntu$ 
```
I started 7-highlander in Terminal #0 and then run 8-beheaded_process in terminal #1 and we can see that the 7-highlander has been killed.