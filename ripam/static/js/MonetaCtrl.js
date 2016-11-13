var plaidBtnActivated = false;
$('body')
    .observe('childlist', function(record) {
        if (plaidBtnActivated) {
            return;
        }
        plaidBtnActivated = true;
        $('button').addClass('btn');
    });

moneta.controller('MonetaCtrl', function($scope, $compile) {
    $scope.init = function () {
        $scope.banksBalanceSum = totalBanksSum.toLocaleString();
    };

    $scope.init();
});
