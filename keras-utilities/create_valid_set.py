import os
import random

valid_pct_of_training = .25

# TODO: warn if validation set already exists
if not os.path.isdir("data/valid"):
    os.mkdir("data/valid")

for i in os.listdir("data/train"):
    num = random.randint(1, (1/valid_pct_of_training))
    if num == 1:
        os.rename("data/train/%s" % i, "data/valid/%s" % i)

