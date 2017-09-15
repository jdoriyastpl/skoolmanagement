(function(){
  'use strict';
  angular
      .module('skoolmanagement.account.controllers')
      .controller('LoginController',LoginController);

  LoginController.$inject=['$location','$scope','Account'];


  function LoginController($location,$scope,Account){
    var vm = this;

   vm.login = login;

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

   function login() {
     Account.login(vm.email, vm.password);
   }

  }

})();
