# Wav2lip-Gfpgan-Cpu-Installation
https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth download this file and rename it to s3fd
https://huggingface.co/spaces/jerryyan21/wav2lip_demo_test/blob/1979f8b69b22b24171adf63e66946cc377bb7390/wav2lip.pth
https://github.com/TencentARC/GFPGAN?tab=readme-ov-file download gfpgan 1.3

python inference.py --checkpoint_path checkpoints/wav2lip.pth --face C:/Users/ggrov/Downloads/wav2lip/Wav2Lip-GFPGAN/inputs/kim.mp4 --audio C:/Users/ggrov/Downloads/wav2lip/Wav2Lip-GFPGAN/inputs/kim.MP3

https://github.com/TencentARC/GFPGAN?tab=readme-ov-file  download this and place in peretrained_models

python inference_gfpgan.py -i "C:\Users\ggrov\Downloads\wav2lip\Wav2Lip-GFPGAN\Wav2Lip-master\results\frames_voice" -o "C:\Users\ggrov\Downloads\wav2lip\Wav2Lip-GFPGAN\Wav2Lip-master\results\xiaobao_restore_images" -v 1.3 -s 2 --only_center_face --bg_upsampler None
