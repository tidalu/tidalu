import requests

# Replace these placeholders with your WakaTime API details
WAKATIME_API_ENDPOINT = "https://api.wakatime.com//api/v1/users/current/all_time_since_today"
WAKATIME_API_KEY = "waka_bbc93713-bf4b-4b73-b59c-18dd00494464"

# Function to fetch WakaTime metrics from the API
def get_wakatime_metrics():
    headers = {"Authorization": f"Bearer {WAKATIME_API_KEY}"}
    response = requests.get(WAKATIME_API_ENDPOINT, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch WakaTime metrics. Status code: {response.status_code}")
        return None

# Function to update the README.md file with the fetched metrics
def update_readme_with_metrics(metrics):
    with open("README.md", "r") as f:
        readme_content = f.read()

    # Parse the fetched metrics and update the corresponding sections in README.md
    # Modify this part according to your desired format and content
    # For example, update a section with total coding time:
    total_coding_time = metrics["data"][0]["grand_total"]["digital"]
    new_readme_content = readme_content.replace("<!--TOTAL_CODING_TIME-->", f"Total Coding Time: {total_coding_time}")

    with open("README.md", "w") as f:
        f.write(new_readme_content)

def main():
    # Fetch the WakaTime metrics from the API
    metrics = get_wakatime_metrics()

    if metrics:
        # Update the README.md with the fetched metrics
        update_readme_with_metrics(metrics)

if __name__ == "__main__":
    main()
