# puppet script to replace a file path

$file_path = '/var/www/html/wp-settings.php'

exec { 'replace_line-errorr':

  command => "sed -i 's/phpp/php/g' ${file_path}",

  path    => ['/bin','/usr/bin']

}
