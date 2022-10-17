import requests


def total(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum


def max_value_in_list(arr):
    max_value = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value


def test_total_issue():
    resp = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
    code = resp.status_code
    assert code == 200, "Code doesn't match"

    json_response = resp.json()

    list_issues = []
    for issues in json_response:
        # print(issues["open_issues_count"])
        list_issues.append(issues["open_issues_count"])

    # Q1: How many total open issues are there across all repositories?

    print("total open issues are there across all repositories", total(list_issues))


def test_sort_repo():
    resp = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
    code = resp.status_code
    assert code == 200, "Code doesn't match"

    json_response = resp.json()

    list_updated = []

    for days in json_response:
        list_updated.append(days["updated_at"])
    print(list_updated)


def test_watcher_view():
    resp = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
    code = resp.status_code
    assert code == 200, "Code doesn't match"

    json_response = resp.json()
    max_watcher = []
    for i in json_response:
        max_watcher.append(i["watchers"])
        print("Repo: %s , watcher is %d" % (i["name"], i["watchers"]))

    print("the most watchers", max_value_in_list(max_watcher))
