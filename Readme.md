## Installing using GitHub
- Fork the project into your GitHub
- Clone it into your dektop
```
git clone https://github.com/jacesca/cv2_quick_sample.git
```
- Setup environment (it requires python3)
```
python -m venv venv
source venv/bin/activate  # for Unix-based system
venv\Scripts\activate  # for Windows
```
- Install requirements
```
pip install -r requirements.txt
```
- Install requirements from source
```
conda create --name cv2 python pandas numpy notebook matplotlib
conda activate cv2
pip install opencv-contrib-python
```

