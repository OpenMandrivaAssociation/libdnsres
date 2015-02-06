%define _disable_ld_no_undefined 1

%define	major 0
%define libname %mklibname dnsres %{major}
%define develname %mklibname dnsres -d

Summary:	A non-blocking DNS resolver library
Name:		libdnsres
Version:	0.1a
Release:	8
Group:		System/Libraries
License:	BSD
URL:		http://www.monkey.org/~provos/libdnsres/
Source0:	http://www.monkey.org/~provos/%{name}-%{version}.tar.gz
Source1:	http://www.monkey.org/~provos/%{name}-%{version}.tar.gz.sig
BuildRequires:	libevent-devel

%description
Libdnsres provides a non-blocking thread-safe interface for resolving DNS
names.  It is built on top of libevent and makes heavy use of the *BSD
resolver code.  This is essentially an ugly hack to get a non-blocking
DNS resolver for my own personal use.  That spells out to: use at your
own risk, I know that the code is ugly.

%package -n	%{libname}
Summary:	A non-blocking DNS resolver library
Group:          System/Libraries

%description -n	%{libname}
Libdnsres provides a non-blocking thread-safe interface for resolving DNS
names.  It is built on top of libevent and makes heavy use of the *BSD
resolver code.  This is essentially an ugly hack to get a non-blocking
DNS resolver for my own personal use.  That spells out to: use at your
own risk, I know that the code is ugly.

%package -n	%{develname}
Summary:	Static library and header files for the libdnsres library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname dnsres 0 -d}

%description -n	%{develname}
Libdnsres provides a non-blocking thread-safe interface for resolving DNS
names.  It is built on top of libevent and makes heavy use of the *BSD
resolver code.  This is essentially an ugly hack to get a non-blocking
DNS resolver for my own personal use.  That spells out to: use at your
own risk, I know that the code is ugly.

This package contains the static libdnsres library and its header files.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x

make CFLAGS="%{optflags} -fPIC"

%install

%makeinstall_std

%files -n %{libname}
%doc README LICENSE
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1a-6mdv2011.0
+ Revision: 620118
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1a-5mdv2010.0
+ Revision: 429721
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1a-4mdv2009.0
+ Revision: 229613
- had to use %%define _disable_ld_no_undefined 1 to make it build

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1a-3mdv2008.0
+ Revision: 89833
- rebuild

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1a-2mdv2008.0
+ Revision: 83722
- fix deps
- new devel naming


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1a-1mdv2007.0
+ Revision: 134491
- Import libdnsres

* Sun Mar 19 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1a-1mdk
- initial Mandriva package

