Name     : usrbinpython
Version  : 3
Release  : 14
URL      : http://localhost/cgit/projects/usrbinpython/snapshot/usrbinpython-3.tar.gz
Source0  : http://localhost/cgit/projects/usrbinpython/snapshot/usrbinpython-3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: usrbinpython-bin

%description
No detailed description available

%package bin
Summary: bin components for the usrbinpython package.
Group: Binaries
Requires: python3-core

%description bin
bin components for the usrbinpython package.


%prep
%setup -q -n usrbinpython-3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1506873880
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1506873880
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/python
