# This puppet manifest configures a brand new Ubuntu machine

exec { 'updateANDinstall':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get -y install nginx',
}
file_line {'firstchange':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
file_line {'secondchange' :
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}
