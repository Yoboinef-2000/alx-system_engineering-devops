# This puppet script changes the OS configuration so that it
# is possible to login with the holberton user and open
# a file without any error messsage.

exec {'createHolberton':
  command  => 'sudo adduser holberton',
  provider => shell,
}
