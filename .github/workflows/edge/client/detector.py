# detector.py - stub que simula uma detecção
import random
def detect(image_path=None):
    # retorna formato: [{"class":"capacete","conf":0.9, "bbox":[x1,y1,x2,y2]}]
    if random.random() > 0.5:
        return [{"class":"capacete","conf":0.95,"bbox":[10,10,100,100]}]
    else:
        return []
