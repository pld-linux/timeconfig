Summary:	Text mode tools for setting system time parameters.
Name:		timeconfig
Version:	2.7
Release:	1
License:	GPL
Group:		Base/Utilities
Group(pl):	Podstawowe/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
Requires:	initscripts >= 2.81, glibc >= 2.0.5-5
Prereq:		fileutils, gawk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The timeconfig package contains two utilities: timeconfig and
setclock. Timeconfig provides a simple text mode tool for configuring
the time parameters in /etc/sysconfig/clock and /etc/localtime. The
setclock tool sets the hardware clock on the system to the current
time stored in the system clock.

%prep
%setup -q

%build
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=$RPM_BUILD_ROOT install
rm -f %{_libdir}/zoneinfo

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -L /etc/localtime -a ! -e /etc/localtime ]; then
    ln -sf `ls -ld /etc/localtime | awk '{ print $11}' | sed 's/lib/share/'` /etc/localtime
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/timeconfig
%attr(755,root,root) %{_sbindir}/setclock
%{_mandir}/man8/timeconfig.8
%{_mandir}/man8/setclock.8
%{_datadir}/locale/*/LC_MESSAGES/timeconfig.mo
