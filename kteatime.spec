#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kteatime
Version  : 23.04.1
Release  : 52
URL      : https://download.kde.org/stable/release-service/23.04.1/src/kteatime-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/kteatime-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/kteatime-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kteatime-bin = %{version}-%{release}
Requires: kteatime-data = %{version}-%{release}
Requires: kteatime-license = %{version}-%{release}
Requires: kteatime-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : knotifyconfig-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kteatime-23.04.1
cd %{_builddir}/kteatime-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684779957
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684779957
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kteatime
cp %{_builddir}/kteatime-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kteatime/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kteatime-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kteatime/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc || :
cp %{_builddir}/kteatime-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kteatime/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kteatime
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kteatime
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
/usr/share/doc/HTML/fr/kteatime/config.png
/usr/share/doc/HTML/fr/kteatime/index.cache.bz2
/usr/share/doc/HTML/fr/kteatime/index.docbook
/usr/share/doc/HTML/it/kteatime/index.cache.bz2
/usr/share/doc/HTML/it/kteatime/index.docbook
/usr/share/doc/HTML/nl/kteatime/index.cache.bz2
/usr/share/doc/HTML/nl/kteatime/index.docbook
/usr/share/doc/HTML/pt/kteatime/index.cache.bz2
/usr/share/doc/HTML/pt/kteatime/index.docbook
/usr/share/doc/HTML/pt_BR/kteatime/config.png
/usr/share/doc/HTML/pt_BR/kteatime/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kteatime/index.docbook
/usr/share/doc/HTML/ru/kteatime/index.cache.bz2
/usr/share/doc/HTML/ru/kteatime/index.docbook
/usr/share/doc/HTML/sv/kteatime/config.png
/usr/share/doc/HTML/sv/kteatime/index.cache.bz2
/usr/share/doc/HTML/sv/kteatime/index.docbook
/usr/share/doc/HTML/uk/kteatime/config.png
/usr/share/doc/HTML/uk/kteatime/index.cache.bz2
/usr/share/doc/HTML/uk/kteatime/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kteatime/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kteatime/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kteatime/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc

%files locales -f kteatime.lang
%defattr(-,root,root,-)

