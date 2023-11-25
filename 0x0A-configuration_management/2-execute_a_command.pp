exec { 'killmenow_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  refreshonly => true,
}
