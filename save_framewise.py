import cv2
import os

emos = ['HAP', 'SAD', 'FEA', 'ANG', 'DIS']
num = len([name for name in os.listdir('results/HAP') if os.path.isfile(os.path.join('results/HAP',name))])
print(num)
for idx in range(num):
    img_list = []
    for emotion in emos:
        img = cv2.imread(f'results/{emotion}/{idx}.jpg')
        img_list.append(img)
    new_img = cv2.hconcat(img_list)
    cv2.imwrite(f'results/frame_wise/{idx}.jpg',new_img)

    