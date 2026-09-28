from django.shortcuts import render
from .models import (
    Language_courses,
    FAQ,
    BannerVideo,
    Graduate,
    Destination,
    Courses,
    CEO,
    COO,
    Testimonial,
    University
)



def home(request):
    context = {
        'banner': BannerVideo.objects.only('video').first(),

        'graduates': Graduate.objects.only(
            'image',
            'name',
            'university',
            'course',
            'country',
            'studied_at'
        ),

        'testimonials': Testimonial.objects.only(
            'image',
            'rating',
            'name',
            'feedback',
            'studied_at'
        ),
        'universities': University.objects.only(

            'image',
        ),
        'languages': Language_courses.objects.only('image'),
    }

    return render(request, 'home.html', context)


def about(request):
    context = {
        'coo': COO.objects.only('image').first(),
        'ceo': CEO.objects.only('image').first(),
        'languages': Language_courses.objects.only('image'),
    }
    return render(request, 'about.html', context)


def Study_in_india(request):
    context = {
        'graduates': Graduate.objects.filter(
            studied_at='India'
        ).only(
            'image',
            'name',
            'university',
            'course',
            'country'
        ),

        'destinations': Destination.objects.filter(
            country='India'
        ).only(
            'title',
            'image',
            'country',
            'highlight1',
            'highlight2',
            'highlight3',
            'highlight4',
            'highlight5'
        ),

        'courses': Courses.objects.filter(
            country='India'
        ).only(
            'image',
            'Course_title',
            'course1',
            'course2',
            'course3',
            'course4',
            'course5',
            'course6',
            'course7',
            'course8',
            'course9',
            'course10',
            'course11',
            'course12'
        ),
        'universities': University.objects.filter(
            country='India'),
        
    }

    return render(request, 'Study_in_india.html', context)


def Study_in_abroad(request):
    context = {
        'languages': Language_courses.objects.only('image'),

        'graduates': Graduate.objects.filter(
            studied_at='Abroad'
        ).only(
            'image',
            'name',
            'university',
            'course',
            'country'
        ),

        'destinations': Destination.objects.filter(
            country='Abroad'
        ).only(
            'title',
            'image',
            'country',
            'highlight1',
            'highlight2',
            'highlight3',
            'highlight4',
            'highlight5'
        ),

        'courses': Courses.objects.filter(
            country='Abroad'
        ).only(
            'image',
            'Course_title',
            'course1',
            'course2',
            'course3',
            'course4',
            'course5',
            'course6',
            'course7',
            'course8',
            'course9',
            'course10',
            'course11',
            'course12'
        ),
        'universities': University.objects.filter(
            country='Abroad'),
    }

    return render(request, 'Study_in_abroad.html', context)


def faq(request):
    context = {
        'faqs': FAQ.objects.only('question', 'answer')
    }

    return render(request, 'faq.html', context)


def contact(request):
    return render(request, 'contact.html')