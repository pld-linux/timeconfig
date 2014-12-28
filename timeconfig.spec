Summary:	Text mode tools for setting system time parameters
Summary(pl.UTF-8):	Tekstowe narzędzie do konfigurowania czasu systemowego
Name:		timeconfig
Version:	2.7
Release:	1
License:	GPL
Group:		Base/Utilities
# https://fedorahosted.org/releases/t/i/timeconfig/ (not yet)
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	d14629320acadaf911feab8807320af1
BuildRequires:	gettext-tools
BuildRequires:	newt-devel
BuildRequires:	popt-devel
Requires:	rc-scripts
Requires:	newt
Requires:	fileutils
Requires:	awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The timeconfig package contains two utilities: timeconfig and
setclock. Timeconfig provides a simple text mode tool for configuring
the time parameters in /etc/sysconfig/clock and /etc/localtime. The
setclock tool sets the hardware clock on the system to the current
time stored in the system clock.

%description -l pl.UTF-8
Pakiet timeconfig zawiera dwa narzędzia: timeconfig oraz setclock.
timeconfig jest prostym tekstowym narzędziem do konfiguracji
parametrów czasu systemowego w /etc/sysconfig/clock i /etc/localtime .
setclock jest narzędziem do ustawiania zegara sprzętowego na aktualny
czas systemowy.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_prefix}/man/* $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -L /etc/localtime -a ! -e /etc/localtime ]; then
	ln -sf `ls -ld /etc/localtime | awk '{ print $11}' | sed 's/lib/share/'` /etc/localtime
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/timeconfig
%attr(755,root,root) %{_sbindir}/setclock
%lang(pt_BR) %{_mandir}/pt_BR/man8/*.8*
%{_mandir}/man8/timeconfig.8*
%{_mandir}/man8/setclock.8*
