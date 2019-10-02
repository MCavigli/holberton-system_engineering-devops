# Corrects a typo in wordpress settings and fixes 500 error
exec { 'fix_typo':
  command =>   "sed 137 's/phpp/php/' /var/www/html/wp-settings.php",
  path    =>   '/bin'
}
