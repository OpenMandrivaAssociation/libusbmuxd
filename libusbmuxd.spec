%define major	6
%define api	2.0
%define libname %mklibname usbmuxd %{api} %{major}
%define devname %mklibname -d usbmuxd

%define	git	20211124

Summary:	Library for usbmuxd which communicates with Apple devices
Name:		libusbmuxd
Version:	2.0.3
Release:	1.%{git}1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/ 
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libplist-2.0) >= 2.2.0
BuildRequires:	pkgconfig(libimobiledevice-1.0)
BuildRequires:	pkgcondig(libimobiledevice-glue-1.0)

%description
libusbmuxd provides support for the usbmuxd daemon
that communicates with Apple devices.
It allows simultaeneous access to multiple device
services supported by libimobiledevice

%package -n %{libname}
Group:		System/Libraries
Summary:	Library that provides support for the usbmuxd daeon

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
%setup -q

%build
./autogen.sh
%configure \
	--disable-static

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
