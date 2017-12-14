moneta.controller('BudgetCtrl', function($scope) {
    $scope.init = function () {
        $('.budget-type-select').select2({
            width: 'resolve'
        });
    };

    $scope.init();
});
