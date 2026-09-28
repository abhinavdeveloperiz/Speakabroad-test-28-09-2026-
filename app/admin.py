from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Language_courses,
    Courses,
    FAQ,
    Testimonial,
    BannerVideo,
    Destination,
    Country,
    CEO,
    COO,
    Graduate,
    University,
)


# =========================
# GLOBAL ADMIN SETTINGS
# =========================

admin.site.site_header = "THIMUSC Administration"
admin.site.site_title = "THIMUSC Admin"
admin.site.index_title = "Welcome to THIMUSC Dashboard"


# =========================
# COMMON IMAGE PREVIEW
# =========================

class ImagePreviewAdmin(admin.ModelAdmin):

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" style="border-radius:10px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


# =========================
# BANNER VIDEO ADMIN
# =========================

@admin.register(BannerVideo)
class BannerVideoAdmin(admin.ModelAdmin):
    list_display = ("id", "video")
    search_fields = ("id",)
    list_per_page = 20


# =========================
# LANGUAGE COURSES ADMIN
# =========================

@admin.register(Language_courses)
class LanguageCoursesAdmin(ImagePreviewAdmin):

    list_display = (
        "id",
        "image_preview",
    )

    fields = (
        "image",
        "image_preview",
    )

    list_per_page = 20


# =========================
# COURSES ADMIN
# =========================

@admin.register(Courses)
class CoursesAdmin(ImagePreviewAdmin):

    list_display = (
        "image_preview",
        "Course_title",
        "country",
        "total_courses",
    )

    list_filter = (
        "country",
    )

    search_fields = (
        "Course_title",
        "course1",
        "course2",
        "course3",
        "course4",
        "course5",
        "course6",
        "course7",
        "course8",
        "course9",
        "course10",
        "course11",
        "course12",
    )

    list_editable = (
        "country",
    )

    readonly_fields = (
        "image_preview",
        "course_count_preview",
    )

    fields = (
        "image",
        "image_preview",
        "Course_title",
        "country",
        "course1",
        "course2",
        "course3",
        "course4",
        "course5",
        "course6",
        "course7",
        "course8",
        "course9",
        "course10",
        "course11",
        "course12",
        "course_count_preview",
    )

    list_per_page = 9999

    def total_courses(self, obj):
        courses = [
            obj.course1,
            obj.course2,
            obj.course3,
            obj.course4,
            obj.course5,
            obj.course6,
            obj.course7,
            obj.course8,
            obj.course9,
            obj.course10,
            obj.course11,
            obj.course12,
        ]
        return len([c for c in courses if c])

    total_courses.short_description = "Total Courses"

    def course_count_preview(self, obj):
        return self.total_courses(obj)

    course_count_preview.short_description = "Filled Course Count"


# =========================
# FAQ ADMIN
# =========================

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):

    list_display = (
        "question",
    )

    search_fields = (
        "question",
        "answer",
    )

    list_per_page = 20


# =========================
# TESTIMONIAL ADMIN
# =========================

@admin.register(Testimonial)
class TestimonialAdmin(ImagePreviewAdmin):

    list_display = (
        "image_preview",
        "name",
        "studied_at",
        "rating",
    )

    list_filter = (
        "studied_at",
        "rating",
    )

    search_fields = (
        "name",
        "feedback",
    )

    list_editable = (
        "rating",
    )

    readonly_fields = (
        "image_preview",
    )

    fields = (
        "image",
        "image_preview",
        "name",
        "rating",
        "studied_at",
        "feedback",
    )

    ordering = ("-rating",)

    list_per_page = 20


# =========================
# GRADUATE ADMIN
# =========================

@admin.register(Graduate)
class GraduateAdmin(ImagePreviewAdmin):

    list_display = (
        "image_preview",
        "name",
        "university",
        "course",
        "country",
        "studied_at",
    )

    list_filter = (
        "studied_at",
        "country",
    )

    search_fields = (
        "name",
        "university",
        "course",
        "country",
    )

    readonly_fields = (
        "image_preview",
    )

    fields = (
        "image",
        "image_preview",
        "name",
        "university",
        "course",
        "country",
        "studied_at",
    )

    ordering = ("name",)

    list_per_page = 20


# =========================
# DESTINATION ADMIN
# =========================

@admin.register(Destination)
class DestinationAdmin(ImagePreviewAdmin):

    list_display = (
        "image_preview",
        "title",
        "country",
        "total_highlights",
    )

    list_filter = (
        "country",
    )

    search_fields = (
        "title",
        "highlight1",
        "highlight2",
        "highlight3",
        "highlight4",
        "highlight5",
    )

    list_editable = (
        "country",
    )

    readonly_fields = (
        "image_preview",
    )

    fields = (
        "title",
        "image",
        "image_preview",
        "country",
        "highlight1",
        "highlight2",
        "highlight3",
        "highlight4",
        "highlight5",
    )

    list_per_page = 9999

    def total_highlights(self, obj):
        highlights = [
            obj.highlight1,
            obj.highlight2,
            obj.highlight3,
            obj.highlight4,
            obj.highlight5,
        ]
        return len([h for h in highlights if h])

    total_highlights.short_description = "Highlights"


# =========================
# COUNTRY ADMIN
# =========================

# @admin.register(Country)
# class CountryAdmin(ImagePreviewAdmin):

#     list_display = (
#         "image_preview",
#         "name",
#     )

#     search_fields = (
#         "name",
#     )

#     readonly_fields = (
#         "image_preview",
#     )

#     fields = (
#         "name",
#         "image",
#         "image_preview",
#     )

#     ordering = ("name",)

#     list_per_page = 20


# =========================
# CEO ADMIN
# =========================

@admin.register(CEO)
class CEOAdmin(ImagePreviewAdmin):

    list_display = (
        "id",
        "image_preview",
    )

    fields = (
        "image",
        "image_preview",
    )

    list_per_page = 20


# =========================
# COO ADMIN
# =========================

@admin.register(COO)
class COOAdmin(ImagePreviewAdmin):

    list_display = (
        "id",
        "image_preview",
    )

    fields = (
        "image",
        "image_preview",
    )

    list_per_page = 20


# =========================
# UNIVERSITY ADMIN
# =========================

@admin.register(University)
class UniversityAdmin(ImagePreviewAdmin):

    list_display = (
        "id",
        "image_preview",
        "country",
    )

    fields = (
        "image",
        "image_preview",
        "country",
    )

    list_per_page = 20