from django.urls import path
from .views import( 
    NumberofSolutionsApiView,
    listofSolutionsApiView,
    DetailedSolutionApiView)

urlpatterns = [
    path('numberOfSolutions/', NumberofSolutionsApiView.as_view(), name='numberOfSolutions'),
    path('listOfSolutions/', listofSolutionsApiView.as_view(), name='listOfSolutions'),
    path('detailedSolution/', DetailedSolutionApiView.as_view(), name='detailedSolution')
]
