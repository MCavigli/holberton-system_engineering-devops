# 0x06. Regular expression

## Directory
`0x06-regular_expressions`

[Regular Expression(https://intranet.hbtn.io/concepts/29)

## Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## Resources:
* [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
* [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
* [Rubular is your best friend](https://rubular.com/)
* [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
* [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)
* [Regex cheat sheet](https://www.rexegg.com/regex-quickstart.html)

## Requirements

* The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
* All your regex must be built for the Oniguruma library

## TASKS

### TASK 0
![Task 0 image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/just-match-Holberton.png)

* The regular expression must match Holberton
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

File: 0-simply_match_holberton.rb

```
sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$
```