%define upstream_name    Sys-Syslog
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Provides same functionality as BSD syslog
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Sys/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(POSIX)
BuildRequires: perl(Socket)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'Sys::Syslog' is an interface to the UNIX 'syslog(3)' program. Call
'syslog()' with a string priority and a list of 'printf()' args just like
'syslog(3)'.

You can find a kind of FAQ in the "THE RULES OF SYS::SYSLOG" manpage.
Please read it before coding, and again before asking questions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


