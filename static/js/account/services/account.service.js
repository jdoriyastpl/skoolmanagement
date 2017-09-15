/**
 * Account
 * @namespace skoolmanagement.account.services
 */
(function () {
    'use strict';

    angular
        .module('skoolmanagement.account.services')
        .factory('Account', Account);

    Account.$inject = ['$cookies', '$http'];

    /**
     * @namespace Account
     * @returns {Factory}
     */
    function Account($cookies, $http) {
        /**
         * @name Account
         * @desc The Factory to be returned
         */
        var Account = {
            getAuthenticatedAccount: getAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            login: login,
            register: register,
            setAuthenticatedAccount: setAuthenticatedAccount,
            unauthenticate: unauthenticate
        };

        return Account;

        ////////////////////

        /**
         * @name getAuthenticatedAccount
         * @desc Return the currently authenticated account
         * @returns {object|undefined} Account if authenticated, else `undefined`
         * @memberOf skoolmanagement.account.services
         */
        function getAuthenticatedAccount() {
            if (!$cookies.authenticatedAccount) {
                return;
            }

            return JSON.parse($cookies.authenticatedAccount);
        }


        /**
         * @name isAuthenticated
         * @desc Check if the current user is authenticated
         * @returns {boolean} True is user is authenticated, else false.
         * @memberOf skoolmanagement.account.services
         */
        function isAuthenticated() {
            return !!$cookies.authenticatedAccount;
        }

        /**
         * @name setAuthenticatedAccount
         * @desc Stringify the account object and store it in a cookie
         * @param {Object} user The account object to be stored
         * @returns {undefined}
         * @memberOf skoolmanagement.account.services
         */
        function setAuthenticatedAccount(account) {
            $cookies.authenticatedAccount = JSON.stringify(account);
        }


        /**
         * @name unauthenticate
         * @desc Delete the cookie where the user object is stored
         * @returns {undefined}
         * @memberOf skoolmanagement.account.services
         */
        function unauthenticate() {
            delete $cookies.authenticatedAccount;
        }
        /**
         * @name login
         * @desc Try to log in with email `email` and password `password`
         * @param {string} email The email entered by the user
         * @param {string} password The password entered by the user
         * @returns {Promise}
         * @memberOf skoolmanagement.account.services
         */
        function login(email, password) {
            return $http.post('/api/account/api/v1/auth/login/', {
                email: email,
                password: password
            }).then(loginSuccessFn, loginErrorFn);

            /**
             * @name loginSuccessFn
             * @desc Set the authenticated account and redirect to index
             */
            function loginSuccessFn(data, status, headers, config) {
                Account.setAuthenticatedAccount(data.data);

                window.location = '/home/';
                console.log( "Yes you are logged in now"  );

            }

            /**
             * @name loginErrorFn
             * @desc Log "Epic failure!" to the console
             */
            function loginErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }
        }
        /**
         * @name register
         * @desc Try to register a new user
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         * @memberOf skoolmanagement.account.services.Account
         */
        function register(username, password, first_name, last_name, phone, email, role) {
            return $http.post('/api/account/api/v1/register/', {
                username: username,
                password: password,
                first_name: first_name,
                last_name: last_name,
                phone: phone,
                email: email,
                role: role
            }).then(registerSuccessFn, registerErrorFn);

            /**
             * @name registerSuccessFn
             * @desc Log the new user in
             */
            function registerSuccessFn(data, status, headers, config) {
                Account.login(email, password);
            }

            /**
             * @name registerErrorFn
             * @desc Log "Epic failure!" to the console
             */
            function registerErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            };
        }
    }
})();
