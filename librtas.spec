Summary:	Libraries for user-space access to the Run-Time Abstraction Services
Summary(pl):	Biblioteki do dostêpu do RTAS z przestrzeni u¿ytkownika
Name:		librtas
Version:	1.3.0
Release:	1
License:	CPL v1.0
Group:		Libraries
Source0:	http://librtas.ozlabs.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	f2b4fee07f46cf00cc8d5e51af8ae565
URL:		http://librtas.ozlabs.org/
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librtas provides a set of libraries for user-space access to the
Run-Time Abstraction Services (RTAS) on the PowerPC architecture.

%description -l pl
Ten pakiet udostêpnia zbiór bibliotek do dostêpu z przestrzeni
u¿ytkownika do RTAS (Run-Time Abstraction Services) na architekturze
PowerPC.

%package devel
Summary:	Header files for librtas library
Summary(pl):	Pliki nag³ówkowe biblioteki librtas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for librtas library.

%description devel -l pl
Pliki nag³ówkowe biblioteki librtas.

%package static
Summary:	Static librtas library
Summary(pl):	Statyczna biblioteka librtas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librtas library.

%description static -l pl
Statyczna biblioteka librtas.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install librtas_src/librtas.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT Changelog README
%attr(755,root,root) %{_libdir}/librtas*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librtas*.so
%{_includedir}/librtas*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librtas.a
