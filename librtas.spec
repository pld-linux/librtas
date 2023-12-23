Summary:	Libraries for user-space access to the Run-Time Abstraction Services
Summary(pl.UTF-8):	Biblioteki do dostępu do RTAS z przestrzeni użytkownika
Name:		librtas
Version:	2.0.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/nfont/librtas/tags
Source0:	https://github.com/nfont/librtas/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6e4aedaa75dbfa2317c34a5ccbde040d
URL:		https://github.com/nfont/librtas
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
# uses PowerPC-specific RTAS proc files/syscalls
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librtas provides a set of libraries for user-space access to the
Run-Time Abstraction Services (RTAS) on the PowerPC architecture.

%description -l pl.UTF-8
Ten pakiet udostępnia zbiór bibliotek do dostępu z przestrzeni
użytkownika do RTAS (Run-Time Abstraction Services) na architekturze
PowerPC.

%package devel
Summary:	Header files for librtas library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki librtas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for librtas library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki librtas.

%package static
Summary:	Static librtas library
Summary(pl.UTF-8):	Statyczna biblioteka librtas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librtas library.

%description static -l pl.UTF-8
Statyczna biblioteka librtas.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librtas*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_libdir}/librtas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librtas.so.2
%attr(755,root,root) %{_libdir}/librtasevent.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librtasevent.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librtas.so
%attr(755,root,root) %{_libdir}/librtasevent.so
%{_includedir}/librtas.h
%{_includedir}/librtasevent*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librtas.a
%{_libdir}/librtasevent.a
