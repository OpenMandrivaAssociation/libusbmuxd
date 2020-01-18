%define major 6
%define libname %mklibname usbmuxd %{major}
%define devname %mklibname -d usbmuxd

Summary:	Library for usbmuxd which communicates with Apple devices
Name:		libusbmuxd
Version:	2.0.1
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/ 
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libplist) >= 2.1.0

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
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std 

%files
%{_bindir}/inetcat
%{_bindir}/iproxy

%files -n %{libname}
%{_libdir}/libusbmuxd.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/libusbmuxd.so
%{_libdir}/pkgconfig/libusbmuxd.pc
