# admin
from os import path


def add_name(name):

    find = 0

    # search duplicates if file exist
    if path.exists("NameDB.txt"):
        f = open("NameDB.txt", "r")
        lines = f.readlines()
        for line in lines:
            if line.strip("\n") == name:
                find = 1
                break
        f.close()

    # if no duplicate add name
    if find == 0:
        f = open("NameDB.txt", "a")
        text = "%s\n" % name
        f.write(text)
        print(name, "added to NameDB")
        f.close()
    else:
        print("not added, duplicate name")


def remove_name(name):

    # if file exist search for name, if find remove
    if not path.exists("NameDB.txt"):
        print("Missing file")
    else:
        f = open("NameDB.txt", "r")
        lines = f.readlines()
        f.close()

        find = 0

        new_f = open("NameDB.txt", "w")
        for line in lines:
            if line.strip("\n") == name:
                find = 1
            if line.strip("\n") != name:
                new_f.write(line)
        new_f.close()

        if find == 0:
            print("name not found in DB")
        else:
            print(name, "removed from NameDB")


def list_name():

    print("NameDB:")
    if not path.exists("NameDB.txt"):
        print("Missing file")
    else:
        f = open("NameDB.txt", "r")
        for x in f:
            print(x)


def add_category(cat):

    find = 0

    if path.exists("CategoryDB.txt"):
        f = open("CategoryDB.txt", "r")
        lines = f.readlines()
        for line in lines:
            if line.strip("\n") == cat:
                find = 1
                break
        f.close()

    if find == 0:
        f = open("CategoryDB.txt", "a")
        text = "%s\n" % cat
        f.write(text)
        print(cat, "added to CategoryDB")
        f.close()
    else:
        print("not added, duplicate name")


def remove_category(cat):

    if not path.exists("CategoryDB.txt"):
        print("Missing file")
    else:
        f = open("CategoryDB.txt", "r")
        lines = f.readlines()
        f.close()

        find = 0

        new_f = open("CategoryDB.txt", "w")
        for line in lines:
            if line.strip("\n") == cat:
                find = 1
            if line.strip("\n") != cat:
                new_f.write(line)
        new_f.close()

        if find == 0:
            print("category not found in DB")
        else:
            print(cat, "removed from CategoryDB")


def list_category():

    print("CategoryDB:")
    if not path.exists("CategoryDB.txt"):
        print("Missing file")
    else:
        f = open("CategoryDB.txt", "r")
        for x in f:
            print(x)


def add_task(task):

    find = 0

    # search duplicates if file exist
    if path.exists("TasksDB.txt"):
        f = open("TasksDB.txt", "r")
        lines = f.readlines()
        for line in lines:
            if line.strip("\n") == task:
                find = 1
                break
        f.close()

    # if no duplicate add name
    if find == 0:
        f = open("TasksDB.txt", "a")
        text = "%s\n" % task
        f.write(text)
        print(task, "added to TasksDB")
        # tasklist += list(task)
        f.close()
    else:
        print("not added, duplicate task")


def remove_task(task):

    # if file exist search for name, if find remove
    if not path.exists("TasksDB.txt"):
        print("Missing file")
    else:
        f = open("TasksDB.txt", "r")
        lines = f.readlines()
        f.close()

        find = 0

        new_f = open("TasksDB.txt", "w")
        for line in lines:
            if line.strip("\n") == task:
                find = 1
            if line.strip("\n") != task:
                new_f.write(line)
        new_f.close()

        if find == 0:
            print("task not found in DB")
        else:
            print(task, "removed from TasksDB")


def list_task():

    print("TasksDB:")
    if not path.exists("TasksDB.txt"):
        print("Missing file")
    else:
        f = open("TasksDB.txt", "r")
        for x in f:
            print(x)


# def ascsort_task():
#     tasklist.sort()
#     print(tasklist)

# def dessort_task():
#     tasklist.sort(reverse=True)
#     print(tasklist)