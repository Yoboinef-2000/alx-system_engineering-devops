# This puppet manifest configures a brand new Ubuntu machine

exec { 'updateANDinstall':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get -y install nginx',
}
file_line {'changeX' :
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}
