import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Messages from '../pages/messages/list'
import Storeup from '../pages/storeup/list'
import AddrList from '../pages/shop-address/list'
import AddrAdd from '../pages/shop-address/addOrUpdate'
import Order from '../pages/shop-order/list'
import OrderConfirm from '../pages/shop-order/confirm'
import Cart from '../pages/shop-cart/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import shejishiList from '../pages/shejishi/list'
import shejishiDetail from '../pages/shejishi/detail'
import shejishiAdd from '../pages/shejishi/add'
import fenggefenleiList from '../pages/fenggefenlei/list'
import fenggefenleiDetail from '../pages/fenggefenlei/detail'
import fenggefenleiAdd from '../pages/fenggefenlei/add'
import jingxuanjiazhuangList from '../pages/jingxuanjiazhuang/list'
import jingxuanjiazhuangDetail from '../pages/jingxuanjiazhuang/detail'
import jingxuanjiazhuangAdd from '../pages/jingxuanjiazhuang/add'
import jingxuangongzhuangList from '../pages/jingxuangongzhuang/list'
import jingxuangongzhuangDetail from '../pages/jingxuangongzhuang/detail'
import jingxuangongzhuangAdd from '../pages/jingxuangongzhuang/add'
import gerendingzhiList from '../pages/gerendingzhi/list'
import gerendingzhiDetail from '../pages/gerendingzhi/detail'
import gerendingzhiAdd from '../pages/gerendingzhi/add'
import shejileixingList from '../pages/shejileixing/list'
import shejileixingDetail from '../pages/shejileixing/detail'
import shejileixingAdd from '../pages/shejileixing/add'
import shejizhuanquList from '../pages/shejizhuanqu/list'
import shejizhuanquDetail from '../pages/shejizhuanqu/detail'
import shejizhuanquAdd from '../pages/shejizhuanqu/add'
import cailiaofenleiList from '../pages/cailiaofenlei/list'
import cailiaofenleiDetail from '../pages/cailiaofenlei/detail'
import cailiaofenleiAdd from '../pages/cailiaofenlei/add'
import zhuangxiucailiaoList from '../pages/zhuangxiucailiao/list'
import zhuangxiucailiaoDetail from '../pages/zhuangxiucailiao/detail'
import zhuangxiucailiaoAdd from '../pages/zhuangxiucailiao/add'
import jiajufenleiList from '../pages/jiajufenlei/list'
import jiajufenleiDetail from '../pages/jiajufenlei/detail'
import jiajufenleiAdd from '../pages/jiajufenlei/add'
import jiajushangpinList from '../pages/jiajushangpin/list'
import jiajushangpinDetail from '../pages/jiajushangpin/detail'
import jiajushangpinAdd from '../pages/jiajushangpin/add'
import chatmessageList from '../pages/chatmessage/list'
import chatmessageDetail from '../pages/chatmessage/detail'
import chatmessageAdd from '../pages/chatmessage/add'
import friendList from '../pages/friend/list'
import friendDetail from '../pages/friend/detail'
import friendAdd from '../pages/friend/add'
import chargerecordList from '../pages/chargerecord/list'
import chargerecordDetail from '../pages/chargerecord/detail'
import chargerecordAdd from '../pages/chargerecord/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import discussjingxuanjiazhuangList from '../pages/discussjingxuanjiazhuang/list'
import discussjingxuanjiazhuangDetail from '../pages/discussjingxuanjiazhuang/detail'
import discussjingxuanjiazhuangAdd from '../pages/discussjingxuanjiazhuang/add'
import discussjingxuangongzhuangList from '../pages/discussjingxuangongzhuang/list'
import discussjingxuangongzhuangDetail from '../pages/discussjingxuangongzhuang/detail'
import discussjingxuangongzhuangAdd from '../pages/discussjingxuangongzhuang/add'
import discusszhuangxiucailiaoList from '../pages/discusszhuangxiucailiao/list'
import discusszhuangxiucailiaoDetail from '../pages/discusszhuangxiucailiao/detail'
import discusszhuangxiucailiaoAdd from '../pages/discusszhuangxiucailiao/add'
import discussjiajushangpinList from '../pages/discussjiajushangpin/list'
import discussjiajushangpinDetail from '../pages/discussjiajushangpin/detail'
import discussjiajushangpinAdd from '../pages/discussjiajushangpin/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'messages',
					component: Messages
				},
				{
					path: 'storeup',
					component: Storeup
				},
                {
                    path: 'shop-address/list',
                    component: AddrList
                },
                {
                    path: 'shop-address/addOrUpdate',
                    component: AddrAdd
                },
				{
					path: 'shop-order/order',
					component: Order
				},
				{
					path: 'cart',
					component: Cart
				},
				{
					path: 'shop-order/orderConfirm',
					component: OrderConfirm
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'shejishi',
					component: shejishiList
				},
				{
					path: 'shejishiDetail',
					component: shejishiDetail
				},
				{
					path: 'shejishiAdd',
					component: shejishiAdd
				},
				{
					path: 'fenggefenlei',
					component: fenggefenleiList
				},
				{
					path: 'fenggefenleiDetail',
					component: fenggefenleiDetail
				},
				{
					path: 'fenggefenleiAdd',
					component: fenggefenleiAdd
				},
				{
					path: 'jingxuanjiazhuang',
					component: jingxuanjiazhuangList
				},
				{
					path: 'jingxuanjiazhuangDetail',
					component: jingxuanjiazhuangDetail
				},
				{
					path: 'jingxuanjiazhuangAdd',
					component: jingxuanjiazhuangAdd
				},
				{
					path: 'jingxuangongzhuang',
					component: jingxuangongzhuangList
				},
				{
					path: 'jingxuangongzhuangDetail',
					component: jingxuangongzhuangDetail
				},
				{
					path: 'jingxuangongzhuangAdd',
					component: jingxuangongzhuangAdd
				},
				{
					path: 'gerendingzhi',
					component: gerendingzhiList
				},
				{
					path: 'gerendingzhiDetail',
					component: gerendingzhiDetail
				},
				{
					path: 'gerendingzhiAdd',
					component: gerendingzhiAdd
				},
				{
					path: 'shejileixing',
					component: shejileixingList
				},
				{
					path: 'shejileixingDetail',
					component: shejileixingDetail
				},
				{
					path: 'shejileixingAdd',
					component: shejileixingAdd
				},
				{
					path: 'shejizhuanqu',
					component: shejizhuanquList
				},
				{
					path: 'shejizhuanquDetail',
					component: shejizhuanquDetail
				},
				{
					path: 'shejizhuanquAdd',
					component: shejizhuanquAdd
				},
				{
					path: 'cailiaofenlei',
					component: cailiaofenleiList
				},
				{
					path: 'cailiaofenleiDetail',
					component: cailiaofenleiDetail
				},
				{
					path: 'cailiaofenleiAdd',
					component: cailiaofenleiAdd
				},
				{
					path: 'zhuangxiucailiao',
					component: zhuangxiucailiaoList
				},
				{
					path: 'zhuangxiucailiaoDetail',
					component: zhuangxiucailiaoDetail
				},
				{
					path: 'zhuangxiucailiaoAdd',
					component: zhuangxiucailiaoAdd
				},
				{
					path: 'jiajufenlei',
					component: jiajufenleiList
				},
				{
					path: 'jiajufenleiDetail',
					component: jiajufenleiDetail
				},
				{
					path: 'jiajufenleiAdd',
					component: jiajufenleiAdd
				},
				{
					path: 'jiajushangpin',
					component: jiajushangpinList
				},
				{
					path: 'jiajushangpinDetail',
					component: jiajushangpinDetail
				},
				{
					path: 'jiajushangpinAdd',
					component: jiajushangpinAdd
				},
				{
					path: 'chatmessage',
					component: chatmessageList
				},
				{
					path: 'chatmessageDetail',
					component: chatmessageDetail
				},
				{
					path: 'chatmessageAdd',
					component: chatmessageAdd
				},
				{
					path: 'friend',
					component: friendList
				},
				{
					path: 'friendDetail',
					component: friendDetail
				},
				{
					path: 'friendAdd',
					component: friendAdd
				},
				{
					path: 'chargerecord',
					component: chargerecordList
				},
				{
					path: 'chargerecordDetail',
					component: chargerecordDetail
				},
				{
					path: 'chargerecordAdd',
					component: chargerecordAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'discussjingxuanjiazhuang',
					component: discussjingxuanjiazhuangList
				},
				{
					path: 'discussjingxuanjiazhuangDetail',
					component: discussjingxuanjiazhuangDetail
				},
				{
					path: 'discussjingxuanjiazhuangAdd',
					component: discussjingxuanjiazhuangAdd
				},
				{
					path: 'discussjingxuangongzhuang',
					component: discussjingxuangongzhuangList
				},
				{
					path: 'discussjingxuangongzhuangDetail',
					component: discussjingxuangongzhuangDetail
				},
				{
					path: 'discussjingxuangongzhuangAdd',
					component: discussjingxuangongzhuangAdd
				},
				{
					path: 'discusszhuangxiucailiao',
					component: discusszhuangxiucailiaoList
				},
				{
					path: 'discusszhuangxiucailiaoDetail',
					component: discusszhuangxiucailiaoDetail
				},
				{
					path: 'discusszhuangxiucailiaoAdd',
					component: discusszhuangxiucailiaoAdd
				},
				{
					path: 'discussjiajushangpin',
					component: discussjiajushangpinList
				},
				{
					path: 'discussjiajushangpinDetail',
					component: discussjiajushangpinDetail
				},
				{
					path: 'discussjiajushangpinAdd',
					component: discussjiajushangpinAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
