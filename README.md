# Python Web Request （网页批量下载系统）
### “用于下载大量的swf档案使用”

介于flash即将在2021年停止营运，不过离线版的flash还能驱动的关系，于是想要一次过下载大量的flash档并把他们转档成html5/mp4/gif档案等让他们拥有重生的机会。

此系統針對 https://dagobah.net/ 的.swf作品。主要原因如下：
 1. dagobah.net的档案下载是有规律的，都是把 "flash" 改成 "flashswf" 就可以下载档案
 2. 没有rate-limited限制，因此可以无限大量下载而不会被网站砍掉封包
 3. 绝大部分的flash都是没什么看过的，所以更要下载来慢慢品味
 4. 转档成其他格式 让这些作品有重生的机会

## 資料檔案
这次的python档案分成4个，有机会就做成一个档案：
 1. 用来截取dagobah.net的275页的html画面，全部把他们拉下来
 2. 过滤掉大部分不重要的html，只保留拥有*.swf的那条线
 3. 那条线里面拉出纯*.swf的那个条码
 4. 塞进预先准备好的下载前缀网址，然后for loop大量下载

## 前置安裝
不需要，有python和手就行

## 效果預覽
![alt text](https://i.imgur.com/ote1Xkd.png)
![alt text](https://i.imgur.com/Il5afCD.png)
总计花时：`16小时`  
介于大量的档案的关系，所以时间真的会拖很长。  
你会得到大约有13876个swf档案，其中有30%全部都是3D龙效果，癲癇症患者还请注意

## 延伸想法
1. 有沒有辦法把這四個檔案合併成一個呢？
2. 如果這次要考古的網頁是 https://z0r.de/，那要怎麼改裝代碼呢?

## 參考文獻
？
