# NOTE: for versions >= 1.5 see ctl.spec
Summary:	OpenEXR interface to CTL (Color Transform Language)
Summary(pl.UTF-8):	Interfejs OpenEXR do CTL (języka przekształceń kolorów)
Name:		openexr_ctl
Version:	1.0.1
Release:	2.1
License:	BSD + IP clause
Group:		Libraries
Source0:	http://downloads.sourceforge.net/ampasctl/%{name}-%{version}.tar.gz
# Source0-md5:	035a68db3b1cc40fe99a7c4012d7f024
Patch0:		%{name}-include.patch
Patch1:		%{name}-openexr2.patch
Patch2:		%{name}-link.patch
URL:		http://www.oscars.org/science-technology/council/projects/ctl.html
BuildRequires:	OpenEXR-devel >= 1.6.1
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.3
BuildRequires:	ctl-devel >= 1.4.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IlmImfCtl provides a simplified OpenEXR interface to CTL (Color
Transform Language).

%description -l pl.UTF-8
IlmImfCtl udostępnia uproszczony interfejs OpenEXR do CTL (języka
przekształceń kolorów).

%package devel
Summary:	Header files for IlmInfCtl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki IlmInfCtl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenEXR-devel >= 1.6.1
Requires:	ctl-devel >= 1.4.1
Requires:	libstdc++-devel

%description devel
Header files for IlmInfCtl library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki IlmInfCtl.

%package static
Summary:	Static IlmInfCtl library
Summary(pl.UTF-8):	Statyczna biblioteka IlmInfCtl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static IlmInfCtl library.

%description static -l pl.UTF-8
Statyczna biblioteka IlmInfCtl.

%package progs
Summary:	Programs utilizing OpenEXR/CTL interface
Summary(pl.UTF-8):	Programy wykorzystujące interfejs OpenEXR/CTL
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Programs utilizing OpenEXR/CTL interface:

exrdpx is an initial version of a CTL-driven file converter that
translates DPX files into OpenEXR files and vice versa. The conversion
between the DPX and OpenEXR color spaces is handled by CTL transforms.

exr_ctl_exr is an initial version of a program that can bake the
effect of a series of CTL transforms into the pixels of an OpenEXR
file.

%description progs -l pl.UTF-8
Programy wykorzystujące interfejs OpenEXR/CTL:

exrdpx to wstępna wersja konwertera plików sterowanego CTL-em,
tłumaczącego pliki DPX na OpenEXR i na odwrót. Przekształcenia między
przestrzeniami kolorów DPX i OpenEXR są obsługiwane przez
przekształcenia CTL.

exr_ctl_exr to wstępna wersja programu potrafiącego zamienić efekt
serii przekształceń CTL na piksele w pliku OpenEXR.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# CTL module dir is hardcoded as %{_prefix}/lib/CTL, so force installation there
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	ctldatadir=%{_prefix}/lib/CTL

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libIlmImfCtl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmImfCtl.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libIlmImfCtl.so
%{_libdir}/libIlmImfCtl.la
%{_includedir}/OpenEXR/ImfCtl*.h
%{_pkgconfigdir}/OpenEXR_CTL.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libIlmImfCtl.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exr_ctl_exr
%attr(755,root,root) %{_bindir}/exrdpx
%{_prefix}/lib/CTL
