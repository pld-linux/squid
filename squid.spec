# TODO
# - REVIEW patches and configuration
# - ZPH TOS -
# For this to work correctly, you will need to patch your linux
# kernel with the TOS preserving ZPH patch.
# The kernel patch can be downloaded from http://zph.bratcheda.org
#
# Conditional build:
%bcond_with	combined_log	# enables apache-like combined log format
#
Summary:	SQUID Internet Object Cache
Summary(es.UTF-8):	proxy/cache para WWW/FTP/gopher
Summary(pl.UTF-8):	Uniwersalny serwer proxy-cache
Summary(pt_BR.UTF-8):	Cache Squid de objetos Internet
Summary(ru.UTF-8):	Squid - кэш объектов Internet
Summary(uk.UTF-8):	Squid - кеш об'єктів Internet
Summary(zh_CN.UTF-8):	SQUID 高速缓冲代理服务器
Name:		squid
Version:	3.5.20
Release:	1
Epoch:		7
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.squid-cache.org/Versions/v3/3.5/%{name}-%{version}.tar.xz
# Source0-md5:	48fb18679a30606de98882528beab3a7
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	http://squid-docs.sourceforge.net/latest/zip-files/book-full-html.zip
# Source3-md5:	4f3b6dab1de9cbb847df89d8b417378a
Source4:	%{name}.conf.patch
Source5:	%{name}.logrotate
Source6:	%{name}.pamd
Source7:	%{name}-cachemgr-apache.conf
Source8:	%{name}.tmpfiles
Source9:	%{name}-cachemgr-httpd.conf
Source10:	%{name}.service
Source11:	%{name}-check_cache
Patch0:		%{name}-fhs.patch
Patch1:		%{name}-location.patch
Patch2:		%{name}-crash-on-ENOSPC.patch
Patch4:		%{name}-2.5.STABLE4-apache-like-combined-log.patch
Patch5:		%{name}-ppc-m32.patch
Patch6:		%{name}-cachemgr-webapp.patch
# still needed? http://bugs.squid-cache.org/show_bug.cgi?id=3806
# http://www.squid-cache.org/mail-archive/squid-dev/201207/att-0177/squidv3-vary-headers-shm-hack.patch
Patch7:		squidv3-vary-headers-shm-hack.patch
Patch8:		ecap-1p0-t2.patch
URL:		http://www.squid-cache.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cppunit-devel
BuildRequires:	cyrus-sasl-devel >= 2.1.0
BuildRequires:	db-devel
BuildRequires:	expat-devel
BuildRequires:	heimdal-devel
BuildRequires:	libcap-devel >= 1:2.09
BuildRequires:	libecap-devel >= 1
BuildRequires:	libltdl-devel
BuildRequires:	libnetfilter_conntrack-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.671
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	unzip
BuildRequires:	xz
Requires(post):	/bin/hostname
Requires(post):	fileutils
Requires(post):	findutils
Requires(post):	grep
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/lib/rpm/user_group.sh
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre,triggerpostun):	/bin/id
Requires(pre,triggerpostun):	/usr/sbin/usermod
Requires(post,preun,postun):	systemd-units >= 38
Requires:	rc-scripts >= 0.2.0
Requires:	setup >= 2.4.6
Requires:	systemd-units >= 38
Provides:	group(squid)
# epoll enabled by default:
Requires:	uname(release) >= 2.6
# TPROXYv4 (v2 disabled b/c it breaks v4)
#Suggests:	uname(release) >= 2.6.28.3
Provides:	user(squid)
Conflicts:	logrotate < 3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		cachemgr
%define		_libexecdir	%{_libdir}/%{name}
%define		_sysconfdir	/etc/%{name}
%define		_cgidir		%{_prefix}/lib/cgi-bin/%{_webapp}

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
Summary(pl.UTF-8):	Skrypt CGI do zarządzania Squidem przez WWW
Group:		Applications/WWW
# does not require squid locally
Requires:	group(http)
Requires:	webapps
Requires:	webserver
Requires:	webserver(access)
Requires:	webserver(alias)
Requires:	webserver(cgi)
Conflicts:	apache-base < 2.4.0-1

%description cachemgr
Cachemgr.cgi is a CGI script that allows administrator to check
various informations about Squid via WWW.

%description cachemgr -l pl.UTF-8
Cachemgr.cgi jest skryptem CGI, który pozwala administratorowi
zapoznać się z informacjami o pracy Squida poprzez WWW.

%package kerberos_auth
Summary:	Authentication via the Negotiate RFC 4559 for proxies
Summary(pl.UTF-8):	Uwierzytelnianie przez negocjację RFC 4559 dla serwerów proxy
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	squid-kerb_auth = %{epoch}:%{version}-%{release}
Obsoletes:	squid-kerb_auth < %{epoch}:%{version}-%{release}

%description kerberos_auth
This squid helper is a reference implementation that supports
authentication via the Negotiate RFC 4559 for proxies. It decodes RFC
2478 SPNEGO GSS-API tokens from IE7 either through helper functions or
via SPNEGO supporting Kerberos libraries and RFC 1964 Kerberos tokens
from Firefox on Linux.

%description kerberos_auth -l pl.UTF-8
Pakiet ten jest implementacją uwierzytelniania przez negocjacji RFC
4559 dla serwerów proxy. Dekoduje żetony SPNEGO GSS-API RFC 2478 z IE7
poprzez funkcje pomocnicze lub przez biblioteki Kerberos wspierające
SPNEGO i żetony Kerberos RFC 1964 z Firefoksa w Linuksie.

%package ldap_auth
Summary:	LDAP authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania LDAP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ldap_auth
This Squid helper allows authentication against LDAP directories using
the "simple authentication" (plain-text).

%description ldap_auth -l pl.UTF-8
Pakiet ten pozwala na uwierzytelnianie przez LDAP za pomocą prostego
uwierzytelniania (otwartym tekstem).

%package pam_auth
Summary:	PAM authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania PAM dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.77.3

%description pam_auth
This program authenticates users against a PAM configured
authentication service "squid". This allows you to authenticate Squid
users to any authentication source for which you have a PAM module.

%description pam_auth -l pl.UTF-8
Program ten pozwala na uwierzytelnianie użytkowników squida w dowolnym
źródle posiadającym moduł PAM.

%package smb_auth
Summary:	SMB authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania SMB dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description smb_auth
This is a proxy authentication module. With smb_auth you can
authenticate proxy users against an SMB server like Windows NT or
Samba.

%description smb_auth -l pl.UTF-8
To jest moduł uwierzytelniania proxy. Przy pomocy smb_auth można
uwierzytelniać użytkowników proxy na serwerach SMB, jak Windows NT czy
Samba.

%package msnt_auth
Summary:	MSNT domain authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania w domenie MSNT dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description msnt_auth
This is an authentication module for the Squid proxy server to
authenticate users on an NT domain.

%description msnt_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy w domenie NT.

%package nis_auth
Summary:	NIS authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania NIS dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	squid-yp_auth = %{epoch}:%{version}-%{release}
Obsoletes:	squid-yp_auth < %{epoch}:%{version}-%{release}

%description nis_auth
This is an authentication module for the Squid proxy server to
authenticate users on NIS.

%description nis_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez NIS.

%package ncsa_auth
Summary:	NCSA httpd style authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania NCSA httpd dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ncsa_auth
This module uses a NCSA httpd style password file for authentication.

%description ncsa_auth -l pl.UTF-8
Moduł uwierzytelniania proxy używający pliku haseł jak w NCSA httpd.

%package sasl_auth
Summary:	SASL authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania SASL dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sasl_auth
This is an authentication module for the Squid proxy server to
authenticate users via SASL.

%description sasl_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez SASL.

%package getpwname_auth
Summary:	getpwname authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania getpwname dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description getpwname_auth
This is an authentication module for the Squid proxy server to
authenticate users using getpwname.

%description getpwname_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez getpwname.

%package passwd_auth
Summary:	passwd authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania passwd dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description passwd_auth
This is an authentication module for the Squid proxy server to
authenticate users with separate passwd file.

%description passwd_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez oddzielny plik passwd.

%package ntlm_auth
Summary:	NTLM authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania NTLM dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ntlm_auth
This is an authentication module for the Squid proxy server to
authenticate users on NTLM.

%description ntlm_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez NTLM.

%package radius_auth
Summary:	RADIUS authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania RADIUS dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description radius_auth
This helper allows Squid to connect to a RADIUS server to validate the
user name and password of Basic HTTP authentication.

%description radius_auth -l pl.UTF-8
Program ten pozwala na uwierzytelnianie użytkowników squida przez
serwer RADIUS.

%package db_auth
Summary:	Database authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania przez bazę danych dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	perl-DBI
Suggests:	perl-DBD-mysql

%description db_auth
This is an authentication module for the Squid proxy server to
authenticate users againsta a database.

%description db_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez bazę danych.

%package pop3_auth
Summary:	POP3 authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania POP3 dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description pop3_auth
This is an authentication module for the Squid proxy server to
authenticate users on POP3.

%description pop3_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez POP3.

%package negotiate_wrapper_auth
Summary:	Kerberos authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania Kerberos dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-kerberos_auth = %{epoch}:%{version}-%{release}
Requires:	%{name}-ntlm_auth = %{epoch}:%{version}-%{release}

%description negotiate_wrapper_auth
This is an authentication module for the Squid proxy server to
authenticate users on Kerberos.

%description negotiate_wrapper_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez Kerberosa.

%package digest_edirectory_auth
Summary:	eDirectory authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania eDirectory dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description digest_edirectory_auth
This is an authentication module for the Squid proxy server to
authenticate users on eDirectory.

%description digest_edirectory_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez eDirectory.

%package digest_ldap_auth
Summary:	LDAP authentication helper for Squid
Summary(pl.UTF-8):	Obsługa uwierzytelniania LDAP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description digest_ldap_auth
This is an authentication module for the Squid proxy server to
authenticate users on LDAP.

%description digest_ldap_auth -l pl.UTF-8
Jest to moduł uwierzytelniania proxy, który pozwala na
uwierzytelnianie użytkowników proxy poprzez LDAP.

%package ip_acl
Summary:	IP external ACL helper for Squid
Summary(pl.UTF-8):	Wsparcie kontroli dostępu przez IP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ip_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on IP address.

%description ip_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich adresu IP.

%package ldap_acl
Summary:	LDAP group external ACL helper for Squid
Summary(pl.UTF-8):	Wsparcie kontroli dostępu przez grupy LDAP dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ldap_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on LDAP group membership.

%description ldap_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich
przynależności do grup LDAP.

%package unix_acl
Summary:	UNIX group external ACL helper for Squid
Summary(pl.UTF-8):	Wsparcie kontroli dostępu przez grupy UNIX dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description unix_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on UNIX group membership.

%description unix_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich
przynależności do grup UNIX.

%package wbinfo_acl
Summary:	NT domain group external ACL helper for Squid
Summary(pl.UTF-8):	Wsparcie kontroli dostępu przez grupy w domenie NT dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description wbinfo_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on NT domain group membership using wbinfo.

%description wbinfo_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich
przynależności do grup w domenie NT przy użyciu wbinfo.

%package session_acl
Summary:	Squid session tracking external ACL group helper
Summary(pl.UTF-8):	Wsparcie kontroli dostępu przez śledzenie sesji
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description session_acl
This helper maintains a concept of sessions by monitoring requests and
timing out sessions if no requests have been seen for the idle timeout
timer.

%description session_acl -l pl.UTF-8
Moduł oparty na koncepcji sesji, śledzący zapytania i wygaszający
sesje jeśli w określonym czasie nie widziano w ich obrębie kolejnych
zapytań.

%package edirectory_userip_acl
Summary:	Squid eDirectory IP Lookup Helper
Summary(pl.UTF-8):	Wsparcie kontroli dostępu przez eDirectory
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description edirectory_userip_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on IP address lookup in eDirectory.

%description edirectory_userip_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich adresu IP
popranego z eDirectory.

%package kerberos_ldap_group_acl
Summary:	Squid LDAP external acl group helper for Kerberos or NTLM credentials
Summary(pl.UTF-8):	Wsparcie kontroli dostępu przez grupy LDAP/Kerberos/NTLM dla squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kerberos_ldap_group_acl
This is an external ACL module for the Squid proxy server to limit
access for users based on LDAP Kerberos or NTLM credentials.

%description kerberos_ldap_group_acl -l pl.UTF-8
Jest to moduł kontroli dostępu (ACL) do proxy, który pozwala na
ograniczenie dostępu użytkowników proxy na podstawie ich uprawnień
Kerberosowych lub NTLM-owych w LDAP.

%package sql_session_acl
Summary:	SQL Database session lookup helper for Squid
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description sql_session_acl
Validates an HTTP requests access authorization with a session
database.

%package time_quota_acl
Summary:	Squid time quota external acl helper
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description time_quota_acl
This extension allows an administrator to define time budgets for the
users of squid to limit the time using squid.

%package log_db_daemon
Summary:	Database logging daemon for Squid
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description log_db_daemon
This program writes Squid access.log entries to a database. Presently
only accepts the squid native format.

%package storeid_file_rewrite
Summary:	File based Store-ID helper for Squid
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description storeid_file_rewrite
This program acts as a store_id helper program, rewriting URLs passed
by Squid into storage-ids that can be used to achieve better caching
for websites that use different URLs for the same content.

%package scripts
Summary:	Perl scripts for Squid
Summary(pl.UTF-8):	Skrypty perlowe dla Squida
Group:		Networking/Admin
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description scripts
This package contains Perl scripts and contributed programs for Squid.

%description scripts -l pl.UTF-8
Ten pakiet zawiera skrypty perlowe i dodatkowe programy dla Squida.

%prep
%setup -q -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{?with_combined_log:%patch4 -p1}
%ifarch ppc
%patch5 -p1
%endif
%patch6 -p1
#%patch7 -p1
#%patch8 -p0

%{__sed} -i -e '1s#!.*bin/perl#!%{__perl}#' {contrib,scripts}/*.pl

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-strict-error-checking \
	--with-default-user=squid \
	--with-logdir=/var/log/squid \
	--with-swapdir=/var/cache/squid \
	--with-pidfile=/var/run/squid.pid \
	--datadir=%{_datadir}/squid \
	--enable-arp-acl \
	--enable-auth \
	--enable-basic-auth-helpers \
	--enable-ntlm-auth-helpers \
	--enable-negotiate-auth-helpers \
	--enable-digest-auth-helpers \
	--enable-external-acl-helpers \
	--enable-url-rewrite-helpers \
	--enable-ntlm-fail-open \
	--enable-cache-digests \
	--enable-coss-aio-ops \
	--enable-delay-pools \
	--enable-err-language=English \
	--enable-esi \
	--enable-follow-x-forwarded-for	\
	--enable-forward-log \
	--enable-forw-via-db \
	--enable-htcp \
	--enable-wccp \
	--enable-wccpv2 \
	--enable-icap-client \
	--enable-ecap \
	--enable-icmp \
	--enable-kill-parent-hack \
	--enable-large-cache-files \
	--enable-linux-netfilter \
	--disable-linux-tproxy \
	--enable-multicast-miss \
	--enable-referer-log \
	--enable-removal-policies="heap,lru" \
	--enable-storeio="aufs,diskd,rock,ufs" \
	--enable-storeid-rewrite-helpers="file" \
	--enable-snmp \
	--enable-ssl \
	--enable-ipv6 \
	--enable-useragent-log \
	--enable-x-accelerator-vary \
	--localstatedir=/var \
	--sysconfdir=%{_sysconfdir} \
	--with-auth-on-acceleration \
	--with-large-files \
	--with-maxfd=32768 \
	--with-pthreads \
	--with-openssl \
	--without-nettle \
	--enable-zph-qos

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_cgidir},%{_webapps}/%{_webapp}} \
	$RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,security,sysconfig,logrotate.d} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_libexecdir}/contrib} \
	$RPM_BUILD_ROOT%{_mandir}/man8 \
	$RPM_BUILD_ROOT%{_datadir}/squid \
	$RPM_BUILD_ROOT/var/{cache,log{,/archive}}/squid \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir} \
	$RPM_BUILD_ROOT%{systemdunitdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__cp} -a contrib/*.pl $RPM_BUILD_ROOT%{_libexecdir}/contrib
install scripts/*.pl $RPM_BUILD_ROOT%{_libexecdir}

install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/squid
touch $RPM_BUILD_ROOT/etc/security/blacklist.squid

install %{SOURCE8} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/squid.conf

%{__mv} -f $RPM_BUILD_ROOT%{_libdir}/squid/cachemgr.cgi $RPM_BUILD_ROOT%{_cgidir}
%{__cp} -a %{SOURCE7} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/apache.conf
%{__cp} -a %{SOURCE9} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/httpd.conf
%{__rm} $RPM_BUILD_ROOT%{_webapps}/%{_webapp}/cachemgr.conf.default

cd $RPM_BUILD_ROOT/etc/squid
%{__patch} -p0 < %{SOURCE4}
%{__rm} *.default squid.conf.documented
cd -

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/squid
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/squid
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/squid

touch $RPM_BUILD_ROOT/var/log/squid/{access,cache,store}.log

%{__rm} $RPM_BUILD_ROOT%{_datadir}/squid/errors/{COPYRIGHT,TRANSLATORS}

# cp, to have re-entrant install
%{__rm} -rf docs
%{__cp} -a doc docs
# We don't want Makefiles as docs...
%{__rm} docs/Makefile*

:> $RPM_BUILD_ROOT/var/cache/squid/netdb_state
:> $RPM_BUILD_ROOT/var/cache/squid/swap.state
:> $RPM_BUILD_ROOT/var/cache/squid/swap.state.clean
:> $RPM_BUILD_ROOT/var/cache/squid/swap.state.last-clean

%{__sed} -e 's|@@LIBEXECDIR@@|%{_libexecdir}|g' %{SOURCE10} >$RPM_BUILD_ROOT%{systemdunitdir}/squid.service
cp -p %{SOURCE11} $RPM_BUILD_ROOT%{_libexecdir}/squid-check_cache

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
%systemd_post squid.service

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del squid
	%service squid stop

	# nuke squid cache if uninstalling
	rm -rf /var/cache/squid/??
fi
%systemd_preun squid.service

%postun
if [ "$1" = "0" ]; then
	%userremove squid
	%groupremove squid
fi
%systemd_reload

%triggerpostun -- squid < 7:2.5.STABLE7-5
%addusertogroup stats squid

%triggerpostun -- squid < 7:3.4.7-2
%systemd_trigger squid.service

%triggerin cachemgr -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun cachemgr -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin cachemgr -- apache-base
%webapp_register httpd %{_webapp}

%triggerun cachemgr -- apache-base
%webapp_unregister httpd %{_webapp}

%triggerpostun -- cachemgr < 7:3.0.STABLE10-0.2
if [ -f %{_sysconfdir}/cachemgr.conf.rpmsave ]; then
	cp -f %{_webapps}/%{_webapp}/cachemgr.conf{,.rpmsave}
	mv -f %{_sysconfdir}/cachemgr.conf.rpmsave %{_webapps}/%{_webapp}/cachemgr.conf
fi

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS CREDITS README ChangeLog QUICKSTART
%doc RELEASENOTES.html SPONSORS docs/* src/mib.txt book-full.html
%doc src/squid.conf.default src/squid.conf.documented src/mime.conf.default
%doc errors/TRANSLATORS
%attr(755,root,root) %{_bindir}/purge
%attr(755,root,root) %{_bindir}/squidclient

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/diskd
# YES, it has to be suid root, it sends ICMP packets.
%attr(4754,root,squid) %{_libexecdir}/pinger
%attr(755,root,root) %{_libexecdir}/unlinkd
%attr(755,root,root) %{_libexecdir}/ntlm_fake_auth
%attr(755,root,root) %{_libexecdir}/basic_fake_auth
%attr(755,root,root) %{_libexecdir}/ext_delayer_acl
%attr(755,root,root) %{_libexecdir}/url_fake_rewrite
%attr(755,root,root) %{_libexecdir}/url_fake_rewrite.sh
%attr(755,root,root) %{_libexecdir}/log_file_daemon
%attr(755,root,root) %{_libexecdir}/squid-check_cache
%attr(755,root,root) %{_sbindir}/squid

%attr(754,root,root) /etc/rc.d/init.d/squid
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/squid
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/squid

%dir %{_sysconfdir}
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/squid.conf
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mime.conf
%attr(640,root,squid) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/errorpage.css

%dir %{_datadir}/squid
%dir %{_datadir}/squid/errors
%{_datadir}/squid/icons
%{_datadir}/squid/mib.txt
%{_datadir}/squid/errors/templates
%lang(af) %{_datadir}/squid/errors/af
%lang(ar) %{_datadir}/squid/errors/ar
%lang(ar) %{_datadir}/squid/errors/ar-*
%lang(az) %{_datadir}/squid/errors/az
%lang(az) %{_datadir}/squid/errors/az-*
%lang(bg) %{_datadir}/squid/errors/bg
%lang(bg) %{_datadir}/squid/errors/bg-*
%lang(ca) %{_datadir}/squid/errors/ca
%lang(cs) %{_datadir}/squid/errors/cs
%lang(cs) %{_datadir}/squid/errors/cs-*
%lang(da) %{_datadir}/squid/errors/da
%lang(da) %{_datadir}/squid/errors/da-*
%lang(de) %{_datadir}/squid/errors/de
%lang(de) %{_datadir}/squid/errors/de-*
%lang(el) %{_datadir}/squid/errors/el
%lang(el) %{_datadir}/squid/errors/el-*
%{_datadir}/squid/errors/en
%{_datadir}/squid/errors/en-*
%lang(es) %{_datadir}/squid/errors/es
%lang(es) %{_datadir}/squid/errors/es-*
%lang(et) %{_datadir}/squid/errors/et
%lang(et) %{_datadir}/squid/errors/et-*
%lang(fa) %{_datadir}/squid/errors/fa
%lang(fa) %{_datadir}/squid/errors/fa-*
%lang(fi) %{_datadir}/squid/errors/fi
%lang(fi) %{_datadir}/squid/errors/fi-*
%lang(fr) %{_datadir}/squid/errors/fr
%lang(fr) %{_datadir}/squid/errors/fr-*
%lang(he) %{_datadir}/squid/errors/he
%lang(he) %{_datadir}/squid/errors/he-*
%lang(hu) %{_datadir}/squid/errors/hu
%lang(hu) %{_datadir}/squid/errors/hu-*
%lang(hy) %{_datadir}/squid/errors/hy
%lang(hy) %{_datadir}/squid/errors/hy-*
%lang(id) %{_datadir}/squid/errors/id
%lang(id) %{_datadir}/squid/errors/id-*
%lang(it) %{_datadir}/squid/errors/it
%lang(it) %{_datadir}/squid/errors/it-*
%lang(ja) %{_datadir}/squid/errors/ja
%lang(ja) %{_datadir}/squid/errors/ja-*
%lang(ka) %{_datadir}/squid/errors/ka
%lang(ka) %{_datadir}/squid/errors/ka-*
%lang(ko) %{_datadir}/squid/errors/ko
%lang(ko) %{_datadir}/squid/errors/ko-*
%lang(lt) %{_datadir}/squid/errors/lt
%lang(lt) %{_datadir}/squid/errors/lt-*
%lang(lv) %{_datadir}/squid/errors/lv
%lang(lv) %{_datadir}/squid/errors/lv-*
%lang(ms) %{_datadir}/squid/errors/ms
%lang(ms) %{_datadir}/squid/errors/ms-*
%lang(nl) %{_datadir}/squid/errors/nl
%lang(nl) %{_datadir}/squid/errors/nl-*
%lang(oc) %{_datadir}/squid/errors/oc
%lang(pl) %{_datadir}/squid/errors/pl
%lang(pl) %{_datadir}/squid/errors/pl-*
%lang(pt) %{_datadir}/squid/errors/pt
%lang(pt) %{_datadir}/squid/errors/pt-pt
%lang(pt_BR) %{_datadir}/squid/errors/pt-br
%lang(pt_BZ) %{_datadir}/squid/errors/pt-bz
%lang(ro) %{_datadir}/squid/errors/ro
%lang(ro) %{_datadir}/squid/errors/ro-*
%lang(ru) %{_datadir}/squid/errors/ru
%lang(ru) %{_datadir}/squid/errors/ru-*
%lang(sk) %{_datadir}/squid/errors/sk
%lang(sk) %{_datadir}/squid/errors/sk-*
%lang(sk) %{_datadir}/squid/errors/sl
%lang(sk) %{_datadir}/squid/errors/sl-*
%lang(sr) %{_datadir}/squid/errors/sr
%lang(sr) %{_datadir}/squid/errors/sr-*
%lang(sv) %{_datadir}/squid/errors/sv
%lang(sv) %{_datadir}/squid/errors/sv-*
%lang(th) %{_datadir}/squid/errors/th
%lang(th) %{_datadir}/squid/errors/th-*
%lang(tr) %{_datadir}/squid/errors/tr
%lang(tr) %{_datadir}/squid/errors/tr-*
%lang(uk) %{_datadir}/squid/errors/uk
%lang(uk) %{_datadir}/squid/errors/uk-*
%lang(uz) %{_datadir}/squid/errors/uz
%lang(vi) %{_datadir}/squid/errors/vi
%lang(vi) %{_datadir}/squid/errors/vi-*
%lang(zh_CN) %{_datadir}/squid/errors/zh-cn
%lang(zh_CN) %{_datadir}/squid/errors/zh-han*
%lang(zh_CN) %{_datadir}/squid/errors/zh-sg
%lang(zh_CN) %{_datadir}/squid/errors/zh-tw
%lang(zh_TW) %{_datadir}/squid/errors/zh-hk
%lang(zh_TW) %{_datadir}/squid/errors/zh-mo

%{systemdunitdir}/squid.service
%{systemdtmpfilesdir}/squid.conf
%attr(770,root,squid) %dir /var/run/squid

%attr(770,root,squid) %dir /var/log/archive/squid
%attr(770,root,squid) %dir /var/log/squid
%attr(660,root,squid) %ghost /var/log/squid/*

%attr(770,root,squid) %dir /var/cache/squid
%ghost /var/cache/squid/netdb_state
%ghost /var/cache/squid/swap.state
%ghost /var/cache/squid/swap.state.clean
%ghost /var/cache/squid/swap.state.last-clean
%{_mandir}/man1/squidclient.1*
%{_mandir}/man8/ext_delayer_acl.8*
%{_mandir}/man8/squid.8*

%files cachemgr
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_webapps}/%{_webapp}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_webapps}/%{_webapp}/cachemgr.conf
%dir %{_cgidir}
%attr(755,root,root) %{_cgidir}/cachemgr.cgi
%{_mandir}/man8/cachemgr.cgi.8*

%files ldap_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/basic_ldap_auth
%{_mandir}/man8/basic_ldap_auth.*

%files pam_auth
%defattr(644,root,root,755)
%config(noreplace) /etc/pam.d/squid
%config(noreplace) /etc/security/blacklist.squid
# it has to be suid root to access /etc/shadow
%attr(4755,root,root) %{_libexecdir}/basic_pam_auth
%{_mandir}/man8/basic_pam_auth.8*

%files smb_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/SMB/ChangeLog
%attr(755,root,root) %{_libexecdir}/basic_smb_lm_auth
%attr(755,root,root) %{_libexecdir}/basic_smb_auth*

%files msnt_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/basic_msnt_multi_domain_auth
%{_mandir}/man8/basic_msnt_multi_domain_auth.8*

%files nis_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/basic_nis_auth

%files ncsa_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/basic_ncsa_auth
%{_mandir}/man8/basic_ncsa_auth.8*

%files sasl_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/SASL/basic_sasl_auth.{conf,pam}
%attr(755,root,root) %{_libexecdir}/basic_sasl_auth
%{_mandir}/man8/basic_sasl_auth.8*

%files getpwname_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/basic_getpwnam_auth
%{_mandir}/man8/basic_getpwnam_auth.8*

%files passwd_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/digest_file_auth
%{_mandir}/man8/digest_file_auth.8*

%files kerberos_auth
%defattr(644,root,root,755)
%doc helpers/negotiate_auth/kerberos/README
%attr(755,root,root) %{_libexecdir}/negotiate_kerberos_auth
%attr(755,root,root) %{_libexecdir}/negotiate_kerberos_auth_test
%{_mandir}/man8/negotiate_kerberos_auth.8*

%files ntlm_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ntlm_smb_lm_auth

%files radius_auth
%defattr(644,root,root,755)
%doc helpers/basic_auth/RADIUS/README
%attr(755,root,root) %{_libexecdir}/basic_radius_auth
%{_mandir}/man8/basic_radius_auth.8*

%files digest_ldap_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/digest_ldap_auth

%files db_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/basic_db_auth
%{_mandir}/man8/basic_db_auth.8*

%files pop3_auth
%defattr(644,root,root,755)
%{_libexecdir}/basic_pop3_auth
%{_mandir}/man8/basic_pop3_auth.8*

%files digest_edirectory_auth
%defattr(644,root,root,755)
%{_libexecdir}/digest_edirectory_auth

%files negotiate_wrapper_auth
%defattr(644,root,root,755)
%{_libexecdir}/negotiate_wrapper_auth

%files ip_acl
%defattr(644,root,root,755)
%doc helpers/external_acl/file_userip/example*
%attr(755,root,root) %{_libexecdir}/ext_file_userip_acl
%{_mandir}/man8/ext_file_userip_acl.*

%files ldap_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ext_ldap_group_acl
%{_mandir}/man8/ext_ldap_group_acl.*

%files unix_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ext_unix_group_acl
%{_mandir}/man8/ext_unix_group_acl.*

%files wbinfo_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ext_wbinfo_group_acl
%{_mandir}/man8/ext_wbinfo_group_acl.8*

%files session_acl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/ext_session_acl
%{_mandir}/man8/ext_session_acl.8*

%files edirectory_userip_acl
%defattr(644,root,root,755)
%{_libexecdir}/ext_edirectory_userip_acl
%{_mandir}/man8/ext_edirectory_userip_acl.8*

%files kerberos_ldap_group_acl
%defattr(644,root,root,755)
%{_libexecdir}/ext_kerberos_ldap_group_acl

%files sql_session_acl
%defattr(644,root,root,755)
%{_libexecdir}/ext_sql_session_acl
%{_mandir}/man8/ext_sql_session_acl.8*

%files time_quota_acl
%defattr(644,root,root,755)
%{_libexecdir}/ext_time_quota_acl
%{_mandir}/man8/ext_time_quota_acl.8*

%files log_db_daemon
%defattr(644,root,root,755)
%{_libexecdir}/log_db_daemon
%{_mandir}/man8/log_db_daemon.8*

%files storeid_file_rewrite
%defattr(644,root,root,755)
%{_libexecdir}/storeid_file_rewrite
%{_mandir}/man8/storeid_file_rewrite.8*

%files scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/contrib
%attr(755,root,root) %{_libexecdir}/AnnounceCache.pl
%attr(755,root,root) %{_libexecdir}/access-log-matrix.pl
%attr(755,root,root) %{_libexecdir}/cache-compare.pl
%attr(755,root,root) %{_libexecdir}/cachetrace.pl
%attr(755,root,root) %{_libexecdir}/calc-must-ids.pl
%attr(755,root,root) %{_libexecdir}/cert_tool
%attr(755,root,root) %{_libexecdir}/cert_valid.pl
%attr(755,root,root) %{_libexecdir}/check_cache.pl
%attr(755,root,root) %{_libexecdir}/fileno-to-pathname.pl
%attr(755,root,root) %{_libexecdir}/find-alive.pl
%attr(755,root,root) %{_libexecdir}/flag_truncs.pl
%attr(755,root,root) %{_libexecdir}/helper-mux.pl
%attr(755,root,root) %{_libexecdir}/icpserver.pl
%attr(755,root,root) %{_libexecdir}/icp-test.pl
%attr(755,root,root) %{_libexecdir}/tcp-banger.pl
%attr(755,root,root) %{_libexecdir}/trace-job.pl
%attr(755,root,root) %{_libexecdir}/trace-master.pl
%attr(755,root,root) %{_libexecdir}/udp-banger.pl
%attr(755,root,root) %{_libexecdir}/upgrade-1.0-store.pl
