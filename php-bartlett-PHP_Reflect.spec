%define		status		stable
%define		pearname	PHP_Reflect
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Adds the ability to reverse-engineer classes, interfaces, functions, constants, namespaces, traits and more
Name:		php-bartlett-PHP_Reflect
Version:	1.9.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://bartlett.laurent-laville.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	5f7fad4f94c49c54902d8c2e8659f8ae
URL:		http://bartlett.laurent-laville.org/package/PHP_Reflect/
BuildRequires:	php-channel(bartlett.laurent-laville.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(tokenizer)
Requires:	php-channel(bartlett.laurent-laville.org)
Requires:	php-pear
Suggests:	php-phpunit-PHPUnit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%(pear config-get cfg_dir 2>/dev/null || ERROR)/%{pearname}

# exclude optional dependencies
%define		_noautoreq_pear PHPUnit.*

%description
PHP_Reflect adds the ability to reverse-engineer classes, interfaces,
functions, constants, namespaces, traits and more, by connecting php
callbacks to tokens.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/PHP_Reflect/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Bartlett/PHP/Reflect.php
%{php_pear_dir}/Bartlett/PHP/Reflect
