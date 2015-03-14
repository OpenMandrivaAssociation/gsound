Name:           gsound
Version:        1.0.1
Release:        1%{?dist}
Summary:        Small gobject library for playing system sounds

License:        LGPLv2
URL:            https://wiki.gnome.org/Projects/GSound
Source0:        http://download.gnome.org/sources/gsound/1.0/gsound-%{version}.tar.xz

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  vala-tools


%description
GSound is a small library for playing system sounds. 
It's designed to be used via GObject Introspection, 
and is a thin wrapper around the libcanberra C library


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-vala
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING README
%{_bindir}/gsound-play
%{_libdir}/*.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GSound-1.0.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gsound.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GSound-1.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gsound
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gsound.*



%changelog
* Mon Dec  1 2014 Yanko Kaneti <yaneti@declera.com> - 1.0.1-1
- Update to 1.0.1

* Sun Nov 30 2014 Yanko Kaneti <yaneti@declera.com> - 1.0.0-2
- Initial spec for review - 0.98.0-0.1.a648648
- Additional patch + references + using %%autopatch - 0.98.0-0.2.a648648
- Update to 1.0.0. drop upstreamed paches - 1.0.0-1
- Own some more directories as per review (#1167482) - 1.0.0-2
