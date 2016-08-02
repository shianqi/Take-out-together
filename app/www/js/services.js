angular.module('starter.services', [])
	.factory('Loadings', function ($rootScope,Guide,Systems,$ionicPopup) {
		return {
			init: function () {
				if(typeof($rootScope.settings)!='undefined'){
					return;
				}
				//加载配置信息

				var settingsStorage = JSON.parse(localStorage.getItem('settings'));
				if(!settingsStorage){
					settingsStorage = {
						fristUse: true,
						enableMeituan: true,
						enableBaidu: true,
						enableElm: true,
						enableImg: false
					}
				}
				$rootScope.settings = settingsStorage;

				//加载定位信息
				var locationStorage = JSON.parse(localStorage.getItem('locations'));
				if(!locationStorage){
					locationStorage = {
						isLoad: false,
						Lng: 116.405994,
						Lat: 39.878511,
						name: '未选定'
					};
				}
				$rootScope.location = locationStorage;

				//加载上次附近地点
				var nearByLocations = JSON.parse(localStorage.getItem('nearByLocations'));
				if(!nearByLocations){
					nearByLocations = {}
				}
				$rootScope.nearByLocations = nearByLocations;

				var gaoDeLocation = JSON.parse(localStorage.getItem('gaoDeLocation'));
				if(!gaoDeLocation){
					gaoDeLocation = {
						Lng: 116.405994,
						Lat: 39.878511,
						name: '点击右侧按钮定位 →'
					}
				}else{
					gaoDeLocation.name="上次定位："+gaoDeLocation.name;
				}
				$rootScope.gaoDeLocation = gaoDeLocation;
				if($rootScope.settings.fristUse){
					Guide.guide1();
				}
				Systems.getMessage().then(function (result) {
					if(result.flag){
						var alertPopup = $ionicPopup.alert({
							title: '通知',
							template: result.msg
						});

						alertPopup.then(function(res) {
							//console.log('Thank you for not eating my delicious ice cream cone');
						});
					}
				});
			}
		}
	})

	.factory('Guide' ,function ($state,$ionicPopup,$rootScope) {
		return {
			guide1: function () {
				var confirmPopup = $ionicPopup.confirm({
					title: '第一次使用？',
					cancelText:'跳过',
					okText: '确定',
					template: '先跳转到定位页，点击右侧 <span class="icon ion-refresh"></span> 定位'
				});

				confirmPopup.then(function(res) {
					if(res) {
						$state.go('tab.location');
					} else {
						$rootScope.settings.fristUse = false;
						localStorage.setItem('settings',JSON.stringify($rootScope.settings));
					}
				});
			},
			guide2: function () {
				var confirmPopup = $ionicPopup.confirm({
					title: '定位成功！',
					cancelText:'跳过',
					okText: '确定',
					template: '返回外卖页，下拉刷新 <span class="icon ion-arrow-down-c"></span> 附近外卖'
				});

				confirmPopup.then(function(res) {
					if(res) {
						$state.go('tab.takeOuts');
						$rootScope.settings.fristUse = false;
						localStorage.setItem('settings',JSON.stringify($rootScope.settings));
					} else {
						$rootScope.settings.fristUse = false;
						localStorage.setItem('settings',JSON.stringify($rootScope.settings));
					}
				});
			}
		}
	})

	.factory('Systems', function ($http, $q) {
		return{
			getMessage: function () {
				var deferred = $q.defer();
				var href = 'http://183.175.12.160:8000/msg.html';
				$http.get(href)
					.success(function(message) {
						deferred.resolve(message);
					})
					.finally(function() {
						// Stop the ion-refresher from spinning
					});
				return deferred.promise;
			}
		}
	})

	.factory('TakeOuts', function($http, $rootScope, $q) {
		// Might use a resource here that returns a JSON array
		var takeOuts = {};
		return {
			all: function() {
				var source = '';
				if($rootScope.settings.enableMeituan){
					source+='meituan';
				}
				if($rootScope.settings.enableBaidu){
					source+='baidu';
				}
				if($rootScope.settings.enableElm){
					source+='eleme';
				}
				var lat = $rootScope.location.Lat;
				var lng = $rootScope.location.Lng;
				var href = 'http://183.175.12.160:8000/index.html?lat='+lat+'&lng='+lng+'&source='+source;
				var deferred = $q.defer();
				$http.get(href)
					.success(function(newTakeOuts) {
						deferred.resolve(newTakeOuts);
						takeOuts = newTakeOuts;
					})
					.finally(function() {
						// Stop the ion-refresher from spinning
						$scope.$broadcast('scroll.refreshComplete');
					});
				return deferred.promise;
			},
			remove: function(takeOut) {
				takeOuts.splice(takeOuts.indexOf(takeOut), 1);
			},
			get: function(takeOutId) {
				for (var i = 0; i < takeOuts.length; i++) {
					if (takeOuts[i].shop_id === takeOutId) {
						return takeOuts[i];
					}
				}
				return null;
			}
		};
	})


	.factory('superCache', ['$cacheFactory', function($cacheFactory) {
		return $cacheFactory('super-cache');
	}]);
