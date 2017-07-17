import os
import random
import shutil

# the pct of the training data to include in our sample
sample_pct = .25
random.seed(2)

dirs = ['data_sample', 
	'data_sample/train', 
	'data_sample/train/dogs',
	'data_sample/train/cats',
	'data_sample/valid', 
	'data_sample/valid/dogs',
	'data_sample/valid/cats']

for d in dirs:
	if not os.path.exists(d): os.mkdir(d)

for i in os.listdir("data/train/dogs"):
	num = random.randint(1,(1/sample_pct))
	if num == 1:
		shutil.copy("data/train/dogs/%s" % i, "data_sample/train/dogs")

for i in os.listdir("data/valid/dogs"):
	num = random.randint(1,(1/sample_pct))
	if num == 1:
		shutil.copy("data/valid/dogs/%s" % i, "data_sample/valid/dogs")

for i in os.listdir("data/train/cats"):
	num = random.randint(1,(1/sample_pct))
	if num == 1:
		shutil.copy("data/train/cats/%s" % i, "data_sample/train/cats")

for i in os.listdir("data/valid/cats"):
	num = random.randint(1,(1/sample_pct))
	if num == 1:
		shutil.copy("data/valid/cats/%s" % i, "data_sample/valid/cats")

