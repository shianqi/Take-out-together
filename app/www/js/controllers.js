angular.module('starter.controllers', [])

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

	.controller('LocationCtrl', function($scope, $rootScope, $state,Location) {
		var locationStorage = localStorage.getItem('location');
		$rootScope.isLoad=false;
		if(!locationStorage){
			locationStorage = 'A'
		}
		$scope.location = {
			choice : locationStorage
		};

		$scope.radioChange = function (val) {
			localStorage.setItem('location',val);
		};
		/**
		 * 跳转到获取新坐标
         */
		$scope.goNewLocation = function () {
			$state.go('tab.location-newLocation');
		};
		$scope.locationString = {

		};
		$scope.locationStringChange = function () {
			console.log($scope.locationString);
		};
		$scope.refurbish = function (){
			Location.getLocation();
		};
		$scope.isLoading = function (num) {
			if(num==1){
				if($rootScope.isLoad==true){
					return 'auto';
				}
				if($rootScope.isLoad==false){
					return 'none';
				}
			}else{
				if($rootScope.isLoad==true){
					return 'none';
				}
				if($rootScope.isLoad==false){
					return 'auto';
				}
			}
		}
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
