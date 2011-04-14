%define name	thunar-dropbox
%define version 0.1.1
%define release %mkrel 1

Summary:	Dropbox extension for Thunar
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source1:	wscript.32
Source2:	wscript.64
License:	GPLv3+
Group:		Graphical desktop/Xfce
Url:		http://www.softwarebakery.com/maato/thunar-dropbox.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	thunar
BuildRequires:	python, thunar-devel

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
%__rm -rf %{buildroot}
./waf install --destdir=%{buildroot}
find %{buildroot} -name *.so -exec chmod 755 {} \;

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%_libdir/thunarx-1/*.so
%_iconsdir/hicolor/*/*/%{name}.png
