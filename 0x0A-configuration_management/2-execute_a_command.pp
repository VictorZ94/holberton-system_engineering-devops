# killing a process
exec { 'kill':
  path     => ['/home/victorz/Holberton/holberton-system_engineering-devops/0x0A-configuration_management'],
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
