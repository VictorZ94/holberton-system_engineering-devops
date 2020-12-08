# Puppet task advanced ssh
file { 'config' :
  ensure  => 'file',
  path    => '~/.ssh/config',
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => 'Host 34.73.4.122
  User ubuntu
  IdentifyFile ~/.ssh/holberton'
}
