(function () {
    'use strict';
    angular.module('skoolmanagement', [
      'skoolmanagement.routes'
      , 'skoolmanagement.account'
      , 'skoolmanagement.config'
    ]);
    angular.module('skoolmanagement.routes', ['ngRoute']).config(function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    });
    angular.module('skoolmanagement.config', []);
})();