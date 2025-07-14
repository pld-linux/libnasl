Summary:	NASL libraries
Summary(pl.UTF-8):	Biblioteki NASL
Name:		libnasl
Version:	2.2.11
Release:	2
License:	GPL
Vendor:		Nessus Project
Group:		Networking
# Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	02889e4829b68cb9d0d827ccdba5db1d
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-linkshared.patch
Patch2:		%{name}-libtool.patch
Patch3:		libnasl-openssl.patch
Patch4:		openssl.patch
Patch5:		bison.patch
URL:		http://www.nessus.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	libtool
BuildRequires:	nessus-libs-devel >= %{version}
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
Requires:	nessus-libs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir		/var/lib

%description
NASL is a scripting language designed for the Nessus security scanner.
Its aim is to allow anyone to write a test for a given security hole
in a few minutes, to allow people to share their tests without having
to worry about their operating system, and to guarantee everyone that
a NASL script can not do anything nasty except performing a given
security test against a given target.

Thus, NASL allows you to easily forge IP packets, or to send regular
packets. It provides you some convenient functions that will make the
test of web and FTP server more easy to write. NASL garantees you that
a NASL script:
- will not send any packet to a host other than the target host,
- will not execute any commands on your local system.

%description -l pl.UTF-8
NASL to język skryptowy stworzony dla skanera bezpieczeństwa Nessus.
Celem języka jest umożliwienie każdemu napisania testu dla danej
dziury w bezpieczeństwie w kilka minut, umożliwienie ludziom na
dzielenie się testami niezależnie od systemu operacyjnego i
zagwarantowanie, że skrypt NASL nie zrobi niczego brzydkiego oprócz
wykonania testu bezpieczeństwa na danym celu.

NASL pozwala na łatwe podrabianie pakietów IP lub wysyłanie normalnych
pakietów. Udostępnia trochę wygodnych funkcji ułatwiających pisanie
testów dla serwerów WWW i FTP. NASL gwarantuje, że taki skrypt:
- nie wyśle żadnego pakietu do hosta innego niż wskazany,
- nie wykona żadnych poleceń na systemie lokalnym.

%package devel
Summary:	NASL libraries development files
Summary(pl.UTF-8):	Pliki dla programistów używających NASL-a
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	nessus-libs-devel >= %{version}

%description devel
Header files for developing applications that use NASL.

%description devel -l pl.UTF-8
Pliki nagłówkowe konieczne do rozwoju aplikacji używających NASL-a.

%package static
Summary:	NASL static libraries
Summary(pl.UTF-8):	Biblioteki statyczne NASL-a
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
NASL static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne NASL-a.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure

%{__make} -j1

%{__make} nasl_guide.ps -C doc
#nasl2_reference.ps requires lyx

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/*.ps
%attr(755,root,root) %ghost %{_libdir}/lib*.so.2
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_bindir}/nasl
%{_mandir}/man1/nasl.1*
%{_var}/lib/nessus/nessus_org.pem

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nasl-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/nessus/nasl.h
%{_mandir}/man1/nasl-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
