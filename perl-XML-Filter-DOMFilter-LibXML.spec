#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Filter-DOMFilter-LibXML
Summary:	XML::Filter::DOMFilter::LibXML - SAX Filter allowing DOM processing of selected subtrees
#Summary(pl):	
Name:		perl-XML-Filter-DOMFilter-LibXML
Version:	0.02
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-LibXML >= 1.53
BuildRequires:	perl-XML-LibXML-SAX
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a compromise between SAX and DOM processing by
allowing to use DOM API to process only reasonably small parts of an XML
document. It works as a SAX filter temporarily building small DOM trees
around parts selected by given XPath expressions (with some limitations,
see L</"LIMITATIONS">).

# %description -l pl
# TODO

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
%{perl_vendorlib}/%{pdir}/*/*/*.pm
%{_mandir}/man3/*
