var jewel = angular.module('jewel', []);

jewel.controller('userLog', ['$scope', '$http', function($scope, $http) {
  $scope.recordLog = new RecordLog();
  $http.get('/').success(function(data) {
    $scope.recordLog.onDataLoaded(data);
  });
}]);

var RecordLog = function() {
  this.isLoading_ = true;
  this.data_ = null;
};

RecordLog.prototype.onDataLoaded = function(data) {
  this.isLoading_ = false;
  this.data_ = data;
}

RecordLog.prototype.getRecordData = function() {
  return this.data_;
}

RecordLog.prototype.isLoadingLog = function() {
  return this.isLoading_;
}
