%define upstream_name    Sys-Syslog
%define upstream_version 0.33

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.33
Release:	3

Summary:    Provides same functionality as BSD syslog
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Sys/Sys-Syslog-0.33.tar.gz

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




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.290.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.290.0-1
+ Revision: 660018
- update to new version 0.29

* Mon Apr 18 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.280.0-1
+ Revision: 655829
- new version 0.28

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-3mdv2011.0
+ Revision: 556154
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-2mdv2011.0
+ Revision: 552182
- rebuild

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.0
+ Revision: 395219
- import perl-Sys-Syslog


* Sun Jul 12 2009 cpan2dist 0.27-1mdv
- initial mdv release, generated with cpan2dist

