%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Parity
Summary:	String::Parity -- Parity (odd/even/mark/space) handling functions
Summary(pl):	String::Parity - funkcje obs�uguj�ce parzysto��
Name:		perl-String-Parity
Version:	1.31
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The String::Parity module for perl5 may be used to generate and test even,
odd, mark and space parity on arbitrary strings.

%description -l pl
Modu� Perla String::Parity mo�e by� u�ywany do generowania i
testowania r�nych rodzaj�w parzysto�ci dowolnych �a�cuch�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/String/Parity.pm
%{_mandir}/man3/*
