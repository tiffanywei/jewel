describe('controller', function() {
  var scope;
  var recordLogSpy;
  var httpBackend;

  beforeEach(module('jewel'));

  beforeEach(inject(function($controller, $rootScope, $httpBackend, $http) {
    scope = $rootScope.$new();
    httpBackend = $httpBackend;
    httpBackend.when("GET", "/").respond([]);
    recordLogSpy = jasmine.createSpyObj('recordLogSpy', ['onDataLoaded']);

    ctrl = $controller('UserLogCtrl', {
      $scope: scope,
      $http: $http,
      recordLog: recordLogSpy
    });
  }));
  
  it('should call recordLog.onDataLoaded on XHR success', function() {
    expect(recordLogSpy.onDataLoaded).not.toHaveBeenCalled();
    httpBackend.flush();
    expect(recordLogSpy.onDataLoaded).toHaveBeenCalled();
  });
});
