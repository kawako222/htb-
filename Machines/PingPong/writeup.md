axmi222 …/htb/Machines/PingPong   main ?   09:13  
❯ nmap -sC -sV -p 53,88,135,139,389,445,464,593,636,3268,3269,5985,9389 10.129.47.232 -Pn
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-01 09:14 -0600
Nmap scan report for 10.129.47.232
Host is up (0.0038s latency).

PORT     STATE    SERVICE          VERSION
53/tcp   open     domain           (generic dns response: NOTIMP)
88/tcp   filtered kerberos-sec
135/tcp  filtered msrpc
139/tcp  filtered netbios-ssn
389/tcp  filtered ldap
445/tcp  filtered microsoft-ds
464/tcp  filtered kpasswd5
593/tcp  filtered http-rpc-epmap
636/tcp  filtered ldapssl
3268/tcp filtered globalcatLDAP
3269/tcp filtered globalcatLDAPssl
5985/tcp filtered wsman
9389/tcp filtered adws
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.99%I=7%D=5/1%Time=69F4C362%P=x86_64-pc-linux-gnu%r(DNSSt
SF:atusRequestTCP,E,"\0\x0c\0\0\x90\x84\0\0\0\0\0\0\0\0");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.20 seconds

axmi222 …/htb/Machines/PingPong   main ?   09:14  
❯ dig @10.129.47.232 SOA .


; <<>> DiG 9.20.22-1-Debian <<>> @10.129.47.232 SOA .
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47110
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;.                              IN      SOA

;; ANSWER SECTION:
.                       21616   IN      SOA     a.root-servers.net. nstld.verisign-grs.com. 2026043002 1800 900 604800 86400

;; Query time: 12 msec
;; SERVER: 10.129.47.232#53(10.129.47.232) (UDP)
;; WHEN: Fri May 01 09:17:03 CST 2026
;; MSG SIZE  rcvd: 103

                                                                                                                    

axmi222 …/htb/Machines/PingPong   main ?   09:17  
❯ dig @10.129.47.232 NS . 

;; communications error to 10.129.47.232#53: timed out
;; communications error to 10.129.47.232#53: timed out
;; communications error to 10.129.47.232#53: timed out

; <<>> DiG 9.20.22-1-Debian <<>> @10.129.47.232 NS .
; (1 server found)
;; global options: +cmd
;; no servers could be reached
                                                                                                                    

axmi222 …/htb/Machines/PingPong   main ?   09:17  
❯ dig @10.129.47.232 axfr ping.htb


; <<>> DiG 9.20.22-1-Debian <<>> @10.129.47.232 axfr ping.htb
; (1 server found)
;; global options: +cmd
; Transfer failed.
