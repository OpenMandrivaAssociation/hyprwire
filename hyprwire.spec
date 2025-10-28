%define major 1
%define libname %mklibname hyprwire
%define devname %mklibname hyprwire -d

Name:		hyprwire
Version:	0.1.1
Release:	1
Source0:        https://github.com/hyprwm/hyprwire/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:        A fast and consistent wire protocol for IPC
URL:		https://github.com/hyprwm/hyprwire
License:	BSD-3-Clause
Group:		System/Libraries

BuildSystem:	cmake

BuildRequires:  pkgconfig(hyprutils) >= 0.9.0
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(pugixml)

%description
Hyprwire is a fast and consistent wire protocol, and its implementation. This is essentially a "method" for processes to talk to each other.

%package -n %{libname}
Summary:	 A fast and consistent wire protocol for IPC
Group:		System/Libraries

%description -n %{libname}
Hyprwire is a fast and consistent wire protocol, and its implementation. This is essentially a "method" for processes to talk to each other.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.*%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
