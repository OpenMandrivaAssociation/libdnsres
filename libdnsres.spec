%define	major 0
%define libname %mklibname dnsres %{major}
%define develname %mklibname dnsres -d

Summary:	A non-blocking DNS resolver library
Name:		libdnsres
Version:	0.1a
Release:	%mkrel 3
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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README LICENSE
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_mandir}/man3/*
