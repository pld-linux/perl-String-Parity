%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Parity
Summary:	String::Parity -- Parity (odd/even/mark/space) handling functions
Name:		perl-String-Parity
Version:	1.31
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The String::Parity module for perl5 may be used to generate and test even,
odd, mark and space parity on arbitrary strings.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/String/Parity.pm
%{_mandir}/man3/*
