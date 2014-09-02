Summary:	Dropbox extension for Thunar
Name:		thunar-dropbox
Version:	0.2.0
Release:	3
Source0:	%{name}-%{version}.tar.bz2
Source1:	wscript.32
Source2:	wscript.64
License:	GPLv3+
Group:		Graphical desktop/Xfce
Url:		http://www.softwarebakery.com/maato/thunar-dropbox.html
Requires:	thunar >= 1.2.0
BuildRequires:	python
BuildRequires:	pkgconfig(thunarx-2)

%description
Dropbox extension for Thunar.

%prep
%setup -q
%ifarch x86_64
cp -f %SOURCE2 wscript
%else
cp -f %SOURCE1 wscript
%endif

%build
./waf configure --prefix=/usr
./waf build

%install
./waf install --destdir=%{buildroot}
find %{buildroot} -name *.so -exec chmod 755 {} \;

%files
%doc AUTHORS ChangeLog COPYING
%_libdir/thunarx-2/*.so
%_iconsdir/hicolor/*/*/%{name}.png
