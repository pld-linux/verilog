Summary:	Icarus Verilog - Verilog compiler and simulator
Summary(pl.UTF-8):	Icarus Verilog - kompilator i symulator Veriloga
Name:		verilog
Version:	0.9.6
Release:	1
License:	GPL (except tgt-edif with more relaxed license)
Group:		Applications/Engineering
Source0:	ftp://ftp.icarus.com/pub/eda/verilog/v0.9/%{name}-%{version}.tar.gz
# Source0-md5:	a77d847198c571ba2bfd55b99162c3b6
URL:		http://www.icarus.com/eda/verilog/
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	flex
BuildRequires:	gperf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.

%description -l pl.UTF-8
Icarus Verilog jest narzędziem do syntezy i symulacji Veriloga.
Dąży do bycia zgodnym ze standardem IEEE-1364.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc attributes.txt BUGS.txt developer-quick-start.txt extensions.txt
%doc glossary.txt ieee1364-notes.txt ivl_target.txt lpm.txt netlist.txt
%doc QUICK_START.txt README.txt swift.txt t-dll.txt va_math.txt vpi.txt
%doc xilinx-hint.txt
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%dir %{_libdir}/ivl
%attr(755,root,root) %{_libdir}/ivl/ivl
%attr(755,root,root) %{_libdir}/ivl/ivlpp
%attr(755,root,root) %{_libdir}/ivl/cadpli.vpl
%attr(755,root,root) %{_libdir}/ivl/*.tgt
%attr(755,root,root) %{_libdir}/ivl/*.vpi
%{_libdir}/ivl/include
%{_libdir}/ivl/*.conf
%{_libdir}/ivl/*.sft
%{_mandir}/*/*
%{_examplesdir}/%{name}-%{version}
