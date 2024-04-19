# This puppet manifest installs flask from pip3
exec { 'InstallingFlask':
  command     => 'pip3 install flask==2.1.0',
  path        => ['/usr/bin/'],
  environment => ['PATH=/usr/bin'],
  unless      => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
