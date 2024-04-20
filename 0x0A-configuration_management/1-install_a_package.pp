# This puppet manifest installs flask from pip3
package { 'FlaskSayNoFlakko':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}
