Summary:	Libraries for user-space access to the Run-Time Abstraction Services
Summary(pl.UTF-8):	Biblioteki do dostępu do RTAS z przestrzeni użytkownika
Name:		librtas
Version:	1.3.8
Release:	1
License:	CPL v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/librtas/%{name}-%{version}.tar.gz
# Source0-md5:	1d737ff4bc9a86b3e2cfd3a805f7632d
Patch0:		%{name}-lib64.patch
URL:		http://librtas.sourceforge.net/
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
%patch0 -p1

find . -name 'lib*.so*' | xargs %{__rm}

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install librtas_src/librtas.a $RPM_BUILD_ROOT%{_libdir}
/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT Changelog README
%attr(755,root,root) %{_libdir}/libofdt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libofdt.so.1
%attr(755,root,root) %{_libdir}/librtas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librtas.so.1
%attr(755,root,root) %{_libdir}/librtasevent.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librtasevent.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libofdt.so
%attr(755,root,root) %{_libdir}/librtas.so
%attr(755,root,root) %{_libdir}/librtasevent.so
%{_includedir}/common.h
%{_includedir}/libofdt.h
%{_includedir}/librtas*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librtas.a
