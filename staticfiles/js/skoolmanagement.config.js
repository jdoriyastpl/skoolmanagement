(function () {
  'use strict';

  angular
    .module('skoolmanagement.config')
    .config(config);

  config.$inject = ['$locationProvider','$interpolateProvider'];

  /**
  * @name config
  * @desc Enable HTML5 routing
  */
  function config($locationProvider,$interpolateProvider) {
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
    $interpolateProvider.startSymbol('{[]');
    $interpolateProvider.endSymbol(']}');
  }



})();
