moneta.controller('IndexCtrl', function($scope, $compile) {
    $scope.toggleLogin = function () {
        $scope.showLogin = true;
        $scope.showRegister = false;
    };

    $scope.toggleRegister = function () {
        $scope.showLogin = false;
        $scope.showRegister = true;
    };

    $scope.hideAll = function () {
        $scope.showLogin = false;
        $scope.showRegister = false;
    };

    $scope.init = function() {
        $scope.showLogin = false;
        $scope.showRegister = false;
    };

    $scope.init();
});
