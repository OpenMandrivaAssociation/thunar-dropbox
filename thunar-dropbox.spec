%define debug_package %{nil}

Summary:	Dropbox extension for Thunar
Name:		thunar-dropbox
Version:	0.3.1
Release:	1
Source0:	https://github.com/Jeinzi/thunar-dropbox/archive/%{version}/%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		Graphical desktop/Xfce
Url:		http://www.softwarebakery.com/maato/thunar-dropbox.html
Requires:	thunar
BuildRequires:	pkgconfig(thunarx-3)
BuildRequires:  cmake
BuildRequires:  cmake(ECM)

%description
Dropbox extension for Thunar.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/usr

%install
%cmake_install

find %{buildroot} -name *.so -exec chmod 755 {} \;

%files
%doc AUTHORS ChangeLog COPYING
%_libdir/thunarx-3/*.so
%_iconsdir/hicolor/*/*/%{name}.png
