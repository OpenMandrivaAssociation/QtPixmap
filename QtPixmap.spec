Name:		QtPixmap
Version:	0.28
Release:	%mkrel 6
Epoch:		0
Summary:	GTK engine
Url:		http://www.kde-look.org/content/show.php?content=7043
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgdkimlib-devel
Conflicts:	Geramik < 0:0.26
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a hacked/modifed version of the original GTK pixmap engine -
which has been modified to obtain widget colours and fonts from
~/.qt/qtrc. This means that GTK apps should follow the KDE color
scheme.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

# remove unpackaged files
%{__rm} %{buildroot}%{_libdir}/gtk/themes/engines/*.la %{buildroot}%{_libdir}/gtk-2.0/*/engines/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README Usage
%defattr(-,root,root)
%{_libdir}/gtk/themes/engines/libqtpixmap.so
%{_libdir}/gtk-2.0/*/engines/libqtpixmap.so
