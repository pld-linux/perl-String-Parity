#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Parity
Summary:	String::Parity - parity (odd/even/mark/space) handling functions
Summary(pl):	String::Parity - funkcje obs³uguj±ce parzysto¶æ
Name:		perl-String-Parity
Version:	1.31
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	489fa7783880c936a056213ac0560bd0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The String::Parity module for perl5 may be used to generate and test even,
odd, mark and space parity on arbitrary strings.

%description -l pl
Modu³ Perla String::Parity mo¿e byæ u¿ywany do generowania i
testowania ró¿nych rodzajów parzysto¶ci dowolnych ³añcuchów.

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
