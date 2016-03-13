var app = angular.module('clt16', []).filter('username', function() {
        return function(input) {
            return input.split("/")[-1];
        }
    });
app.controller('MainController', ['$scope', function ($scope) {
    $scope.init = function() {
        $scope.context = {{CONTEXT}};
        $scope.current_picture = $scope.context.pictures[0];
        $scope.current_picture_id = 0;
        $scope.project = $scope.context.projects[0];
        $scope.project_id = 0;
        setTimeout($scope.nextProject, 1000);
        setTimeout($scope.nextImage, 10000);
    }
    $scope.nextImage = function() {
        $scope.current_picture_id += 1;
        $scope.current_picture_id = $scope.current_picture_id % $scope.context.pictures.length;
        $scope.current_picture = $scope.context.pictures[$scope.current_picture_id];
        $scope.$apply();
        setTimeout($scope.nextImage, 10000);
    }
    $scope.nextProject = function() {
        $scope.project_id += 1;
        $scope.project_id = $scope.project_id % $scope.context.projects.length;
        $scope.project = $scope.context.projects[$scope.project_id];
        $scope.$apply();
        setTimeout($scope.nextProject, 1000);
    }
    $scope.init();

}]);

if (!Array.prototype.last){
    Array.prototype.last = function(){
        return this[this.length - 1];
    };
};
String.prototype.contains = function(it) { return this.indexOf(it) != -1; };