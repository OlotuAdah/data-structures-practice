import os


def disk_usage(path):
    total_size = os.path.getsize(path)
    if os.path.isdir(path):  # if the path given is a folder and not an individual file
        for filename in os.listdir(path):  # get the list of all sub folders
            child_dir = os.path.join(path, filename)  # create fullpath for each item. NB: works well for all OS
            total_size = total_size + disk_usage(child_dir)  # recursively add size to total for each item
    print(f"{total_size}: {path}")  # each time disk_usage is called, print the total and the path
    return total_size


if __name__ == '__main__':
    total = disk_usage("C:/Users/HP/PycharmProjects")
    print(total)

    # OUTPUT:
    # 20: C: / Users / HP / PycharmProjects\DataStrcutures\.git\COMMIT_EDITMSG
    # 316: C: / Users / HP / PycharmProjects\DataStrcutures\.git\config
    # 73: C: / Users / HP / PycharmProjects\DataStrcutures\.git\description
    # 21: C: / Users / HP / PycharmProjects\DataStrcutures\.git\HEAD
    # 478: C: / Users / HP / PycharmProjects\DataStrcutures\.git\hooks\applypatch - msg.sample
    # ...
