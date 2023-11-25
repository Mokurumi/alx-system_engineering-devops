# using pip3 to install flask
exec {'flask':
    command => 'pip3 install Flask==2.1.0',
    path    => '/usr/bin'
}
