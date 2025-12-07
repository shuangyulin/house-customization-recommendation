<template>
	<div class="home-preview">




		<!-- 新闻资讯 -->
		<div id="animate_newsnews" class="news animate__animated">
			<div class="news_title_box">
				<span class="news_title">装修资讯</span>
				<span class="news_subhead">{{'news'.toUpperCase()}}</span>
			</div>
			<!-- 样式五 -->
			<div v-if="newsList.length" class="list list5 index-pv1">
				<div @click="toDetail('newsDetail', newsList[0])" v-if="newsList.length>0" class="list-item animation-box">
					<img :src="baseUrl + newsList[0].picture" alt="">
					<div class="infoBox">
						<div class="name line1">{{newsList[0].title}}</div>
						<div class="desc line3">{{newsList[0].introduction}}</div>
						<div class="time_item">
							<span class="icon iconfont icon-shijian21"></span>
							<span class="label">发布时间：</span>
							<span class="text">{{newsList[0].addtime.split(' ')[0]}}</span>
						</div>
						<div class="publisher_item">
							<span class="icon iconfont icon-geren16"></span>
							<span class="label">发布人：</span>
							<span class="text">{{newsList[0].name}}</span>
						</div>
						<div class="like_item">
							<span class="icon iconfont icon-zan10"></span>
							<span class="label">点赞：</span>
							<span class="text">{{newsList[0].thumbsupnum}}</span>
						</div>
						<div class="collect_item">
							<span class="icon iconfont icon-shoucang10"></span>
							<span class="label">收藏：</span>
							<span class="text">{{newsList[0].storeupnum}}</span>
						</div>
						<div class="view_item">
							<span class="icon iconfont icon-chakan2"></span>
							<span class="label">点击量：</span>
							<span class="text">{{newsList[0].clicknum}}</span>
						</div>
					</div>
				</div>
				<div class="list-body">
					<div @click="toDetail('newsDetail', newsList[1])" v-if="newsList.length>1" class="list-item1 animation-box">
						<div class="name line1">{{newsList[1].title}}</div>
						<div class="desc line3">{{newsList[1].introduction}}</div>
						<div class="time_item">
							<span class="icon iconfont icon-shijian21"></span>
							<span class="label">发布时间：</span>
							<span class="text">{{newsList[1].addtime.split(' ')[0]}}</span>
						</div>
						<div class="publisher_item">
							<span class="icon iconfont icon-geren16"></span>
							<span class="label">发布人：</span>
							<span class="text">{{newsList[1].name}}</span>
						</div>
						<div class="like_item">
							<span class="icon iconfont icon-zan10"></span>
							<span class="label">点赞：</span>
							<span class="text">{{newsList[1].thumbsupnum}}</span>
						</div>
						<div class="collect_item">
							<span class="icon iconfont icon-shoucang10"></span>
							<span class="label">收藏：</span>
							<span class="text">{{newsList[1].storeupnum}}</span>
						</div>
						<div class="view_item">
							<span class="icon iconfont icon-chakan2"></span>
							<span class="label">浏览次数：</span>
							<span class="text">{{newsList[1].clicknum}}</span>
						</div>
					</div>
					<div @click="toDetail('newsDetail', newsList[2])" v-if="newsList.length>2" class="list-item2 animation-box">
						<div class="name line1">{{newsList[2].title}}</div>
						<div class="desc line3">{{newsList[2].introduction}}</div>
						<div class="time_item">
							<span class="icon iconfont icon-shijian21"></span>
							<span class="label">发布时间：</span>
							<span class="text">{{newsList[2].addtime.split(' ')[0]}}</span>
						</div>
						<div class="publisher_item">
							<span class="icon iconfont icon-geren16"></span>
							<span class="label">发布人：</span>
							<span class="text">{{newsList[2].name}}</span>
						</div>
						<div class="like_item">
							<span class="icon iconfont icon-zan10"></span>
							<span class="label">点赞：</span>
							<span class="text">{{newsList[2].thumbsupnum}}</span>
						</div>
						<div class="collect_item">
							<span class="icon iconfont icon-shoucang10"></span>
							<span class="label">收藏：</span>
							<span class="text">{{newsList[2].storeupnum}}</span>
						</div>
						<div class="view_item">
							<span class="icon iconfont icon-chakan2"></span>
							<span class="label">浏览次数：</span>
							<span class="text">{{newsList[2].clicknum}}</span>
						</div>
					</div>
					<div @click="toDetail('newsDetail', newsList[3])" v-if="newsList.length>3" class="list-item3 animation-box">
						<div class="name line1">{{newsList[3].title}}</div>
						<div class="desc line3">{{newsList[3].introduction}}</div>
						<div class="time_item">
							<span class="icon iconfont icon-shijian21"></span>
							<span class="label">发布时间：</span>
							<span class="text">{{newsList[3].addtime.split(' ')[0]}}</span>
						</div>
						<div class="publisher_item">
							<span class="icon iconfont icon-geren16"></span>
							<span class="label">发布人：</span>
							<span class="text">{{newsList[3].name}}</span>
						</div>
						<div class="like_item">
							<span class="icon iconfont icon-zan10"></span>
							<span class="label">点赞：</span>
							<span class="text">{{newsList[3].thumbsupnum}}</span>
						</div>
						<div class="collect_item">
							<span class="icon iconfont icon-shoucang10"></span>
							<span class="label">收藏：</span>
							<span class="text">{{newsList[3].storeupnum}}</span>
						</div>
						<div class="view_item">
							<span class="icon iconfont icon-chakan2"></span>
							<span class="label">浏览次数：</span>
							<span class="text">{{newsList[3].clicknum}}</span>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('news')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 新闻资讯 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendjingxuanjiazhuang" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">精选家装推荐</span>
				<span class="recommend_subhead">{{'jingxuanjiazhuang'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div class="list list21 index-pv1">
				<div class="list-body-top">
					<div class="tab-title">精选家装推荐</div>
					<div class="tab-right" @click="moreBtn('jingxuanjiazhuang')">
						<span class="text">查看更多</span>
						<span class="icon iconfont icon-gengduo1"></span>
					</div>
				</div>
				<div class="list-body">
					<div v-if="index<Number(4)" class="list-item" v-for="(item,index) in jingxuanjiazhuangRecommend" :key="index" @click="toDetail('jingxuanjiazhuangDetail', item)">
						<div class="img">
							<img v-if="preHttp(item.fenggezhanshi)" :src="item.fenggezhanshi.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (item.fenggezhanshi?item.fenggezhanshi.split(',')[0]:'')" alt="" />
						</div>
						<div class="infoBox">
							<div class="name">{{item.xiangmumingcheng}}</div>
							<div class="name">户型实用:{{item.huxingshiyong}}</div>
							<div class="bottomInfo">
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
								<div class="publisher_item">
									<span class="icon iconfont icon-touxiang18"></span>
									<span class="label">发布人：</span>
									<span class="text">{{item.shejishizhanghao}}</span>
								</div>
								<div class="like_item">
									<span class="icon iconfont icon-zan10"></span>
									<span class="label">点赞：</span>
									<span class="text">{{item.thumbsupnum}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏：</span>
									<span class="text">{{item.storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-liulan04"></span>
									<span class="label">浏览次数：</span>
									<span class="text">{{item.clicknum}}</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('jingxuanjiazhuang')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendjingxuangongzhuang" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">精选工装推荐</span>
				<span class="recommend_subhead">{{'jingxuangongzhuang'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div class="list list21 index-pv1">
				<div class="list-body-top">
					<div class="tab-title">精选工装推荐</div>
					<div class="tab-right" @click="moreBtn('jingxuangongzhuang')">
						<span class="text">查看更多</span>
						<span class="icon iconfont icon-gengduo1"></span>
					</div>
				</div>
				<div class="list-body">
					<div v-if="index<Number(4)" class="list-item" v-for="(item,index) in jingxuangongzhuangRecommend" :key="index" @click="toDetail('jingxuangongzhuangDetail', item)">
						<div class="img">
							<img v-if="preHttp(item.fenggezhanshi)" :src="item.fenggezhanshi.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (item.fenggezhanshi?item.fenggezhanshi.split(',')[0]:'')" alt="" />
						</div>
						<div class="infoBox">
							<div class="name">{{item.xiangmumingcheng}}</div>
							<div class="name">户型实用:{{item.huxingshiyong}}</div>
							<div class="bottomInfo">
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
								<div class="publisher_item">
									<span class="icon iconfont icon-touxiang18"></span>
									<span class="label">发布人：</span>
									<span class="text">{{item.shejishizhanghao}}</span>
								</div>
								<div class="like_item">
									<span class="icon iconfont icon-zan10"></span>
									<span class="label">点赞：</span>
									<span class="text">{{item.thumbsupnum}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏：</span>
									<span class="text">{{item.storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-liulan04"></span>
									<span class="label">浏览次数：</span>
									<span class="text">{{item.clicknum}}</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('jingxuangongzhuang')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendzhuangxiucailiao" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">装修材料推荐</span>
				<span class="recommend_subhead">{{'zhuangxiucailiao'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div class="list list21 index-pv1">
				<div class="list-body-top">
					<div class="tab-title">装修材料推荐</div>
					<div class="tab-right" @click="moreBtn('zhuangxiucailiao')">
						<span class="text">查看更多</span>
						<span class="icon iconfont icon-gengduo1"></span>
					</div>
				</div>
				<div class="list-body">
					<div v-if="index<Number(4)" class="list-item" v-for="(item,index) in zhuangxiucailiaoRecommend" :key="index" @click="toDetail('zhuangxiucailiaoDetail', item)">
						<div class="img">
							<img v-if="preHttp(item.cailiaozhaopian)" :src="item.cailiaozhaopian.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (item.cailiaozhaopian?item.cailiaozhaopian.split(',')[0]:'')" alt="" />
						</div>
						<div class="infoBox">
							<div class="name">{{item.cailiaomingcheng}}</div>
							<div class="name">{{item.cailiaofenlei}}</div>
							<div class="bottomInfo">
								<div class="price">￥{{item.price}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
								<div class="like_item">
									<span class="icon iconfont icon-zan10"></span>
									<span class="label">点赞：</span>
									<span class="text">{{item.thumbsupnum}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏：</span>
									<span class="text">{{item.storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-liulan04"></span>
									<span class="label">浏览次数：</span>
									<span class="text">{{item.clicknum}}</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('zhuangxiucailiao')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendjiajushangpin" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">家具商品推荐</span>
				<span class="recommend_subhead">{{'jiajushangpin'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div class="list list21 index-pv1">
				<div class="list-body-top">
					<div class="tab-title">家具商品推荐</div>
					<div class="tab-right" @click="moreBtn('jiajushangpin')">
						<span class="text">查看更多</span>
						<span class="icon iconfont icon-gengduo1"></span>
					</div>
				</div>
				<div class="list-body">
					<div v-if="index<Number(4)" class="list-item" v-for="(item,index) in jiajushangpinRecommend" :key="index" @click="toDetail('jiajushangpinDetail', item)">
						<div class="img">
							<img v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
						</div>
						<div class="infoBox">
							<div class="name">{{item.shangpinmingcheng}}</div>
							<div class="name">品牌:{{item.pinpai}}</div>
							<div class="bottomInfo">
								<div class="price">￥{{item.price}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
								<div class="like_item">
									<span class="icon iconfont icon-zan10"></span>
									<span class="label">点赞：</span>
									<span class="text">{{item.thumbsupnum}}</span>
								</div>
								<div class="collect_item">
									<span class="icon iconfont icon-shoucang10"></span>
									<span class="label">收藏：</span>
									<span class="text">{{item.storeupnum}}</span>
								</div>
								<div class="view_item">
									<span class="icon iconfont icon-liulan04"></span>
									<span class="label">浏览次数：</span>
									<span class="text">{{item.clicknum}}</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('jiajushangpin')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
		<!-- 特价商品 -->
		<div id="animate_listjingxuangongzhuang" class="lists animate__animated">
			<div class="list_title_box">
				<span class="list_title">精选工装展示</span>
				<span class="list_subhead">{{'jingxuangongzhuang'.toUpperCase()}} SHOW</span>
			</div>
			<!-- 样式九 -->
			<div class="list list9 index-pv1">
				<div class="list-body-top">
					<div v-if="jingxuangongzhuangList.length>0" @click="toDetail('jingxuangongzhuangDetail', jingxuangongzhuangList[0])" class="list-item1 animation-box">
						<img v-if="preHttp(jingxuangongzhuangList[0].fenggezhanshi)" :src="jingxuangongzhuangList[0].fenggezhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (jingxuangongzhuangList[0].fenggezhanshi?jingxuangongzhuangList[0].fenggezhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jingxuangongzhuangList[0].xiangmumingcheng}}</div>
							<div class="name">户型实用:{{jingxuangongzhuangList[0].huxingshiyong}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jingxuangongzhuangList[0].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{jingxuangongzhuangList[0].shejishizhanghao}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jingxuangongzhuangList[0].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jingxuangongzhuangList[0].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jingxuangongzhuangList[0].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="jingxuangongzhuangList.length>1" @click="toDetail('jingxuangongzhuangDetail', jingxuangongzhuangList[1])" class="list-item2 animation-box">
						<img v-if="preHttp(jingxuangongzhuangList[1].fenggezhanshi)" :src="jingxuangongzhuangList[1].fenggezhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (jingxuangongzhuangList[1].fenggezhanshi?jingxuangongzhuangList[1].fenggezhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jingxuangongzhuangList[1].xiangmumingcheng}}</div>
							<div class="name">户型实用:{{jingxuangongzhuangList[1].huxingshiyong}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jingxuangongzhuangList[1].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{jingxuangongzhuangList[1].shejishizhanghao}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jingxuangongzhuangList[1].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jingxuangongzhuangList[1].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jingxuangongzhuangList[1].clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
				<div class="list-body-bottom">
					<div v-if="jingxuangongzhuangList.length>2" @click="toDetail('jingxuangongzhuangDetail', jingxuangongzhuangList[2])" class="list-item1 animation-box">
						<img v-if="preHttp(jingxuangongzhuangList[2].fenggezhanshi)" :src="jingxuangongzhuangList[2].fenggezhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl +  (jingxuangongzhuangList[2].fenggezhanshi?jingxuangongzhuangList[2].fenggezhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jingxuangongzhuangList[2].xiangmumingcheng}}</div>
							<div class="name">户型实用:{{jingxuangongzhuangList[2].huxingshiyong}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jingxuangongzhuangList[2].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{jingxuangongzhuangList[2].shejishizhanghao}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jingxuangongzhuangList[2].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jingxuangongzhuangList[2].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jingxuangongzhuangList[2].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="jingxuangongzhuangList.length>3" @click="toDetail('jingxuangongzhuangDetail', jingxuangongzhuangList[3])" class="list-item2 animation-box">
						<img v-if="preHttp(jingxuangongzhuangList[3].fenggezhanshi)" :src="jingxuangongzhuangList[3].fenggezhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (jingxuangongzhuangList[3].fenggezhanshi?jingxuangongzhuangList[3].fenggezhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jingxuangongzhuangList[3].xiangmumingcheng}}</div>
							<div class="name">户型实用:{{jingxuangongzhuangList[3].huxingshiyong}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jingxuangongzhuangList[3].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{jingxuangongzhuangList[3].shejishizhanghao}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jingxuangongzhuangList[3].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jingxuangongzhuangList[3].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jingxuangongzhuangList[3].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="jingxuangongzhuangList.length>4" @click="toDetail('jingxuangongzhuangDetail', jingxuangongzhuangList[4])" class="list-item3 animation-box">
						<img v-if="preHttp(jingxuangongzhuangList[4].fenggezhanshi)" :src="jingxuangongzhuangList[4].fenggezhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (jingxuangongzhuangList[4].fenggezhanshi?jingxuangongzhuangList[4].fenggezhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jingxuangongzhuangList[4].xiangmumingcheng}}</div>
							<div class="name">户型实用:{{jingxuangongzhuangList[4].huxingshiyong}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jingxuangongzhuangList[4].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{jingxuangongzhuangList[4].shejishizhanghao}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jingxuangongzhuangList[4].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jingxuangongzhuangList[4].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jingxuangongzhuangList[4].clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('jingxuangongzhuang')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
	

		</div>
		<!-- 特价商品 -->
		<!-- 特价商品 -->
		<div id="animate_listshejizhuanqu" class="lists animate__animated">
			<div class="list_title_box">
				<span class="list_title">设计专区展示</span>
				<span class="list_subhead">{{'shejizhuanqu'.toUpperCase()}} SHOW</span>
			</div>
			<!-- 样式九 -->
			<div class="list list9 index-pv1">
				<div class="list-body-top">
					<div v-if="shejizhuanquList.length>0" @click="toDetail('shejizhuanquDetail', shejizhuanquList[0])" class="list-item1 animation-box">
						<img v-if="preHttp(shejizhuanquList[0].xiaoguozhanshi)" :src="shejizhuanquList[0].xiaoguozhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shejizhuanquList[0].xiaoguozhanshi?shejizhuanquList[0].xiaoguozhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shejizhuanquList[0].shejizhuti}}</div>
							<div class="name">{{shejizhuanquList[0].shejileixing}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shejizhuanquList[0].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{shejizhuanquList[0].shejishizhanghao}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{shejizhuanquList[0].storeupnum}}</span>
							</div>
						</div>
					</div>
					<div v-if="shejizhuanquList.length>1" @click="toDetail('shejizhuanquDetail', shejizhuanquList[1])" class="list-item2 animation-box">
						<img v-if="preHttp(shejizhuanquList[1].xiaoguozhanshi)" :src="shejizhuanquList[1].xiaoguozhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shejizhuanquList[1].xiaoguozhanshi?shejizhuanquList[1].xiaoguozhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shejizhuanquList[1].shejizhuti}}</div>
							<div class="name">{{shejizhuanquList[1].shejileixing}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shejizhuanquList[1].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{shejizhuanquList[1].shejishizhanghao}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{shejizhuanquList[1].storeupnum}}</span>
							</div>
						</div>
					</div>
				</div>
				<div class="list-body-bottom">
					<div v-if="shejizhuanquList.length>2" @click="toDetail('shejizhuanquDetail', shejizhuanquList[2])" class="list-item1 animation-box">
						<img v-if="preHttp(shejizhuanquList[2].xiaoguozhanshi)" :src="shejizhuanquList[2].xiaoguozhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl +  (shejizhuanquList[2].xiaoguozhanshi?shejizhuanquList[2].xiaoguozhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shejizhuanquList[2].shejizhuti}}</div>
							<div class="name">{{shejizhuanquList[2].shejileixing}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shejizhuanquList[2].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{shejizhuanquList[2].shejishizhanghao}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{shejizhuanquList[2].storeupnum}}</span>
							</div>
						</div>
					</div>
					<div v-if="shejizhuanquList.length>3" @click="toDetail('shejizhuanquDetail', shejizhuanquList[3])" class="list-item2 animation-box">
						<img v-if="preHttp(shejizhuanquList[3].xiaoguozhanshi)" :src="shejizhuanquList[3].xiaoguozhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shejizhuanquList[3].xiaoguozhanshi?shejizhuanquList[3].xiaoguozhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shejizhuanquList[3].shejizhuti}}</div>
							<div class="name">{{shejizhuanquList[3].shejileixing}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shejizhuanquList[3].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{shejizhuanquList[3].shejishizhanghao}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{shejizhuanquList[3].storeupnum}}</span>
							</div>
						</div>
					</div>
					<div v-if="shejizhuanquList.length>4" @click="toDetail('shejizhuanquDetail', shejizhuanquList[4])" class="list-item3 animation-box">
						<img v-if="preHttp(shejizhuanquList[4].xiaoguozhanshi)" :src="shejizhuanquList[4].xiaoguozhanshi.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (shejizhuanquList[4].xiaoguozhanshi?shejizhuanquList[4].xiaoguozhanshi.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{shejizhuanquList[4].shejizhuti}}</div>
							<div class="name">{{shejizhuanquList[4].shejileixing}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{shejizhuanquList[4].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{shejizhuanquList[4].shejishizhanghao}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{shejizhuanquList[4].storeupnum}}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('shejizhuanqu')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
	

		</div>
		<!-- 特价商品 -->
		<!-- 特价商品 -->
		<div id="animate_listzhuangxiucailiao" class="lists animate__animated">
			<div class="list_title_box">
				<span class="list_title">装修材料展示</span>
				<span class="list_subhead">{{'zhuangxiucailiao'.toUpperCase()}} SHOW</span>
			</div>
			<!-- 样式九 -->
			<div class="list list9 index-pv1">
				<div class="list-body-top">
					<div v-if="zhuangxiucailiaoList.length>0" @click="toDetail('zhuangxiucailiaoDetail', zhuangxiucailiaoList[0])" class="list-item1 animation-box">
						<img v-if="preHttp(zhuangxiucailiaoList[0].cailiaozhaopian)" :src="zhuangxiucailiaoList[0].cailiaozhaopian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (zhuangxiucailiaoList[0].cailiaozhaopian?zhuangxiucailiaoList[0].cailiaozhaopian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{zhuangxiucailiaoList[0].cailiaomingcheng}}</div>
							<div class="name">{{zhuangxiucailiaoList[0].cailiaofenlei}}</div>
							<div class="price">￥{{zhuangxiucailiaoList[0].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{zhuangxiucailiaoList[0].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{zhuangxiucailiaoList[0].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{zhuangxiucailiaoList[0].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{zhuangxiucailiaoList[0].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="zhuangxiucailiaoList.length>1" @click="toDetail('zhuangxiucailiaoDetail', zhuangxiucailiaoList[1])" class="list-item2 animation-box">
						<img v-if="preHttp(zhuangxiucailiaoList[1].cailiaozhaopian)" :src="zhuangxiucailiaoList[1].cailiaozhaopian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (zhuangxiucailiaoList[1].cailiaozhaopian?zhuangxiucailiaoList[1].cailiaozhaopian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{zhuangxiucailiaoList[1].cailiaomingcheng}}</div>
							<div class="name">{{zhuangxiucailiaoList[1].cailiaofenlei}}</div>
							<div class="price">￥{{zhuangxiucailiaoList[1].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{zhuangxiucailiaoList[1].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{zhuangxiucailiaoList[1].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{zhuangxiucailiaoList[1].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{zhuangxiucailiaoList[1].clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
				<div class="list-body-bottom">
					<div v-if="zhuangxiucailiaoList.length>2" @click="toDetail('zhuangxiucailiaoDetail', zhuangxiucailiaoList[2])" class="list-item1 animation-box">
						<img v-if="preHttp(zhuangxiucailiaoList[2].cailiaozhaopian)" :src="zhuangxiucailiaoList[2].cailiaozhaopian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl +  (zhuangxiucailiaoList[2].cailiaozhaopian?zhuangxiucailiaoList[2].cailiaozhaopian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{zhuangxiucailiaoList[2].cailiaomingcheng}}</div>
							<div class="name">{{zhuangxiucailiaoList[2].cailiaofenlei}}</div>
							<div class="price">￥{{zhuangxiucailiaoList[2].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{zhuangxiucailiaoList[2].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{zhuangxiucailiaoList[2].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{zhuangxiucailiaoList[2].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{zhuangxiucailiaoList[2].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="zhuangxiucailiaoList.length>3" @click="toDetail('zhuangxiucailiaoDetail', zhuangxiucailiaoList[3])" class="list-item2 animation-box">
						<img v-if="preHttp(zhuangxiucailiaoList[3].cailiaozhaopian)" :src="zhuangxiucailiaoList[3].cailiaozhaopian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (zhuangxiucailiaoList[3].cailiaozhaopian?zhuangxiucailiaoList[3].cailiaozhaopian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{zhuangxiucailiaoList[3].cailiaomingcheng}}</div>
							<div class="name">{{zhuangxiucailiaoList[3].cailiaofenlei}}</div>
							<div class="price">￥{{zhuangxiucailiaoList[3].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{zhuangxiucailiaoList[3].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{zhuangxiucailiaoList[3].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{zhuangxiucailiaoList[3].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{zhuangxiucailiaoList[3].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="zhuangxiucailiaoList.length>4" @click="toDetail('zhuangxiucailiaoDetail', zhuangxiucailiaoList[4])" class="list-item3 animation-box">
						<img v-if="preHttp(zhuangxiucailiaoList[4].cailiaozhaopian)" :src="zhuangxiucailiaoList[4].cailiaozhaopian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (zhuangxiucailiaoList[4].cailiaozhaopian?zhuangxiucailiaoList[4].cailiaozhaopian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{zhuangxiucailiaoList[4].cailiaomingcheng}}</div>
							<div class="name">{{zhuangxiucailiaoList[4].cailiaofenlei}}</div>
							<div class="price">￥{{zhuangxiucailiaoList[4].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{zhuangxiucailiaoList[4].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{zhuangxiucailiaoList[4].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{zhuangxiucailiaoList[4].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{zhuangxiucailiaoList[4].clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('zhuangxiucailiao')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
	

		</div>
		<!-- 特价商品 -->
		<!-- 特价商品 -->
		<div id="animate_listjiajushangpin" class="lists animate__animated">
			<div class="list_title_box">
				<span class="list_title">家具商品展示</span>
				<span class="list_subhead">{{'jiajushangpin'.toUpperCase()}} SHOW</span>
			</div>
			<!-- 样式九 -->
			<div class="list list9 index-pv1">
				<div class="list-body-top">
					<div v-if="jiajushangpinList.length>0" @click="toDetail('jiajushangpinDetail', jiajushangpinList[0])" class="list-item1 animation-box">
						<img v-if="preHttp(jiajushangpinList[0].tupian)" :src="jiajushangpinList[0].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (jiajushangpinList[0].tupian?jiajushangpinList[0].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jiajushangpinList[0].shangpinmingcheng}}</div>
							<div class="name">品牌:{{jiajushangpinList[0].pinpai}}</div>
							<div class="price">￥{{jiajushangpinList[0].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jiajushangpinList[0].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jiajushangpinList[0].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jiajushangpinList[0].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jiajushangpinList[0].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="jiajushangpinList.length>1" @click="toDetail('jiajushangpinDetail', jiajushangpinList[1])" class="list-item2 animation-box">
						<img v-if="preHttp(jiajushangpinList[1].tupian)" :src="jiajushangpinList[1].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (jiajushangpinList[1].tupian?jiajushangpinList[1].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jiajushangpinList[1].shangpinmingcheng}}</div>
							<div class="name">品牌:{{jiajushangpinList[1].pinpai}}</div>
							<div class="price">￥{{jiajushangpinList[1].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jiajushangpinList[1].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jiajushangpinList[1].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jiajushangpinList[1].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jiajushangpinList[1].clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
				<div class="list-body-bottom">
					<div v-if="jiajushangpinList.length>2" @click="toDetail('jiajushangpinDetail', jiajushangpinList[2])" class="list-item1 animation-box">
						<img v-if="preHttp(jiajushangpinList[2].tupian)" :src="jiajushangpinList[2].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl +  (jiajushangpinList[2].tupian?jiajushangpinList[2].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jiajushangpinList[2].shangpinmingcheng}}</div>
							<div class="name">品牌:{{jiajushangpinList[2].pinpai}}</div>
							<div class="price">￥{{jiajushangpinList[2].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jiajushangpinList[2].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jiajushangpinList[2].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jiajushangpinList[2].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jiajushangpinList[2].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="jiajushangpinList.length>3" @click="toDetail('jiajushangpinDetail', jiajushangpinList[3])" class="list-item2 animation-box">
						<img v-if="preHttp(jiajushangpinList[3].tupian)" :src="jiajushangpinList[3].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (jiajushangpinList[3].tupian?jiajushangpinList[3].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jiajushangpinList[3].shangpinmingcheng}}</div>
							<div class="name">品牌:{{jiajushangpinList[3].pinpai}}</div>
							<div class="price">￥{{jiajushangpinList[3].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jiajushangpinList[3].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jiajushangpinList[3].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jiajushangpinList[3].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jiajushangpinList[3].clicknum}}</span>
							</div>
						</div>
					</div>
					<div v-if="jiajushangpinList.length>4" @click="toDetail('jiajushangpinDetail', jiajushangpinList[4])" class="list-item3 animation-box">
						<img v-if="preHttp(jiajushangpinList[4].tupian)" :src="jiajushangpinList[4].tupian.split(',')[0]" alt="" />
						<img v-else :src="baseUrl + (jiajushangpinList[4].tupian?jiajushangpinList[4].tupian.split(',')[0]:'')" alt="" />
						<div class="infoBox">
							<div class="name">{{jiajushangpinList[4].shangpinmingcheng}}</div>
							<div class="name">品牌:{{jiajushangpinList[4].pinpai}}</div>
							<div class="price">￥{{jiajushangpinList[4].price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{jiajushangpinList[4].addtime.split(' ')[0]}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞：</span>
								<span class="text">{{jiajushangpinList[4].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏：</span>
								<span class="text">{{jiajushangpinList[4].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan2"></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{jiajushangpinList[4].clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('jiajushangpin')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
	

		</div>
		<!-- 特价商品 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				newsList: [],
				jingxuanjiazhuangRecommend: [],
				jingxuangongzhuangRecommend: [],
				zhuangxiucailiaoRecommend: [],
				jiajushangpinRecommend: [],

				jingxuangongzhuangList: [],
				shejizhuanquList: [],
				zhuangxiucailiaoList: [],
				jiajushangpinList: [],


				recommendIndex21jingxuanjiazhuang: 0,
				recommendList21jingxuanjiazhuang: [],
				recommendColumn21jingxuanjiazhuang: '',
				recommendIndex21jingxuangongzhuang: 0,
				recommendList21jingxuangongzhuang: [],
				recommendColumn21jingxuangongzhuang: '',


			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getNewsList();
			this.getList();
			this.jingxuanjiazhuangRecommendCate()
			this.jingxuangongzhuangRecommendCate()
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				setTimeout(()=>{
				},750)
			},
			jingxuanjiazhuangRecommendCate(){
				this.$http.get('fenggefenlei/list',{
					params: {
						limit: Number(6)
					}
				}).then(res => {
					if (res.data.code == 0) {
						this.recommendList21jingxuanjiazhuang = res.data.data.list
					}
				});
				this.recommendColumn21jingxuanjiazhuang = 'fenggefenlei'
			},
			jingxuangongzhuangRecommendCate(){
				this.$http.get('fenggefenlei/list',{
					params: {
						limit: Number(6)
					}
				}).then(res => {
					if (res.data.code == 0) {
						this.recommendList21jingxuangongzhuang = res.data.data.list
					}
				});
				this.recommendColumn21jingxuangongzhuang = 'fenggefenlei'
			},
			async recommendIndexClick21(index, name) {
				this['recommendIndex21' + name] = index
				await this.getList()
			},


			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendjingxuanjiazhuang',css:'animate__'},
					{id:'animate_recommendjingxuangongzhuang',css:'animate__'},
					{id:'animate_listjingxuangongzhuang',css:'animate__'},
					{id:'animate_listshejizhuanqu',css:'animate__'},
					{id:'animate_recommendzhuangxiucailiao',css:'animate__'},
					{id:'animate_listzhuangxiucailiao',css:'animate__'},
					{id:'animate_recommendjiajushangpin',css:'animate__'},
					{id:'animate_listjiajushangpin',css:'animate__'},
					{id:'animate_newsnews',css:'animate__'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getNewsList() {
				let data = {
					page: 1,
					limit: 4,
					sort: 'addtime',
					order: 'desc'
				}
				this.$http.get('news/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
					
					}
				});
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "jingxuanjiazhuang/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "jingxuanjiazhuang/autoSort2";
				}
				data = {
					page: 1,
					limit: 8,
				}
				if(this.recommendIndex21jingxuanjiazhuang != 0){
					data.fenggefenlei = this.recommendList21jingxuanjiazhuang[this.recommendIndex21jingxuanjiazhuang - 1].fenggefenlei
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.jingxuanjiazhuangRecommend = res.data.data.list;
					}
				});
				autoSortUrl = "jingxuangongzhuang/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "jingxuangongzhuang/autoSort2";
				}
				data = {
					page: 1,
					limit: 8,
				}
				if(this.recommendIndex21jingxuangongzhuang != 0){
					data.fenggefenlei = this.recommendList21jingxuangongzhuang[this.recommendIndex21jingxuangongzhuang - 1].fenggefenlei
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.jingxuangongzhuangRecommend = res.data.data.list;
					}
				});
				autoSortUrl = "zhuangxiucailiao/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "zhuangxiucailiao/autoSort2";
				}
				data = {
					page: 1,
					limit: 8,
					onshelves: 1,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.zhuangxiucailiaoRecommend = res.data.data.list;
					}
				});
				autoSortUrl = "jiajushangpin/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "jiajushangpin/autoSort2";
				}
				data = {
					page: 1,
					limit: 8,
					onshelves: 1,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.jiajushangpinRecommend = res.data.data.list;
					}
				});
			
				data = {
					page: 1,
					limit: 5,
				}

				this.$http.get('jingxuangongzhuang/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.jingxuangongzhuangList = res.data.data.list;
					}
				});
				data = {
					page: 1,
					limit: 5,
				}

				this.$http.get('shejizhuanqu/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.shejizhuanquList = res.data.data.list;
					}
				});
				data = {
					page: 1,
					limit: 5,
				}

				this.$http.get('zhuangxiucailiao/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.zhuangxiucailiaoList = res.data.data.list;
					}
				});
				data = {
					page: 1,
					limit: 5,
				}

				this.$http.get('jiajushangpin/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.jiajushangpinList = res.data.data.list;
					}
				});
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		margin: 0px auto;
		flex-direction: column;
		background: #fff;
		display: flex;
		width: 100%;
		.news {
			padding: 0;
			margin: 0;
			background: url(http://codegen.caihongy.cn/20250103/5efd25a6df7c4bed92416b2d2de8f137.jpg) no-repeat center top / 100% 100%;
			width: 100%;
			position: relative;
			text-align: center;
			order: 11;
			.news_title_box {
				padding: 0;
				margin: 0;
				background: url(http://codegen.caihongy.cn/20241228/f151b89f53c94b7fa5ae510c2f7bd563.png) no-repeat center bottom;
				width: 100%;
				position: relative;
				text-align: center;
				height: 191px;
				.news_title {
					margin: 0 auto;
					color: #fff;
					background: none;
					font-weight: 600;
					display: block;
					letter-spacing: 1px;
					width: auto;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
				}
				.news_subhead {
					margin: 0;
					color: #999;
					display: none;
					width: 100%;
					font-size: 18px;
					line-height: 40px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list5 {
				padding: 0;
				margin: 20px auto;
				color: #888;
				background: none;
				width: 1200px;
				font-size: 14px;
				text-align: left;
				height: auto;
				.list-item {
					cursor: pointer;
					border: 4px solid #dfb858;
					padding: 20px;
					margin: 0 0 25px;
					background: #fff;
					width: 100%;
					height: auto;
					img {
						object-fit: cover;
						width: 275px;
						float: left;
						height: 275px;
					}
					.infoBox {
						padding: 10px;
						align-content: center;
						background: none;
						display: inline-flex;
						width: calc(100% - 275px);
						align-items: center;
						flex-wrap: wrap;
						height: 275px;
						.name {
							padding: 10px;
							overflow: hidden;
							color: #333;
							white-space: nowrap;
							font-weight: 600;
							width: 100%;
							font-size: 16px;
							line-height: 1.5;
							text-overflow: ellipsis;
						}
						.desc {
							padding: 10px;
							max-height: 150px;
							overflow: hidden;
							color: #666;
							width: 100%;
							font-size: 14px;
							line-height: 30px;
							height: auto;
						}
						.time_item {
							padding: 0 10px;
							margin: 5px 0;
							color: #555;
							display: inline-block;
							width: 100%;
							order: 11;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.publisher_item {
							padding: 0 10px;
							color: #214ea1;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.like_item {
							padding: 0 10px;
							color: #ea8021;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.collect_item {
							padding: 0 10px;
							color: #179da9;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								color: #666;
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.view_item {
							padding: 0 10px;
							color: #f00;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								color: #666;
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
					}
				}
				.list-body {
					background: none;
					display: flex;
					width: 100%;
					justify-content: space-between;
					flex-wrap: wrap;
					height: 275px;
					.list-item1 {
						cursor: pointer;
						border: 4px solid #3397da;
						padding: 20px 10px 10px 20px;
						align-content: center;
						background: #fff;
						display: flex;
						width: 32%;
						align-items: center;
						position: relative;
						flex-wrap: wrap;
						height: 275px;
						.name {
							padding: 0 10px 0 0;
							overflow: hidden;
							color: #333;
							white-space: nowrap;
							font-weight: 600;
							width: 100%;
							font-size: 16px;
							line-height: 1.5;
							text-overflow: ellipsis;
						}
						.desc {
							padding: 10px 10px 10px 0;
							overflow: hidden;
							color: #666;
							width: 100%;
							font-size: 14px;
							line-height: 28px;
							height: 150px;
						}
						.time_item {
							padding: 0 0px;
							margin: 5px 0;
							color: #555;
							display: inline-block;
							width: 100%;
							order: 11;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.publisher_item {
							padding: 0 10px 0 0;
							color: #214ea1;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.like_item {
							padding: 0 10px 0 0;
							color: #ea8021;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.collect_item {
							padding: 0 10px 0 0;
							color: #179da9;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.view_item {
							padding: 0 10px 0 0;
							color: #f00;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
					}
					.list-item2 {
						cursor: pointer;
						border: 4px solid #3397da;
						padding: 20px 10px 10px 20px;
						align-content: center;
						background: #fff;
						display: flex;
						width: 32%;
						align-items: center;
						position: relative;
						flex-wrap: wrap;
						height: 275px;
						.name {
							padding: 0 10px 0 0;
							overflow: hidden;
							color: #333;
							white-space: nowrap;
							font-weight: 600;
							width: 100%;
							font-size: 16px;
							line-height: 1.5;
							text-overflow: ellipsis;
						}
						.desc {
							padding: 10px 10px 10px 0;
							overflow: hidden;
							color: #666;
							width: 100%;
							font-size: 14px;
							line-height: 28px;
							height: 150px;
						}
						.time_item {
							padding: 0 0px;
							margin: 5px 0;
							color: #555;
							display: inline-block;
							width: 100%;
							order: 11;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.publisher_item {
							padding: 0 10px 0 0;
							color: #214ea1;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.like_item {
							padding: 0 10px 0 0;
							color: #ea8021;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.collect_item {
							padding: 0 10px 0 0;
							color: #179da9;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.view_item {
							padding: 0 10px 0 0;
							color: #f00;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
					}
					.list-item3 {
						cursor: pointer;
						border: 4px solid #3397da;
						padding: 20px 10px 10px 20px;
						align-content: center;
						background: #fff;
						display: flex;
						width:  32%;
						align-items: center;
						position: relative;
						flex-wrap: wrap;
						height: 275px;
						.name {
							padding: 0 10px 0 0;
							overflow: hidden;
							color: #333;
							white-space: nowrap;
							font-weight: 600;
							width: 100%;
							font-size: 16px;
							line-height: 1.5;
							text-overflow: ellipsis;
						}
						.desc {
							padding: 10px 10px 10px 0;
							overflow: hidden;
							color: #666;
							width: 100%;
							font-size: 14px;
							line-height: 28px;
							height: 150px;
						}
						.time_item {
							padding: 0 0px;
							margin: 5px 0;
							color: #555;
							display: inline-block;
							width: 100%;
							order: 11;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.publisher_item {
							padding: 0 10px 0 0;
							color: #214ea1;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.like_item {
							padding: 0 10px 0 0;
							color: #ea8021;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.collect_item {
							padding: 0 10px 0 0;
							color: #179da9;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
						.view_item {
							padding: 0 10px 0 0;
							color: #f00;
							display: inline-block;
							.icon {
								margin: 0 2px 0 0;
								line-height: 1.5;
							}
							.label {
								display: none;
								line-height: 1.5;
							}
							.text {
								line-height: 1.5;
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #999;
				cursor: pointer;
				border-radius: 10px;
				padding: 0 20px;
				margin: 20px auto 40px;
				background: #3397da;
				display: inline-block;
				width: 250px;
				line-height: 48px;
				text-align: center;
				.text {
					color: #fff;
					font-size: 16px;
				}
				.icon {
					color: #333;
					display: none;
					font-size: 15px;
				}
			}
		}
		.recommend {
			padding: 0 0 10px;
			margin: 0px auto;
			background: url(http://codegen.caihongy.cn/20241228/80c792bd909b471aa43fff826e4d14d7.jpg) no-repeat center bottom / 100% auto;
			width: 100%;
			position: relative;
			text-align: center;
			order: 1;
			.recommend_title_box {
				padding: 0;
				margin: 0;
				background: url(http://codegen.caihongy.cn/20241228/f151b89f53c94b7fa5ae510c2f7bd563.png) no-repeat center bottom;
				width: 100%;
				position: relative;
				text-align: center;
				height: 191px;
				.recommend_title {
					margin: 0 auto;
					color: #fff;
					background: none;
					font-weight: 600;
					display: block;
					letter-spacing: 1px;
					width: auto;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
				}
				.recommend_subhead {
					margin: 0;
					color: #999;
					display: none;
					width: 100%;
					font-size: 18px;
					line-height: 40px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list21 {
				border: 0;
				padding: 0;
				background: none;
				width: 100%;
				text-align: left;
				.list-body-top {
					padding: 60px 20px 180px;
					margin: 0 auto;
					background: url(http://codegen.caihongy.cn/20240809/ce61590e38bc47b0b2b556bdeaa52d38.jpg) no-repeat center bottom / cover;
					display: none;
					width: 100%;
					justify-content: center;
					align-items: center;
					.tab-title {
						margin: 0 40px 0 0;
						color: #fff;
						display: none;
						font-size: 28px;
						line-height: 34px;
						height: 38px;
					}
					.tab_view {
						display: flex;
						.tab {
							cursor: pointer;
							padding: 0 30px;
							margin: 2px 0 0;
							color: #fff;
							font-size: 16px;
							line-height: 34px;
							height: 34px;
						}
						.tab::before {
						}
						.tab:hover {
							color: #000;
							background: #fff;
							position: relative;
						}
						.tab:hover::before {
							border: 1px solid #ddd;
							margin: 0 0 0 -6px;
							left: 50%;
							bottom: -6px;
							display: inline-block;
							border-color: #fff transparent;
							border-width: 6px 6px 0;
							position: absolute;
							content: "";
						}
						.tab.tabActive:hover {
							color: #000;
							background: #fff;
							position: relative;
						}
						.tab.tabActive:hover::before {
							border: 1px solid #fff;
							margin: 0 0 0 -6px;
							left: 50%;
							bottom: -6px;
							display: inline-block;
							border-color: #fff transparent;
							border-width: 6px 6px 0;
							position: absolute;
							content: "";
						}
					}
					.tab-right {
						cursor: pointer;
						display: none;
						line-height: 38px;
						height: 38px;
						.text {
							color: #fff;
							font-size: 16px;
						}
						.icon {
							color: #f5f5f5;
							font-size: 12px;
						}
					}
				}
				.list-body {
					padding: 0;
					margin: 50px auto 0;
					display: flex;
					width: 1200px;
					justify-content: space-between;
					.list-item {
						padding: 0 0 60px;
						margin: 0;
						background: #fff;
						width: 23.5%;
						position: relative;
						.img {
							width: 100%;
							height: 300px;
							img {
								object-fit: cover;
								width: 100%;
								height: 100%;
							}
						}
						.infoBox {
							border: 1px solid #ddd;
							padding: 20px;
							left: 0;
							background: #fff;
							bottom: 0;
							border-width: 0 1px 1px;
							position: absolute;
							right: 0;
							.name {
								margin: 0 0 0px;
								overflow: hidden;
								color: #333;
								white-space: nowrap;
								font-weight: 600;
								display: block;
								width: 100%;
								font-size: 16px;
								line-height: 28px;
								text-overflow: ellipsis;
								text-align: left;
							}
							.bottomInfo {
								overflow: hidden;
								transition: all 0.6s;
								height: 0;
								.price {
									margin: 10px auto 4px;
									color: #f00;
									width: 100%;
									font-size: 18px;
									line-height: 24px;
								}
								.time_item {
									padding: 0;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.publisher_item {
									padding: 0;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.like_item {
									padding: 0;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.collect_item {
									padding: 0;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
								.view_item {
									padding: 0;
									.icon {
										margin: 0 2px 0 0;
										color: inherit;
										display: none;
										font-size: inherit;
										line-height: 1.5;
									}
									.label {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
									.text {
										color: inherit;
										font-size: inherit;
										line-height: 1.5;
									}
								}
							}
						}
					}
					.list-item::after {
						bottom: 0;
						background: #ffcb2d;
						width: 0;
						position: absolute;
						content: "";
						transition: all 0.6s;
						height: 5px;
					}
					.list-item:hover {
						box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
						.infoBox {
							.bottomInfo {
								cursor: pointer;
								height: 200px;
							}
						}
					}
					.list-item:hover::after {
						width: 100%;
					}
				}
			}
			.moreBtn {
				border: 0px solid #999;
				cursor: pointer;
				border-radius: 10px;
				padding: 0 20px;
				margin: 30px auto;
				background: #3397da;
				display: inline-block;
				width: 250px;
				line-height: 48px;
				text-align: center;
				.text {
					color: #fff;
					font-size: 16px;
				}
				.icon {
					color: #fff;
					display: none;
					font-size: 15px;
				}
			}
		}
		.lists {
			padding: 0;
			margin: 0;
			background: url() no-repeat center center;
			width: 100%;
			position: relative;
			text-align: center;
			order: 7;
			.list_title_box {
				padding: 0;
				margin: 0;
				background: url(http://codegen.caihongy.cn/20241228/f151b89f53c94b7fa5ae510c2f7bd563.png) no-repeat center bottom;
				width: 100%;
				position: relative;
				text-align: center;
				height: 191px;
				.list_title {
					margin: 0 auto;
					color: #fff;
					background: none;
					font-weight: 600;
					display: block;
					letter-spacing: 1px;
					width: auto;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
				}
				.list_subhead {
					margin: 0;
					color: #999;
					display: none;
					width: 100%;
					font-size: 18px;
					line-height: 40px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list9 {
				padding: 0;
				margin: 40px auto 20px;
				color: #fff;
				align-content: flex-start;
				background: none;
				display: flex;
				width: 1200px;
				font-size: 14px;
				justify-content: space-between;
				align-items: flex-start;
				text-align: left;
				height: auto;
				.list-body-top {
					margin: 0 10px 0 0;
					width: calc(50% - 10px);
					height: auto;
					.list-item1 {
						cursor: pointer;
						margin: 0 0 16px;
						display: inline-block;
						width: 100%;
						position: relative;
						height: 580px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 5px 0 10px;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							width: 100%;
							position: absolute;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 30px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								font-size: 20px;
								line-height: 30px;
							}
							.time_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
					.list-item2 {
						cursor: pointer;
						margin: 0 0 20px;
						display: inline-block;
						width: 100%;
						position: relative;
						height: 580px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 5px 0 10px;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							width: 100%;
							position: absolute;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 30px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								font-size: 20px;
								line-height: 30px;
							}
							.time_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
				}
				.list-body-bottom {
					margin: 0 0 0 10px;
					display: flex;
					width: calc(50% - 10px);
					justify-content: space-between;
					flex-wrap: wrap;
					height: auto;
					.list-item1 {
						cursor: pointer;
						margin: 0 0 20px;
						width: 100%;
						position: relative;
						height: 380px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 5px 0 10px;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							width: 100%;
							position: absolute;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 30px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								font-size: 20px;
								line-height: 30px;
							}
							.time_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
					.list-item2 {
						cursor: pointer;
						margin: 0 0 20px;
						width: 100%;
						position: relative;
						height: 380px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 5px 0 10px;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							width: 100%;
							position: absolute;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 30px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								font-size: 20px;
								line-height: 30px;
							}
							.time_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 0 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
					.list-item3 {
						cursor: pointer;
						margin: 0 0 20px;
						width: 100%;
						position: relative;
						height: 380px;
						img {
							object-fit: cover;
							width: 100%;
							float: left;
							height: 100%;
						}
						.infoBox {
							padding: 5px 0 10px;
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.3);
							width: 100%;
							position: absolute;
							.name {
								padding: 0 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								width: 100%;
								font-size: 15px;
								line-height: 30px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0 10px;
								color: #f00;
								font-size: 20px;
								line-height: 30px;
							}
							.time_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0 10px;
								display: inline-block;
								.icon {
									margin: 0 2px 0 0;
									line-height: 1.5;
								}
								.label {
									line-height: 1.5;
								}
								.text {
									line-height: 1.5;
								}
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0px solid #999;
				cursor: pointer;
				border-radius: 10px;
				padding: 0 20px;
				margin: 0px auto 40px;
				background: #3397da;
				display: inline-block;
				width: 250px;
				line-height: 48px;
				text-align: center;
				.text {
					color: #fff;
					font-size: 16px;
				}
				.icon {
					color: #fff;
					font-size: 16px;
				}
			}
		}
	}
</style>
