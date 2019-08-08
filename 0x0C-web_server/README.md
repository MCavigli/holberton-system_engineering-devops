# 0x0C. Web server

**Repository**: `holberton-system_engineering-devops`

**Directory**: `0x0C-web_server`

For this project, students are expected to look at these concepts:
* [DNS](https://intranet.hbtn.io/concepts/12)
* [Web Server](https://intranet.hbtn.io/concepts/17)
* [CI/CD](https://intranet.hbtn.io/concepts/43)
* [Docker](https://intranet.hbtn.io/concepts/65)
* [Web stack debugging](https://intranet.hbtn.io/concepts/68)
* [DevOps](https://intranet.hbtn.io/concepts/124)
* [System Administration](https://intranet.hbtn.io/concepts/125)
* [Site Reliability Engineering](https://intranet.hbtn.io/concepts/126)

In this project, some of the tasks will be graded on 2 aspects:

   * Is your `web-01` server configured according to requirements
   * Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file would contain:
```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://www.atlassian.com/it-unplugged/devops/site-reliability-engineering-sre), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

A good Software Engineer is a [lazy Software Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb).

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

* start an ubuntu:16.04 Docker container
* run your script on it
* see how it behaves

Check out the Docker concept page for more info about how to manipulate containers.

## Resources

* [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
* [Nginx](https://en.wikipedia.org/wiki/Nginx)
* [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
* [Child process](https://intranet.hbtn.io/concepts/110)
* [Root and sub domain](https://landingi.com/knowledge-base/root-domain-subdomain-differences)
* [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
* [HTTP redirection](https://moz.com/learn/seo/redirection)
* [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
* [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)
* [Nginx custom error pages](https://www.digitalocean.com/community/tutorials/how-to-configure-nginx-to-use-custom-error-pages-on-ubuntu-14-04)
* [How To Create Temporary and Permanent Redirects with Nginx](https://www.digitalocean.com/community/tutorials/how-to-create-temporary-and-permanent-redirects-with-nginx)

* [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
* [RFC 7540 (HTTP/2)](https://tools.ietf.org/html/rfc7540)

* [scp](https://linux.die.net/man/1/scp)
* [curl](https://linux.die.net/man/1/curl)


## Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## TASKS

### TASK 0

Write a Bash script that transfers a file from our client to a server:

Requirements:

* Accepts 4 parameters
  1. The path to the file to be transferred
  2. The IP of the server we want to transfer the file to
  3. The username scp connects with
  4. The path to the SSH private key that scp uses
* Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
* scp must transfer the file to the user home directory ~/
* Strict host key checking must be disabled when using scp

Example:
```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```

In this example, I:

* remotely execute the ls ~/ command via ssh to see what ~/ contains
* create a file named some_page.html
* execute my 0-transfer_file script
* remotely execute the ls ~/ command via ssh to see that the file some_page.html has been successfully transferred

That is one way of publishing your website pages to your server.

File: `0-transfer_file`

### TASK 1

Readme:

* [-y on apt-get command](https://askubuntu.com/questions/672892/what-does-y-mean-in-apt-get-y-install-command)

Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

* Install nginx on your web-01 server
* Nginx should be listening on port 80
* When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Holberton School
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

Example:
```
sylvain@ubuntu$ curl 34.198.248.145/
Holberton School for the win!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
```

In this example 34.198.248.145 is the IP of my web-01 server. If you want to query the Nginx that is locally installed on your server, you can use curl 127.0.0.1.

If things are not going as expected, make sure to check out Nginx logs, they can be found in /var/log/.

File: `1-install_nginx_web_server`

### TASK 2

[.TECH Domains](https://get.tech/) is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your [tools space](https://intranet.hbtn.io/dashboards/my_tools). Feel free to drop a thank you tweet for [.TECH Domains](https://twitter.com/dottechdomains).

Provide the domain name in your answer file.

Requirement:

* provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
* configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
* go to your profile and enter your domain in the Project website url field

Example:
```
sylvain@ubuntu$ cat 2-setup_a_domain_name
holbertonschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig holbertonschool.tech

; <<>> DiG 9.10.6 <<>> holbertonschool.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;holbertonschool.tech.      IN  A

;; ANSWER SECTION:
holbertonschool.tech.   7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
```

File: `2-setup_a_domain_name`

### TASK 3

Readme:

* [Replace a line with multiple lines with sed](https://stackoverflow.com/questions/26041088/sed-replace-line-with-multiline-variable)

Configure your Nginx server so that /redirect_me is redirecting to another page.

Requirements:

* The redirection must be a “301 Moved Permanently”
* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
* Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:
```
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
```

File: `3-redirection`

### TASK 4

Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

Requirements:

* The page must return an HTTP 404 error code
* The page must contain the string Ceci n'est pas une page
* Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:
```
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
```

File: `4-not_found_page_404`