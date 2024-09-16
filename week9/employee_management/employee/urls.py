from django.urls import path
from . import views

urlpatterns = [
    # ex: /employee/
    path("", views.EmployeeView.as_view(), name="employee"),
    path("position/", views.PositionView.as_view(), name="position"),
    path("project/", views.ProjectView.as_view(), name="project"),
    path("project/<int:project_id>/", views.ProjectDetailView.as_view(), name="detail"),
    path("project/delete/<int:project_id>/", views.ProjectDeleteView.as_view(), name="delete_project"),
    path("project/<int:project_id>/delete_staff/<int:emp_id>/", views.ProjectDetailView.as_view(), name="delete_staff"),
    path("project/<int:project_id>/add_staff/<int:emp_id>/", views.ProjectDetailView.as_view(), name="add_staff"),
    path("project/formEMP/", views.formView, name="formEMP"),
    path("project/formProject/", views.formprojectView, name="formProject"),
]
