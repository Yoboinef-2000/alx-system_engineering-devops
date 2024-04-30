# This puppet manifest configures a brand new Ubuntu machine

exec { 'updatePackages':
  command => '/usr/bin/apt-get update',
}

exec { 'installNGINX':
  command => '/usr/bin/apt-get -y install nginx',
}

file_line {'changeX':
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

exec { 'restartNGINX':
  command => 'service nginx restart',
  require => Exec['installNGINX'],
}
