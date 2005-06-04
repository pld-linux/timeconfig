Summary:	Text mode tools for setting system time parameters
Summary(pl):	Tekstowe narzêdzie do konfigurowania czasu systemowego
Name:		timeconfig
Version:	2.7
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	d14629320acadaf911feab8807320af1
BuildRequires:	gettext-devel
BuildRequires:	newt-devel
Requires:	rc-scripts
Requires:	newt
Prereq:		fileutils, awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The timeconfig package contains two utilities: timeconfig and
setclock. Timeconfig provides a simple text mode tool for configuring
the time parameters in /etc/sysconfig/clock and /etc/localtime. The
setclock tool sets the hardware clock on the system to the current
time stored in the system clock.

%description -l pl
Pakiet timeconfig zawiera dwa narzêdzia: timeconfig oraz setclock.
timeconfig jest prostym tekstowym narzêdziem do konfiguracji
parametrów czasu systemowego w /etc/sysconfig/clock i /etc/localtime .
setclock jest narzêdziem do ustawiania zegara sprzêtowego na aktualny
czas systemowy.

%prep
%setup -q

%build
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_prefix}/man/* $RPM_BUILD_ROOT%{_mandir}

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
%{_mandir}/man8/timeconfig.8*
%{_mandir}/man8/setclock.8*
%{_datadir}/locale/*/LC_MESSAGES/timeconfig.mo
