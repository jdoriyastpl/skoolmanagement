(function () {
        var app = angular.module('skoolmanagement.routes', ['ngRoute']);

        // app.controller('emp',['$scope',function($scope){
        //
        // }]);

        app.config(['$routeProvider', function ($routeProvider) {

  $routeProvider
            .when('/register', {
                controller : 'RegisterController',
                controllerAs: 'vm',
                templateUrl: '/static/views/account/register.html'
            }).
            otherwise({
                redirectTo: '/',
                controller: 'LoginController',
                controllerAs: 'vm',
                templateUrl: '/static/views/account/login.html'
            });


        }]);
})();
