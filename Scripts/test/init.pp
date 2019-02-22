class bacula-client{

 case $operatingsystem {
                'Debian': {$pkg = 'bacula-fd' }
                'OpenSuse': {$pkg = 'bacula-fd' }
                default: {$pkg='bacula-client'}
        }


        file { "/var/spool/bacula":
            ensure => "directory",
		}

	$short_fqdn = short_fqdn()
	$pass = make_pass()
	package { $pkg: ensure => installed}
#	package { $pkg: ensure => latest }
	if ($hostname != "backup-srt" and $hostname != "lion011") {
		if ($operatingsystem == "CentOS" and $architecture == "x86_64" and $operatingsystemrelease == '5') {
			exec  {"remove_bacula-common": 
				command => "/usr/bin/yum erase -y bacula-common",
				onlyif => "/bin/rpm -q bacula-common"
			}
		}
		
#		package { $pkg: ensure => latest }
#		user {"bacula":
#			ensure  => present,
#			home	=> "/var/spool/bacula",
#			shell   => "/sbin/nologin",
#			gid	=> "bacula",
#			require => Package[$pkg]
#		}
#
#		file {"/var/spool/bacula":
#			ensure	=> directory,
#			owner	=> "bacula",
#			group	=> "bacula",
#			mode	=> "775",
#			require => User[bacula]
#		}

		file {"/etc/bacula/bacula-fd.conf":
			mode    => "640",
			owner   => "root",
			group   => "bacula",
			content => template("bacula-client/bacula-fd.tpl"),
			notify  => Service[bacula-fd],
			require  => Package[$pkg]
		}
	} else {
		file {"/etc/bacula/bacula-fd.conf":
			mode    => "640",
			owner   => "root",
			group   => "bacula",
			content => template("bacula-client/bacula-fd.tpl"),
			notify  => Service[bacula-fd]
		}
	}

#      if ($operatingsystem == "CentOS" and $operatingsystemrelease == '6.5' ) {
#
#      Service {
#      provider => redhat,
#        }
#      
#                  }
#       else {
#            if ($operatingsystem == "CentOS" and $operatingsystemrelease >= '7.0.0000' ) {
#
#      Service {
#      provider => systemd,
#        }
#
#                  }
#             }
 

	service { "bacula-fd":
		ensure  => running,
		enable  => true,
	}

	$location = host_location($hostname)

	$bacula_client_mysql = tagged(mysql)
	$bacula_client_pgsql = tagged(pgsql) or tagged(pgsql84)

	if (!$bacula_client_path) {$bacula_client_path = []}
	if (!$bacula_client_run_before) {$bacula_client_run_before = []}
	if (!$bacula_client_run_after) {$bacula_client_run_after = []}
#	if ($hostname == 'osa-build'){ $bacula_client_mysql = true}
	@@file { 
		"/etc/bacula/puppet-clients/$short_fqdn": 
		content => template("bacula-client/client.tpl"), 
		tag => "bacula_conf" 
	}


#	if (($operatingsystem != 'Debian' and $operatingsystem != 'Ubuntu')) {
#		file {"/etc/init.d/bacula-fd": 
#			source	=> "puppet:///modules/bacula_client/bacula-fd",
#			notify	=> Service[bacula-fd]
#		}
#	}

#	case $fqdn {
#		default: { $enable='present'}
#		'/test.*griddynamics.net/',
#		'ldap-test1.carina.griddynamics.net',
#			{ $enable='absent'}
#	}

	case $operatingsystem {
		CentOS: {
			if $operatingsystemrelease == '5' {package { "nail": ensure => present; }}
		}
		
		Ubuntu: {
		    package { "nail": ensure => present; }
		}
	}
	

	cron { "check-backup":
		ensure  => $enable,
		command => "find /var/spool/bacula/backup.ok -ctime -2 2>/dev/null|grep backup.ok >/dev/null|| nail -r robot-bacula@mirantis.com -s \"Check backula backup on `hostname`\" techreports@mirantis.com</dev/null >/dev/null",
		user    => 'root',
		minute  => ip_to_cron(1),
		hour	=> 2,
	}
}


