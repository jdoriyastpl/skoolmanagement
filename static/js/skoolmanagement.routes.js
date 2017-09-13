(function () {
        var app = angular.module('skoolmanagement.routes', ['ngRoute']);

        // app.controller('emp',['$scope',function($scope){
        //
        // }]);

        app.config(['$routeProvide', function ($routeProvide) {}

  $routeProvide
            .when('/register', {
                controller = 'RegisterController',
                controllerAs: 'vm',
                templateUrl: '/static/views/account/register.html'
            }).
            otherwise({
                redirectTo: '/'
            });
                    

        }]);
})();
