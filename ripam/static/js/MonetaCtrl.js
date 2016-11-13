moneta.controller('MonetaCtrl', function($scope, $compile) {
    $scope.init = function () {
        var plaidBtnActivated = false;
        $('body')
            .observe('childlist', function(record) {
                if (plaidBtnActivated) {
                    return;
                }
                plaidBtnActivated = true;
                $('button').addClass('btn');
            });
    };

    $scope.init();
});
