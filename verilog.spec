Summary:	Icarus Verilog is Verilog compiler and simulator
Summary(pl):	Icarus Verilog jest kompilatorem i symulatorem Veriloga
Name:		verilog
Version:	0.8.2
Release:	1
License:	GPL (except tgt-edif with more relaxed license)
Group:		Applications/Engineering
Source0:	ftp://ftp.icarus.com/pub/eda/verilog/v0.8/%{name}-%{version}.tar.gz
# Source0-md5:	41650504e4460508a0800008a2628e07
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.icarus.com/eda/verilog
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	flex
BuildRequires:	gperf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.

%description -l pl
Icarus Verilog jest narzêdziem do syntezy i symulacji Veriloga.
D±¿y do bycia zgodnym ze standardem IEEE-1364.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f examples/.cvsignore
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv tgt-edif/LICENSE.txt LICENSE_edif.txt

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc attributes.txt glossary.txt BUGS.txt QUICK_START.txt README.txt ieee1364-notes.txt lpm.txt swift.txt xilinx-hint.txt xnf.txt LICENSE_edif.txt
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%dir %{_libdir}/ivl
%attr(755,root,root) %{_libdir}/ivl/ivl
%attr(755,root,root) %{_libdir}/ivl/ivlpp
%attr(755,root,root) %{_libdir}/ivl/edif.tgt
%attr(755,root,root) %{_libdir}/ivl/fpga.tgt
%attr(755,root,root) %{_libdir}/ivl/null.tgt
%attr(755,root,root) %{_libdir}/ivl/vvp.tgt
%{_libdir}/ivl/cadpli.vpl
%{_libdir}/ivl/s*
%{_libdir}/ivl/v*.conf
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}
