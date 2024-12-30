import cv2
import os
import random


def txtShow(img, txt, save=True):
    image = cv2.imread(img)
    height, width = image.shape[:2]  # 获取原始图像的高和宽

    # 读取classes类别信息
    with open('classes.txt', 'r') as f:
        classes = f.read().splitlines()
    # ['Leconte', 'Boerner', 'linnaeus', 'armandi', 'coleoptera', 'acuminatus', 'Linnaeus']

    # 读取yolo格式标注的txt信息
    with open(txt, 'r') as f:
        labels = f.read().splitlines()
    # ['0 0.403646 0.485491 0.103423 0.110863', '1 0.658482 0.425595 0.09375 0.099702', '2 0.482515 0.603795 0.061756 0.045387', '3 0.594122 0.610863 0.063244 0.052083', '4 0.496652 0.387649 0.064732 0.049107']

    ob = []  # 存放目标信息
    for i in labels:
        cl, x_centre, y_centre, w, h = i.split(' ')

        # 需要将数据类型转换成数字型
        cl, x_centre, y_centre, w, h = int(cl), float(x_centre), float(y_centre), float(w), float(h)
        name = classes[cl]  # 根据classes文件获取真实目标
        xmin = int(x_centre * width - w * width / 2)  # 坐标转换
        ymin = int(y_centre * height - h * height / 2)
        xmax = int(x_centre * width + w * width / 2)
        ymax = int(y_centre * height + h * height / 2)

        tmp = [name, xmin, ymin, xmax, ymax]  # 单个检测框
        ob.append(tmp)

    # 绘制检测框
    for name, x1, y1, x2, y2 in ob:
        cv2.rectangle(image, (x1, y1), (x2, y2), color=(255, 0, 0), thickness=2)  # 绘制矩形框
        cv2.putText(image, name, (x1, y1 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5, thickness=1, color=(0, 0, 255))

        # 保存图像
    if save:
        cv2.imwrite('result.png', image)

    #     # 展示图像
    # cv2.imshow('test', image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    img_path = './datasets/images/train/'  # 传入图片
    image = [os.path.join(img_path, i) for i in os.listdir(img_path)]
    r = random.randint(0, len(image) - 1)  # 生成随机索引

    image_path = image[r]
    labels_path = image_path.replace('images', 'labels')  # 自动获取对应的 txt 标注文件
    labels_path = labels_path.replace('.jpg', '.txt')

    txtShow(img=image_path, txt=labels_path, save=True)