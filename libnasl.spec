Summary:	NASL libraries
Summary(pl):	Biblioteki NASL
Name:		libnasl
Version:	2.0.8
Release:	1
License:	GPL
Group:		Networking
Vendor:		Nessus Project
Source0:	ftp://ftp.nessus.org/pub/nessus/nessus-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	dcaf86be755eeca67427af7c7535cd74
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-linkshared.patch
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

%description
NASL is a scripting language designed for the Nessus security scanner.
Its aim is to allow anyone to write a test for a given security hole
in a few minutes, to allow people to share their tests without having
to worry about their operating system, and to guarantee everyone that
a NASL script can not do anything nasty except performing a given
security test against a given target.

Thus, NASL allows you to easily forge IP packets, or to send regular
packets. It provides you some convenient functions that will make the
test of web and ftp server more easy to write. NASL garantees you that
a NASL script:
- will not send any packet to a host other than the target host,
- will not execute any commands on your local system.

%description -l pl
NASL to jêzyk skryptowy stworzony dla skanera bezpieczeñstwa Nessus.
Celem jêzyka jest umo¿liwienie ka¿demu napisania testu dla danej
dziury w bezpieczeñstwie w kilka minut, umo¿liwienie ludziom na
dzielenie siê testami niezale¿nie od systemu operacyjnego i
zagwarantowanie, ¿e skrypt NASL nie zrobi niczego brzydkiego oprócz
wykonania testu bezpieczeñstwa na danym celu.

NASL pozwala na ³atwe podrabianie pakietów IP lub wysy³anie normalnych
pakietów. Udostepnia trochê wygodnych funkcji u³atwiaj±cych pisanie
testów dla serwerów WWW i FTP. NASL gwarantuje, ¿e taki skrypt:
- nie wy¶le ¿adnego pakietu do hosta innego ni¿ wskazany,
- nie wykona ¿adnych poleceñ na systemie lokalnym.

%package devel
Summary:	NASL libraries development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych NASL-a
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	nessus-libs-devel >= %{version}

%description devel
Header files for developing applications that use NASL.

%description devel -l pl
Pliki nag³ówkowe konieczne do rozwoju aplikacji u¿ywaj±cych NASL-a.

%package static
Summary:	NASL static libraries
Summary(pl):	Biblioteki statyczne NASLa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
NASL static libraries.

%description static -l pl
Biblioteki statyczne NASLa.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure

%{__make}

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_bindir}/nasl
%{_mandir}/man1/nasl.1*

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
