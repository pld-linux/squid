#
# Conditional build:
%bcond_with	esi	# build ESI support (www.esi.org)
#
Summary:	SQUID Internet Object Cache
Summary(es.UTF-8):   proxy/cache para www/ftp/gopher
Summary(pl.UTF-8):   Uniwersalny proxy-cache server
Summary(pt_BR.UTF-8):   Cache Squid de objetos Internet
Summary(ru.UTF-8):   Squid - кэш объектов Internet
Summary(uk.UTF-8):   Squid - кеш об'єктів Internet
Summary(zh_CN.UTF-8):   SQUID 高速缓冲代理服务器
Name:		squid
Version:	3.0
Release:	0.PRE3.0.1
Epoch:		6
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.squid-cache.org/Versions/v3/3.0/%{name}-%{version}-PRE3.tar.bz2
# Source0-md5:	f43e08e9aba72e5544910d86f88dc8b6
Source1:        %{name}-1.1.19-faq.tar.gz
# Source1-md5:  77d04ae621d19548797e3a0deb540df6
Source2:	%{name}.init
Source3:	%{name}.sysconfig
Source4:        http://cache.is.co.za/%{name}-docs.tar.gz
# Source4-md5:  0cfee556bf6394a0bd3c438c89dd2e63
Source5:	%{name}.conf.patch
Source6:	%{name}.logrotate
Source7:	%{name}.pamd
# Bug fixes from Squid home page:
Patch0:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-russian.patch
Patch1:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-resolver-length.patch
Patch2:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-extacl_auth.patch
Patch3:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-epoll-100cpu.patch
Patch4:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-originserver_port.patch
Patch5:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-digest_auth_pwchange.patch
Patch6:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-cachemgr_accel.patch
Patch7:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-pam_auth.patch
Patch8:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-fqdnnegcache.patch
Patch9:		http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-memidle.patch
Patch10:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-winbind.patch
Patch11:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-https_accel_doc.patch
Patch12:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-ftp_abort_closing.patch
Patch13:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-swapoutcbdata.patch
Patch14:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-PURIFY.patch
Patch15:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-cbdatadebugleak.patch
Patch16:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-httpversion.patch
Patch17:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-cossParsing.patch
Patch18:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-coss-options.patch
Patch19:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-debug-parsing.patch
Patch20:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-ufs-race.patch
Patch21:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-windows-dup2.patch
Patch22:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-mount-sys-detection.patch
Patch23:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-coss-postmerge.patch
Patch24:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-inprogressios.patch
Patch25:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-access_log_none.patch
Patch26:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-ncsa_auth_passwdfile.patch
Patch27:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-hugeobjects-detection.patch
Patch28:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-ssl-session-reuse.patch
Patch29:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-Solaris-gethostname.patch
Patch30:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-main-pid.patch
Patch31:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-endian-bracket.patch
Patch32:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-accel_cache_peer_name.patch
Patch33:	http://www.squid-cache.org/Versions/v3/3.0/bugs/squid-3.0.PRE3-pconn.patch
# Other patches:
Patch100:	%{name}-types.patch
Patch101:	%{name}-sasl.patch
BuildRequires:	autoconf
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7a
BuildRequires:	cyrus-sasl-devel >= 2.1.0
BuildRequires:	pam-devel
BuildRequires:	perl
PreReq:		rc-scripts >= 0.2.0
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post,preun):	/sbin/chkconfig
Requires(post):	fileutils
Requires(post):	findutils
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
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

%description -l es.UTF-8
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

%description -l pl.UTF-8
Squid jest wysoce wydajnym serwerem proxy-cache dla przeglądarek WWW,
klientów FTP i gopher. Squid przechowuje najczęściej pobierane dane w
pamięci RAM i zapamiętuje odwołania do DNS. Squid oferuje wsparcie dla
SSL, rozbudowaną kontrolę dostępu oraz pełne rejestrowanie pobieranych
danych. Dzięki użyciu protokołu ICP (Internet Cache Protocol), serwer
squid można łączyć w hierarchię, zwiększając ich efektywność. Pakiet
squid obejmuje: główny program serwera squid, program dostarczający
informacji z DNS dnsserver, program odbierający dane FTP ftpget, oraz
pomocnicze programy do zarządzania. Squid wywodzi się ze
sponsorowanego przez ARPA projektu Harvest.

%description -l pt_BR.UTF-8
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

%description -l ru.UTF-8
Squid - это высокопроизводительный кэширующий прокси-сервер для
клиентов web, поддерживающий объекты данных типа FTP, gopher и HTTP. В
отличие от традиционных кэширующих программ, Squid обрабатывает все
запросы при помощи одного неблокирующегося, управляемого
вводом-выводом процесса.

Этот пакет имеет встроенную поддержку базы данных сетевых ICMP-проб
(Netdb).

%description -l uk.UTF-8
Squid - це кешуючий проксі-сервер для web-клієнтів, що підтримує
об'єкти даних типу FTP, gopher та HTTP. На відміну від традиційних
кешуючих програм, Squid обробляє всі запити за допомогою одного
неблокуючого, керованого вводом-виводом процесу.

Цей пакет має вбудовану підтримку бази даних мережевих ICMP-проб
(Netdb).

%package cachemgr
Summary:	CGI script for Squid management
Summary(pl.UTF-8):   Skrypt CGI do zarządzania Squidem przez WWW
Group:		Networking/Admin
Requires:	%{name} = %{version}
Requires:	httpd

%description cachemgr
Cachemgr.cgi is a CGI script that allows administrator to chceck
various informations about Squid via WWW.

%description cachemgr -l pl.UTF-8
Cachemgr.cgi jest skryptem CGI, który pozwala administratorowi
zapoznać się z informacjami o pracy Squida poprzez WWW.

%package ldap_auth
Summary:	LDAP authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji LDAP dla squida
Group:		Networking/Admin
Requires:	%{name}

%description ldap_auth
This Squid helper allows authentication against LDAP directories using
the "simple authentication" (plain-text).

%description ldap_auth -l pl.UTF-8
Pakiet ten pozwala na autentykację LDAP za pomocą prostej autentykacji
(otwartym tekstem).

%package pam_auth
Summary:	PAM authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji PAM dla squida
Group:		Networking/Admin
Requires:	%{name}

%description pam_auth
This program authenticates users against a PAM configured
authentication service "squid". This allows you to authenticate Squid
users to any authentication source for which you have a PAM module.

%description pam_auth -l pl.UTF-8
Program ten pozwala na autentykację użytkowników squida w dowolnym
źródle posiadającym moduł PAM.

%package smb_auth
Summary:	SMB authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji SMB dla squida
Group:		Networking/Admin
Requires:	%{name}

%description smb_auth
This is a proxy authentication module. With smb_auth you can
authenticate proxy users against an SMB server like Windows NT or
Samba.

%description smb_auth -l pl.UTF-8
To jest moduł autentykacji proxy. Z smb_auth możesz autentyfikować
użytkowników proxy na serwerach SMB, jak Windows NT czy Samba.

%package msnt_auth
Summary:	MSNT domain authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji domen MSNT dla squida
Group:		Networking/Admin
Requires:	%{name}

%description msnt_auth
This is an authentication module for the Squid proxy server to 
authenticate users on an NT domain.

%description msnt_auth -l pl.UTF-8
Jest to moduł autentykacji proxy, który pozwala na autentyfikowanie
użytkowników proxy w domenie NT.

%package yp_auth
Summary:	YP authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji YP dla squida
Group:		Networking/Admin
Requires:	%{name}

%description yp_auth
This is an authentication module for the Squid proxy server to
authenticate users on YP.

%description yp_auth -l pl.UTF-8
Jest to moduł autentykacji proxy, który pozwala na autentyfikowanie
użytkowników proxy poprzez YP.

%package ncsa_auth
Summary:	NCSA httpd style authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji NCSA httpd dla squida
Group:		Networking/Admin
Requires:	%{name}

%description ncsa_auth
This module uses a NCSA httpd style password file for authentication.

%description ncsa_auth -l pl.UTF-8
Moduł autentykacji proxy używający pliku haseł jak w NCSA httpd.

%package sasl_auth
Summary:	SASL authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji SASL dla squida
Group:		Networking/Admin
Requires:	%{name}

%description sasl_auth
This is an authentication module for the Squid proxy server to
authenticate users via SASL.

%description sasl_auth -l pl.UTF-8
Jest to moduł autentykacji proxy, który pozwala na autentyfikowanie
użytkowników proxy poprzez SASL.

%package winbind_auth
Summary:	WINBIND authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji WINBIND dla squida
Group:		Networking/Admin
Requires:	%{name}

%description winbind_auth
This is an authentication module for the Squid proxy server to
authenticate users via WINBIND.

%description winbind_auth -l pl.UTF-8
Jest to moduł autentykacji proxy, który pozwala na autentyfikowanie
użytkowników proxy poprzez WINBIND.

%package getpwname_auth
Summary:	getpwname authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji getpwname dla squida
Group:		Networking/Admin
Requires:	%{name}

%description getpwname_auth
This is an authentication module for the Squid proxy server to
authenticate users using getpwname.

%description getpwname_auth -l pl.UTF-8
Jest to moduł autentykacji proxy, który pozwala na autentyfikowanie
użytkowników proxy poprzez getpwname.

%package passwd_auth
Summary:	passwd authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji passwd dla squida
Group:		Networking/Admin
Requires:	%{name}

%description passwd_auth
This is an authentication module for the Squid proxy server to
authenticate users with separate passwd file.

%description passwd_auth -l pl.UTF-8
Jest to moduł autentykacji proxy, który pozwala na autentyfikowanie
użytkowników proxy poprzez oddzielny plik passwd.

%package ntlm_auth
Summary:	NTLM authentication helper for Squid
Summary(pl.UTF-8):   Wsparcie autentykacji NTLM dla squida
Group:		Networking/Admin
Requires:	%{name}

%description ntlm_auth
This is an authentication module for the Squid proxy server to
authenticate users on NTLM.

%description ntlm_auth -l pl.UTF-8
Jest to moduł autentykacji proxy, który pozwala na autentyfikowanie
użytkowników proxy poprzez NTLM.

%package ip_acl
Summary:	IP external ACL helper for Squid
Summary(pl.UTF-8):   Wsparcie kontroli dostępu przez IP dla squida
Group:		Networking/Admin
Requires:	%{name}

%description ip_acl
This is an external ACL module for the Squid proxy server to
limit acces for users based on IP address.

%description ip_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich adresu IP.

%package ldap_acl
Summary:	LDAP group external ACL helper for Squid
Summary(pl.UTF-8):   Wsparcie kontroli dostępu przez grupy LDAP dla squida
Group:		Networking/Admin
Requires:	%{name}

%description ldap_acl
This is an external ACL module for the Squid proxy server to
limit acces for users based on LDAP group membership.

%description ldap_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich
przynależności do grup LDAP.

%package unix_acl
Summary:	UNIX group external ACL helper for Squid
Summary(pl.UTF-8):   Wsparcie kontroli dostępu przez grupy UNIX dla squida
Group:		Networking/Admin
Requires:	%{name}

%description unix_acl
This is an external ACL module for the Squid proxy server to
limit acces for users based on UNIX group membership.

%description unix_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich
przynależności do grup UNIX.

%package wbinfo_acl
Summary:	NT domain group external ACL helper for Squid
Summary(pl.UTF-8):   Wsparcie kontroli dostępu przez grupy w domenie NT dla squida
Group:		Networking/Admin
Requires:	%{name}

%description wbinfo_acl
This is an external ACL module for the Squid proxy server to
limit acces for users based on NT domain group membership using wbinfo.


%description wbinfo_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich
przynależności do grup w domenie NT przy użyciu wbinfo.

%package winbind_acl
Summary:	NT domain group external ACL helper for Squid
Summary(pl.UTF-8):   Wsparcie kontroli dostępu przez grupy w domenie NT dla squida
Group:		Networking/Admin
Requires:	%{name}

%description winbind_acl
This is an external ACL module for the Squid proxy server to
limit acces for users based on NT domain group membership
based on Samba Winbindd from Samba 2.2.4 or greater.

%description winbind_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich
przynależności do grup w domenie NT oparty na Samba Winbindd
z pakietu Samba 2.2.4 lub wyższego.

%prep
%setup -q -n %{name}-%{version}-PRE3 -a 1 -a 4

# Bug fixes from Squid home page:
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
#%patch13 -p1
#%patch14 -p1
%patch15 -p1
#%patch16 -p1
#%patch17 -p1
#%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
#%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
#%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1

# Other patches:
%patch100 -p1
%patch101 -p1

%build
%configure \
	--localstatedir=/var \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir}/squid \
	--enable-icmp \
	--enable-useragent-log \
	--enable-snmp \
	--enable-arp-acl \
	--enable-default-err-language=English \
	--enable-htcp \
	--enable-ssl \
	--enable-forw-via-db \
	--enable-cache-digests \
	--enable-storeio="aufs,coss,diskd,null,ufs" \
	--enable-removal-policies="lru heap" \
	--disable-ipf-transparent \
	--enable-delay-pools \
	--with-pthreads \
	--enable-auth="basic digest ntlm" \
	--enable-basic-auth-helpers="LDAP MSNT NCSA PAM SASL SMB YP getpwnam multi-domain-NTLM winbind" \
	--enable-ntlm-auth-helpers="SMB fakeauth no_check winbind" \
	--enable-digest-auth-helpers=password \
	--enable-external-acl-helpers="ip_user ldap_group unix_group wbinfo_group winbind_group" \
	--enable-x-accelerator-vary \
	--enable-linux-netfilter \
	--enable-delay-pools \
	%{?with_esi:--enable-esi} \
	--enable-large-files \
	--with-openssl
	

mv -f squid/* doc
%{__make}

perl -pi -e 's#/usr/.*bin/perl#/usr/bin/perl#g' contrib/*
perl -pi -e 's#/usr/.*bin/perl#/usr/bin/perl#g' scripts/*
find helpers/ -type f | xargs perl -pi -e 's#/usr/.*bin/perl#/usr/bin/perl#g'

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT/home/services/httpd/cgi-bin \
	$RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,security,sysconfig,logrotate.d} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_libexecdir}/contrib} \
	$RPM_BUILD_ROOT%{_mandir}/{man1,man8} \
	$RPM_BUILD_ROOT%{_datadir}/squid \
	$RPM_BUILD_ROOT/var/{cache,log{,/archiv}}/squid

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a contrib/*.pl $RPM_BUILD_ROOT%{_libexecdir}/contrib

install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/squid
touch $RPM_BUILD_ROOT/etc/security/blacklist.squid

mv -f $RPM_BUILD_ROOT%{_libdir}/squid/cachemgr.cgi $RPM_BUILD_ROOT/home/services/httpd/cgi-bin

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

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid squid`" ]; then
	if [ "`getgid squid`" != "91" ]; then
		echo "Error: group squid doesn't have gid=91. Correct this before installing squid." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 91 -r -f squid 1>&2 || :
fi
if [ -n "`id -u squid 2>/dev/null`" ]; then
	if [ "`id -u squid`" != "91" ]; then
		echo "Error: user squid doesn't have uid=91. Correct this before installing squid." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -M -o -r -u 91 -s /bin/false \
		-g squid -c "SQUID http caching daemon" -d /var/cache/squid squid 1>&2 || :
fi
[ -L %{_datadir}/squid/errors ] && rm -f %{_datadir}/squid/errors

%post
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
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/userdel squid
	/usr/sbin/groupdel squid
fi
				
%files
%defattr(644,root,root,755)
%doc faq CONTRIBUTORS COPYRIGHT CREDITS README
%doc ChangeLog QUICKSTART RELEASENOTES.html SPONSORS
%doc doc/*
%attr(755,root,root) %{_bindir}/squidclient
%attr(755,root,root) %{_libexecdir}/diskd
# YES, it has to be suid root, it sends ICMP packets.
%attr(4754,root,squid) %{_libexecdir}/pinger
%attr(755,root,root) %{_libexecdir}/unlinkd
%attr(755,root,root) %{_sbindir}/*

%attr(755,root,root) %dir %{_sysconfdir}

%attr(754,root,root) /etc/rc.d/init.d/squid
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/squid
%attr(640,root,squid) %config(noreplace) /etc/sysconfig/squid
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/squid.conf
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mime.conf
%attr(640,root,root) %{_sysconfdir}/mime.conf.default
%attr(640,root,root) %{_sysconfdir}/squid.conf.default

%dir %{_datadir}/squid
%dir %{_datadir}/squid/errors
%{_datadir}/squid/icons
%{_datadir}/squid/mib.txt
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
%lang(zh) %{_datadir}/squid/errors/Simplify_Chinese
%lang(sk) %{_datadir}/squid/errors/Slovak
%lang(es) %{_datadir}/squid/errors/Spanish
%lang(sr) %{_datadir}/squid/errors/Serbian
%lang(sv) %{_datadir}/squid/errors/Swedish
%lang(zh) %{_datadir}/squid/errors/Traditional_Chinese
%lang(tr) %{_datadir}/squid/errors/Turkish

%attr(755,root,root) %dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/*.pl
%attr(755,root,root) %{_libexecdir}/contrib

%attr(644,root,root) %{_mandir}/man8/squid.*

%attr(770,root,squid) %dir /var/log/archiv/squid
%attr(770,root,squid) %dir /var/log/squid
%attr(660,root,squid) %ghost /var/log/squid/*

%attr(770,root,squid) %dir /var/cache/squid

%files cachemgr
%defattr(644,root,root,755)
%attr(755,root,root) /home/services/httpd/cgi-bin/*

%files ldap_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/LDAP/README
%attr(755,root,root) %{_libexecdir}/%{name}_ldap_auth
%attr(644,root,root) %{_mandir}/man8/%{name}_ldap_auth.*

%files pam_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/PAM/pam_auth.c
%config(noreplace) /etc/pam.d/squid
%config(noreplace) /etc/security/blacklist.squid
%attr(755,root,root) %{_libexecdir}/pam_auth
%attr(644,root,root) %{_mandir}/man8/pam_auth.*

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

%files sasl_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/SASL/{README,squid_sasl*}
%attr(755,root,root) %{_libexecdir}/sasl_auth

%files winbind_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/wb_auth

%files getpwname_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/getpwname_auth

%files passwd_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/digest_pw_auth

%files ntlm_auth
%defattr(644,root,root,755)
%doc helpers/ntlm_auth/no_check/{README*,no_check.pl}
%attr(755,root,root) %{_libexecdir}/wb_ntlmauth
%attr(755,root,root) %{_libexecdir}/ntlm_auth
%attr(755,root,root) %{_libexecdir}/fakeauth_auth

%files ip_acl
%defattr(644,root,root,755)
%doc helpers/external_acl/ip_user/{README,example*}
%attr(755,root,root) %{_libexecdir}/ip_user_check

%files ldap_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/squid_ldap_group
%attr(644,root,root) %{_mandir}/man8/%{name}_ldap_group.*

%files unix_acl
%defattr(644,root,root,755)
%doc helpers/external_acl/unix_group/README
%attr(755,root,root) %{_libexecdir}/squid_unix_group
%attr(644,root,root) %{_mandir}/man8/%{name}_unix_group.*

%files wbinfo_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/wbinfo_group.pl

%files winbind_acl
%defattr(644,root,root,755)
%doc helpers/external_acl/winbind_group/readme.txt
%attr(755,root,root) %{_libexecdir}/wb_group
