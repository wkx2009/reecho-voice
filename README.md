本脚本可用于方便用户使用睿声api
本脚本以睿声官方文档为基本来编写
仅为研究用途，若有违法行为与作者无关

使用前注意：
请提前在系统中安装requests依赖
1.本脚本功能不多，仅挑选了个别功能来编写，有能力者可以在本脚本的基础上加以修改
2.可能有bug，若出现bug请与作者联系
3.脚本以后可能会更新
使用介绍：
安装
1.获取 api（语言）
2.打开脚本，输入api就可以正常使用（默认使用国内服务器，有需要请自己修改）
功能介绍：
1.查看账号中的角色：选择后可以获取到api账号中的角色信息，请对需要的角色id进行保存
例：{“id”：'500cd3d8-4dff-43f7-9 d16-68 e77 e92 ab5b'，“名称”：'500cd3d8'，'status'：'pending'，'from'：'community'，（com）
只需要保存[500cd3 d8-4dff-43f7-9d16-68 e77 e92 ab5b]
2.生成语音：选择后请填入想要让角色说的话和角色id即可，完成后会返回音频链接
例：{“status”:200，“message”：“OK”，“data”：{“audio”：https：//voc-public-storage. reecho. cn/generate/f 352a 9 f 6-7 a 67-4213-88 e 4-d 1b 38870 c 2 b 5/f 352 a 9 f 6-7 a 67-4213-88 e 4-d 1 b 38870 c 2 b 5-simple-c 44 idq. mp3}（black）
用户可以修改默认参数，但不建议修改
3.测试api连接：选择后就可以测试api服务器的连接，会输出api用户的个人信息
例：{“status”:200，“message”：“OK”，“user”：{“id”：
4.退出：选择后可以退出脚本
