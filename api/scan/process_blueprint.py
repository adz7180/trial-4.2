# /api/scan/process_blueprint.py

import cv2
import numpy as np
import fitz                  # PyMuPDF for PDF → PNG
import torch
import torchvision
from torchvision.transforms import functional as F
from shapely.geometry import Polygon
from convert_to_glb import convert_to_glb_from_geometry
from segmentation_blueprint import blueprint_segmentation

# Load pretrained Mask R‑CNN
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Map COCO classes to home elements
CLASS_MAP = {1:'wall', 2:'door', 3:'window'}

def convert_pdf_to_image(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap(matrix=fitz.Matrix(3,3))
    img_path = pdf_path.replace('.pdf','.png')
    pix.save(img_path)
    return img_path

def detect_objects(image):
    # 1) Blueprint‑tuned segmentation for walls
    segments = blueprint_segmentation('/tmp/blueprint.png')
    objects, suggestions = [], []
    for seg in segments:
        x1,y1,x2,y2 = seg['coords']
        w,h = abs(x2-x1), abs(y2-y1)
        objects.append({
            'type':'wall',
            'x': min(x1,x2), 'y': min(y1,y2),
            'w': w, 'h': h,
            'material':'painted drywall'
        })
        suggestions.append('Blueprint wall segment added.')

    # 2) Mask R‑CNN for doors/windows/etc.
    img_tensor = F.to_tensor(image).unsqueeze(0)
    with torch.no_grad():
        out = model(img_tensor)[0]
    for i,score in enumerate(out['scores']):
        if score < 0.7: continue
        cls = out['labels'][i].item()
        if cls not in CLASS_MAP: continue
        mask = out['masks'][i,0].mul(255).byte().cpu().numpy()
        cnts,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in cnts:
            poly = cv2.approxPolyDP(cnt,5,True).reshape(-1,2)
            if Polygon(poly).area < 200: continue
            x,y,w,h = cv2.boundingRect(cnt)
            typ = CLASS_MAP[cls]
            mat = 'glass' if typ=='window' else 'wood'
            objects.append({
                'type': typ, 'x': x, 'y': y,
                'w': w, 'h': h,
                'material': mat,
                'polygon': poly.tolist()
            })
            suggestions.append(f'Detected {typ}, default to {mat}.')
    return objects, suggestions

def process_blueprint(file_path, output_glb_path):
    if file_path.lower().endswith('.pdf'):
        file_path = convert_pdf_to_image(file_path)
    image = cv2.imread(file_path)
    image = cv2.resize(image, (1024,1024))
    objs, sugg = detect_objects(image)
    convert_to_glb_from_geometry(objs, output_glb_path)
    import json; print(json.dumps({'suggestions': sugg}))
    return True
