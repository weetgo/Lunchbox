Name:		LunchBox
Version:	@VERSION@
Release:	1%{?dist}
Summary:	Library for multi-threaded programming

Group:		Development/Libraries
License:	LGPLv2
URL:		http://www.equalizergraphics.com/
Source0:	http://www.equalizergraphics.com/downloads/%{name}-%{version}.tar.gz
#Patch0:		LunchBox-@VERSION@-build-fix.patch
BuildRequires:	cmake boost-devel

%description
Lunchbox is a C++ toolkit library for multi-threaded programming.

%package devel
Summary:	Development files for Lunchbox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the Lunchbox.

%prep
%setup -q
%patch0 -p1 -b .build-fix

%build
%cmake

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_datadir}/%{name}/doc _tmpdoc/


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc _tmpdoc/*
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Sep 19 2011 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-1
- Initial Release
