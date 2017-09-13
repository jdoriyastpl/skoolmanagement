/**
* Authentication
* @namespace skoolmanagement.account.services
*/
(function () {
  'use strict';

  angular
    .module('skoolmanagement.account.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http'];

  /**
  * @namespace Authentication
  * @returns {Factory}
  */
  function Authentication($cookies, $http) {
    /**
    * @name Authentication
    * @desc The Factory to be returned
    */
    var Authentication = {
      register: register
    };

    return Authentication;

    ////////////////////

    /**
    * @name register
    * @desc Try to register a new user
    * @param {string} username The username entered by the user
    * @param {string} password The password entered by the user
    * @param {string} email The email entered by the user
    * @returns {Promise}
    * @memberOf skoolmanagement.account.services.Authentication
    */
    function register(email, password, username) {
      return $http.post('/api/account/register/', {
        username: username,
        password: password,
        email: email
      });
    }
  }
})();
