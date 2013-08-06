Name:		QtPixmap
Version:	0.28
Release:	8
Epoch:		0
Summary:	GTK engine
Url:		http://www.kde-look.org/content/show.php?content=7043
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	gtk+2.0-devel
Conflicts:	Geramik < 0:0.26

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

%files
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README Usage
%defattr(-,root,root)
%{_libdir}/gtk-2.0/*/engines/libqtpixmap.so


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.28-7mdv2011.0
+ Revision: 616438
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0:0.28-6mdv2010.0
+ Revision: 433043
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0:0.28-5mdv2009.0
+ Revision: 242503
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 28 2007 David Walluck <walluck@mandriva.org> 0:0.28-3mdv2008.0
+ Revision: 72487
- rebuild
- Import QtPixmap



* Mon Aug 14 2006 David Walluck <walluck@mandriva.org> 0:0.28-2mdv2007.0 
- BuildRequires: libgdkimlib-devel

* Sun Jun 04 2006 David Walluck <walluck@mandriva.org> 0:0.28-1mdv2007.0
- 0.28
- rebuild

* Fri May 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.27-4mdk
- Rebuild

* Mon Apr 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.27-3mdk
- rebuild for gtk+-2.4.x (because of theme engine path)

* Sun Feb 22 2004 David Walluck <walluck@linux-mandrake.com> 0:0.27-2mdk
- rebuild to fix my email address

* Sun Nov 30 2003 David Walluck <walluck@linux-mandrake.com> 0:0.27-1mdk
- release
