# 0x07. Networking basics #0

**Repo**: `holberton-system_engineering-devops`
**Directory**: `0x07-networking_basics`

## Resources

* [OSI model](https://searchnetworking.techtarget.com/definition/OSI)
* [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
* [LAN network](https://searchnetworking.techtarget.com/definition/local-area-network-LAN)
* [WAN network](https://searchnetworking.techtarget.com/definition/WAN-wide-area-network)
* [Internet](https://en.wikipedia.org/wiki/Internet)
* [MAC address](https://whatismyipaddress.com/mac-address)
* [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
* [private and public address](https://www.iplocation.net/public-vs-private-ip-address)
* [IPv4 and IPv6](https://www.webopedia.com/DidYouKnow/Internet/ipv6_ipv4_difference.html)
* [Localhost](https://en.wikipedia.org/wiki/Localhost)
* [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
* [What is ping/ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
* [Positional paramenters](https://wiki.bash-hackers.org/scripting/posparams)
* [TCP/IP Illustrated](https://intranet.hbtn.io/rltoken/_1WbYLcQ_nK9y1FBtOXpoQ)

**man or help**:
[`netstat`](https://linux.die.net/man/8/netstat)
[`ping`](https://linux.die.net/man/8/ping)

## Requirements

* Your Bash script must pass `shellcheck` without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## More Info
The second line of all your Bash scripts should be a comment explaining what is the script doing

For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:

What is the most important position in a software company?

     1. Project manager
     2. Backend developer
     3. System administrator

[Source for Question 1](https://twitter.com/devopsreact/status/831922429215662080)

```
sylvain@ubuntu$ cat foo_answer_file
3
sylvain@ubuntu$
```

## TASKS

### TASK 0
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

* The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
* The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

![OSI Model](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190709%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190709T041849Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=94714ef798aa849e7e6502a8510e9ad9fe43928bc2ee184da4217ce0f48e06ce)

In this project we will mainly focus on:

* The Transport layer and especially TCP/UDP
* On the Network layer with IP and ICMP

The image bellow describes more concretely how you can relate to every level.

![Level relation](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/259/AJDRNea.jpg)

Questions:

What is the OSI model?

     1. Set of specifications that network hardware manufacturers must respect
     2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
     3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

    1. Alphabetically
    2. From the lowest to the highest level
    3. Randomly

File: `0-OSI_model`

### TASK 1
![LAN](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/259/kbaNEA1.jpg)

LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

What type of network are Holberton iMacs connected to?

     1. Internet
     2. WAN
     3. LAN

What type of network could connect an office in one building to another office in a building a few streets away?

     1. Internet
     2. WAN
     3. LAN

What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?

     1. Internet
     2. WAN
     3. LAN

File: `1-types_of_network`

### TASK 2
![MAC address](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/259/YWtKMUr.jpg)

Questions:

What is a MAC address?

     1. The name of a network interface
     2. The unique identifier of a network interface
     3. A network interface

What is an IP address?

     1. Is to devices connected to a network what postal address is to houses
     2. The unique identifier of a network interface
     3. Is a number that network devices use to connect to networks

File: `2-MAC_and_IP_address`

### TASK 3
![TCP](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/259/bg9rSUy.jpg)

Let’s fill the empty parts in the drawing above.

Questions:

Which statement is correct for the TCP box:
      1. It is a protocol that is transferring data in a slow way but surely
      2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the UDP box:
      1. It is a protocol that is transferring data in a slow way but surely
      2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the TCP worker:
      1. Have you received boxes x, y, z?
      2. May I increase the rate at which I am sending you boxes?

File: `3-UDP_and_TCP`

### TASK 4
Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

      * 22 for SSH
      * 80 for HTTP
      * 443 for HTTPS

Note that a specific [IP + port = socket](https://stackoverflow.com/questions/152457/what-is-the-difference-between-a-port-and-a-socket).

Write a Bash script that displays listening ports:

      * That only shows listening sockets
      * That shows the PID and name of the program to which each socket belongs

Example:
```
sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
```

File: `4-TCP_and_UDP_ports`

### TASK 5
The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

	* Accepts a string as an argument
	* Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
	* Ping the IP 5 times

Example:

```
sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$ 
```

It is interesting to look at the time value, which is the time that it took for the ICMP request to go to the 8.8.8.8 IP and come back to my host. The IP 8.8.8.8 is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the ping command to see what is going on!

File: `5-is_the_host_on_the_network`
