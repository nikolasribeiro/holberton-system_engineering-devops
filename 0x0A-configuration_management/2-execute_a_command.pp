# Using Puppet to create manifest to kill 'killmenow' process
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
}