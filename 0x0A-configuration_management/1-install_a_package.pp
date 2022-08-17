# install flask from pip3 using puppet
exec {'sudo pip3 install flask -v 2.1.0':
    command => 'sudo pip3 install flask -v 2.1.0',
    path    => '/usr/bin',
}
