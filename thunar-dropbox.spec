%define debug_package %{nil}

Summary:	Dropbox extension for Thunar
Name:		thunar-dropbox
Version:	0.3.1
Release:	1
Source0:	https://github.com/Jeinzi/thunar-dropbox/archive/%{version}/%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		Graphical desktop/Xfce
Url:		https://www.softwarebakery.com/maato/thunar-dropbox.html
Requires:	thunar
BuildRequires:	pkgconfig(thunarx-3)
BuildRequires:  cmake ninja
BuildRequires:  cmake(ECM)
Recommends:     dropbox

%description
Dropbox extension for Thunar.

%prep
%setup -q
%autopatch -p1
# Fix wrong libraries install path
sed -i -e 's,lib/,%{_lib}/,g' CMakeLists.txt

%build
%cmake  -DCMAKE_BUILD_TYPE=Release \
        -G Ninja
%ninja_build


%install
%ninja_install -C build

find %{buildroot} -name *.so -exec chmod 755 {} \;

%files
%doc AUTHORS ChangeLog COPYING
%{_libdir}/thunarx-3/*.so
%{_iconsdir}/hicolor/*/*/%{name}.png
