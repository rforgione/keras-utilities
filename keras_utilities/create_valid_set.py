import os
import random


def create_val_dir(val_pct=.25):
    # TODO: warn if validation set already exists
    if not os.path.isdir("data/valid"):
        os.mkdir("data/valid")

    for i in os.listdir("data/train"):
        num = random.randint(1, (1/val_pct))
        if num == 1:
            os.rename("data/train/%s" % i, "data/valid/%s" % i)

