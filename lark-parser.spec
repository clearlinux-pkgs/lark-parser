#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lark-parser
Version  : 0.12.0
Release  : 41
URL      : https://files.pythonhosted.org/packages/5a/ee/fd1192d7724419ddfe15b6f17d1c8742800d4de917c0adac3b6aaf22e921/lark-parser-0.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/ee/fd1192d7724419ddfe15b6f17d1c8742800d4de917c0adac3b6aaf22e921/lark-parser-0.12.0.tar.gz
Summary  : a modern parsing library
Group    : Development/Tools
License  : MIT
Requires: lark-parser-license = %{version}-%{release}
Requires: lark-parser-python = %{version}-%{release}
Requires: lark-parser-python3 = %{version}-%{release}
Requires: atomicwrites
Requires: regex
BuildRequires : atomicwrites
BuildRequires : buildreq-distutils3
BuildRequires : regex

%description
Lark is a modern general-purpose parsing library for Python.
        
        With Lark, you can parse any context-free grammar, efficiently, with very little code.

%package license
Summary: license components for the lark-parser package.
Group: Default

%description license
license components for the lark-parser package.


%package python
Summary: python components for the lark-parser package.
Group: Default
Requires: lark-parser-python3 = %{version}-%{release}

%description python
python components for the lark-parser package.


%package python3
Summary: python3 components for the lark-parser package.
Group: Default
Requires: python3-core
Provides: pypi(lark_parser)

%description python3
python3 components for the lark-parser package.


%prep
%setup -q -n lark-parser-0.12.0
cd %{_builddir}/lark-parser-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631206757
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lark-parser
cp %{_builddir}/lark-parser-0.12.0/LICENSE %{buildroot}/usr/share/package-licenses/lark-parser/af7225973c108376de2c312098b16c5a7a8828e6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lark-parser/af7225973c108376de2c312098b16c5a7a8828e6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
