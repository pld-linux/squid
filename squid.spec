# TODO
# - use /usr/lib/cgi-bin instead of /home/services
#
# Conditional build:
%bcond_with	combined_log	# enables apache-like combined log format
#
Summary:	SQUID Internet Object Cache
Summary(es):	proxy/cache para WWW/FTP/gopher
Summary(pl):	Uniwersalny serwer proxy-cache
Summary(pt_BR):	Cache Squid de objetos Internet
Summary(ru):	Squid - ËÜÛ ÏÂßÅËÔÏ× Internet
Summary(uk):	Squid - ËÅÛ ÏÂ'¤ËÔ¦× Internet
Summary(zh_CN):	SQUID ¸ßËÙ»º³å´úÀí·þÎñÆ÷
Name:		squid
Version:	2.6.STABLE5
Release:	0.6
Epoch:		7
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.squid-cache.org/Versions/v2/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	b9f2e3b2c9e2c44e0fb729bf8f26d945
# http://www.squid-cache.org/Doc/FAQ/FAQ.tar.gz
Source1:	%{name}-FAQ.tar.gz
# Source1-md5:	cb9a955f8cda9cc166e086fccd412a43
Source2:	%{name}.init
Source3:	%{name}.sysconfig
# http://squid-docs.sourceforge.net/latest/zip-files/book-full-html.zip
Source4:	%{name}-book-full-html.zip
# Source4-md5:	4f3b6dab1de9cbb847df89d8b417378a
Source5:	%{name}.conf.patch
Source6:	%{name}.logrotate
Source7:	%{name}.pamd
# Bug fixes from Squid home page, please include URL
# lets have fun - there is no patches... yet :)
# Other patches:
#Patch100:	http://www.sed.pl/~mrk/qos/%{name}_hit_miss_mark.patch
# http://lists.debian.org/debian-user-polish/2006/07/msg00213.html
Patch100:	%{name}_hit_miss_mark.patch
Patch101:	%{name}-fhs.patch
Patch102:	%{name}-location.patch
Patch103:	%{name}-domainmatch.patch
Patch104:	%{name}-libnsl_fixes.patch
Patch106:	%{name}-crash-on-ENOSPC.patch
Patch107:	%{name}-newssl.patch
Patch108:	%{name}-nolibs.patch
Patch109:	%{name}-more_FD-new.patch
Patch110:	%{name}-empty-referer.patch
Patch111:	%{name}-align.patch
Patch112:	%{name}-2.5.STABLE4-apache-like-combined-log.patch
Patch113:	%{name}-auth_on_acceleration.patch
Patch114:	%{name}-fd-config.patch
URL:		http://www.squid-cache.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cyrus-sasl-devel >= 2.1.0
BuildRequires:	db-devel
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires(post):	/bin/hostname
Requires(post):	fileutils
Requires(post):	findutils
Requires(post):	grep
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/lib/rpm/user_group.sh
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	rc-scripts >= 0.2.0
Requires:	setup >= 2.4.6
Provides:	group(squid)
Provides:	user(squid)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}
%define		_sysconfdir	/etc/%{name}
%define		_cgidir		/home/services/httpd/cgi-bin

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

%description -l es
Squid es un servidor proxy con caché de alto desempeño para clientes
web, soportando FTP, gopher y HTTP. Diferentemente de softwares
tradicionales de caché squid manipula todas las requisiciones en un
único proceso sin bloqueos, direccionado a E/S. Mantienen metadatos y
objetos frecuentemente pedidos en uno caché en memoria RAM. Hace caché
de resoluciones DNS, soporta resoluciones DNS sin bloqueo y implementa
un caché negativo de requisiciones que fallen. Si tiene poca memoria
da un vistazo en la versión NOVM de este paquete. También soporta SSL,
controles extensivos de acceso y registro (log) completo de las
requisiciones. Usando el ligero Protocolo de Caches Internet (ICP)
puede ser usado en una jerarquía de servidores para mayor ahorro de la
banda de comunicación. Está compuesto del programa squid (servidor
principal), del programa dnsserver (para resolución DNS), del programa
ftpget (para transmisiones ftp) y otras herramientas clientes y para
administración. Cuando squid se inicia, dispara un número configurable
de procesos dnsserver, cada uno pudiendo ejecutar solamente una
resolución DNS con poder de bloquear. Esto reduce el tiempo que el
caché espera por resoluciones DNS. Fue derivado del proyecto Harvest,
financiado por la ARPA.

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

%description -l pt_BR
O Squid é um servidor proxy com cache de alta performance para
clientes web, suportando FTP, gopher e HTTP. Diferentemente de
softwares tradicionais de cache o squid manipula todas as requisições
em um único processo sem bloqueios, direcionado a E/S.

Mantém meta dados e objetos freqüentemente pedidos num cache em
memória RAM. Faz cache de resoluções DNS, suporta resoluções DNS sem
bloqueio e implementa um cache negativo de requisições que falharem.
Se você tem pouca memória dê uma olhada na versão NOVM deste pacote.

Também suporta SSL, controles extensivos de acesso e registro (log)
completo das requisições. Usando o leve Protocolo de Caches Internet
(ICP) ele pode ser usado em uma hierarquia de servidores para maior
economia de banda de comunicação.

Ele consiste do programa squid (servidor principal), do programa
dnsserver (para resolução DNS), do programa ftpget (para transmissões
ftp) e outras ferramentas clientes e para gerenciamento. Quando o
squid é inicializado ele dispara um número configurável de processos
dnsserver, cada um podendo executar somente uma resolução DNS
bloqueante. Isto reduz o tempo que o cache espera por resoluções DNS.

Foi derivado do projeto Harvest, financiado pela ARPA.

%description -l ru
Squid - ÜÔÏ ×ÙÓÏËÏÐÒÏÉÚ×ÏÄÉÔÅÌØÎÙÊ ËÜÛÉÒÕÀÝÉÊ ÐÒÏËÓÉ-ÓÅÒ×ÅÒ ÄÌÑ
ËÌÉÅÎÔÏ× web, ÐÏÄÄÅÒÖÉ×ÁÀÝÉÊ ÏÂßÅËÔÙ ÄÁÎÎÙÈ ÔÉÐÁ FTP, gopher É HTTP. ÷
ÏÔÌÉÞÉÅ ÏÔ ÔÒÁÄÉÃÉÏÎÎÙÈ ËÜÛÉÒÕÀÝÉÈ ÐÒÏÇÒÁÍÍ, Squid ÏÂÒÁÂÁÔÙ×ÁÅÔ ×ÓÅ
ÚÁÐÒÏÓÙ ÐÒÉ ÐÏÍÏÝÉ ÏÄÎÏÇÏ ÎÅÂÌÏËÉÒÕÀÝÅÇÏÓÑ, ÕÐÒÁ×ÌÑÅÍÏÇÏ
××ÏÄÏÍ-×Ù×ÏÄÏÍ ÐÒÏÃÅÓÓÁ.

üÔÏÔ ÐÁËÅÔ ÉÍÅÅÔ ×ÓÔÒÏÅÎÎÕÀ ÐÏÄÄÅÒÖËÕ ÂÁÚÙ ÄÁÎÎÙÈ ÓÅÔÅ×ÙÈ ICMP-ÐÒÏÂ
(Netdb).

%description -l uk
Squid - ÃÅ ËÅÛÕÀÞÉÊ ÐÒÏËÓ¦-ÓÅÒ×ÅÒ ÄÌÑ web-ËÌ¦¤ÎÔ¦×, ÝÏ Ð¦ÄÔÒÉÍÕ¤
ÏÂ'¤ËÔÉ ÄÁÎÉÈ ÔÉÐÕ FTP, gopher ÔÁ HTTP. îÁ ×¦ÄÍ¦ÎÕ ×¦Ä ÔÒÁÄÉÃ¦ÊÎÉÈ
ËÅÛÕÀÞÉÈ ÐÒÏÇÒÁÍ, Squid ÏÂÒÏÂÌÑ¤ ×Ó¦ ÚÁÐÉÔÉ ÚÁ ÄÏÐÏÍÏÇÏÀ ÏÄÎÏÇÏ
ÎÅÂÌÏËÕÀÞÏÇÏ, ËÅÒÏ×ÁÎÏÇÏ ××ÏÄÏÍ-×É×ÏÄÏÍ ÐÒÏÃÅÓÕ.

ãÅÊ ÐÁËÅÔ ÍÁ¤ ×ÂÕÄÏ×ÁÎÕ Ð¦ÄÔÒÉÍËÕ ÂÁÚÉ ÄÁÎÉÈ ÍÅÒÅÖÅ×ÉÈ ICMP-ÐÒÏÂ
(Netdb).

%package cachemgr
Summary:	CGI script for Squid management
Summary(pl):	Skrypt CGI do zarz±dzania Squidem przez WWW
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	webserver

%description cachemgr
Cachemgr.cgi is a CGI script that allows administrator to chceck
various informations about Squid via WWW.

%description cachemgr -l pl
Cachemgr.cgi jest skryptem CGI, który pozwala administratorowi
zapoznaæ siê z informacjami o pracy Squida poprzez WWW.

%package ldap_auth
Summary:	LDAP authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania LDAP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ldap_auth
This Squid helper allows authentication against LDAP directories using
the "simple authentication" (plain-text).

%description ldap_auth -l pl
Pakiet ten pozwala na uwierzytelnianie przez LDAP za pomoc± prostego
uwierzytelniania (otwartym tekstem).

%package pam_auth
Summary:	PAM authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania PAM dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.77.3

%description pam_auth
This program authenticates users against a PAM configured
authentication service "squid". This allows you to authenticate Squid
users to any authentication source for which you have a PAM module.

%description pam_auth -l pl
Program ten pozwala na uwierzytelnianie u¿ytkowników squida w dowolnym
¼ródle posiadaj±cym modu³ PAM.

%package smb_auth
Summary:	SMB authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania SMB dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description smb_auth
This is a proxy authentication module. With smb_auth you can
authenticate proxy users against an SMB server like Windows NT or
Samba.

%description smb_auth -l pl
To jest modu³ uwierzytelniania proxy. Przy pomocy smb_auth mo¿na
uwierzytelniaæ u¿ytkowników proxy na serwerach SMB, jak Windows NT czy
Samba.

%package msnt_auth
Summary:	MSNT domain authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania w domenie MSNT dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description msnt_auth
This is an authentication module for the Squid proxy server to
authenticate users on an NT domain.

%description msnt_auth -l pl
Jest to modu³ uwierzytelniania proxy, który pozwala na
uwierzytelnianie u¿ytkowników proxy w domenie NT.

%package yp_auth
Summary:	YP authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania YP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description yp_auth
This is an authentication module for the Squid proxy server to
authenticate users on YP.

%description yp_auth -l pl
Jest to modu³ uwierzytelniania proxy, który pozwala na
uwierzytelnianie u¿ytkowników proxy poprzez YP.

%package ncsa_auth
Summary:	NCSA httpd style authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania NCSA httpd dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ncsa_auth
This module uses a NCSA httpd style password file for authentication.

%description ncsa_auth -l pl
Modu³ uwierzytelniania proxy u¿ywaj±cy pliku hase³ jak w NCSA httpd.

%package sasl_auth
Summary:	SASL authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania SASL dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sasl_auth
This is an authentication module for the Squid proxy server to
authenticate users via SASL.

%description sasl_auth -l pl
Jest to modu³ uwierzytelniania proxy, który pozwala na
uwierzytelnianie u¿ytkowników proxy poprzez SASL.

%package getpwname_auth
Summary:	getpwname authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania getpwname dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description getpwname_auth
This is an authentication module for the Squid proxy server to
authenticate users using getpwname.

%description getpwname_auth -l pl
Jest to modu³ uwierzytelniania proxy, który pozwala na
uwierzytelnianie u¿ytkowników proxy poprzez getpwname.

%package passwd_auth
Summary:	passwd authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania passwd dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description passwd_auth
This is an authentication module for the Squid proxy server to
authenticate users with separate passwd file.

%description passwd_auth -l pl
Jest to modu³ uwierzytelniania proxy, który pozwala na
uwierzytelnianie u¿ytkowników proxy poprzez oddzielny plik passwd.

%package ntlm_auth
Summary:	NTLM authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania NTLM dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ntlm_auth
This is an authentication module for the Squid proxy server to
authenticate users on NTLM.

%description ntlm_auth -l pl
Jest to modu³ uwierzytelniania proxy, który pozwala na
uwierzytelnianie u¿ytkowników proxy poprzez NTLM.

%package digest_ldap_auth
Summary:	LDAP authentication helper for Squid
Summary(pl):	Obs³uga uwierzytelniania LDAP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description digest_ldap_auth
This is an authentication module for the Squid proxy server to
authenticate users on LDAP.

%description digest_ldap_auth -l pl
Jest to modu³ uwierzytelniania proxy, który pozwala na
uwierzytelnianie u¿ytkowników proxy poprzez LDAP.

%package ip_acl
Summary:	IP external ACL helper for Squid
Summary(pl):	Wsparcie kontroli dostêpu przez IP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ip_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on IP address.

%description ip_acl -l pl
Jest to modu³ kontroli dostêpu (ACL) do proxy, który pozwala na
ograniczenie dostêpu u¿ytkowników proxy na podstawie ich adresu IP.

%package ldap_acl
Summary:	LDAP group external ACL helper for Squid
Summary(pl):	Wsparcie kontroli dostêpu przez grupy LDAP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ldap_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on LDAP group membership.

%description ldap_acl -l pl
Jest to modu³ kontroli dostêpu (ACL) do proxy, który pozwala na
ograniczenie dostêpu u¿ytkowników proxy na podstawie ich
przynale¿no¶ci do grup LDAP.

%package unix_acl
Summary:	UNIX group external ACL helper for Squid
Summary(pl):	Wsparcie kontroli dostêpu przez grupy UNIX dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description unix_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on UNIX group membership.

%description unix_acl -l pl
Jest to modu³ kontroli dostêpu (ACL) do proxy, który pozwala na
ograniczenie dostêpu u¿ytkowników proxy na podstawie ich
przynale¿no¶ci do grup UNIX.

%package wbinfo_acl
Summary:	NT domain group external ACL helper for Squid
Summary(pl):	Wsparcie kontroli dostêpu przez grupy w domenie NT dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description wbinfo_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on NT domain group membership using wbinfo.

%description wbinfo_acl -l pl
Jest to modu³ kontroli dostêpu (ACL) do proxy, który pozwala na
ograniczenie dostêpu u¿ytkowników proxy na podstawie ich
przynale¿no¶ci do grup w domenie NT przy u¿yciu wbinfo.

%package session_acl
Summary:	Squid session tracking external acl group helper
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description session_acl
This  helper maintains a concept of sessions by monitoring requests and
timing out sessions if no requests have been seen for the idle  timeout
timer.

%package scripts
Summary:	Perl scripts for Squid
Summary(pl):	Skrypty perlowe dla Squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description scripts
This package contains Perl scripts and contributed programs for Squid.

%description scripts -l pl
Ten pakiet zawiera skrypty perlowe i dodatkowe programy dla Squida.

%prep
%setup -q -a1 -a4
# Bug fixes from Squid home page:

# Other patches:
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
#%patch104 -p1	--needs fix
%patch106 -p1
%patch107 -p1
#%patch108 -p1	--needs fix
%patch109 -p1
%patch110 -p1
%patch111 -p1
%{?with_combined_log:%patch112 -p1}
%patch113 -p1
%patch114 -p1

%{__sed} -i -e '1s#!.*bin/perl#!%{__perl}#' {contrib,scripts,helpers/*/*}/*.pl

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--datadir=%{_datadir}/squid \
	--enable-storeio="aufs,coss,diskd,null,ufs" \
	--enable-removal-policies="heap,lru" \
	--enable-icmp \
	--enable-delay-pools \
	--enable-useragent-log \
	--enable-referer-log \
	--enable-kill-parent-hack \
	--enable-forward-log \
	--enable-multicast-miss \
	--enable-snmp \
	--enable-arp-acl \
	--enable-htcp \
	--enable-ssl \
	--enable-forw-via-db \
	--enable-cache-digests \
	--enable-err-language=English \
	--enable-coss-aio-ops \
	--enable-linux-netfilter \
	--enable-large-cache-files \
	--enable-auth="basic,digest,negotiate,ntlm" \
	--enable-basic-auth-helpers="LDAP,MSNT,NCSA,PAM,SASL,SMB,YP,getpwnam,multi-domain-NTLM" \
	--enable-digest-auth-helpers="ldap,password" \
	--enable-external-acl-helpers="ip_user,ldap_group,session,unix_group,wbinfo_group" \
	--enable-ntlm-auth-helpers="SMB,fakeauth,no_check" \
	--enable-ntlm-fail-open \
	--enable-x-accelerator-vary \
	--enable-follow-x-forwarded-for	\
	--localstatedir=/var \
	--sysconfdir=%{_sysconfdir} \
	--with-auth-on-acceleration \
	--with-pthreads \
	--enable-fd-config \
	--with-maxfd=32768

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_cgidir} \
	$RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,security,sysconfig,logrotate.d} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_libexecdir}/contrib} \
	$RPM_BUILD_ROOT%{_mandir}/man8 \
	$RPM_BUILD_ROOT%{_datadir}/squid \
	$RPM_BUILD_ROOT/var/{cache,log{,/archiv}}/squid

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a contrib/*.pl $RPM_BUILD_ROOT%{_libexecdir}/contrib
install scripts/*.pl $RPM_BUILD_ROOT%{_libexecdir}

install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/squid
touch $RPM_BUILD_ROOT/etc/security/blacklist.squid

mv -f $RPM_BUILD_ROOT%{_libdir}/squid/cachemgr.cgi $RPM_BUILD_ROOT%{_cgidir}

cd $RPM_BUILD_ROOT/etc/squid
cp -f squid.conf{,.default}
patch -p0 < %{SOURCE5}
cd -

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/squid
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/squid
install %{SOURCE6} $RPM_BUILD_ROOT/etc/logrotate.d/squid

touch $RPM_BUILD_ROOT/var/log/squid/{access,cache,store}.log

# These two files start squid. They are replaced by /etc/rc.d/init.d script.
rm -f $RPM_BUILD_ROOT%{_bindir}/R*

# cp, to have re-entrant install
rm -rf docs
cp -a doc docs
# dunno why, but manual is not installed
mv docs/squid.8 $RPM_BUILD_ROOT%{_mandir}/man8
# We don't want Makefiles as docs...
rm -f docs/Makefile*

# We don't like message: rpm found unpackaged files ...
rm -f $RPM_BUILD_ROOT/etc/squid/msntauth.conf.default \
	$RPM_BUILD_ROOT/etc/squid/squid.conf.orig

> $RPM_BUILD_ROOT/var/cache/squid/netdb_state
> $RPM_BUILD_ROOT/var/cache/squid/swap.state
> $RPM_BUILD_ROOT/var/cache/squid/swap.state.clean
> $RPM_BUILD_ROOT/var/cache/squid/swap.state.last-clean

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 91 squid
%useradd -o -u 91 -s /bin/false -g squid -c "SQUID http caching daemon" -d /var/cache/squid squid
%addusertogroup stats squid

[ -L %{_datadir}/squid/errors ] && rm -f %{_datadir}/squid/errors || :

%post
if ! grep -q "^visible_hostname" /etc/squid/squid.conf; then
	hostname=`/bin/hostname -f 2>/dev/null` || hostname='localhost'
	echo visible_hostname $hostname >> /etc/squid/squid.conf
fi

/sbin/chkconfig --add squid
if [ "$1" = "1" ]; then
	/sbin/service squid init >&2
fi
%service squid restart

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del squid
	%service squid stop

	# nuke squid cache if uninstalling
	rm -rf /var/cache/squid/??
fi

%postun
if [ "$1" = "0" ]; then
	%userremove squid
	%groupremove squid
fi

%triggerpostun -- squid < 7:2.5.STABLE7-5
%addusertogroup stats squid

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS COPYRIGHT CREDITS README ChangeLog QUICKSTART RELEASENOTES.html SPONSORS
%doc docs/* src/mib.txt FAQ*.html book-full.html
%attr(755,root,root) %{_bindir}/squidclient
%attr(755,root,root) %{_bindir}/cossdump
%attr(755,root,root) %{_libexecdir}/diskd-daemon
# YES, it has to be suid root, it sends ICMP packets.
%attr(4754,root,squid) %{_libexecdir}/pinger
%attr(755,root,root) %{_libexecdir}/unlinkd
%attr(755,root,root) %{_libexecdir}/fakeauth_auth
%attr(755,root,root) %{_sbindir}/*

%attr(755,root,root) %dir %{_sysconfdir}

%attr(754,root,root) /etc/rc.d/init.d/squid
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/squid
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/squid
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/squid.conf
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mime.conf
%attr(640,root,root) %{_sysconfdir}/mime.conf.default
%attr(640,root,root) %{_sysconfdir}/squid.conf.default

%dir %{_datadir}/squid
%dir %{_datadir}/squid/errors
%{_datadir}/squid/icons
%{_datadir}/squid/mib.txt
%lang(az) %{_datadir}/squid/errors/Azerbaijani
%lang(bg) %{_datadir}/squid/errors/Bulgarian
%lang(ca) %{_datadir}/squid/errors/Catalan
%lang(cs) %{_datadir}/squid/errors/Czech
%lang(da) %{_datadir}/squid/errors/Danish
%lang(nl) %{_datadir}/squid/errors/Dutch
%{_datadir}/squid/errors/English
%lang(et) %{_datadir}/squid/errors/Estonian
%lang(fi) %{_datadir}/squid/errors/Finnish
%lang(fr) %{_datadir}/squid/errors/French
%lang(de) %{_datadir}/squid/errors/German
%lang(el) %{_datadir}/squid/errors/Greek
%lang(he) %{_datadir}/squid/errors/Hebrew
%lang(hu) %{_datadir}/squid/errors/Hungarian
%lang(it) %{_datadir}/squid/errors/Italian
%lang(ja) %{_datadir}/squid/errors/Japanese
%lang(ko) %{_datadir}/squid/errors/Korean
%lang(lt) %{_datadir}/squid/errors/Lithuanian
%lang(pl) %{_datadir}/squid/errors/Polish
%lang(pt) %{_datadir}/squid/errors/Portuguese
%lang(ro) %{_datadir}/squid/errors/Romanian
%lang(ru) %{_datadir}/squid/errors/Russian-1251
%lang(ru) %{_datadir}/squid/errors/Russian-koi8-r
%lang(zh_CN) %{_datadir}/squid/errors/Simplify_Chinese
%lang(sk) %{_datadir}/squid/errors/Slovak
%lang(es) %{_datadir}/squid/errors/Spanish
%lang(sr) %{_datadir}/squid/errors/Serbian
%lang(sv) %{_datadir}/squid/errors/Swedish
%lang(zh_TW) %{_datadir}/squid/errors/Traditional_Chinese
%lang(tr) %{_datadir}/squid/errors/Turkish

%attr(755,root,root) %dir %{_libexecdir}

%attr(770,root,squid) %dir /var/log/archiv/squid
%attr(770,root,squid) %dir /var/log/squid
%attr(660,root,squid) %ghost /var/log/squid/*

%attr(770,root,squid) %dir /var/cache/squid
%ghost /var/cache/squid/netdb_state
%ghost /var/cache/squid/swap.state
%ghost /var/cache/squid/swap.state.clean
%ghost /var/cache/squid/swap.state.last-clean
%{_mandir}/man8/squid.8*

%files cachemgr
%defattr(644,root,root,755)
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cachemgr.conf
%attr(755,root,root) %{_cgidir}/*
%{_mandir}/man8/cachemgr.cgi.8*

%files ldap_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/LDAP/README
%attr(755,root,root) %{_libexecdir}/%{name}_ldap_auth
%{_mandir}/man8/%{name}_ldap_auth.*

%files pam_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/PAM/pam_auth.c
%config(noreplace) /etc/pam.d/squid
%config(noreplace) /etc/security/blacklist.squid
%attr(755,root,root) %{_libexecdir}/pam_auth
%{_mandir}/man8/pam_auth.8*

%files smb_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/SMB/{README,ChangeLog,smb_auth.sh}
%doc helpers/basic_auth/multi-domain-NTLM/*
%attr(755,root,root) %{_libexecdir}/smb_auth*

%files msnt_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/MSNT/README*
%attr(755,root,root) %{_libexecdir}/msnt_auth
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/msntauth.conf

%files yp_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/yp_auth

%files ncsa_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ncsa_auth
%{_mandir}/man8/ncsa_auth.8*

%files sasl_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/SASL/{README,squid_sasl*}
%attr(755,root,root) %{_libexecdir}/sasl_auth

%files getpwname_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/getpwname_auth

%files passwd_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/digest_pw_auth

%files ntlm_auth
%defattr(644,root,root,755)
%doc helpers/ntlm_auth/no_check/{README*,no_check.pl}
%attr(755,root,root) %{_libexecdir}/ntlm_auth

%files digest_ldap_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/digest_ldap_auth

%files ip_acl
%defattr(644,root,root,755)
%doc helpers/external_acl/ip_user/{README,example*}
%attr(755,root,root) %{_libexecdir}/ip_user_check

%files ldap_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/squid_ldap_group
%{_mandir}/man8/%{name}_ldap_group.*

%files unix_acl
%defattr(644,root,root,755)
%doc helpers/external_acl/unix_group/README
%attr(755,root,root) %{_libexecdir}/squid_unix_group
%{_mandir}/man8/%{name}_unix_group.*

%files wbinfo_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/wbinfo_group.pl

%files session_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/squid_session
%{_mandir}/man8/%{name}_session.8*

%files scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/*.pl
%attr(755,root,root) %{_libexecdir}/contrib
