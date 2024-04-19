# This puppet manifest installs flask from pip3
exec { 'Flask':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin/']
}
