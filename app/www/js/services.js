angular.module('starter.services', [])
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
