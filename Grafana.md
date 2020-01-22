## Grafana
##### grafana on docker
```
https://grafana.com/docs/installation/docker/
```
##### script
```
$ docker run \
  -d \
  -p 3000:3000 \
  --name=grafana \
  -e "GF_SERVER_ROOT_URL=http://grafana.server.name" \
  -e "GF_SECURITY_ADMIN_PASSWORD=9527" \
  grafana/grafana
```
##### 設定連線到postgresql或elasticsearch
```
#host必須選擇container ip, 而非localhost:5432
```

##### Grafana 連接 Postgresql
```
#1.timestamp不能有null值
#2.資料型態要正確
#3.table 不能用graph繪圖
```
##### Grafana 連接 Elastic
```
#1.index選項必須加[ ], for ex:[p1*]
```
##### Grafana reset password
```
grafana-cli --homepath "/usr/share/grafana" admin reset-admin-password admin

http://localhost:3000/login/generic_oauth
```
##### Grafana Login with Oauth2
```
#config
[auth]
signout_redirect_url =  https://openamlab.pouchen.com/openam/logout?goto=http://localhost:3000/login/generic_oauth

[auth.generic_oauth]
enabled = true
name = OAuth
allow_sign_up = true
client_id = DON
client_secret = 12345
scopes = openid uid pccuid profile
email_attribute_name = email:primary
auth_url = https://openamlab.pouchen.com:443/openam/oauth2/authorize
token_url = https://openamlab.pouchen.com:443/openam/oauth2/access_token
api_url = https://openamlab.pouchen.com:443/openam/oauth2/userinfo
allowed_domains = pouchen.com
team_ids =
allowed_organizations =
tls_skip_verify_insecure = true
tls_client_cert =
tls_client_key =
tls_client_ca =
#http://localhost:3000/login/generic_oauth

; Set to true to enable sending client_id and client_secret via POST body instead of Basic authentication HTTP header
; This might be required if the OAuth provider is not RFC6749 compliant, only supporting credentials passed via POST payload
send_client_credentials_via_post = false
```

##### Grafana
```
# The ip address to bind to, empty will bind to all interfaces
http_addr = 172.23.181.193

# The http port  to use
http_port = 3000

# The public facing domain name used to access grafana from a browser
domain = 172.23.181.193
```

##### html
```
[panels]
# If set to true Grafana will allow script tags in text panels. Not recommended as it enable XSS vulnerabilities.
disable_sanitize_html = true

Netdata auto fresh
NETDATA.options.current.stop_updates_when_focus_is_lost = false;


```

##### strcture
```
.
├── Makefile
├── docker-compose.yml          # docker-compose file that
│                               # aggregates `prometheus`,
│                               # `node_exporter` and `grafana`.
│ 
├── grafana                     # Grafana config
│   ├── Dockerfile              # Dockerfile that adds config to the image
│   ├── config.ini              # Base configuration
│   ├── dashboards              # Pre-made dashboards
│   │   └── mydashboard.json    # Sample dashboard
│   └── provisioning            # Configuration for automatic provisioning at
│       │                       # grafana startup.
│       ├── dashboards          
│       │   └── all.yml         # Configuration about grafana dashboard provisioning
│       └── datasources
│           └── all.yml         # Configuration about grafana data sources provisioning
│ 
└── prometheus                  # Prometheus config
    ├── Dockerfile
    └── config.yml
```

##### html panel
```
[panels]   
│# If set to true Grafana will allow script tags in text panels. Not recommended as i$
disable_sanitize_html = true   

```
                                                                          
