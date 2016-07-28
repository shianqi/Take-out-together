angular.module('starter.controllers', [])

	.controller('ChatsCtrl', function($scope, Chats, $state) {
		// With the new view caching in Ionic, Controllers are only called
		// when they are recreated or on app start, instead of every page change.
		// To listen for when this page is active (for example, to refresh data),
		// listen for the $ionicView.enter event:
		//
		//$scope.$on('$ionicView.enter', function(e) {
		//});

		$scope.chats = Chats.all();
		$scope.remove = function(chat) {
			Chats.remove(chat);
		};
		$scope.getLocation = function () {
			$state.go('tab.dash');
		};
	})

	.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
		$scope.chat = Chats.get($stateParams.chatId);
	})

	.controller('DashCtrl', function($scope, $rootScope, $state) {
		var locationStorage = localStorage.getItem('location');
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
			$state.go('tab.dash-newLocation');
		};
		$scope.locationString = {

		};
		$scope.locationStringChange = function () {
			console.log($scope.locationString);
		};
		$scope.refurbish = function (){
			$rootScope.hello = 'success';
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
