import os


class OutputPath:
    @staticmethod
    def path(args):
        file_name = '{content_img}-w{content_weight}_TO_{style_img}-w{style_weight}_iter{iteration}_res{res}.png'.format(
            content_img=os.path.split(os.path.splitext(args.content_img)[0])[1],
            content_weight=int(args.content_weight),
            style_img=os.path.split(os.path.splitext(args.style_img)[0])[1],
            style_weight=int(args.style_weight),
            iteration=args.iteration,
            res=args.hard_width
        )
        return os.path.join(args.output_dir, file_name)
