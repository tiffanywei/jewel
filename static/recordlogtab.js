var RecordLogTab = function($http) {
  this.isLoading_ = true;
  this.http_ = $http;
  this.userPairLogs_ = [];
};


RecordLogTab.prototype.onAllDataLoaded = function() {
  this.isLoading_ = false;
};


RecordLogTab.prototype.getRecordData = function() {
  var allData = [];
  if (this.isLoading_) {
    return allData;
  }
  this.userPairLogs_.forEach(function(userPairLog) {
    allData = allData.concat(userPairLog.getRecordData());
  });
  // TODO: Cache/sort/pagination?
  return allData;
};


RecordLogTab.prototype.isLoadingLog = function() {
  return this.isLoading_;
};


RecordLogTab.prototype.isAllTab = function() {
  // TODO: Return whether this is the "all" tab.
  return true;
};


RecordLogTab.prototype.fetch = function() {
  // TODO: Should we use a factory instead of calling the constructor directly?
  this.userPairLogs_.push(new UserPairLog(this.http_));
  this.userPairLogs_.push(new UserPairLog(this.http_));

  // TODO: Create more UserPairLogs if needed for the 'all' tab.
  var counter = this.userPairLogs_.length;
  this.userPairLogs_.forEach(function(userPairLog) {
    userPairLog.fetch(function() {
      console.log(counter);
      counter = counter - 1;
      if (counter == 0) {
        this.onAllDataLoaded();
      }
    }.bind(this));
  }, this);
};
