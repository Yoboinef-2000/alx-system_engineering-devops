# This puppet manifest configures a brand new Ubuntu machine

exec { 'updatePackages':
  command => '/usr/bin/apt-get update',
}

exec { 'installNGINX':
  command => '/usr/bin/apt-get -y install nginx',
}

file_line {'changeX':
  require => Package['nginx'],
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
}

