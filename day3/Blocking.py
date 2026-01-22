import time

def fetch_data():
    print("Fetching data...")
    time.sleep(3)   # BLOCKING
    print("Data fetched")

print("Start")
fetch_data()
print("End")
