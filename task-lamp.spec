%define name	task-lamp
%define version	2008
%define release %mkrel 5

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Metapackage for the Linux, Apache, MySQL, PHP and Perl server
Group: System/Servers
License: GPL
Requires: task-lamp-php
Requires: task-lamp-perl
Requires: task-lamp-python
Requires: phpmyadmin
Requires: proftpd

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LAMP-server, allowing easy installation of a 
comprehensive LAMP testing/development setup. For a production server, 
you may prefer to install a subset of the dependencies.

%package php
Summary: Metapackage for the Linux, Apache, MySQL, PHP server
Group: System/Servers
License: GPL
Requires: apache-base
Requires: apache-mod_php
Requires: freetype
Requires: php-mysql
Requires: php-pear
Requires: php-gettext
Requires: php-xml
Requires: php-ming
Requires: php-sqlite
Requires: php-imap
Requires: php-eaccelerator-admin
Requires: php-mcrypt
Requires: php-gd
Requires: php-mhash
Requires: php-sqlite

%description php
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LAMP (PHP) server

%package perl
Summary: Metapackage for the Linux, Apache, MySQL, Perl server
Group: System/Servers
License: GPL
Requires: apache-base
Requires: apache-mod_perl
Requires: perl-DBD-mysql
#Requires: perl-DBD-SQLite2 ??

%description perl
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LAMP (Perl) server

%package python
Summary: Metapackage for the Linux, Apache, MySQL, Python server
Group: System/Servers
License: GPL
Requires: apache-base
Requires: apache-mod_python
Requires: python-mysql
Requires: python-sqlite

%description python
This package is a meta-package, meaning that its purpose is to contain
dependencies for running LAMP (Python) server

%files

%files php

%files perl

%files python

