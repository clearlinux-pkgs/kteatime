#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kteatime
Version  : 19.08.2
Release  : 13
URL      : https://download.kde.org/stable/applications/19.08.2/src/kteatime-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/kteatime-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/kteatime-19.08.2.tar.xz.sig
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
%setup -q -n kteatime-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570770138
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570770138
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

