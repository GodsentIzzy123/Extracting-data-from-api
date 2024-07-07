import http.client
import ssl
import json
import csv

# Step 1: Fetch the data from the API and save it as a JSON file
# Establish an HTTPS connection to the API host with SSL verification disabled
context = ssl._create_unverified_context()
conn = http.client.HTTPSConnection("euro-20242.p.rapidapi.com", context=context)

# Set up the necessary headers with your API key and host information
headers = {
    'x-rapidapi-key': "0d7dd7de9cmsh09cdaf8a8a716b9p1968ebjsn936e3ca5e493",
    'x-rapidapi-host': "euro-20242.p.rapidapi.com"
}

# Send a GET request to the /players/topScorers endpoint
conn.request("GET", "/players/topScorers", headers=headers)

# Get the response from the API
res = conn.getresponse()
data = res.read()
json_data = json.loads(data.decode("utf-8"))

# Step 2: Write data to a JSON file
json_file = "top_scorers.json"

with open(json_file, mode='w', encoding="utf-8") as file:
    json.dump(json_data, file, indent=4)

#print(f"Data has been written to {json_file}")

# Step 3: Read the JSON file and write it to a CSV file
csv_file = "top_scorers.csv"

with open(json_file, mode='r', encoding="utf-8") as file:
    json_data = json.load(file)

# Assuming json_data is a list of JSON objects
top_scorers = json_data  # json_data is already the list

with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write the header row (adjust the field names based on your JSON structure)
    writer.writerow(["ID", "Name", "Goals", "Assists", "Appearances", "First Team Appearances", "Minutes Played", "Team Name"])

    # Write the data rows
    for scorer in top_scorers:
        writer.writerow([
            scorer["_id"],
            scorer["name"],
            scorer["goals"],
            scorer["assists"],
            scorer["appearances"],
            scorer["firstTeamAppearances"],
            scorer["minutesPlayed"],
            scorer["teamName"]
        ])

print(f"Data has been written to {csv_file}")