import argparse
from pathlib import Path

from utils.funcs import load_json
from utils.split import get_split, split_video

ROOT = Path(__file__).resolve().parent / '..'

fake_sets = load_json(str(ROOT / "./download/fake/raw_videos/trains.json"))

video_dict = {}

def load_real_video_dict(source):
    for item in load_json(str(ROOT / f"./download/real/{source}.json")):
        if item['video_id'] not in video_dict:
            video_dict[item['video_id']] = {
                'source': item['source'],
            }
        video_dict[item['video_id']]['real'] = str(ROOT / f"./download/real/{item['source']}/raw_videos/{item['video']}")
load_real_video_dict("MSVD/msvd_train")
load_real_video_dict("MSVD/msvd_test")
load_real_video_dict("MSVD/msvd_val")
load_real_video_dict("MSR-VTT/msrvtt_test_1k")
load_real_video_dict("MSR-VTT/msrvtt_train_9k")

def load_fake_video_dict(source):
    for item in load_json(str(ROOT / f"./download/fake/{source}.json")):
        if 'fake' not in video_dict[item['video_id']]:
            video_dict[item['video_id']]['fake'] = {}
        video_dict[item['video_id']]['fake'][item['source']] = str(ROOT / f'./download/fake/raw_videos/{item['video']}')
load_fake_video_dict("gvf_fakes_train")


DATASET_ROOT = ROOT / "data"
def create_dataset(subdatasets_name):
    dataset_path = DATASET_ROOT / subdatasets_name
    for phase in ['train', 'val', 'test']:
        create_dataset_for_phase(subdatasets_name, phase, dataset_path)

def create_dataset_for_phase(subdatasets_name, phase, save_to):
    video_list = get_split(phase)
    for video_id in video_list:
        if video_id not in video_dict:
            print(f'{video_id} not found video_dict')
            continue
        video = video_dict[video_id]
        split_video(video['real'], save_to / phase / '0_real' / video_id)
        split_video(video['fake'][subdatasets_name], save_to / phase / '1_fake' / video_id)


def main(args):
    dataset_config = load_json(str(ROOT / f'./src/configs/{args.config}.json'))
    subdatasets_name = dataset_config['subdatasets_name']
    assert subdatasets_name in fake_sets
    create_dataset(subdatasets_name)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument(dest='config')
    args=parser.parse_args()
    main(args)
