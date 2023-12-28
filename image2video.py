import os
import cv2
from tqdm import tqdm

restored_frames_path = 'C:\\Users\\ggrov\\Downloads\\wav2lip\\Wav2Lip-GFPGAN\\Wav2Lip-master\\results\\xiaobao_restore_images\\restored_imgs'
processed_video_output_path = 'C:\\Users\\ggrov\\Downloads\\wav2lip\\Wav2Lip-GFPGAN\\Wav2Lip-master\\results\\xiaobao_final_image'
input_audio_path = 'C:\\Users\\ggrov\\Downloads\\wav2lip\\Wav2Lip-GFPGAN\\inputs\\kimk_audio.mp3'

# Create the output directory if it doesn't exist
if not os.path.exists(processed_video_output_path):
    os.makedirs(processed_video_output_path)

# Get the list of restored frames
dir_list = os.listdir(restored_frames_path)
dir_list.sort()

# Set batch parameters
batch_size = 300
batch = 0

# Process frames in batches
for i in tqdm(range(0, len(dir_list), batch_size)):
    img_array = []

    start, end = i, i + batch_size

    print("Processing frames ", start, "to", end)

    for filename in tqdm(dir_list[start:end]):
        file_path = os.path.join(restored_frames_path, filename)

        # Read the image
        img = cv2.imread(file_path)

        if img is None:
            continue

        height, width, layers = img.shape
        size = (width, height)

        img_array.append(img)

    # Combine images in img_array to create a video
    output_video_path = os.path.join(processed_video_output_path, f'batch_{batch}.avi')
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

    for img in img_array:
        out.write(img)

    out.release()
    batch += 1

print("Video processing completed.")

# Concatenate videos
concat_text_file_path = os.path.join(processed_video_output_path, 'concat.txt')
with open(concat_text_file_path, 'w') as concat_file:
    for i in range(batch):
        concat_file.write(f"file 'batch_{i}.avi'\n")

concated_video_output_path = os.path.join(processed_video_output_path, 'concated_output.avi')
os.system(f"ffmpeg -y -f concat -i {concat_text_file_path} -c copy {concated_video_output_path}")

# Add audio to the final output video in MP4 format
final_processed_output_video_mp4 = os.path.join(processed_video_output_path, 'final_with_audio.mp4')
os.system(f"ffmpeg -y -i {concated_video_output_path} -i {input_audio_path} -map 0:v -map 1:a -c:v copy -shortest {final_processed_output_video_mp4}")

print("Video concatenation and audio addition completed.")
