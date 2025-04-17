import json

# open gg task json file
takeout = {}

with open('./Tasks.json', 'r') as file:
    takeout = json.load(file)


def pluckout(item):
    return {
        "title"
    }

# GOAL: get list of task lists
# from the list of task lists, select a list to output the tasks in it

def get_list_of_task_lists(takeout):
    for key in takeout.keys():
        print("key", key)
    task_lists = takeout['items']
    title_list = []
    for task_list in task_lists:
        title = task_list['title']
        print("list_title", title)
        title_list.append(title)
    return title_list


def get_tasks_by_task_list_name(takeout, title_to_get):
    task_lists = takeout['items']
    for task_list in task_lists:
        if task_list['title'] == title_to_get:
            return task_list['items']
    return []

task_list_titles = get_list_of_task_lists(takeout)
print("task_list_titles", task_list_titles)

task_to_get = get_tasks_by_task_list_name(takeout, 'Pending 0')
print("task_to_get", task_to_get)

for task in task_to_get:
    print("task: ", task.get('title'))
    print("-------------------")