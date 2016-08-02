angular.module('starter.controllers', [])
	/**
 	* 外卖页面控制器
 	*/
	.controller('TakeOutsCtrl', function($scope, TakeOuts, $state, Loadings) {
		Loadings.init();
		$scope.allTakeOuts = [];
		$scope.pageNumber = -1;

		$scope.remove = function(takeOut) {
			TakeOuts.remove(takeOut);
		};

		$scope.getLocation = function () {
			$state.go('tab.location');
		};

		/**
		 * 下拉刷新执行操作
         */
		$scope.doRefresh = function () {
			TakeOuts.all().then(function (result) {
				$scope.pageNumber = 0;
				$scope.allTakeOuts = result;
				$scope.takeOuts = $scope.allTakeOuts.slice(0,(++$scope.pageNumber)*10);
				$scope.$broadcast('scroll.refreshComplete');
			});
		};

		$scope.addItems = function() {
			if ($scope.pageNumber == -1) {
				TakeOuts.all().then(function (result) {
					$scope.allTakeOuts = result;
					$scope.takeOuts = $scope.allTakeOuts.slice(0, 9);
					$scope.$broadcast('scroll.infiniteScrollComplete');
					$scope.pageNumber = 1;
				});
			} else {
				//$ionicBackdrop.retain()
				$scope.takeOuts = $scope.allTakeOuts.slice(0, (++$scope.pageNumber) * 10);
				$scope.$broadcast('scroll.infiniteScrollComplete');
			}
			if ($scope.pageNumber * 10 > $scope.allTakeOuts.length) {
				//$scope.$broadcast('scroll.infiniteScrollComplete');
			}
		}
	})

	.controller('TakeOutDetailCtrl', function($scope, $stateParams, TakeOuts, Loadings) {
		Loadings.init();

		$scope.takeOut = TakeOuts.get($stateParams.takeOutId);
		$scope.transmit = function (url) {
			location.href=url;
		};
	})


	/**
	 * 定位页面控制器
     */
	.controller('LocationCtrl', function($scope, $rootScope, $state, Loadings,Guide) {
		Loadings.init();


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

		$scope.changeLocation = function (newLocation) {
			$rootScope.location.Lng = newLocation.location.lng;
			$rootScope.location.Lat = newLocation.location.lat;
			$rootScope.location.name = newLocation.name;
			localStorage.setItem('locations',JSON.stringify($rootScope.location));
		};

		$scope.changeLocationToGaoLocation = function () {
			$rootScope.location.Lng = $rootScope.gaoDeLocation.Lng;
			$rootScope.location.Lat = $rootScope.gaoDeLocation.Lat;
			$rootScope.location.name = $rootScope.gaoDeLocation.name;
			localStorage.setItem('locations',JSON.stringify($rootScope.location));
		};

		$scope.refurbish = function (){
			$rootScope.location.isLoad = true;
			$rootScope.location.name = '定位中...';
			$rootScope.gaoDeLocation.name = '定位中...';

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
				$rootScope.location.isLoad = false;
				$rootScope.location.Lng = data.position.getLng();
				$rootScope.location.Lat = data.position.getLat();
				$rootScope.gaoDeLocation.Lng = data.position.getLng();
				$rootScope.gaoDeLocation.Lat = data.position.getLat();
				$rootScope.$apply();
				POISearch();
			}
			//解析定位错误信息
			function onError(data) {
				$rootScope.location.name = '定位失败';
				$rootScope.location.isLoad = false;
				$rootScope.gaoDeLocation.name = '定位失败';
				$rootScope.gaoDeLocation.Lng = 0;
				$rootScope.gaoDeLocation.Lat = 0;
				$rootScope.$apply();
			}

			//附近搜索
			function POISearch(){
				AMap.service(["AMap.PlaceSearch"], function() {
					var placeSearch = new AMap.PlaceSearch({ //构造地点查询类
						pageSize: 8,
						type:'汽车服务|汽车销售|汽车维修|摩托车服务|餐饮服务|购物服务|生活服务|体育休闲服务|' +
						'医疗保健服务|住宿服务|商务住宅|政府机构及社会团体|科教文化服务|' +
						'金融保险服务|公司企业|道路附属设施',
						pageIndex: 1,
						city: "all",
						map: map,
						panel: "panel"
					});

					var cpoint = [$rootScope.gaoDeLocation.Lng, $rootScope.gaoDeLocation.Lat]; //中心点坐标
					placeSearch.searchNearBy('', cpoint, 200, function(status, result) {
						$rootScope.location.name = result.poiList.pois[0].name;
						$rootScope.gaoDeLocation.name = result.poiList.pois[0].name;
						$rootScope.nearByLocations = result.poiList.pois.slice(1);

						localStorage.setItem('locations',JSON.stringify($rootScope.location));
						localStorage.setItem('gaoDeLocation',JSON.stringify($rootScope.gaoDeLocation));
						localStorage.setItem('nearByLocations',JSON.stringify($rootScope.nearByLocations));

						$rootScope.$apply();
						Guide.guide2();
					});
				});
			}
		};
	})

	.controller('AccountCtrl', function($scope, $rootScope, Loadings, $state) {
		Loadings.init();

		$scope.settingsChange = function () {
			localStorage.setItem('settings',JSON.stringify($rootScope.settings));
		};

		$scope.goAboutUs = function () {
			$state.go('tab.account-aboutUs');
		}
	});
