from time import strptime

import requests
from datetime import datetime, date


def total(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum


def sort_date(date_list):
    date_list.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ"))
    return date_list


def sort_tuple(date_tuple):
    return sorted(date_tuple, key=lambda x: strptime(x[0], "%Y-%m-%dT%H:%M:%SZ"), reverse=True)


def get_max_value(tup):
    maximum = tup[0]
    for i in tup:
        if i[1] > maximum[1]:
            maximum = i
    return maximum


def test_total_issue():
    resp = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
    code = resp.status_code
    assert code == 200, "Code doesn't match"

    json_response = resp.json()

    list_issues = []
    for issues in json_response:
        list_issues.append(issues["open_issues_count"])

    # Q1: How many total open issues are there across all repositories?

    print("total open issues are there across all repositories:", total(list_issues))


def test_sort_repo():
    resp = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
    code = resp.status_code
    assert code == 200, "Code doesn't match"

    json_response = resp.json()
    list_updated = []

    for days in json_response:
        list_updated.append([days["updated_at"], days["name"]])

    print(sort_tuple(list_updated))
    list_updated = sort_tuple(list_updated)

    for i, sublist in enumerate(list_updated):
        for j, item in enumerate(sublist):
            print(f"{item} in be {list_updated[i][j]}")


def test_watcher_view():
    resp = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
    code = resp.status_code
    assert code == 200, "Code doesn't match"

    json_response = resp.json()
    max_watcher = []
    for i in json_response:
        max_watcher.append((i["name"], i["watchers"]))

    maximum = get_max_value(max_watcher)
    print("the most watchers is %d of repo %s" % (maximum[1], maximum[0]))
