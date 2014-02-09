var UserPairLog = function($http) {
  this.isLoading_ = true;
  this.data_ = null;
  this.http_ = $http;
};


UserPairLog.prototype.onDataLoaded = function(onFinish, data) {
  this.isLoading_ = false;
  this.data_ = data;
  onFinish();
};


UserPairLog.prototype.getRecordData = function() {
  return this.data_;
};


UserPairLog.prototype.isLoadingLog = function() {
  return this.isLoading_;
};


UserPairLog.prototype.fetch = function(onFinish) {
  this.http_.get('/test_records.json').success(this.onDataLoaded.bind(this, onFinish));
};
