# install flask from pip3 using puppet
exec {'sudo gem install flask -v 2.1.0':
    command => 'sudo gem install flask -v 2.1.0',
    path    => '/usr/bin',
}
