# This puppet manifest installs flask from pip3
exec { 'InstallingFlask':
  command     => 'pip3 install flask==2.1.0',
}
