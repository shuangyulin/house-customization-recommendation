#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    shoujihao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    money=models.FloatField   (  null=True, unique=False,default='0', verbose_name='余额' )
    '''
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    yonghuxingming=VARCHAR
    touxiang=Text
    shoujihao=VARCHAR
    xingbie=VARCHAR
    money=Float
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class shejishi(BaseModel):
    __doc__ = u'''shejishi'''
    __tablename__ = 'shejishi'

    __loginUser__='shejishizhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='shejishizhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shejishizhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='设计师账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    shejishixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='设计师姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shanzhangfengge=models.CharField ( max_length=255, null=True, unique=False, verbose_name='擅长风格' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    zhengshutupian=models.TextField   ( null=False, unique=False, verbose_name='证书图片' )
    congyeshizhang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='从业时长' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    money=models.FloatField   (  null=True, unique=False,default='0', verbose_name='余额' )
    '''
    shejishizhanghao=VARCHAR
    mima=VARCHAR
    shejishixingming=VARCHAR
    xingbie=VARCHAR
    shanzhangfengge=VARCHAR
    lianxidianhua=VARCHAR
    zhengshutupian=Text
    congyeshizhang=VARCHAR
    touxiang=Text
    money=Float
    '''
    class Meta:
        db_table = 'shejishi'
        verbose_name = verbose_name_plural = '设计师'
class fenggefenlei(BaseModel):
    __doc__ = u'''fenggefenlei'''
    __tablename__ = 'fenggefenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    fenggefenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='风格分类' )
    '''
    fenggefenlei=VARCHAR
    '''
    class Meta:
        db_table = 'fenggefenlei'
        verbose_name = verbose_name_plural = '风格分类'
class jingxuanjiazhuang(BaseModel):
    __doc__ = u'''jingxuanjiazhuang'''
    __tablename__ = 'jingxuanjiazhuang'



    __authTables__={'shejishizhanghao':'shejishi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmumingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='家装项目' )
    fenggezhanshi=models.TextField   (  null=True, unique=False, verbose_name='风格展示' )
    huxingshiyong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='户型实用' )
    fenggefenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='风格分类' )
    pingfangdanjia=models.IntegerField  (  null=True, unique=False, verbose_name='平方单价' )
    xiangmumianji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目面积㎡' )
    fenggetese=models.TextField   (  null=True, unique=False, verbose_name='风格特色' )
    jiajuyuruanzhuang=models.TextField   (  null=True, unique=False, verbose_name='家具与软装' )
    cailiaoyugongyi=models.TextField   (  null=True, unique=False, verbose_name='材料与工艺' )
    shejishizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计师账号' )
    shejishixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计师姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    totalscore=models.FloatField   (  null=True, unique=False,default='0', verbose_name='评分' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    xiangmumingcheng=VARCHAR
    fenggezhanshi=Text
    huxingshiyong=VARCHAR
    fenggefenlei=VARCHAR
    pingfangdanjia=Integer
    xiangmumianji=VARCHAR
    fenggetese=Text
    jiajuyuruanzhuang=Text
    cailiaoyugongyi=Text
    shejishizhanghao=VARCHAR
    shejishixingming=VARCHAR
    lianxidianhua=VARCHAR
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    totalscore=Float
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'jingxuanjiazhuang'
        verbose_name = verbose_name_plural = '精选家装'
class jingxuangongzhuang(BaseModel):
    __doc__ = u'''jingxuangongzhuang'''
    __tablename__ = 'jingxuangongzhuang'



    __authTables__={'shejishizhanghao':'shejishi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmumingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='工装项目' )
    fenggezhanshi=models.TextField   (  null=True, unique=False, verbose_name='风格展示' )
    huxingshiyong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='户型实用' )
    fenggefenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='风格分类' )
    pingfangdanjia=models.IntegerField  (  null=True, unique=False, verbose_name='平方单价' )
    xiangmumianji=models.FloatField   (  null=True, unique=False, verbose_name='项目面积㎡' )
    cailiaoyugongyi=models.TextField   (  null=True, unique=False, verbose_name='材料与工艺' )
    fenggejieshao=models.TextField   (  null=True, unique=False, verbose_name='风格介绍' )
    shejishizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计师账号' )
    shejishixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计师姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    totalscore=models.FloatField   (  null=True, unique=False,default='0', verbose_name='评分' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    xiangmumingcheng=VARCHAR
    fenggezhanshi=Text
    huxingshiyong=VARCHAR
    fenggefenlei=VARCHAR
    pingfangdanjia=Integer
    xiangmumianji=Float
    cailiaoyugongyi=Text
    fenggejieshao=Text
    shejishizhanghao=VARCHAR
    shejishixingming=VARCHAR
    lianxidianhua=VARCHAR
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    totalscore=Float
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'jingxuangongzhuang'
        verbose_name = verbose_name_plural = '精选工装'
class gerendingzhi(BaseModel):
    __doc__ = u'''gerendingzhi'''
    __tablename__ = 'gerendingzhi'



    __authTables__={'shejishizhanghao':'shejishi','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dingzhibianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='定制编号' )
    xiangmumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='定制项目' )
    dingzhileixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='定制类型' )
    shejishizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计师账号' )
    shejishixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计师姓名' )
    fenggefenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='风格分类' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    dingzhimianji=models.FloatField   ( null=False, unique=False, verbose_name='定制面积' )
    dingzhishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='定制时间' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    shoujihao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号' )
    dingzhixuqiu=models.TextField   ( null=False, unique=False, verbose_name='定制需求' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    dingzhibianhao=VARCHAR
    xiangmumingcheng=VARCHAR
    dingzhileixing=VARCHAR
    shejishizhanghao=VARCHAR
    shejishixingming=VARCHAR
    fenggefenlei=VARCHAR
    lianxidianhua=VARCHAR
    dingzhimianji=Float
    dingzhishijian=DateTime
    fengmian=Text
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    shoujihao=VARCHAR
    dingzhixuqiu=Text
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'gerendingzhi'
        verbose_name = verbose_name_plural = '个人定制'
class shejileixing(BaseModel):
    __doc__ = u'''shejileixing'''
    __tablename__ = 'shejileixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shejileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计类型' )
    '''
    shejileixing=VARCHAR
    '''
    class Meta:
        db_table = 'shejileixing'
        verbose_name = verbose_name_plural = '设计类型'
class shejizhuanqu(BaseModel):
    __doc__ = u'''shejizhuanqu'''
    __tablename__ = 'shejizhuanqu'



    __authTables__={'shejishizhanghao':'shejishi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shejizhuti=models.CharField ( max_length=255,null=False, unique=False, verbose_name='设计主题' )
    xiaoguozhanshi=models.TextField   (  null=True, unique=False, verbose_name='效果展示' )
    shejileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计类型' )
    lingganlaiyuan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='灵感来源' )
    shejiyuansu=models.TextField   (  null=True, unique=False, verbose_name='设计元素' )
    gongnengbuju=models.TextField   (  null=True, unique=False, verbose_name='功能布局' )
    jishuyugongyi=models.TextField   (  null=True, unique=False, verbose_name='技术与工艺' )
    shejixiangqing=models.TextField   (  null=True, unique=False, verbose_name='设计详情' )
    shejishizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计师账号' )
    shejishixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设计师姓名' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    shejizhuti=VARCHAR
    xiaoguozhanshi=Text
    shejileixing=VARCHAR
    lingganlaiyuan=VARCHAR
    shejiyuansu=Text
    gongnengbuju=Text
    jishuyugongyi=Text
    shejixiangqing=Text
    shejishizhanghao=VARCHAR
    shejishixingming=VARCHAR
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'shejizhuanqu'
        verbose_name = verbose_name_plural = '设计专区'
class cailiaofenlei(BaseModel):
    __doc__ = u'''cailiaofenlei'''
    __tablename__ = 'cailiaofenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cailiaofenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='材料分类' )
    '''
    cailiaofenlei=VARCHAR
    '''
    class Meta:
        db_table = 'cailiaofenlei'
        verbose_name = verbose_name_plural = '材料分类'
class zhuangxiucailiao(BaseModel):
    __doc__ = u'''zhuangxiucailiao'''
    __tablename__ = 'zhuangxiucailiao'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    cailiaobianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='材料编号' )
    cailiaomingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='材料名称' )
    cailiaofenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='材料分类' )
    cailiaozhaopian=models.TextField   (  null=True, unique=False, verbose_name='材料照片' )
    cailiaojiage=models.FloatField   (  null=True, unique=False, verbose_name='材料价格' )
    cailiaoyongtu=models.TextField   (  null=True, unique=False, verbose_name='材料用途' )
    cailiaoxiangqing=models.TextField   (  null=True, unique=False, verbose_name='材料详情' )
    onelimittimes=models.IntegerField  (  null=True, unique=False, verbose_name='单限' )
    alllimittimes=models.IntegerField  (  null=True, unique=False, verbose_name='库存' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    price=models.FloatField   ( null=False, unique=False, verbose_name='价格' )
    onshelves=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='是否上架(1:上架，0:下架)' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    cailiaobianhao=VARCHAR
    cailiaomingcheng=VARCHAR
    cailiaofenlei=VARCHAR
    cailiaozhaopian=Text
    cailiaojiage=Float
    cailiaoyongtu=Text
    cailiaoxiangqing=Text
    onelimittimes=Integer
    alllimittimes=Integer
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    price=Float
    onshelves=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'zhuangxiucailiao'
        verbose_name = verbose_name_plural = '装修材料'
class jiajufenlei(BaseModel):
    __doc__ = u'''jiajufenlei'''
    __tablename__ = 'jiajufenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiajufenlei=models.CharField ( max_length=255, null=True,unique=True, verbose_name='家具分类' )
    '''
    jiajufenlei=VARCHAR
    '''
    class Meta:
        db_table = 'jiajufenlei'
        verbose_name = verbose_name_plural = '家具分类'
class jiajushangpin(BaseModel):
    __doc__ = u'''jiajushangpin'''
    __tablename__ = 'jiajushangpin'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='商品编号' )
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    jiajufenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='家具分类' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    shangpinjieshao=models.TextField   (  null=True, unique=False, verbose_name='商品介绍' )
    onelimittimes=models.IntegerField  (  null=True, unique=False, verbose_name='单限' )
    alllimittimes=models.IntegerField  (  null=True, unique=False, verbose_name='库存' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    price=models.FloatField   ( null=False, unique=False, verbose_name='价格' )
    onshelves=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='是否上架(1:上架，0:下架)' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    shangpinbianhao=VARCHAR
    shangpinmingcheng=VARCHAR
    tupian=Text
    jiajufenlei=VARCHAR
    pinpai=VARCHAR
    guige=VARCHAR
    shangpinjieshao=Text
    onelimittimes=Integer
    alllimittimes=Integer
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    price=Float
    onshelves=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'jiajushangpin'
        verbose_name = verbose_name_plural = '家具商品'
class chatmessage(BaseModel):
    __doc__ = u'''chatmessage'''
    __tablename__ = 'chatmessage'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    uid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户ID' )
    fid=models.BigIntegerField  ( null=False, unique=False, verbose_name='好友用户ID' )
    content=models.CharField ( max_length=255, null=True, unique=False, verbose_name='内容' )
    format=models.IntegerField  (  null=True, unique=False, verbose_name='格式(1:文字，2:图片)' )
    isread=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='消息已读(0:未读，1:已读)' )
    '''
    uid=BigInteger
    fid=BigInteger
    content=VARCHAR
    format=Integer
    isread=Integer
    '''
    class Meta:
        db_table = 'chatmessage'
        verbose_name = verbose_name_plural = '消息表'
class friend(BaseModel):
    __doc__ = u'''friend'''
    __tablename__ = 'friend'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    uid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户ID' )
    fid=models.BigIntegerField  ( null=False, unique=False, verbose_name='好友用户ID' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    role=models.CharField ( max_length=255, null=True, unique=False, verbose_name='角色' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    alias=models.CharField ( max_length=255, null=True, unique=False, verbose_name='别名' )
    type=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='类型(0:好友申请，1:好友，2:消息)' )
    '''
    uid=BigInteger
    fid=BigInteger
    name=VARCHAR
    picture=Text
    role=VARCHAR
    tablename=VARCHAR
    alias=VARCHAR
    type=Integer
    '''
    class Meta:
        db_table = 'friend'
        verbose_name = verbose_name_plural = '好友表'
class chat(BaseModel):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    adminid=models.BigIntegerField  (  null=True, unique=False, verbose_name='管理员id' )
    ask=models.TextField   (  null=True, unique=False, verbose_name='提问' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复' )
    isreply=models.IntegerField  (  null=True, unique=False, verbose_name='是否回复' )
    isread=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='已读/未读(1:已读,0:未读)' )
    uname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户头像' )
    uimage=models.TextField   (  null=True, unique=False, verbose_name='用户名' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='内容类型(1:文本,2:图片,3:视频,4:文件,5:表情)' )
    '''
    userid=BigInteger
    adminid=BigInteger
    ask=Text
    reply=Text
    isreply=Integer
    isread=Integer
    uname=VARCHAR
    uimage=Text
    type=Integer
    '''
    class Meta:
        db_table = 'chat'
        verbose_name = verbose_name_plural = '在线客服'
class cart(BaseModel):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='jiajushangpin', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   (  null=True, unique=False, verbose_name='单价' )
    '''
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=Text
    buynumber=Integer
    price=Float
    '''
    class Meta:
        db_table = 'cart'
        verbose_name = verbose_name_plural = '购物车表'
class orders(BaseModel):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    orderid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='订单编号' )
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='jiajushangpin', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='商品图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   ( null=False, unique=False,default='0', verbose_name='价格' )
    total=models.FloatField   ( null=False, unique=False,default='0', verbose_name='总价格' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='支付类型' )
    status=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    address=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    tel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    consignee=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货人' )
    logistics=models.TextField   (  null=True, unique=False, verbose_name='物流' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    role=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户角色' )
    returnreason=models.CharField ( max_length=255, null=True, unique=False, verbose_name='退货原因' )
    '''
    orderid=VARCHAR
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=Text
    buynumber=Integer
    price=Float
    total=Float
    type=Integer
    status=VARCHAR
    address=VARCHAR
    tel=VARCHAR
    consignee=VARCHAR
    logistics=Text
    remark=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    role=VARCHAR
    returnreason=VARCHAR
    '''
    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '订单'
class address(BaseModel):
    __doc__ = u'''address'''
    __tablename__ = 'address'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    address=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收货人' )
    phone=models.CharField ( max_length=255,null=False, unique=False, verbose_name='电话' )
    isdefault=models.CharField ( max_length=255,null=False, unique=False, verbose_name='是否默认地址[是/否]' )
    '''
    userid=BigInteger
    address=VARCHAR
    name=VARCHAR
    phone=VARCHAR
    isdefault=VARCHAR
    '''
    class Meta:
        db_table = 'address'
        verbose_name = verbose_name_plural = '地址'
class chargerecord(BaseModel):
    __doc__ = u'''chargerecord'''
    __tablename__ = 'chargerecord'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    username=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
    role=models.CharField ( max_length=255,null=False, unique=False, verbose_name='角色' )
    amount=models.FloatField   ( null=False, unique=False, verbose_name='金额' )
    '''
    userid=BigInteger
    username=VARCHAR
    role=VARCHAR
    amount=Float
    '''
    class Meta:
        db_table = 'chargerecord'
        verbose_name = verbose_name_plural = '充值记录表'
class newstype(BaseModel):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    typename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类名称' )
    '''
    typename=VARCHAR
    '''
    class Meta:
        db_table = 'newstype'
        verbose_name = verbose_name_plural = '装修资讯分类'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    typename=VARCHAR
    name=VARCHAR
    headportrait=Text
    clicknum=Integer
    clicktime=DateTime
    thumbsupnum=Integer
    crazilynum=Integer
    storeupnum=Integer
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '装修资讯'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class messages(BaseModel):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'#表属性hasMessage为是，新增留言板表messages,字段content（内容），userid（用户id）
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='留言人id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    content=models.TextField   ( null=False, unique=False, verbose_name='留言内容' )
    cpicture=models.TextField   (  null=True, unique=False, verbose_name='留言图片' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    rpicture=models.TextField   (  null=True, unique=False, verbose_name='回复图片' )
    '''
    userid=BigInteger
    username=VARCHAR
    avatarurl=Text
    content=Text
    cpicture=Text
    reply=Text
    rpicture=Text
    '''
    class Meta:
        db_table = 'messages'
        verbose_name = verbose_name_plural = '意见反馈'
class discussjingxuanjiazhuang(BaseModel):
    __doc__ = u'''discussjingxuanjiazhuang'''
    __tablename__ = 'discussjingxuanjiazhuang'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    score=models.FloatField   (  null=True, unique=False, verbose_name='评分' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    score=Float
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussjingxuanjiazhuang'
        verbose_name = verbose_name_plural = '精选家装评论表'
class discussjingxuangongzhuang(BaseModel):
    __doc__ = u'''discussjingxuangongzhuang'''
    __tablename__ = 'discussjingxuangongzhuang'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    score=models.FloatField   (  null=True, unique=False, verbose_name='评分' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    score=Float
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussjingxuangongzhuang'
        verbose_name = verbose_name_plural = '精选工装评论表'
class discusszhuangxiucailiao(BaseModel):
    __doc__ = u'''discusszhuangxiucailiao'''
    __tablename__ = 'discusszhuangxiucailiao'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discusszhuangxiucailiao'
        verbose_name = verbose_name_plural = '装修材料评论表'
class discussjiajushangpin(BaseModel):
    __doc__ = u'''discussjiajushangpin'''
    __tablename__ = 'discussjiajushangpin'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussjiajushangpin'
        verbose_name = verbose_name_plural = '家具商品评论表'
