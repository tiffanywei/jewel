jewel.controller('UserLogCtrl', ['$scope', '$http', 'recordLog',
    function UserLogCtrl($scope, $http, recordLog) {
      $scope.recordLog = recordLog;
      $http.get('/').success(function(data) {
        recordLog.onDataLoaded(data);
      });
    }]);
