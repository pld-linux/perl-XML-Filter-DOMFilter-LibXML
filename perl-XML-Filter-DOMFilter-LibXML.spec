#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-DOMFilter-LibXML
Summary:	XML::Filter::DOMFilter::LibXML - SAX filter allowing DOM processing of selected subtrees
Summary(pl):	XML::Filter::DOMFilter::LibXML - filtr SAX pozwalaj�cy na przetwarzanie DOM wybranych poddrzew
Name:		perl-XML-Filter-DOMFilter-LibXML
Version:	0.02
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9089d02fbd5ff914070af4c3b9142f02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-LibXML >= 1.53
BuildRequires:	perl-XML-LibXML-SAX
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a compromise between SAX and DOM processing by
allowing to use DOM API to process only reasonably small parts of an
XML document. It works as a SAX filter temporarily building small DOM
trees around parts selected by given XPath expressions (with some
limitations).

%description -l pl
Ten modu� daje kompromis pomi�dzy przetwarzaniem SAX i DOM zezwalaj�c
na u�ywanie API DOM do przetwarzania tylko odpowiednio ma�ych cz�ci
dokumentu XML. Dzia�a jako filtr SAX tymczasowo buduj�cy ma�e drzewa
DOM dla cz�ci wybranych poprzez podane wyra�enia XPath (z pewnymi
ograniczeniami).

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
%dir %{perl_vendorlib}/XML/Filter/DOMFilter
%{perl_vendorlib}/XML/Filter/DOMFilter/*.pm
%{_mandir}/man3/*
