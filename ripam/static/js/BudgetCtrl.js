moneta.controller('BudgetCtrl', function($scope) {
    $scope.init = function () {
        $('.budget-add__select').select2({
            width: 'resolve'
        });

        $scope.state = {
            showAddBudget: false
        }
    }

    $scope.addBudget = function () {
        $scope.state.showAddBudget = true;
    }

    $scope.closeAddBudget = function () {
        $scope.state.showAddBudget = false;
    }

    $scope.init();
});
