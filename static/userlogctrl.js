jewel.controller('UserLogCtrl', ['$scope', 'recordLogTab',
    function UserLogCtrl($scope, recordLogTab) {
      $scope.recordLogTab = recordLogTab;
      // TODO: Pass in desired userpairs.
      recordLogTab.fetch();
    }]);
