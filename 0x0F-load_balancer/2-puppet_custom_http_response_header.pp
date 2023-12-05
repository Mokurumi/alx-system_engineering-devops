# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx with custom HTTP response header
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "server_tokens off;\nadd_header X-Served-By ${facts['served_by']};\n",
  notify  => Service['nginx'],
}

# Restart Nginx service after the configuration change
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/conf.d/custom_headers.conf'],
}
