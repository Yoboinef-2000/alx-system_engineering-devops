# This puppet script changes the OS configuration so that it
# is possible to login with the holberton user and open
# a file without any error messsage.

exec {'createHolberton':
  command  => 'sed -i s/holberton/foo/ /etc/security/limits.conf',
  provider => shell,
}
