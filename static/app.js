var jewel = angular.module('jewel', []);

jewel.factory('recordLog', function() {
  return new RecordLog();
});
