describe('controller', function() {
  var scope;
  var recordLogTabSpy;
  var httpBackend;

  beforeEach(module('jewel'));

  beforeEach(inject(function($controller, $rootScope) {
    scope = $rootScope.$new();
    recordLogTabSpy = jasmine.createSpyObj('recordLogTabSpy', ['fetch']);

    ctrl = $controller('UserLogCtrl', {
      $scope: scope,
      recordLogTab: recordLogTabSpy
    });
  }));
  
  it('should call recordLogTab.fetch()', function() {
    expect(recordLogTabSpy.fetch).toHaveBeenCalled();
  });
});
