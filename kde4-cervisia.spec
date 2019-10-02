#
# TODO:
# - add man files
#
%define		orgname		cervisia
%define		_state		stable
%define		qtver		4.8.1

Summary:	A KDE CVS frontend
Summary(pl.UTF-8):	Frontend do CVS dla KDE
Name:		kde4-cervisia
Version:	4.14.3
Release:	2
License:	GPL
Group:		X11/Development/Tools
Requires:	cvs-client >= 1.10
Requires:	kde4-kdebase >= %{version}
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	25fb6ddc4ab3c249e7f398d3b03814e4
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdesdk-cervisia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gimpdir	%{_datadir}/gimp/2.0
%define		_appdefsdir	%{_datadir}/X11/app-defaults
%define		_emacspkgdir	/usr/share/emacs/%(rpm -q --qf %{V} emacs-common | tr -d '[a-z]')
%define		_xemacspkgdir	/usr/share/xemacs-packages
%define		_zshfcdir	/usr/share/zsh/latest/functions

%description
A KDE CVS frontend. It features:
- updating or retrieving the status of a working directory or single
  files. Files are displayed in different colors depending on their
  status, and the shown files can be filtered according to their status
- common operations like adding, removing and commiting files.
- advanced operations like adding and removing watches, editing and
  unediting files, locking and unlocking.
- checking out and importing modules.
- graphical diff against the repository and between different
  revisions.
- blame-annotated view of a file.
- view of the log messages in tree and list form.
- resolving of conflicts in a file.
- tagging and branching.
- updating to a tag, branch or date.
- a Changelog editor coupled with the commit dialog.

%description -l pl.UTF-8
Frontend do CVS dla KDE. Ma następujące możliwości:
- uaktualnianie lub odtwarzanie stanu katalogu lub pojedynczych
  plików; pliki są wyświetlane w różnych kolorach zależnie od ich stanu,
  a pokazywane pliki mogą być filtrowane według ich stanu
- podstawowe operacje, takie jak dodawanie, usuwanie i commitowanie
  plików
- zaawansowane operacje, takie jak dodawanie i usuwanie śledzenia,
  włączanie i wyłączanie edycji plików, blokowanie i odblokowywanie
- pobieranie i importowanie modułów
- graficzne wyświetlanie różnic względem repozytorium i między różnymi
  rewizjami
- widok pliku opisany winnymi
- widok loga komentarzy do zmian w postaci drzewa i listy
- rozwiązywanie konfliktów w pliku
- tagowanie i branchowanie
- uaktualnianie do taga, brancha lub daty
- edytor changelogów połączony z oknem dialogowym do commitowania.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang	cervisia	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files -f cervisia.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cervisia
%attr(755,root,root) %{_bindir}/cvsaskpass
%attr(755,root,root) %{_bindir}/cvsservice
%attr(755,root,root) %{_libdir}/libkdeinit4_cervisia.so
%attr(755,root,root) %{_libdir}/libkdeinit4_cvsservice.so
%attr(755,root,root) %{_libdir}/libkdeinit4_cvsaskpass.so
%attr(755,root,root) %{_libdir}/kde4/*cervisia*.so
%{_datadir}/apps/cervisia*
%{_datadir}/config.kcfg/cervisiapart.kcfg
%{_datadir}/dbus-1/interfaces/*.cervisia.*.xml
%{_datadir}/kde4/services/cvsservice.desktop
%{_datadir}/kde4/services/cervisiapart.desktop
%{_desktopdir}/kde4/cervisia.desktop
%{_iconsdir}/*/*/actions/vcs-*-cvs-*.*
%{_iconsdir}/*/*/*/cervisia.png
%{_mandir}/man1/cervisia.1*
