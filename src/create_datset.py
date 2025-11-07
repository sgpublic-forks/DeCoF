import argparse
import os

from utils.funcs import load_json
from utils.split import get_split

ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')

fake_sets = load_json(os.path.join(ROOT, "./download/fake/raw_videos/trains.json"))

video_dict = {}

def load_real_video_dict(source):
    for item in load_json(os.path.join(ROOT, f"./download/real/{source}.json")):
        if item.video_id not in video_dict:
            video_dict[item.video_id] = {
                'source': item.source,
            }
        video_dict[item.video_id]['real'] = os.path.join(ROOT, f"./download/real/{item.source}/raw_videos/{item.video}")
load_real_video_dict("MSVD/msvd_train")
load_real_video_dict("MSVD/msvd_test")
load_real_video_dict("MSVD/msvd_val")
load_real_video_dict("MSR-VTT/msrvtt_test_1k")
load_real_video_dict("MSR-VTT/msrvtt_train_9k")

def load_fake_video_dict(source):
    for item in load_json(os.path.join(ROOT, f"./download/fake/{source}.json")):
        video_dict[item.video_id]['fake'] = os.path.join(ROOT, f'./download/fake/{video_dict[item.video_id]['source']}/raw_videos/{item.video}')
load_fake_video_dict("gvf_fakes_train")


def create_dataset_by_phase(phase):
    video_list = get_split(phase)



def main(args):
    dataset_config = load_json(args.config)
    subdatasets_name = dataset_config['subdatasets_name']
    assert subdatasets_name in fake_sets


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument(dest='config')
    args=parser.parse_args()
    main(args)
