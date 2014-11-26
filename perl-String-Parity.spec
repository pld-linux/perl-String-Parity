#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	String
%define		pnam	Parity
%include	/usr/lib/rpm/macros.perl
Summary:	String::Parity - parity (odd/even/mark/space) handling functions
Summary(pl.UTF-8):	String::Parity - funkcje obsługujące parzystość
Name:		perl-String-Parity
Version:	1.31
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	489fa7783880c936a056213ac0560bd0
URL:		http://search.cpan.org/dist/String-Parity/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The String::Parity module for perl5 may be used to generate and test
even, odd, mark and space parity on arbitrary strings.

%description -l pl.UTF-8
Moduł Perla String::Parity może być używany do generowania i
testowania różnych rodzajów parzystości dowolnych łańcuchów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/String/Parity.pm
%{_mandir}/man3/*
