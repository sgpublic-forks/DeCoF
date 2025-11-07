import os
from glob import glob


def init_ff(phase,data_name='text2video_zero'):
	root = os.path.join(os.path.dirname(__file__), '../../data')

	dataset_path_r=os.path.join(root,data_name,phase,'0_real/')
	
	dataset_path_f=os.path.join(root,data_name,phase,'1_fake/')
	



	
	real_img_list   = sorted(glob(dataset_path_r+'*'))
	fake_img_list  = sorted(glob(dataset_path_f+'*'))
	



				
	fake_label_list = [1 for _ in range(len(fake_img_list))]
	print(fake_img_list[0])

	
		
	real_label_list = [0 for _ in range(len(real_img_list))]
	
	img = real_img_list+fake_img_list
	label = real_label_list+fake_label_list

	return img,label


	

	
