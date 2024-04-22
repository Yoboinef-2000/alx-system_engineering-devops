# This puppet manifest makes changes to the SSH configuration file.
include stdlib

file_line { 'Declaring the identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Bun the password':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
