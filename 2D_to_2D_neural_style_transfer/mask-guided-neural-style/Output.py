import os

import scipy.misc
import numpy as np

class Output:
    args = None
    def __init__(self, args):
        self.args = args

    def path(self):
        file_name = '{content_img}-w{content_weight}_TO_{style_img}-w{style_weight}_iter{iteration}_res{res}.png'.format(
            content_img=os.path.split(os.path.splitext(self.args.content_img)[0])[1],
            content_weight=int(self.args.content_weight),
            style_img=os.path.split(os.path.splitext(self.args.style_img)[0])[1],
            style_weight=int(self.args.style_weight),
            iteration=self.args.iteration,
            res=self.args.hard_width
        )
        return os.path.join(self.args.output_dir, file_name)

    def write_image(self, path, img):  # postprocess and write
        img = img + [123.68, 116.779, 103.939]
        img = img[0]
        img = np.clip(img, 0, 255).astype('uint8')
        scipy.misc.imsave(path, img)


    def save_result(self, img):
        # Create directory if it not exists
        if not os.path.exists(self.args.output_dir):
            os.mkdir(self.args.output_dir)
        # dir path + filename
        path = self.path()
        # Save image
        self.write_image(path, img)