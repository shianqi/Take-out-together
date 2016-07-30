angular.module('starter.services', [])

	.factory('TakeOuts', function($http, $rootScope, $q) {
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
				var settingsStorage = JSON.parse(localStorage.getItem('settings'));
				if(!settingsStorage){
					settingsStorage = {
						enableMeituan: true,
						enableBaidu: true,
						enableElm: true
					}
				}
				var source = '';
				if(settingsStorage.enableMeituan){
					source+='meituan';
				}
				if(settingsStorage.enableBaidu){
					source+='baidu';
				}
				if(settingsStorage.enableElm){
					source+='eleme';
				}
				var lat = $rootScope.location.Lat;
				var lng = $rootScope.location.Lng;
				var href = 'http://183.175.12.160:8000/index.html?lat='+lat+'&lng='+lng+'&source='+source;
				var deferred = $q.defer();
				$http.get(href)
					.success(function(newTakeOuts) {
						console.log(JSON.stringify(newTakeOuts));
						deferred.resolve(newTakeOuts);
						return newTakeOuts;
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
					if (takeOuts[i].id === parseInt(takeOutId)) {
						return takeOuts[i];
					}
				}
				return null;
			}
		};
	})


	.factory('Location',function ($rootScope) {
		return {
			getLocation: function () {

			}
		}
	})


	.factory('superCache', ['$cacheFactory', function($cacheFactory) {
		return $cacheFactory('super-cache');
	}]);
