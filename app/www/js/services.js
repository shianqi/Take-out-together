angular.module('starter.services', [])
	.factory('Loadings', function ($rootScope) {
		return {
			init: function () {
				if(typeof($rootScope.settings)!='undefined'){
					return;
				}
				//加载配置信息
				var settingsStorage = JSON.parse(localStorage.getItem('settings'));
				if(!settingsStorage){
					settingsStorage = {
						enableMeituan: true,
						enableBaidu: true,
						enableElm: true,
						enableImg: true
					}
				}
				$rootScope.settings = settingsStorage;

				//加载定位信息
				var locationStorage = JSON.parse(localStorage.getItem('locations'));
				if(!locationStorage){
					locationStorage = {
						isLoad: false,
						Lng: 0,
						Lat: 0,
						name: '未选定'
					}
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
						Lng: 0,
						Lat: 0,
						name: '未定位'
					}
				}else{
					gaoDeLocation.name="上次定位："+gaoDeLocation.name;
				}
				$rootScope.gaoDeLocation = gaoDeLocation;
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
