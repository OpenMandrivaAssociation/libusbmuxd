%define major 2
%define libname %mklibname usbmuxd %{major}
%define devname %mklibname -d usbmuxd

Summary:	C Library for usbmuxd which communicates with Apple devices
Name:		libusbmuxd
Version:	1.0.9
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.libimobiledevice.org/ 
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libplist) >=1.11
BuildRequires:	cmake

%description
libusbmuxd is a library for the usbmuxd daemon which is used for communicating with Apple 
devices which allows simultaeneous access to multiple services on the device.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for manipulating Apple Binary and XML Property Lists

%description -n %{libname}
libusbmuxd is a library that provideds support for the usbmuxd daeon.

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
export CMAKE_PREFIX_PATH=/usr
%cmake

%make

%install
%makeinstall_std -C build


%files
%files -n %{libname}
%{_libdir}/libusbmuxd.so.%{major}*
%{_libdir}/libusbmuxd.so.%{version}


%files -n %{devname}
%doc README.devel
%{_includedir}/*.h
%{_libdir}/libusbmuxd.so
%{_libdir}/pkgconfig/libusbmuxd.pc

