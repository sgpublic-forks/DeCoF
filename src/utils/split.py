from os import path
from pathlib import Path

import ffmpeg


def get_split(phase):
    assert phase in ['train', 'val', 'test']
    with open(path.join(path.dirname(path.realpath(__file__)), f'../../datas/split/{phase}.json'), 'r') as f:
        return [item.strip() for item in f.readlines()]

# ffmpeg -i input_video.mp4 -vf "select='not(mod(n\,4))',setpts=N/FRAME_RATE/TB" -vsync vfr output_%03d.png
def split_video(video_path: str, save_path: Path, filenames='%03d.jpg', range=32, count=8):
    print(f'processing {video_path}')
    save_path.mkdir(parents=True, exist_ok=True)
    stream = (
        ffmpeg
        .input(video_path)
        .filter('select', f'lte(n,{range - 1})')
        .filter('select', f'not(mod(n,{range / count}))')
        .filter('crop', 'min(iw,ih)', 'min(iw,ih)', '(iw-min(iw,ih))/2', '(ih-min(iw,ih))/2')
        .output(path.join(save_path, filenames), vsync='0', start_number=0)
    )
    ffmpeg.run(stream, overwrite_output=True, quiet=True)
