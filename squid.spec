%define	calamaris_ver	2.24

Summary:	SQUID Internet Object Cache
Summary(pl):	Uniwersalny proxy-cache
Name:		squid
Version:	2.2.STABLE3
Release:	1
Copyright:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://squid.nlanr.net/pub/Squid/squid-2/%{name}-%{version}-src.tar.gz
Source1:	%{name}-1.1.19-faq.tar.gz
Source2:	%{name}.init
Source3:	http://www.detmold.netsurf.de/homepages/cord/tools/squid/calamaris/calamaris-%{calamaris_ver}.tar.gz
Source4:	%{name}.crontab
Source5:	fix.pl
Source6:	%{name}.conf
Source7:	http://cache.is.co.za/squid-docs.tar.gz
Source8:	calamaris.crontab
Source9:	%{name}.sysconfig
Patch0:		%{name}-2.0-make.patch
Patch1:		%{name}-perl.patch
PAtch2:		squid-linux.patch
BuildPrereq:	autoconf
BuildPrereq:	perl
BuildRoot:	/tmp/%{name}-%{version}-root
Prereq:		/sbin/chkconfig
Requires:	crontabs

%define		_libexecdir	%{_libdir}/%{name}
%define		_sysconfdir	/etc/%{name}

%description
Squid is a high-performance proxy caching server for web clients, supporting
FTP, gopher, and HTTP data objects. Unlike traditional caching software,
Squid handles all requests in a single, non-blocking, I/O-driven process.

Squid keeps meta data and especially hot objects cached in RAM, caches DNS
lookups, supports non-blocking DNS lookups, and implements negative caching
of failed requests. If you are tight on memory, check out the NOVM version
of this package.

Squid supports SSL, extensive access controls, and full request logging. By
using the lightweight Internet Cache Protocol, Squid caches can be arranged
in a hierarchy or mesh for additional bandwidth savings.

Squid consists of a main server program squid, a Domain Name System lookup
program dnsserver, a program for retrieving FTP data ftpget, and some
management and client tools. When squid starts up, it spawns a configurable
number of dnsserver processes, each of which can perform a single, blocking
Domain Name System (DNS) lookup. This reduces the amount of time the cache
waits for DNS lookups.

Squid is derived from the ARPA-funded Harvest project.

%description -l pl
Squid jest wysoce wydajnym serwerem proxy-cache dla przegl±darek WWW,
klientów FTP i gopher. Squid przechowuje najczê¶ciej pobierane dane 
w pamiêci RAM i zapamiêtuje odwo³ania do DNS.
Squid oferuje wsparcie dla SSL, rozbudowan± kontrolê dostêpu oraz pe³ne
rejestrowanie pobieranych danych. Dziêki u¿yciu protoko³u ICP (Internet
Cache Protocol), serwer squid mo¿na ³±czyæ w hierarchiê, zwiêkszaj±c ich
efektywno¶æ.
Pakiet squid obejmuje: g³ówny program serwera squid, program
dostarczaj±cy informacji z DNS dnsserver, program odbieraj±cy dane FTP
ftpget, oraz pomocnicze programy do zarz±dzania.

Squid wywodzi siê ze sponsorowanego przez ARPA projektu Harvest.

%prep
%setup -q -a 1 -a 7 -a 3
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 

%build
install -d  $RPM_BUILD_DIR/%{name}-%{version}/errors/{English.Polish,tmp}
cd $RPM_BUILD_DIR/%{name}-%{version}/errors/English
for i in ERR* 
do awk '/BODY/,/\/BODY/ {print}' ../Polish/$i | sed 's/<BODY>/<HR>/g' | \
sed 's/<\/BODY>/<HR>/g' > ../tmp/$i 
cat $i ../tmp/$i > ../English.Polish/$i 
done 

cd ../English.Polish 
perl %{SOURCE5} +m ERR* 

cd ../..
pwd
autoconf
LDFLAGS="-s" ; export LDFLAGS
%configure \
	--localstatedir=/var \
	--enable-icmp \
	--enable-useragent-log \
	--enable-snmp \
	--enable-arp-acl \
	--enable-err-language=English.Polish \
	--enable-htcp \
	--enable-carp 

mv -f squid/* doc
make 

%install
rm -rf $RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT/home/httpd/cgi-bin \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,crontab.d,sysconfig} \
	$RPM_BUILD_ROOT/usr/{sbin,lib/squid,man/man1}

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT/etc/squid \
	localstatedir=$RPM_BUILD_ROOT/var

mv $RPM_BUILD_ROOT%{_bindir}/cachemgr.cgi $RPM_BUILD_ROOT/home/httpd/cgi-bin
mv $RPM_BUILD_ROOT%{_bindir}/squid $RPM_BUILD_ROOT%{_sbindir}/

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/squid
install %{SOURCE4} $RPM_BUILD_ROOT/etc/crontab.d/squid
install %{SOURCE8} $RPM_BUILD_ROOT/etc/crontab.d/calamaris
install %{SOURCE6} $RPM_BUILD_ROOT/etc/squid
install %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/squid

install calamaris-%{calamaris_ver}/calamaris $RPM_BUILD_ROOT%{_bindir}
install calamaris-%{calamaris_ver}/calamaris.1 $RPM_BUILD_ROOT%{_mandir}/man1

install scripts/*.pl $RPM_BUILD_ROOT%{_libdir}/squid

touch $RPM_BUILD_ROOT/var/log/squid/{access,cache,store}.log

rm -f $RPM_BUILD_ROOT%{_bindir}/R*

gzip -9nf README ChangeLog QUICKSTART \
	contrib/url-normalizer.pl contrib/rredir.pl contrib/user-agents.pl \
	$RPM_BUILD_ROOT%{_mandir}/man*/*

%post
/sbin/chkconfig --add squid

%preun
if [ -e /var/lock/sybsys/squid ]; then
    /etc/rc.d/init.d/squid stop >&2
fi

if [ $1 = 0 ]; then
    /sbin/chkconfig --del squid
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc faq/* README* ChangeLog* QUICKSTART* doc/*
%doc contrib/url-normalizer.pl* contrib/rredir.pl* 
%doc contrib/user-agents.pl*

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%dir /etc/squid

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/squid/squid.conf
%config %verify(not md5 mtime size) /etc/squid/mime.conf

/etc/squid/mib.txt
/etc/squid/mime.conf.default
/etc/squid/squid.conf.default

%dir /etc/squid/icons
/etc/squid/icons/*

%dir /etc/squid/errors
/etc/squid/errors/*

%attr(640,root,root) /etc/crontab.d/*

%attr(755,nobody,nobody) /home/httpd/cgi-bin/*

%attr(750,root,root) /etc/rc.d/init.d/squid
%attr(640,root,root) /etc/sysconfig/squid

%attr(750,root,root) %dir %{_libdir}/squid
%attr(750,root,root) %{_libdir}/squid/*

%attr(750,nobody,root) %dir /var/log/squid
%ghost %attr(644,nobody,nobody) /var/log/squid/*.log

%attr(700,nobody,nobody) %dir /var/spool/squid

%changelog
* Tue Jan 26 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.1-PATCH2-5d]
- rebuild against new kernel-2.2.0. 

* Thu Jan 21 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.1-PATCH2-4d]
- fixed files permissions,
- fixed init-script,
- another minor changes.

* Sun Jan 10 1999 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
  [2.1-PATCH2-2d]
- added manual 
- created mixed Polish-English errors 
- fixed directory permisions 

* Tue Oct 06 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [2.0-1d]
- spec modified for version 2.0 and PLD standards

* Sat Sep 05 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- do make packages conflict witch each other ;)
- removed squid-novm section (squid-novm is now build from its own spec)
- moved config dir to /etc/squid
- translations modified for pl
- built against glibc 2.1
- changed files permission
- added calamaris.pl for log processing
- added squid.log for logrotate

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- don't make packages conflict with each other...

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- added a proxy auth patch from Alex deVries <adevries@engsoc.carleton.ca>
- fixed initscripts

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- rebuilt for Manhattan

* Fri Mar 20 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.21/1.NOVM.21

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- updated the init script to use reconfigure option to restart squid instead
  of shutdown/restart (both safer and quicker)

* Sat Feb 07 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.20
- added the NOVM package and tryied to reduce the mess in the spec file

* Wed Jan 7 1998 Cristian Gafton <gafton@redhat.com>
- first build against glibc
- patched out the use of setresuid(), which is available only on kernels
  2.1.44 and later
