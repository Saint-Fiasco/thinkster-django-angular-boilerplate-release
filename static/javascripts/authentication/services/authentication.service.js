/**
* Authentication
* @namespace thinkster.authentication.services
*/
(function () {
  'use strict';

  angular
    .module('thinkster.authentication.services')
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
       * @returns {Promise}
       * @memberOf thinkster.authentication.services.Authentication
       * @param nombre {string} nombre real del usuario
       * @param apellido {string} apellido del usuario
       */
    function register(nombre, apellido, password, username ) {
      return $http.post('/api/v1/usuarios/', {
        username: username,
        password: password,
        nombre: nombre,
        apellido: apellido
      });
    }
  }
})();