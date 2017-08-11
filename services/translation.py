# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from services.models import Category

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)
