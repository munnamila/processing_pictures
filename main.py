import func
import glob
import cv2
def main(path):
    # func.make_dir(path)
    folders = sorted(glob.glob(path + '/*/*'))
    for i in folders:
        img = cv2.imread(i,0)
        img = func.choose_face(img)
        img_h = func.oppo(img)
        try:
            cv2.imwrite(path + '_d/' + i.split('/')[-2] + '/' + i.split('/')[-1],img)
            cv2.imwrite(path + '_d/' + i.split('/')[-2] + '/' + i.split('/')[-1][:-4] + '_p.png',img_h)
        except:
            print('error!!!')

        

if __name__ == "__main__":
    main('/Users/songminglun/Desktop/research/github/processing_pictures/new_data_20191128')