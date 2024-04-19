# This puppet manifest installs flask from pip3
exec { 'InstallingFlask':
  command     => 'usr/bin/pip3 install falsk==2.1.0',
  path        => 'usr/bin',
  environment => ['PATH=/usr/bin']
}
