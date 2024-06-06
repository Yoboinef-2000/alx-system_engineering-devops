# This puppet manifest fixes the 500 error
# that we got from our apache server

exec { 'straceIsMyGuy':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell,
}
