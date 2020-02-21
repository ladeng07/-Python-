import sys
import os
import you_get
path='//storage//emulated//0//python作品//视频'
def download(url,path=path):
	sys.argv=['you-get','-o',path,url]
	you_get.main()
	
if __name__ == '__main__':
    # 视频网站的地址
    url = 'http://www.bilibili.com/video/av73126723?share_medium=android&share_source=copy_link&bbid=XY05C2B0B2E6C3F03516011EFDECA756E8853&ts=1582212382966'
    if not os.path.exists(path):
    	os.mkdir(path)
    os.chdir(path)
    download(input('请输入要下载的视频，图片，音乐地址: '))
