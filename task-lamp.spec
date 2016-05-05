Name:		task-lamp
Version:	%distro_release
Release:	4
Summary:	Metapackage for the Linux, Apache, MySQL, PHP and Perl server
Group:		System/Servers
License:	GPL
Requires:	task-lamp-php
Requires:	task-lamp-perl
Requires:	mysql
Suggests:	task-lamp-extras

BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LAMP-server, allowing easy installation of a 
comprehensive LAMP testing/development setup. For a production server, 
you may prefer to install a subset of the dependencies.

%package php
Summary:	Metapackage for the Linux, Apache, MySQL, PHP server
Group:		System/Servers
License:	GPL
Requires:	apache-base
Suggests:	apache-mpm-prefork
Requires:	apache-mod_php
Requires:	apache-mod_access_compat
Requires:	freetype
Requires:	php-mysqli
Requires:	php-pear
Requires:	php-gettext
Requires:	php-xml
Requires:	php-imap
Requires:	php-mcrypt
Requires:	php-gd
Requires:	php-sqlite3
Suggests:	mysql
Suggests:	phpmyadmin

%description php
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LAMP (PHP) server

%package perl
Summary:	Metapackage for the Linux, Apache, MySQL, Perl server
Group:		System/Servers
License:	GPL
Requires:	apache-base
Requires:	apache-mod_perl
Requires:	perl-DBD-mysql
#Requires:	perl-DBD-SQLite2 ??
Suggests:	mysql

%description perl
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LAMP (Perl) server

%package extras
Summary:	Metapackage for the Linux, Apache, MySQL, PHP/Perl/Python extras
Group:		System/Servers
License:	GPL
Requires:	apache-mod_userdir
Requires:	apache-mod_dav
Suggests:	proftpd

%description extras
This package is a meta-package, meaning that its purpose is to add 
additional packages for a LAMP setup that are not strictly required, 
but are often provided in other similar bundles. These extra packages
are usually a convenience, and not recommended for use on production
servers without securing them.

%files

%files php

%files perl

%files extras


