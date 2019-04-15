#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kteatime
Version  : 18.12.3
Release  : 5
URL      : https://download.kde.org/stable/applications/18.12.3/src/kteatime-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/kteatime-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/kteatime-18.12.3.tar.xz.sig
Summary  : A handy timer for steeping tea
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kteatime-bin = %{version}-%{release}
Requires: kteatime-data = %{version}-%{release}
Requires: kteatime-license = %{version}-%{release}
Requires: kteatime-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : knotifyconfig-dev

%description
No detailed description available

%package bin
Summary: bin components for the kteatime package.
Group: Binaries
Requires: kteatime-data = %{version}-%{release}
Requires: kteatime-license = %{version}-%{release}

%description bin
bin components for the kteatime package.


%package data
Summary: data components for the kteatime package.
Group: Data

%description data
data components for the kteatime package.


%package doc
Summary: doc components for the kteatime package.
Group: Documentation

%description doc
doc components for the kteatime package.


%package license
Summary: license components for the kteatime package.
Group: Default

%description license
license components for the kteatime package.


%package locales
Summary: locales components for the kteatime package.
Group: Default

%description locales
locales components for the kteatime package.


%prep
%setup -q -n kteatime-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555359020
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555359020
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kteatime
cp COPYING %{buildroot}/usr/share/package-licenses/kteatime/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kteatime/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang kteatime

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kteatime

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kteatime.desktop
/usr/share/icons/hicolor/16x16/apps/kteatime.png
/usr/share/icons/hicolor/22x22/apps/kteatime.png
/usr/share/icons/hicolor/32x32/apps/kteatime.png
/usr/share/icons/hicolor/48x48/apps/kteatime.png
/usr/share/icons/hicolor/64x64/apps/kteatime.png
/usr/share/icons/hicolor/scalable/apps/kteatime.svgz
/usr/share/knotifications5/kteatime.notifyrc
/usr/share/metainfo/org.kde.kteatime.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kteatime/index.cache.bz2
/usr/share/doc/HTML/ca/kteatime/index.docbook
/usr/share/doc/HTML/de/kteatime/config.png
/usr/share/doc/HTML/de/kteatime/index.cache.bz2
/usr/share/doc/HTML/de/kteatime/index.docbook
/usr/share/doc/HTML/en/kteatime/config.png
/usr/share/doc/HTML/en/kteatime/index.cache.bz2
/usr/share/doc/HTML/en/kteatime/index.docbook
/usr/share/doc/HTML/es/kteatime/config.png
/usr/share/doc/HTML/es/kteatime/index.cache.bz2
/usr/share/doc/HTML/es/kteatime/index.docbook
/usr/share/doc/HTML/it/kteatime/index.cache.bz2
/usr/share/doc/HTML/it/kteatime/index.docbook
/usr/share/doc/HTML/nl/kteatime/index.cache.bz2
/usr/share/doc/HTML/nl/kteatime/index.docbook
/usr/share/doc/HTML/pt/kteatime/index.cache.bz2
/usr/share/doc/HTML/pt/kteatime/index.docbook
/usr/share/doc/HTML/pt_BR/kteatime/config.png
/usr/share/doc/HTML/pt_BR/kteatime/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kteatime/index.docbook
/usr/share/doc/HTML/sv/kteatime/config.png
/usr/share/doc/HTML/sv/kteatime/index.cache.bz2
/usr/share/doc/HTML/sv/kteatime/index.docbook
/usr/share/doc/HTML/uk/kteatime/config.png
/usr/share/doc/HTML/uk/kteatime/index.cache.bz2
/usr/share/doc/HTML/uk/kteatime/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kteatime/COPYING
/usr/share/package-licenses/kteatime/COPYING.DOC

%files locales -f kteatime.lang
%defattr(-,root,root,-)

