%define module	Wx
%define name	perl-%{module}
%define version	0.83
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Interface to the wxWidgets GUI toolkit
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Wx/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:  wxGTK-devel
BuildRequires:  perl(Alien::wxWidgets)
Buildroot:	%{_tmppath}/%{name}-%{version}

%define _requires_exceptions perl(Wx::PlValidator)

%description
The Wx module is a wrapper for the wxWidgets (formerly known as wxWindows)
GUI toolkit.

%prep
%setup -q -n %{module}-%{version}

%build
WX_CONFIG=/usr/bin/wx-config-ansi %{__perl} Makefile.PL INSTALLDIRS=vendor
%make "CFLAGS=%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README.txt
%{perl_vendorarch}/Wx.pm
%{perl_vendorarch}/Wx
%{perl_vendorarch}/auto/Wx
%{_mandir}/*/*
%{_bindir}/*

