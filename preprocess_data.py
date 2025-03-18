import os
import argparse
import glob
import shutil

def process_data(args):
    data_dir = args.data_dir
    zip_file_dir = f'{data_dir}/SMPL-H.zip'
    if not os.path.exists(zip_file_dir):
        raise Exception(f'{zip_file_dir} does not exist.')

    os.system(f'unzip {zip_file_dir} -d {data_dir}')
    
    print("Removing shape_*.npz files...")
    for file_name in glob.glob(f'{data_dir}/**/**/**/shape_*.npz'):
        os.remove(file_name)

    print("Changing folder structures...")
    parent_styles_list = glob.glob(f'{data_dir}/**')
    
    for style_dir in glob.glob(f'{data_dir}/**/**'):
        shutil.move(style_dir, data_dir)

    for parent_style_dir in parent_styles_list:
        if os.path.isdir(parent_style_dir):
            shutil.rmtree(parent_style_dir)
        else:
            # Remove SMPL-H.zip
            os.remove(parent_style_dir)
    
    print("Done!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='./data')
    args = parser.parse_args()
    
    process_data(args)
