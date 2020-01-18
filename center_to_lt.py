# this script convert darknet's format [normalized_center_x, normalized_center_y, normalized_w, normalized_h] to the format required by Object-Detection-Metrics [normalized_left, normalized_top, normalized_w, normalized_h]
import os
from tqdm import tqdm
import re

dirs = ["/home2/haval/VOCdevkit/VOC2019-san-corrected-2000/labels",
        "/home2/haval/VOCdevkit/VOC2019-san-corrected-2000/results"]

def center2tl(line, fname):
    t = line.split()
    if len(t) == 5:
        # label
        label, cx, cy, w, h = line.split()
        cx, cy, w, h = float(cx), float(cy), float(w), float(h)
        left = cx - w/2
        top = cy - h/2
        left, top, w, h = str(left), str(top), str(w), str(h)
        return " ".join([label, left, top, w, h])
    elif len(t) == 6:
        # prediction
        label, cx, cy, w, h, conf = line.split()
        cx, cy, w, h = float(cx), float(cy), float(w), float(h)
        left = cx - w/2
        top = cy - h/2
        left, top, w, h = str(left), str(top), str(w), str(h)
        # note the position of conf!
        return " ".join([label, conf, left, top, w, h])
    else:
        print(fname)

for srcdir in dirs:
    dstdir = srcdir + "_lt"
    print(srcdir)
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)
    fnames = os.listdir(srcdir)
    
    fnames = [fname for fname in fnames if len(re.findall("\d+\.txt", fname)) != 0]
    for fname in tqdm(fnames):
        with open(os.path.join(srcdir, fname), 'r') as f:
            lines = f.readlines()
        lines = [center2tl(line, fname)+"\n" for line in lines]
        with open(os.path.join(dstdir, fname), 'w') as f:
            f.writelines(lines)
