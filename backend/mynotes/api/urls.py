from django.urls import path
from . import views
from django.urls import path

urlpatterns= [

    path('',views.getRoutes, name="routes"),
    path('notes/',views.getNotes, name="notes"),
    path('notes/<str:pk>/',views.getNote, name="note"),
    path('fiternotes/',views.getFilteredNote, name="fiternotes"),
    # path('notes/create/',views.createNote, name="create-node"),
    # path('notes/<str:pk>/update/',views.updateNote, name="update-note"),
    # path('notes/<str:pk>/delete/',views.deleteNote, name="delete-note"),
    
]

    