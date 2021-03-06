"""openedu_dashboard_student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test1.views import test1_view
from SuggestedCourses.views import suggested_courses_view, popular_courses_age_view, popular_courses_education_view
from index.views import index_view
from BasicCourseData.views import basic_course_data_view
from Glossary.views import glossary_view
from AfterSurvey.views import after_survey
from MovieData.views import movie_data_view
from ChartData.views import chart_data_view
from ForumData.views import forum_data_view
from Practive.views import practive_view
from BeforeSurvey.views import before_survey_view

urlpatterns = [
    path('/', index_view, name="index"),
    path('admin/', admin.site.urls),
    path('test/', test1_view),
    path('SuggestedCoursesServlet/', suggested_courses_view, name='SuggestedCoursesServlet'),
    path('BasicCourseDataServlet_student/', basic_course_data_view, name='BasicCourseDataServlet'),
    path('glossary_student/', glossary_view, name='glossary'),
    path('PopularCourseAge/', popular_courses_age_view),
    path('PopularCourseEducation/', popular_courses_education_view),
    path('AfterSurveyServlet/', after_survey, name='AfterSurveyServlet'),
    path('MovieDataServlet/', movie_data_view, name='MovieDataServlet'),
    path('ForumDataServlet/', forum_data_view, name='ForumDataServlet'),
    path('PractiveServlet/', practive_view, name='practiveServlet'),
    path('BeforeSurveyServlet/', before_survey_view, name='BeforeSurveyServlet'),
    path('certificateServlet/', before_survey_view, name='certificateServlet'),
    path('analysisServlet?select=2/', before_survey_view, name='analysisServlet?select=2'),
    path('ErrorReportServlet/', before_survey_view, name='ErrorReportServlet'),
    path('CourseOverviewServlet/', before_survey_view, name='CourseOverviewServlet'),
]
