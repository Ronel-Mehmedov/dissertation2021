import os

# Directory
directory = "website4"

# Parent Directory path
parent_dir = "/home/x/dissertation/scraper"

# mode
mode = 0o755

# Path
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
