简体中文:
首先声明 本文所爬取的数据均为公开 且不涉及任何隐私

前段时间，有同学向我咨询一个老师的邮箱。
我第一时间想到了bjtu研究生院下的导师在线。但是那位同学要找的老师不是研究生导师，于是乎我只能退出研究生院，去所属学院的官网，然后通过师资力量去检索​。可谓是较为麻烦的。

于是乎，我在想能否在本地建立一个教师数据库，​把所有老师主页上的信息纳入囊中呢？

这里用到了python的request库

首先，分析北京交通大学教师主页的网址结构，那就是

http://faculty.bjtu.edu.cn/+工号
如http://faculty.bjtu.edu.cn/8888/是工号为8888的老师的主页

好的，有了这一点，只需要遍历工号范围，挨个荡下来，就可以实现获取整个北京交通大学教师的数据爬取。

本项目有2个程序，一个是爬取并批量保存为txt，另一个是批量读取txt文件生成excel，包含教师姓名，主页，和邮箱。

English:
First, declare that the data crawled in this article are public and do not involve any privacy
Some time ago, a classmate asked me about a teacher's email.
I thought of the online tutor of BJTU graduate school for the first time. But the teacher the student was looking for was not a graduate tutor, so I had to quit the graduate school, go to the official website of my college, and then search through the faculty. It can be said to be more troublesome.
So I was wondering if I could set up a local teacher database and put all the information on the teacher's home page into the bag?
The request Library of Python is used here
First of all, analyze the website structure of the teachers' home page of Beijing Jiaotong University, that is
http://faculty.bjtu.edu.cn/ +Job number
as http://faculty.bjtu.edu.cn/8888/ This is the homepage of the teacher with job number 8888
OK, with this, you only need to traverse the job number range and swing down one by one to obtain the data of the teachers of Beijing Jiaotong University.
This project has two programs, one is to crawl and save in batches as TXT, the other is to read txt files in batches and generate excel, including teacher name, home page and email.
