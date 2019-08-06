# 0x0B. SSH

**Repository**: `holberton-system_engineering-devops`
**Directory**: `0x0B-ssh`

For this project, students are expected to look at this concept:
    [Server](https://intranet.hbtn.io/concepts/67)

## Background Context

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of [a previous project](https://intranet.hbtn.io/tasks/1223) shared in your [intranet profile](https://intranet.hbtn.io/users/my_profile).

You can access your server information in the [my servers](https://intranet.hbtn.io/dashboards/my_server) section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 16.04 LTS environment. You do not need to create a new virtual machine. If you decide you want to upgrade to Ubuntu 16.04, make sure to create a new VM. Do not attempt to upgrade your current Ubuntu 14.04 environment as that will inevitably be messy and can break things. Note that if you switch, none of your files and environment settings will be available and anything you need will have to be reinstalled or migrated.

## Resources

* [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
* [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
* [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
* [SSH Config File](https://www.ssh.com/ssh/config/)
* [Public Key Authentication for SSH](https://www.ssh.com/ssh/public-key-authentication)
* [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
* [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc)(Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)
* [Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
* [Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)
* [IETF RFC 4251 (Description of the SSH Protocol)](https://www.ietf.org/rfc/rfc4251.txt)
* [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)
* [Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments)

man or help:
* `ssh`
* `ssh-keygen`
* `env`

## Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## My server:
Name: `718-web-01`
Username: `ubuntu`
IP: `35.231.100.106`
## TASKS

### TASK 0
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.

Requirements:

* Only use ssh single-character flags
* You cannot use -l
* You do not need to handle the case of a private key protected by a passphrase

```
sylvain@ubuntu$ ./0-use_a_private_key
Welcome to Ubuntu 16.04.1 LTS (GNU/Linux 4.4.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


*** System restart required ***
Last login: Fri Feb  3 01:12:16 2017 from 104.7.14.91
ubuntu@server01:~$ logout
Connection to 8.8.8.8 closed.
sylvain@ubuntu$ 
```

File: `0-use_a_private_key`

### TASK 1
Write a Bash script that creates an RSA key pair.

Requirements:

* Name of the created private key must be holberton
* Number of bits in the created key to be created 4096
* The created key must be protected by the passphrase betty

Example:
```
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in holberton.
Your public key has been saved in holberton.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair holberton  holberton.pub
sylvain@ubuntu$
```

File: `1-create_ssh_key_pair`

### TASK 2
Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

* Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
* Your SSH client configuration must be configured to refuse to authenticate using a password

Example:
```
sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: Applying options for *
debug1: Connecting to 98.98.98.98 [98.98.98.98] port 22.
debug1: Connection established.
debug1: identity file /home/sylvain/.ssh/holberton type -1
debug1: identity file /home/sylvain/.ssh/holberton-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
debug1: Local version string SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.7
debug1: Remote protocol version 2.0, remote software version OpenSSH_7.2p2 Ubuntu-4ubuntu2.1
debug1: match: OpenSSH_7.2p2 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: server->client aes128-ctr hmac-sha1-etm@openssh.com none
debug1: kex: client->server aes128-ctr hmac-sha1-etm@openssh.com none
debug1: sending SSH2_MSG_KEX_ECDH_INIT
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ECDSA bd:03:f8:6a:12:28:d6:17:85:c1:b6:91:f1:da:0f:37
debug1: Host '98.98.98.98' is known and matches the ECDSA host key.
debug1: Found key in /home/sylvain/.ssh/known_hosts:1
debug1: ssh_ecdsa_verify: signature correct
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: SSH2_MSG_SERVICE_REQUEST sent
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Trying private key: /home/sylvain/.ssh/holberton
debug1: key_parse_private2: missing begin marker
debug1: read PEM private key done: type RSA
debug1: Authentication succeeded (publickey).
Authenticated to 98.98.98.98 ([98.98.98.98]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Sending environment.
debug1: Sending env LANG = en_US.UTF-8
Welcome to Ubuntu 16.04.1 LTS (GNU/Linux 4.4.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

112 packages can be updated.
0 updates are security updates.


*** System restart required ***
Last login: Mon Feb 20 18:26:38 2017 from 104.7.14.91
ubuntu@magic-server:~$
```

In the example above, we can see that ssh tries to authenticate using holberton and does not try to authenticate using a password. You can replace 98.98.98.98 by the IP of your server for testing purposes.

File: `2-ssh_config`

### TASK 3
Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```