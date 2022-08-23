import os
import configuration as cfg
import cv2
import numpy as np


class Data_Process():
    def __init__(self, annotation_path, augmenation=None):
        super(Data_Process,self).__init__()
        self.annotation_path = annotation_path  
        self.augmenation = augmenation

    def pre_process_img(self):
        for annot_file_name in os.listdir(self.annotation_path):
            file_id = annot_file_name.split('.txt')[0]
            annot_file = os.path.join(self.annotation_path, annot_file_name)
            rgb_img_path = os.path.join(cfg.rgb_imgs, file_id+'.png')
            ir_img_path = os.path.join(cfg.ir_imgs, file_id+'.png')
            rgb_img = cv2.imread(rgb_img_path)
            ir_img = cv2.imread(ir_img_path)
            print(rgb_img.shape, ir_img.shape)

            # Read File
            with open(annot_file, 'r') as f:
                objs = f.readlines()[1:]
            boxes = []
            for ix, obj in enumerate(objs):
                obj_split = obj.split(' ')
                #obj_count += 1
                x1 = int(obj_split[1])
                y1 = int(obj_split[2])
                x2 = x1 + int(obj_split[3])
                y2 = y1 + int(obj_split[4])
                boxes.append([x1, y1, x2, y2])

            boxes = np.asarray(boxes)
            print("annotations: ",boxes, boxes.shape)


            ######Augmentation implementation
            #aug_rgb_img, aug_ir_img, updated_boxes = augmentation(rgb_img, ir_img, bboxes)
            ################


if __name__=="__main__":
    ###########We need to implement augmentation class
    #augmentation = Augmentation()
    ################################
    data_process = Data_Process(cfg.annotation_path, augmenation=None) ###pass your augmentation object here instead of None
    data_process.pre_process_img()