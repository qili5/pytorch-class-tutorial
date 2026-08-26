import requests

# Iowa Environmental Mesonet (IEM), hosted by Iowa State. No API key needed.
# IA_ASOS is the network of airport weather stations across Iowa.
API_URL = "https://mesonet.agron.iastate.edu/api/1/currents.json?network=IA_ASOS"

response = requests.get(API_URL)

print("Status Code:", response.status_code)
print(response.text[:500])
