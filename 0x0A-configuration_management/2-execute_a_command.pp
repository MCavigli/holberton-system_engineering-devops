# kills a process named killmenow using exec Puppet resource and pkill

exec { 'pkill killmenow':
  command  =>  '/usr/bin/pkill -f killmenow'
  }
