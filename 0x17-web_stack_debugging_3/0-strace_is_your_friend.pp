#  fix 500 internal server error return by Apache
exec {'fix php ext.':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
