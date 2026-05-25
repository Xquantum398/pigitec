import httpx
from mediaflow_proxy.main import app as mediaflow_app

# Mediaflow'un kullandığı varsayılan client'ı özelleştirilmiş bir client ile değiştir
# (mediaflow'un iç yapısına göre bu değişebilir)
CUSTOM_HEADERS = {"Referer": "https://inattv1308.xyz/"}

# httpx client'ı oluştur
client = httpx.AsyncClient(headers=CUSTOM_HEADERS)

# mediaflow_app.state'a atayabilirsiniz, ya da mediaflow'un bağımlılıklarını monkeypatch yapabilirsiniz
mediaflow_app.state.http_client = client
