import requests

WAKATIME_API_ENDPOINT = "https://api.wakatime.com//api/v1/users/current/all_time_since_today"
WAKATIME_API_KEY = "waka_e3dec692-24d8-4624-a61f-5e283d172ebd"

def get_wakatime_metrics():
    headers = {"Authorization": f"Bearer {WAKATIME_API_KEY}"}
    response = requests.get(WAKATIME_API_ENDPOINT, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch WakaTime metrics. Status code: {response.status_code}")
        return None

def update_readme_with_metrics(metrics):
    with open("README.md", "r") as f:
        readme_content = f.read()

    if "<!--START_SECTION:waka-->" in readme_content and "<!--END_SECTION:waka-->" in readme_content:
        start_marker = "<!--START_SECTION:waka-->"
        end_marker = "<!--END_SECTION:waka-->"

        metrics_data = f"Total Coding Time: {metrics['total_coding_time']} hours\n"  # Replace this with the actual metrics format

        new_readme_content = (
            readme_content.split(start_marker)[0]
            + start_marker
            + "\n"
            + metrics_data
            + "\n"
            + end_marker
            + readme_content.split(end_marker)[1]
        )

        with open("README.md", "w") as f:
            f.write(new_readme_content)

def main():
    metrics = get_wakatime_metrics()

    if metrics:
        update_readme_with_metrics(metrics)

if __name__ == "__main__":
    main()

