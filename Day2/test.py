import requests

url = "https://api.github.com/repos/vaibhav-gammaEdge/Backend-Development-Terminal-Fundamentals"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Repository Name:", data["name"])
print("Owner Username:", data["owner"]["login"])
print("Stars:", data["stargazers_count"])
print("Forks:", data["forks_count"])
