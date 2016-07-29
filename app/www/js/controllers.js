angular.module('starter.controllers', [])

	/**
 	* 外卖页面控制器
 	*/
	.controller('TakeOutsCtrl', function($scope, TakeOuts, $state) {
		// With the new view caching in Ionic, Controllers are only called
		// when they are recreated or on app start, instead of every page change.
		// To listen for when this page is active (for example, to refresh data),
		// listen for the $ionicView.enter event:
		//
		//$scope.$on('$ionicView.enter', function(e) {
		//});

		$scope.takeOuts = TakeOuts.all();
		$scope.remove = function(takeOut) {
			TakeOuts.remove(takeOut);
		};
		$scope.getLocation = function () {
			$state.go('tab.location');
		};
	})

	.controller('TakeOutDetailCtrl', function($scope, $stateParams, TakeOuts) {
		$scope.takeOut = TakeOuts.get($stateParams.takeOutId);
	})


	/**
	 * 定位页面控制器
     */
	.controller('LocationCtrl', function($scope, $rootScope, $state) {
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

		$rootScope.gaoDeLocation = {
			Lng: 0,
			Lat: 0,
			name: '未定位'
		};

		/**
		 * 跳转到获取新坐标
         */
		$scope.goNewLocation = function () {
			$state.go('tab.location-newLocation');
		};

		$scope.isLoading = function (num) {
			if(num==1){
				if($rootScope.location.isLoad==true){
					return 'auto';
				}
				if($rootScope.location.isLoad==false){
					return 'none';
				}
			}else{
				if($rootScope.location.isLoad==true){
					return 'none';
				}
				if($rootScope.location.isLoad==false){
					return 'auto';
				}
			}
		};


		$scope.refurbish = function ($scope){
			$rootScope.location.isLoad = true;
			$rootScope.location.name = '定位中...';


			var map, geolocation;
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
				$rootScope.location.name = (data.position.getLng()+' '+data.position.getLat());
				$rootScope.location.isLoad = false;
				$rootScope.gaoDeLocation.name = (data.position.getLng()+' '+data.position.getLat());
				$rootScope.gaoDeLocation.Lng = data.position.getLng();
				$rootScope.gaoDeLocation.Lat = data.position.getLat();
				localStorage.setItem('locations',JSON.stringify($rootScope.location));
				$rootScope.$apply();
			}
			//解析定位错误信息
			function onError(data) {
				$rootScope.location.name = '定位失败';
				$rootScope.location.isLoad = false;
				$rootScope.$apply();
			}
		};
	})

	.controller('AccountCtrl', function($scope) {
		var settingsStorage = JSON.parse(localStorage.getItem('settings'));
		if(!settingsStorage){
			settingsStorage = {
				enableMeituan: true,
				enableBaidu: true,
				enableElm: true
			}
		}

		$scope.settings = settingsStorage;
		$scope.settingsChange = function () {
			localStorage.setItem('settings',JSON.stringify($scope.settings));
		};
	});
