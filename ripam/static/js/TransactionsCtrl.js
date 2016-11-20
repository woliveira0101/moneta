moneta.controller('TransactionsCtrl', function($scope, $compile) {
    $scope.init = function () {
        $('.transactions-table').DataTable();
    };

    $scope.init();
});
