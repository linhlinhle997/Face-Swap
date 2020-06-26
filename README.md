# Face-Swap

### Prerequisites
- Python 3.7

### Installation
```markdown
pip install -r requirements.txt
```
### YAML configs
See `config/vox-256-sem-5segments.yaml` to get description of each parameter

### Pre-trained checkpoints
Checkpoints can be found under following links: [yandex-disk](https://yadi.sk/d/2hTyhEcqo_5ruA) and [google-drive](https://drive.google.com/drive/folders/1SsBifjoM_qO0iFzb8wLlsz_4qW2j8dZe).

### Part-swap demo
```markdown
python part_swap.py  --config config/vox-256-sem-5segments.yaml --target_video input/video/01.mp4 --result_video output/result.mp4 --source_image input/image/05.png --checkpoint checkpoint/vox-5segments.pth.tar --swap_index 0,1,2,3,4,5
```
### Notebook demo
see: `part_swap.ipynb`

### Datasets
1. Taichi. Please follow the instruction from
[https://github.com/AliaksandrSiarohin/video-preprocessing](https://github.com/AliaksandrSiarohin/video-preprocessing.)
2. VoxCeleb. Please follow the instruction from
[https://github.com/AliaksandrSiarohin/video-preprocessing](https://github.com/AliaksandrSiarohin/video-preprocessing)

### Reference
- Motion Supervised co-part Segmentation: [https://github.com/AliaksandrSiarohin/motion-cosegmentation](https://github.com/AliaksandrSiarohin/motion-cosegmentation)
- First Order Motion Model for Image Animation: [https://github.com/AliaksandrSiarohin/first-order-model](https://github.com/AliaksandrSiarohin/first-order-model)
