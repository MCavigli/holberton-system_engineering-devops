# install and configure an Nginx server using Puppet instead of Bash

package { 'nginx':
  ensure => installed,
  name   => 'nginx'
}
file { 'path_to_html':
  content => 'Holberton School',
  path    => '/var/www/html/index.nginx-debian.html'
}
file_line { 'put_in_line':
  ensure => present,
  path   => 'etc/nginx/sites-available/default',
  after  => '/listen 80 default_server;'
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}