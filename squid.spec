Summary:	SQUID Internet Object Cache
Summary(pl):	Uniwersalny proxy-cache server
Name:		squid
Version:	2.4.STABLE4
Release:	1
Epoch:		6
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://www.squid-cache.org/Versions/v2/2.4/%{name}-%{version}-src.tar.gz
Source1:	%{name}-1.1.19-faq.tar.gz
Source2:	%{name}.init
Source3:	%{name}.sysconfig
Source4:	http://cache.is.co.za/%{name}-docs.tar.gz
Source5:	%{name}.conf.patch
Source6:	%{name}.logrotate
Patch10:	%{name}-perl.patch
Patch11:	%{name}-linux.patch
Patch12:	%{name}-fhs.patch
Patch13:	%{name}-location.patch
Patch14:	%{name}-domainmatch.patch
Patch15:	%{name}-libnsl_fixes.patch
BuildRequires:	autoconf
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
PreReq:		rc-scripts >= 0.2.0
PreReq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}
%define		_sysconfdir	/etc/%{name}

%description
Squid is a high-performance proxy caching server for web clients,
supporting FTP, gopher, and HTTP data objects. Unlike traditional
caching software, Squid handles all requests in a single,
non-blocking, I/O-driven process. Squid keeps meta data and especially
hot objects cached in RAM, caches DNS lookups, supports non-blocking
DNS lookups, and implements negative caching of failed requests. If
you are tight on memory, check out the NOVM version of this package.
Squid supports SSL, extensive access controls, and full request
logging. By using the lightweight Internet Cache Protocol, Squid
caches can be arranged in a hierarchy or mesh for additional bandwidth
savings. Squid consists of a main server program squid, a Domain Name
System lookup program dnsserver, a program for retrieving FTP data
ftpget, and some management and client tools. When squid starts up, it
spawns a configurable number of dnsserver processes, each of which can
perform a single, blocking Domain Name System (DNS) lookup. This
reduces the amount of time the cache waits for DNS lookups. Squid is
derived from the ARPA-funded Harvest project.

%description -l pl
Squid jest wysoce wydajnym serwerem proxy-cache dla przegl±darek WWW,
klientów FTP i gopher. Squid przechowuje najczê¶ciej pobierane dane w
pamiêci RAM i zapamiêtuje odwo³ania do DNS. Squid oferuje wsparcie dla
SSL, rozbudowan± kontrolê dostêpu oraz pe³ne rejestrowanie pobieranych
danych. Dziêki u¿yciu protoko³u ICP (Internet Cache Protocol), serwer
squid mo¿na ³±czyæ w hierarchiê, zwiêkszaj±c ich efektywno¶æ. Pakiet
squid obejmuje: g³ówny program serwera squid, program dostarczaj±cy
informacji z DNS dnsserver, program odbieraj±cy dane FTP ftpget, oraz
pomocnicze programy do zarz±dzania. Squid wywodzi siê ze
sponsorowanego przez ARPA projektu Harvest.

%package cachemgr
Summary:	CGI script for Squid management
Summary(pl):	Skrypt CGI do zarz±dzania Squidem przez WWW
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administracyjne
Requires:	%{name} = %{version}
Requires:	httpd

%description cachemgr
Cachemgr.cgi is a CGI script that allows administrator to chceck
various informations about Squid via WWW.

%description cachemgr -l pl
Cachemgr.cgi jest skryptem CGI, który pozwala administratorowi
zapoznaæ siê z informacjami o pracy Squida poprzez WWW.

%package ldap_auth
Summary:	LDAP authentication helper for Squid
Summary(pl):	Wsparcie autentykacji LDAP dla squida
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administracyjne
Requires:	%{name}

%description ldap_auth
This Squid helper allows authentication against LDAP directories using
the "simple authentication" (plain-text).

%description ldap_auth -l pl
Pakiet ten pozwala na autentykacjê LDAP za pomoc± prostej autentykacji
(otwartym tekstem).

%package pam_auth
Summary:	PAM authentication helper for Squid
Summary(pl):	Wsparcie autentykacji PAM dla squida
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administracyjne
Requires:	%{name}

%description pam_auth
This program authenticates users against a PAM configured
authentication service "squid". This allows you to authenticate Squid
users to any authentication source for which you have a PAM module.

%description pam_auth -l pl
Program ten pozwala na autentykacjê u¿ytkowników squida w dowolnym
¼ródle posiadaj±cym modu³ PAM.

%package smb_auth
Summary:	SMB authentication helper for Squid
Summary(pl):	Wsparcie autentykacji SMB dla squida
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administracyjne
Requires:	%{name}

%description smb_auth
This is a proxy authentication module. With smb_auth you can
authenticate proxy users against an SMB server like Windows NT or
Samba.

%description smb_auth -l pl
To jest modu³ autentykacji proxy. Z smb_auth mo¿esz autentyfikowaæ
u¿ytkowników proxy na serwerach SMB, jak Windows NT czy Samba.

%prep
%setup -q -a 1 -a 4

# Bug fixes from Squid home page.

# Other patches:
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%build
autoconf
%configure \
	--localstatedir=/var \
	--enable-icmp \
	--enable-useragent-log \
	--enable-snmp \
	--enable-arp-acl \
	--enable-err-language=English \
	--enable-htcp \
	--enable-carp \
	--enable-storeio="aufs,coss,diskd,null,ufs" \
	--enable-removal-policies="lru heap" \
	--disable-ipf-transparent \
	--enable-delay-pools \
	--with-pthreads \
	--enable-cache-digests \
	--with-auth-modules=yes
# old dns-checker:
#	--disable-internal-dns \
# for 2.4 kernel:
#	--enable-linux-netfilter\

mv -f squid/* doc
%{__make}

%{__make} -C auth_modules SUBDIRS="LDAP MSNT NCSA PAM SMB YP getpwnam"

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT/home/httpd/cgi-bin \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig,logrotate.d} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_libexecdir}/{contrib,auth_modules}} \
	$RPM_BUILD_ROOT%{_mandir}/{man1,man8} \
	$RPM_BUILD_ROOT%{_datadir}/squid \
	$RPM_BUILD_ROOT/var/{cache,log{,/archiv}}/squid

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT/etc/squid \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	libexecdir=$RPM_BUILD_ROOT%{_bindir} \
	localstatedir=$RPM_BUILD_ROOT/var \
	datadir=$RPM_BUILD_ROOT%{_datadir}

# We don't use %{__make} install-pinger, because it tries to set it suid root.
install src/pinger $RPM_BUILD_ROOT%{_bindir}

mv -f contrib/*.pl $RPM_BUILD_ROOT%{_libexecdir}/contrib

# auth modules
install auth_modules/LDAP/squid_ldap_auth $RPM_BUILD_ROOT%{_libexecdir}/auth_modules
install -d $RPM_BUILD_ROOT%{_mandir}/man8
install auth_modules/LDAP/squid_ldap_auth.8 $RPM_BUILD_ROOT%{_mandir}/man8
gzip -9nf auth_modules/LDAP/README

install auth_modules/PAM/pam_auth $RPM_BUILD_ROOT%{_libexecdir}/auth_modules
gzip -9nf auth_modules/PAM/pam_auth.c # there is documentation


install auth_modules/SMB/smb_auth $RPM_BUILD_ROOT%{_libexecdir}/auth_modules
gzip -9nf auth_modules/SMB/README

mv -f $RPM_BUILD_ROOT%{_bindir}/cachemgr.cgi $RPM_BUILD_ROOT/home/httpd/cgi-bin
mv -f $RPM_BUILD_ROOT%{_bindir}/squid	$RPM_BUILD_ROOT%{_sbindir}/
mv -f $RPM_BUILD_ROOT/etc/squid/icons	$RPM_BUILD_ROOT%{_datadir}/squid

cd errors
for LNG in *; do
	if [ -d $LNG ]; then
		mv -f $LNG $RPM_BUILD_ROOT%{_datadir}/squid/errors.$LNG
	fi
done
cd ..

cd $RPM_BUILD_ROOT/etc/squid
cp -f squid.conf{,.default}
patch -p0 < %{SOURCE5}
cd -

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/squid
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/squid
install %{SOURCE6} $RPM_BUILD_ROOT/etc/logrotate.d/squid

install scripts/*.pl $RPM_BUILD_ROOT%{_libexecdir}

touch $RPM_BUILD_ROOT/var/log/squid/{access,cache,store}.log

# These two files start squid. They are replaced by /etc/rc.d/init.d script.
rm -f $RPM_BUILD_ROOT%{_bindir}/R*

gzip -9nf CONTRIBUTORS COPYRIGHT CREDITS README ChangeLog QUICKSTART \
	TODO

%clean
#rm -rf $RPM_BUILD_ROOT

%pre
grep -q squid /etc/group || (
	/usr/sbin/groupadd -g 91 -r -f squid 1>&2 || :
)
grep -q squid /etc/passwd || (
	/usr/sbin/useradd -M -o -r -u 91 -s /bin/false \
		-g squid -c "SQUID http caching daemon" -d /var/cache/squid squid 1>&2 || :
)

%post
# If there is already link, don't do anything.
if [ ! -e %{_datadir}/squid/errors ]; then

# Try to create link to Polish, and then any directory but English.
if [ -d %{_datadir}/squid/errors.Polish ]; then
	ln -sf %{_datadir}/squid/errors{.Polish,}
	exit
else
	find %{_datadir}/squid/errors/ -type d -name 'errors.*'| while read NAME; do
		if [ $NAME != "English" ]; then
			ln -fs $NAME %{_datadir}/squid/errors
			exit
		fi
	done
fi

# Create symlink to English if everything else fails.
ln -sf %{_datadir}/squid/errors{.English,}

fi

if [ "$1" = "1" ]; then
	/sbin/chkconfig --add squid
	echo "Run \"/etc/rc.d/init.d/squid start\" to start squid." >&2
else
	if [ -f /var/lock/subsys/squid ]; then
		/etc/rc.d/init.d/squid restart >&2
	fi
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/squid ]; then
		/etc/rc.d/init.d/squid stop >&2
	fi
	/sbin/chkconfig --del squid
	rm -f %{_datadir}/squid/errors
fi

%files
%defattr(644,root,root,755)
%doc faq *.gz doc/*

%attr(755,root,root) %{_bindir}/client
%attr(755,root,root) %{_bindir}/diskd
# It's obsolete while internal-dns is enabled
#%attr(755,root,root) %{_bindir}/dnsserver
# YES, it has to be suid root, it sends ICMP packets.
%attr(4754,root,squid) %{_bindir}/pinger
%attr(755,root,root) %{_bindir}/unlinkd
%attr(755,root,root) %{_sbindir}/*

%attr(755,root,root) %dir %{_sysconfdir}

%attr(754,root,root) /etc/rc.d/init.d/squid
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/squid
%attr(640,root,squid) %config(noreplace) /etc/sysconfig/squid
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/squid.conf
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mime.conf
%attr(640,root,root) %{_sysconfdir}/mime.conf.default
%attr(640,root,root) %{_sysconfdir}/squid.conf.default

%{_datadir}/squid/icons
%{_datadir}/squid/mib.txt
%lang(bg) %{_datadir}/squid/errors.Bulgarian
%lang(cs) %{_datadir}/squid/errors.Czech
%lang(da) %{_datadir}/squid/errors.Danish
%lang(nl) %{_datadir}/squid/errors.Dutch
%{_datadir}/squid/errors.English
%lang(et) %{_datadir}/squid/errors.Estonian
%lang(fi) %{_datadir}/squid/errors.Finnish
%lang(fr) %{_datadir}/squid/errors.French
%lang(de) %{_datadir}/squid/errors.German
%lang(hu) %{_datadir}/squid/errors.Hungarian
%lang(it) %{_datadir}/squid/errors.Italian
%lang(ja) %{_datadir}/squid/errors.Japanese
%lang(ko) %{_datadir}/squid/errors.Korean
%lang(pl) %{_datadir}/squid/errors.Polish
%lang(pt) %{_datadir}/squid/errors.Portuguese
%lang(ro) %{_datadir}/squid/errors.Romanian
%lang(ru) %{_datadir}/squid/errors.Russian-1251
%lang(ru) %{_datadir}/squid/errors.Russian-koi8-r
%lang(zh) %{_datadir}/squid/errors.Simplify_Chinese
%lang(sk) %{_datadir}/squid/errors.Slovak
%lang(es) %{_datadir}/squid/errors.Spanish
%lang(sv) %{_datadir}/squid/errors.Swedish
%lang(zh) %{_datadir}/squid/errors.Traditional_Chinese
%lang(tr) %{_datadir}/squid/errors.Turkish

%attr(750,root,root) %dir %{_libexecdir}
%attr(750,root,root) %{_libexecdir}/*.pl
%attr(750,root,root) %{_libexecdir}/contrib
%attr(750,root,root) %dir %{_libexecdir}/auth_modules

%attr(770,root,squid) %dir /var/log/archiv/squid
%attr(770,root,squid) %dir /var/log/squid
%attr(660,root,squid) %ghost /var/log/squid/*

%attr(770,root,squid) %dir /var/cache/squid

%files cachemgr
%defattr(644,root,root,755)
%attr(755,root,root) /home/httpd/cgi-bin/*

%files ldap_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/auth_modules/%{name}_ldap_auth
%attr(644,root,root) %{_mandir}/man8/%{name}_ldap_auth.*
%doc auth_modules/LDAP/*.gz

%files pam_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/auth_modules/pam_auth
%doc auth_modules/PAM/*.gz

%files smb_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/auth_modules/smb_auth
%doc auth_modules/SMB/*.gz
