%define debug_package %{nil}

Summary:	Dropbox extension for Thunar
Name:		thunar-dropbox
Version:	0.3.0
Release:	1
Source0:	https://github.com/Jeinzi/thunar-dropbox/archive/%{version}/%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		Graphical desktop/Xfce
Url:		http://www.softwarebakery.com/maato/thunar-dropbox.html
Requires:	thunar >= 1.2.0
BuildRequires:	python2
BuildRequires:	pkgconfig(thunarx-2)

%description
Dropbox extension for Thunar.

%prep
%setup -q

%build
python2 waf configure --prefix=%{_prefix} --libdir=%{_libdir} --verbose
python2 waf build --verbose

%install
python2 waf install --destdir=%{buildroot} 
find %{buildroot} -name *.so -exec chmod 755 {} \;

%files
%doc AUTHORS ChangeLog COPYING
%_libdir/thunarx-2/*.so
%_iconsdir/hicolor/*/*/%{name}.png
