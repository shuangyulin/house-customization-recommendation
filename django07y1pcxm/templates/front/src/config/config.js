export default {
	baseUrl: 'http://localhost:8080/django07y1pcxm/',
	name: '/django07y1pcxm',
	indexNav: [
		{
			name: '精选家装',
			url: '/index/jingxuanjiazhuang',
		},
		{
			name: '精选工装',
			url: '/index/jingxuangongzhuang',
		},
		{
			name: '设计专区',
			url: '/index/shejizhuanqu',
		},
		{
			name: '装修材料',
			url: '/index/zhuangxiucailiao',
		},
		{
			name: '家具商品',
			url: '/index/jiajushangpin',
		},
		{
			name: '装修资讯',
			url: '/index/news'
		},
		{
			name: '意见反馈',
			url: '/index/messages'
		},
	],
	cateList: [
		{
			name: '精选家装',
			refTable: 'fenggefenlei',
			refColumn: 'fenggefenlei',
		},
		{
			name: '精选工装',
			refTable: 'fenggefenlei',
			refColumn: 'fenggefenlei',
		},
		{
			name: '装修资讯',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
