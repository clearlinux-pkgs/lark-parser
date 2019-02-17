#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lark-parser
Version  : 0.6.6
Release  : 1
URL      : https://files.pythonhosted.org/packages/7c/1a/36d20242838a523252d053f718b8d6e98c72c07afc45a581d493f8a9dd69/lark-parser-0.6.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/7c/1a/36d20242838a523252d053f718b8d6e98c72c07afc45a581d493f8a9dd69/lark-parser-0.6.6.tar.gz
Summary  : a modern parsing library
Group    : Development/Tools
License  : MIT
Requires: lark-parser-license = %{version}-%{release}
Requires: lark-parser-python = %{version}-%{release}
Requires: lark-parser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Lark - a modern parsing library for Python
Parse any context-free grammar, FAST and EASY!

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

%description python3
python3 components for the lark-parser package.


%prep
%setup -q -n lark-parser-0.6.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550422706
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lark-parser
cp LICENSE %{buildroot}/usr/share/package-licenses/lark-parser/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lark-parser/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
