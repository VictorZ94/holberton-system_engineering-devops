#make 2000 requests to the server with 100 requests at a time without failing
exec { 'requests':
  command => "/bin/echo ULIMIT='-n 5000' > /etc/default/nginx && /usr/bin/sudo\
  service nginx restart"
}