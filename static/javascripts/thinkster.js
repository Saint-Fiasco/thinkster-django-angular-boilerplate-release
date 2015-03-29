(function () {
  'use strict';

  angular
    .module('thinkster', [
      'thinkster.routes',
      'thinkster.authentication',
      'thinkster.config'
    ]);

  angular
    .module('thinkster.routes', ['ngRoute']);

  angular
  .module('thinkster.config', []);


})();
