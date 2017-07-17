import os
from sys import argv

target_dir = argv[1]

if not os.path.isdir(target_dir + "/dogs"):
	os.mkdir(target_dir + "/dogs")

if not os.path.isdir(target_dir + "/cats"):
	os.mkdir(target_dir + "/cats")

for filename in os.listdir(target_dir):

	if os.path.isdir("/".join([target_dir, filename])):
		continue

	if filename[:3] == "dog":
		os.rename("/".join([target_dir, filename]), "/".join([target_dir, "dogs", filename]))
	elif filename[:3] == "cat":
		os.rename("/".join([target_dir, filename]), "/".join([target_dir, "cats", filename]))
	else:
		raise ValueError("Image must either be a dog or a cat.")


