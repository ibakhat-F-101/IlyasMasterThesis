# Reverse Proxy Setup
The reverse proxy implementation was done with NGINX. Basic authentication has been added to it to enhance the security of the services. At the moment, all services with the exception of nextcloud work with the authentication. To locally setup the reverse proxy, add the following line to your ```/etc/hosts``` file. 

```sh
10.10.13.12  bitwarden.micropole.com mattermost.micropole.com nextcloud.micropole.com jitsi.micropole.com invoiceninja.micropole.com syncthing.micropole.com drawio.micropole.com codimd.micropole.com logseq.micropole.com
```
