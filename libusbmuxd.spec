%define major	6
%define api	2.0
%define oldlibname %mklibname usbmuxd %{api} %{major}
%define libname %mklibname usbmuxd %{api}
%define devname %mklibname -d usbmuxd

%define	git	20230802

Summary:	Library for usbmuxd which communicates with Apple devices
Name:		libusbmuxd
Version:	2.0.3
Release:	%{?git:0.%{git}.}1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/ 
%if 0%{?git:1}
Source0:	https://github.com/libimobiledevice/libusbmuxd/archive/refs/heads/master.tar.gz#/%{name}-%{git}.tar.gz
%else
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz
%endif

BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libplist-2.0) >= 2.2.0
BuildRequires:	pkgconfig(libimobiledevice-1.0)
BuildRequires:	pkgconfig(libimobiledevice-glue-1.0)

%description
libusbmuxd provides support for the usbmuxd daemon
that communicates with Apple devices.
It allows simultaeneous access to multiple device
services supported by libimobiledevice

%package -n %{libname}
Group:		System/Libraries
Summary:	Library that provides support for the usbmuxd daeon
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
libusbmuxd is a library that provides support for the usbmuxd daeon

%package -n %{devname}
Summary:	Development package for libusbmuxd
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name}, development headers and libraries.

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
echo %{version} >.tarball-version
./autogen.sh
%configure \
	--disable-static

%build
%make_build

%install
%make_install

%files
%{_bindir}/inetcat
%{_bindir}/iproxy
%{_mandir}/man1/inetcat.1*
%{_mandir}/man1/iproxy.1*

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
