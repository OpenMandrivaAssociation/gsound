%define major   0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:           gsound
Version:        1.0.3
Release:        6
Summary:        Small gobject library for playing system sounds

License:        LGPLv2
URL:            https://wiki.gnome.org/Projects/GSound
Source0:        https://download.gnome.org/sources/gsound/1.0/gsound-%{version}.tar.xz

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:  vala-tools
BuildRequires:  meson


%description
GSound is a small library for playing system sounds. 
It's designed to be used via GObject Introspection, 
and is a thin wrapper around the libcanberra C library

%package -n %{libname}
Summary:        Dynamic libraries for %{name}
Group:          System/Libraries
Suggests:       %{name} = %{version}

%description -n %{libname}
this package contains dynamic libraries for gsound.

%package        -n %{devname}
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description    -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING README
%{_bindir}/gsound-play
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GSound-1.0.typelib

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gsound.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GSound-1.0.gir
#dir %{_datadir}/gtk-doc
#dir %{_datadir}/gtk-doc/html
#{_datadir}/gtk-doc/html/gsound
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gsound.*
