(function() {
  var app = angular.module('realEstate', []);

  app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
 }); // NEWLY ADDED

  app.controller("TabController", function() {
    this.tab = 1;

    this.isSet = function(checkTab) {
      return checkTab === this.tab;
    };

    this.setTab = function(setTab) {
      this.tab = setTab;
    };
  });

  app.controller("searchController", function() {
    this.neighborhood = 'tenderloin';
  });

  app.directive("hello", function(){
    return {
      restrict: 'AE',
      templateUrl: "index-direct.html"
    };
  });

  app.directive('helloWorld', function() {
  return {
      restrict: 'AE',
      replace: 'true',
      template: '<h3>Hello World!!</h3>'
  };
});

})();