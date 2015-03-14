%define major 0
%define gir_major 1.0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}
%define girname %mklibname %{name}-gir %{gir_major}

Name:           gsound
Version:        1.0.1
Release:        1
Summary:        Small gobject library for playing system sounds

License:        LGPLv2
Group:		Graphical desktop/GNOME
URL:            https://wiki.gnome.org/Projects/GSound
Source0:        http://download.gnome.org/sources/gsound/1.0/gsound-%{version}.tar.xz

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  vala-tools

Requires:	%{girname} = %{EVRD}


%description
GSound is a small library for playing system sounds. 
It's designed to be used via GObject Introspection, 
and is a thin wrapper around the libcanberra C library


%package -n %{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries

%description -n %{libname}
This package contains libraries used by %{name}.

%package -n %{girname}
Summary: GObject Introspection interface description for %{name}
Group: System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/GNOME and GTK+
Requires:       %{libname} = %{EVRD}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure2_5x	\
	--disable-static \
	--enable-vala

%make


%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -delete


%files
%doc COPYING README
%{_bindir}/gsound-play
%dir %{_libdir}/girepository-1.0

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GSound-1.0.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gsound.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GSound-%{gir_major}.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gsound
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gsound.*
