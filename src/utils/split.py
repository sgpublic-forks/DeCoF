import os

def get_split(phase):
    assert phase in ['train', 'val', 'test']
    with open(os.path.join(os.path.realpath(__file__), f'../../datas/split/{phase}.json'), 'r') as f:
        return f.readlines()

# ffmpeg -i input_video.mp4 -vf "select='not(mod(n\,4))',setpts=N/FRAME_RATE/TB" -vsync vfr output_%03d.png
def split_video(video_path, save_path, range=32, count=8):
    pass
