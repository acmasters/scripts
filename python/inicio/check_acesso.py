import requests

from requests.auth import HTTPBasicAuth
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# defining the api-endpoint 
ENDPOINT = "http://visitante.acesso.uol.com.br/login.html"

def consulta_status(user, pwd):
    if ((requests.get(ENDPOINT,  auth=HTTPBasicAuth('user', 'pwd'),
    timeout=1.00)).status_code) == 200:
        registry = CollectorRegistry()
        g = Gauge('acesso_ok', 'OK - Autenticacao URL visitante.acesso.uol.com.br', registry=registry)
        g.set_to_current_time()
        push_to_gateway('http://pushgateway.qa.uh.aws.mail.sys.intranet:9091', job='check_acesso', registry=registry)
    else:
        registry = CollectorRegistry()
        g = Gauge('acesso_fora', 'ERRO - Autenticacao URL visitante.acesso.uol.com.br', registry=registry)
        g.set_to_current_time()
        push_to_gateway('http://pushgateway.qa.uh.aws.mail.sys.intranet:9091', job='check_acesso', registry=registry)


if __name__ == "__main__":
    consulta_status("rabuchaim","jul1nh4U0L" )