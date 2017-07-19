import os
import random
import shutil


def create_sample_data(src_dir, target_dir=None, sample_pct=.1, method='copy'):
    """
    A function for taking a chunk of training data and either copying or
    moving it to a chosen location with probability `sample_pct`. This
    can be used to build a sample training set, or it could be used to
    build a validation set.

    Args:
        src_dir (str): the path to the original dataset
        target_dir (str): the path to directory where the sample data
            will live
        sample_pct (float): the percentage of the data to use in a sample
        method (str): can be 'copy' or 'move'; copy copies the files while
            move moves them

    Returns:
        None
    """
    if not target_dir:
        target_dir = src_dir + "/../sample"

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for i in os.listdir(src_dir):
        num = random.randint(1, (1/sample_pct))
        if num == 1:
            if method == 'copy':
                shutil.copy(src_dir + "/%s" % i, target_dir + "/%s" % i)
            elif method == 'move':
                os.rename(src_dir + "/%s" % i, target_dir + "/%s" % i)
            else:
                raise ValueError("Method must be either 'copy' or 'move'.")


def split_directory_by_class(img_dir, class_list):
    """
    A function to split a directory into a collection of subdirectories
    where each subdirectory contains images in one of our predicted classes.
    The function assumes that each string in class_list is a mutually-exclusive
    pattern that can be used to identify the class of the image using the
    image's name. If there is a class name that is a substring of another class
    name, put the longer class name first in the class_list (though try to avoid this
    where possible). Hopefully in future versions there will be the option to pass
    more sophisticated regex to determine the class of a file with more precision.

    Args:
        img_dir (str): the directory containing our images
        class_list (list): a list of strings, each string serving
            as the name of a single class
    Returns:
        None
    """

    # create the appropriate directory structure
    for c in class_list:
        if not os.path.exists(image_dir + "%s" % c):
            os.mkdir(image_dir + "/%s" % c)

    for img_name in os.listdir(img_dir):
        for c in class_list:
            if c in img_name:
                shutil.rename(img_dir + "/%s" % img_name, img_dir + "/%s/%s" % (c, img_name))


def apply_directory_structure(data_dir, sample_dir, class_list, sample_pct=.25, val_pct=.25):
    """
    Args:
        data_dir (str): The original folder containing training data
        sample_dir (str): The directory we want to use for our sample data
        sample_pct (float): The percentage of data we want to use in our sample
        val_pct (float): The percentage of our data we want to use in our validation set
        class_list (list[str]): A list of strings containing the class names of our images

    Returns:
        None
    """
    create_sample_data(data_dir, sample_dir, sample_pct)

    for subdir in [data_dir, sample_dir]:
        create_val_set(subdir, val_pct)

        for dataset in ['train', 'valid']:
            split_directory_by_class(subdir + "/%s" % dataset, class_list)

    return None





