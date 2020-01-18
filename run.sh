#python3 pascalvoc.py -gt /home2/haval/VOCdevkit/VOC2019-san-corrected-2000/labels_lt_2000 -det /home2/haval/VOCdevkit/VOC2019-san-corrected-2000/results_lt_2000 -gtcoords rel -detcoords rel -imgsize 1280,720 -sp results_haval
#python3 pascalvoc.py -gt /home2/haval/VOCdevkit/VOC2019-all-corrected-2000/labels -det /home2/haval/VOCdevkit/VOC2019-all-corrected-2000/results -gtcoords rel -detcoords rel -imgsize 1280,720 -sp results_haval_all_corrected_2000
python3 pascalvoc.py -gt /home2/15/lefttop_labels -det /home2/15/INT8_results -gtcoords rel -detcoords rel -imgsize 1280,720 -sp results_15 -t 0.1
#python3 pascalvoc.py -gt /home2/15/lefttop_labels -det /home2/15/trt_lefttop_results -gtcoords rel -detcoords rel -imgsize 1280,720 -sp results_15
