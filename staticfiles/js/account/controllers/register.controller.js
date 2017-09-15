/**
* Register controller
* @namespace skoolmanagement.account.controllers
*/
(function () {
  'use strict';

  angular
    .module('skoolmanagement.account.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location', '$scope', 'Account'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Account) {
    var vm = this;

    vm.register = register;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf skoolmanagement.account.controllers
    */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Account.isAuthenticated()) {
        $location.url('/');
      }
    }
    /**
    * @name register
    * @desc Register a new user
    * @memberOf skoolmanagement.account.controllers.RegisterController
    */
    function register() {
      Account.register(vm.username, vm.password, vm.first_name,vm.last_name,vm.phone,vm.email,vm.role);
    }
  }
})();
