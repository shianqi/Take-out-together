angular.module('starter.services', [])

	.factory('TakeOuts', function() {
		// Might use a resource here that returns a JSON array

		// Some fake testing data
		var takeOuts = [{
			id: 0,
			name: 'Ben Sparrow',
			lastText: 'You on your way?',
			face: 'img/ben.png'
		}, {
			id: 1,
			name: 'Max Lynx',
			lastText: 'Hey, it\'s me',
			face: 'img/max.png'
		}, {
			id: 2,
			name: 'Adam Bradleyson',
			lastText: 'I should buy a boat',
			face: 'img/adam.jpg'
		}, {
			id: 3,
			name: 'Perry Governor',
			lastText: 'Look at my mukluks!',
			face: 'img/perry.png'
		}, {
			id: 4,
			name: 'Mike Harrington',
			lastText: 'This is wicked good ice cream.',
			face: 'img/mike.png'
		}];

		return {
			all: function() {
				return takeOuts;
			},
			remove: function(takeOut) {
				takeOuts.splice(takeOuts.indexOf(takeOut), 1);
			},
			get: function(takeOutId) {
				for (var i = 0; i < takeOuts.length; i++) {
					if (takeOuts[i].id === parseInt(takeOutId)) {
						return takeOuts[i];
					}
				}
				return null;
			}
		};
	})


	.factory('Location',function ($rootScope,$ionicLoading) {
		return {
			getLocation: function () {
				// $ionicLoading.show({
				// 	template: 'Loading...'
				// });
				$rootScope.isLoad = true;
				var map, geolocation;
				//加载地图，调用浏览器定位服务
				map = new AMap.Map('container', {
					resizeEnable: true
				});
				map.plugin('AMap.Geolocation', function() {
					geolocation = new AMap.Geolocation({
						enableHighAccuracy: true,//是否使用高精度定位，默认:true
						timeout: 10000,          //超过10秒后停止定位，默认：无穷大
						maximumAge: 0,           //定位结果缓存0毫秒，默认：0
						convert: true,           //自动偏移坐标，偏移后的坐标为高德坐标，默认：true
						showButton: true,        //显示定位按钮，默认：true
						buttonPosition: 'LB',    //定位按钮停靠位置，默认：'LB'，左下角
						buttonOffset: new AMap.Pixel(10, 20),//定位按钮与设置的停靠位置的偏移量，默认：Pixel(10, 20)
						showMarker: true,        //定位成功后在定位到的位置显示点标记，默认：true
						showCircle: true,        //定位成功后用圆圈表示定位精度范围，默认：true
						panToLocation: true,     //定位成功后将定位到的位置作为地图中心点，默认：true
						zoomToAccuracy:true      //定位成功后调整地图视野范围使定位位置及精度范围视野内可见，默认：false
					});
					map.addControl(geolocation);
					geolocation.getCurrentPosition();
					AMap.event.addListener(geolocation, 'complete', onComplete);//返回定位信息
					AMap.event.addListener(geolocation, 'error', onError);      //返回定位出错信息
				});
				//解析定位结果
				function onComplete(data) {
					var str=['定位成功'];
					str.push('经度：' + data.position.getLng());
					str.push('纬度：' + data.position.getLat());

					str.push('是否经过偏移：' + (data.isConverted ? '是' : '否'));
					$rootScope.hello = (data.position.getLng()+' '+data.position.getLat());
					$rootScope.isLoad = false;
					$state.go('tab.location');
				};
				//解析定位错误信息
				function onError(data) {
					$rootScope.hello = '定位失败';
					$rootScope.isLoad = false;
					$state.go('tab.location');
				};
			}
		}
	})


	.factory('superCache', ['$cacheFactory', function($cacheFactory) {
		return $cacheFactory('super-cache');
	}]);
