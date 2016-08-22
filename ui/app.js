var app = angular.module('pos-app', []);

app.run(function($rootScope) {
    $rootScope.viewCustomer = function(customer_id) {
    console.log('in view customer');
    $http.get(
      'http://127.0.0.1:8000/customers/' + customer_id +  '/invoices/').success(
      function(data, status, headers, config) {
              $scope.invoices = data;
              $scope.customer_identifier = data.customer_identifier;
    });
});

app.controller('pos-controller', function($scope, $http) {
  // $scope.customer = {
  //   'identifier': 'malka',
  //   'id': 1
  // };

  $http.get('http://127.0.0.1:8000/customers/').success(
    function(data, status, headers, config) {
      $scope.customers = data;
    });

  $scope.viewCustomer = function(customer_id) {
    console.log('in view customer');
    $http.get(
      'http://127.0.0.1:8000/customers/' + customer_id +  '/invoices/').success(
      function(data, status, headers, config) {
              $scope.invoices = data;
              $scope.customer_identifier = data.customer_identifier;
    });
    // $.mobile.changePage('/customers/#customer-invoices-view');
  }
});